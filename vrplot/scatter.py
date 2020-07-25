from math import ceil, floor
from typing import Union

from vrplot.basic_objects import Figure, Point
from vrplot.exceptions import check_pandas_column_exist
from vrplot.grid import create_grid

import pandas as pd


def scatter3d(
        df: pd.DataFrame,
        x: str,
        y: str,
        z: str,
        point_size: Union[str, float] = 0.1,
        grid: bool = True,
        size_multiplier=1.,
    ) -> Figure:

    # Grab columns and handle exceptions
    X = check_pandas_column_exist(df, x)
    Y = check_pandas_column_exist(df, y)
    Z = check_pandas_column_exist(df, z)
    if isinstance(point_size, str):
        SIZE = check_pandas_column_exist(df, point_size)
    N = len(X)

    if isinstance(point_size, str):
        entities = [Point(x=x_*size_multiplier, y=y_*size_multiplier, z=z_*size_multiplier, radius=size*size_multiplier)
                    for x_, y_, z_, size in zip(X, Y, Z, SIZE)]
    else:
        entities = [Point(x=x_*size_multiplier, y=y_*size_multiplier, z=z_*size_multiplier, radius=point_size*size_multiplier)
                    for x_, y_, z_ in zip(X, Y, Z)]

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
