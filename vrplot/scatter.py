from math import ceil, floor
from typing import Union

from vrplot.basic_objects import Figure, Point, DEFAULT_COLOR
from vrplot.exceptions import check_pandas_column_exist
from vrplot.grid import create_grid

import pandas as pd

from vrplot.types import Column, Color


def scatter3d(
        df: pd.DataFrame,
        *,
        x: Column,
        y: Column,
        z: Column,
        point_size: Union[Column, float] = 0.1,
        color: Union[Column, Color] = DEFAULT_COLOR,
        grid: bool = True,
        size_multiplier: float = 1.
) -> Figure:

    # Grab columns and handle exceptions
    X = check_pandas_column_exist(df, x)
    Y = check_pandas_column_exist(df, y)
    Z = check_pandas_column_exist(df, z)
    if isinstance(point_size, str):
        SIZE = check_pandas_column_exist(df, point_size)
    if color in df:
        raise NotImplementedError("Color as a part of the dataframe has not been implemented yet.")
    N = len(X)

    # Create all our points
    entities = [
        Point(
            x=X[i]*size_multiplier,
            y=Y[i]*size_multiplier,
            z=Z[i]*size_multiplier,
            radius=point_size*size_multiplier if isinstance(point_size, float) else SIZE[i]*size_multiplier,
            color=color
        )
        for i in range(N)
    ]

    # Create the Grid
    out = Figure(entities=entities)
    if grid:
        out += create_grid(
            (floor(X.min())*size_multiplier, ceil(X.max())*size_multiplier),
            (floor(Y.min())*size_multiplier, ceil(Y.max())*size_multiplier),
            (floor(Z.min())*size_multiplier, ceil(Z.max())*size_multiplier)
        )

    # Return
    return out
