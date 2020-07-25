import os
from typing import List, Tuple, Optional
import math
import webbrowser
import tempfile

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

from vrplot.exceptions import check_color, PointSizeException

DEFAULT_COLOR = "#FF0000"


class Entity:
    """
    This is what every aframe entity will inherit.
    """
    entity_string: str

    def __init__(self,
                 entity_string: str,
                 color: str = DEFAULT_COLOR):
        self.entity_string = entity_string
        check_color(color)


class Point(Entity):
    """
    This is what we will use for a 3d point entity.
    """
    def __init__(
            self,
            x: float,
            y: float,
            z: float,
            radius: float = 0.1,
            color: str = DEFAULT_COLOR
    ):
        if radius == 0.:
            raise PointSizeException("Radius can not be zero.")
        super(Point, self).__init__(
            f'<a-sphere position="{x} {y} {z}" color="{color}" radius="{radius}"></a-sphere>',
            color=color
        )


class Line(Entity):
    """
    This will be a 3D line.
    This is a custom A-Frame object.
    """
    def __init__(
        self,
        x_range: (float, float),
        y_range: (float, float),
        z_range: (float, float),
        color: str = DEFAULT_COLOR
    ):
        x0, x1 = x_range
        y0, y1 = y_range
        z0, z1 = z_range
        super(Line, self).__init__(
            f'<a-entity line="start: {x0}, {y0}, {z0}; end: {x1}, {y1}, {z1}; color: {color}"></a-entity>',
            color=color
        )


class Arrow(Entity):
    """
    This will be a 3D arrow (which is really just a fancy line, but double inheritance can be weird).
    This is a custom A-Frame object.

    :reference: http://mathforum.org/library/drmath/view/54146.html
    """
    def __init__(
        self,
        x_range: (float, float),
        y_range: (float, float),
        z_range: (float, float),
        color: str = DEFAULT_COLOR
    ):
        x0, x1 = x_range
        y0, y1 = y_range
        z0, z1 = z_range
        t = math.pi/4
        l = math.sqrt((x1-x0)**2 + (y1-y0)**2 + (z1-z0)**2)
        d = 1
        x0_, x1_, y0_, y1_ = x0, x1, y0, y1
        x2 = x1_ - ((x1_ - x0_)*math.cos(t) - (y1_ - y0_)*math.sin(t)) * d / l
        y2 = y1_ - ((y1_ - y0_)*math.cos(t) + (x1_ - x0_)*math.sin(t)) * d / l
        x3 = x1_ - ((x1_ - x0_)*math.cos(-t) - (y1_ - y0_)*math.sin(-t)) * d / l
        y3 = y1_ - ((y1_ - y0_)*math.cos(-t) + (x1_ - x0_)*math.sin(-t)) * d / l
        super(Arrow, self).__init__(
            f'<a-entity line="start: {x0}, {y0}, {z0}; end: {x1}, {y1}, {z1}; color: {color}"></a-entity>'
            f'<a-entity line="start: {x1}, {y1}, {z1}; end: {x2}, {y2}, {z1}; color: {color}"></a-entity>'
            f'<a-entity line="start: {x1}, {y1}, {z1}; end: {x3}, {y3}, {z1}; color: {color}"></a-entity>',
            color=color
        )


class Figure:
    """
    This represents a 3D figure in VR.
    These can be added together to join figures.
    """
    entities: List[Entity]
    user_position: Tuple[float, float, float]
    user_rotation: Tuple[float, float, float]
    _render: Optional[str]

    def __init__(
            self,
            entities: List[Entity],
            user_position: Tuple[float, float, float] = (1, 1, 1),
            user_rotation: Tuple[float, float, float] = (0, 0, 0)
    ):
        self.entities = entities
        self.user_position = user_position
        self.user_rotation = user_rotation
        self._render = None

    def render(self, open=True):
        env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('aframe.html.jinja')
        self._render = template.render(entities=self.entities,
                                       position=self.user_position,
                                       rotation=self.user_rotation)
        if open:
            fd, name = tempfile.mkstemp(suffix=".html")
            with os.fdopen(fd, mode="w") as f:
                f.write(self._render)
            webbrowser.open(name)

    def save(self, file_path: str):
        if not self._render:
            self.render(open=False)
        with open(file_path, 'w') as f:
            f.write(self._render)

    def __add__(self, other: "Figure") -> "Figure":
        return Figure(self.entities + other.entities)
