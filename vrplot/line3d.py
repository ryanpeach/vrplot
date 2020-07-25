from typing import Union
from math import ceil, floor

from vrplot.basic_objects import Figure, Line, DEFAULT_COLOR
from vrplot.exceptions import check_pandas_column_exist
from vrplot.grid import create_grid

import pandas as pd

from vrplot.types import Column, Color


def line3d(
        df: pd.DataFrame,
        *,
        x: Column,
        y: Column,
        z: Column,
        color: Union[Column, Color] = DEFAULT_COLOR,
        grid: bool = True,
        size_multiplier: float = 1.
) -> Figure:

    # Grab columns and handle exceptions
    X = check_pandas_column_exist(df, x)
    Y = check_pandas_column_exist(df, y)
    Z = check_pandas_column_exist(df, z)
    N = len(X)

    # Create our lines as each point connected to each next point
    entities = [
        Line(
            x_range=(X[i]*size_multiplier, X[i+1]*size_multiplier),
            y_range=(Y[i]*size_multiplier, Y[i+1]*size_multiplier),
            z_range=(Z[i]*size_multiplier, Z[i+1]*size_multiplier),
            color=color
        )
        for i in range(N-1)
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
