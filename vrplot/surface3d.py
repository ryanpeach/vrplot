from typing import Optional, Union
from math import floor, ceil

import pandas as pd
import numpy as np

from vrplot import create_grid
from vrplot.basic_objects import Figure, Box, DEFAULT_COLOR
from vrplot.exceptions import check_pandas_column_exist
from vrplot.types import Column, Color


def bar3d(
        df: pd.DataFrame,
        *,
        x: Column,
        z: Column,
        height: Column,
        size: Optional[Union[Column, float]] = None,
        color: Union[Column, Color] = DEFAULT_COLOR,
        grid: bool = True,
        size_multiplier: float = 1.
) -> Figure:

    # Grab columns and handle exceptions
    Y = check_pandas_column_exist(df, height)
    filter = Y != 0
    Y = Y[filter]
    X = check_pandas_column_exist(df, x)[filter]
    Z = check_pandas_column_exist(df, z)[filter]
    if isinstance(size, str):
        SIZE = check_pandas_column_exist(df, size)[filter]
    elif size is None:
        # Automatically determine the size to be the minimum difference between points in the X and Z dimensions
        size = min(np.diff(sorted(set(list(X)))).min(), np.diff(sorted(set(list(Z)))).min())
    if color in df:
        raise NotImplementedError("Color as a part of the dataframe has not been implemented yet.")
        # COLOR = map_float_to_color(check_pandas_column_exist(df, color))
    N = len(X)

    # Create our boxes
    # We start them at Y[i]/2*size_multiplier because their height grows from their centroid
    entities = [
        Box(
            position=(X[i]*size_multiplier, Y[i]/2*size_multiplier, Z[i]*size_multiplier),
            height=abs(Y[i]*size_multiplier),
            depth=size*size_multiplier if isinstance(size, float) else SIZE[i]*size_multiplier,
            width=size*size_multiplier if isinstance(size, float) else SIZE[i]*size_multiplier,
            color=color
        ) for i in range(N)
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
