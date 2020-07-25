from math import ceil, floor

from vrplot.basic_objects import Figure, Line, DEFAULT_COLOR
from vrplot.exceptions import check_pandas_column_exist
from vrplot.grid import create_grid

import pandas as pd


def line3d(
        df: pd.DataFrame,
        x: str,
        y: str,
        z: str,
        grid: bool = True,
        size_multiplier: float = 1.,
        color: str = DEFAULT_COLOR
    ) -> Figure:

    # Grab columns and handle exceptions
    X = check_pandas_column_exist(df, x)
    Y = check_pandas_column_exist(df, y)
    Z = check_pandas_column_exist(df, z)
    N = len(X)

    entities = [Line(x_range=(x0_*size_multiplier, x1_*size_multiplier),
                     y_range=(y0_*size_multiplier, y1_*size_multiplier),
                     z_range=(z0_*size_multiplier, z1_*size_multiplier),
                     color=color)
                for x0_, y0_, z0_, x1_, y1_, z1_ in zip(X, Y, Z, X[1:], Y[1:], Z[1:])]

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
