import pandas as pd
import numpy as np


class PositiveException(Exception):
    """ Indicates that a value should not be less than or equal to zero. """
    pass


class NonZeroException(Exception):
    """ Indicates that a value should not be zero. """
    pass


class ColorException(Exception):
    """ Indicates an invalid hexadecimal color string. """
    pass


def check_color(color: str) -> None:
    """
    Checks that a hexadecimal color string is valid.
    :param color: A color string. Like '#FFFFFF'.
    :return:
    """
    if color[0] != "#":
        raise ColorException("Colors should start with #")
    if len(color) != 7:
        raise ColorException("Colors should have 7 characters. First # and then 6 values between 0-9 A-F.")
    for i, char in enumerate(color[1:]):
        if char not in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}:
            raise ColorException(f"Color value {i+1}=={char} not in 0-9 A-F.")


class PandasColumnDoesNotExistException(Exception):
    """ Indicates a pandas column does not exist in a given dataframe. """
    pass


def check_pandas_column_exist(
        df: pd.DataFrame,
        col: str
    ) -> np.ndarray:
    """
    Checks that a given column exists in a given pandas DataFrame.

    :param df: A pandas DataFrame.
    :param col: The column name you would like to check for.
    :return: A pandas series representing the column.
    """
    if col not in df:
        raise PandasColumnDoesNotExistException(f"Column {col} does not exist in given pandas DataFrame.")
    return df[col].values