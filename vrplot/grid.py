from vrplot.basic_objects import Figure, Arrow


DEFAULT_GRID_COLOR = "#000000"


def create_grid(
        x_range: (float, float),
        y_range: (float, float),
        z_range: (float, float)
    ) -> Figure:

    def _create_grid_arrows(_x_range, _y_range, _z_range):
        return [
            Arrow(
                x_range=_x_range,
                y_range=(0, 0),
                z_range=(0, 0),
                color=DEFAULT_GRID_COLOR
            ),
            Arrow(
                x_range=(0, 0),
                y_range=_y_range,
                z_range=(0, 0),
                color=DEFAULT_GRID_COLOR
            ),
            Arrow(
                x_range=(0, 0),
                y_range=(0, 0),
                z_range=_z_range,
                color=DEFAULT_GRID_COLOR
            )
        ]

    entities = []
    if x_range[1] >= 0 and y_range[0] >= 0 and z_range[0] >= 0:
        entities += _create_grid_arrows((0, x_range[1]), (0, y_range[1]), (0, z_range[1]))
    if x_range[1] < 0 and y_range[0] >= 0 and z_range[0] >= 0:
        entities += _create_grid_arrows((x_range[0], 0), (0, y_range[1]), (0, z_range[1]))
    if x_range[1] >= 0 and y_range[0] < 0 and z_range[0] >= 0:
        entities += _create_grid_arrows((0, x_range[1]), (y_range[0], 0), (0, z_range[1]))
    if x_range[1] < 0 and y_range[0] < 0 and z_range[0] >= 0:
        entities += _create_grid_arrows((x_range[0], 0), (y_range[0], 0), (0, z_range[1]))
    if x_range[1] >= 0 and y_range[0] >= 0 and z_range[0] < 0:
        entities += _create_grid_arrows((0, x_range[1]), (0, y_range[1]), (z_range[0], 0))
    if x_range[1] < 0 and y_range[0] >= 0 and z_range[0] < 0:
        entities += _create_grid_arrows((x_range[0], 0), (0, y_range[1]), (z_range[0], 0))
    if x_range[1] >= 0 and y_range[0] < 0 and z_range[0] < 0:
        entities += _create_grid_arrows((0, x_range[1]), (y_range[0], 0), (z_range[0], 0))
    if x_range[1] < 0 and y_range[0] < 0 and z_range[0] < 0:
        entities += _create_grid_arrows((x_range[0], 0), (y_range[0], 0), (z_range[0], 0))
    return Figure(entities=list(set(entities)))  # Deduplicate arrows and lines
