"""Custom implementation of array."""
from __future__ import annotations

import ctypes


class ArrayIterator:
    """Iterator for array."""

    def __init__(self, array: Array) -> None:
        self._array = array

    def __iter__(self):
        for i in range(len(self._array)):
            yield self._array[i]


class Array:
    """A custom array class."""

    def __init__(self, size: int, to_nullify: bool = True) -> None:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Invalid size")
        self._size = size
        CtypesArrayClass = ctypes.py_object * size
        self._array = CtypesArrayClass()
        if to_nullify:
            self.nullify()

    def __len__(self) -> int:
        return self._size

    def nullify(self) -> None:
        self.clear(None)

    def clear(self, value) -> None:
        for i in range(self._size):
            self._array[i] = value

    def __getitem__(self, index: int) -> object:
        return self._array[index]

    def __setitem__(self, index: int, value: object) -> None:
        self._array[index] = value

    def __iter__(self):
        return ArrayIterator(self)

    def __str__(self) -> str:
        return str([self._array[i] for i in range(self._size)])

    def __repr__(self) -> str:
        return str(self)


class Array2D(Array):
    """A custom 2D array class."""

    def __init__(self, n_rows: int, n_cols: int) -> None:
        if not isinstance(n_rows, int) or n_rows <= 0:
            raise ValueError("Invalid number of rows")
        if not isinstance(n_cols, int) or n_cols <= 0:
            raise ValueError("Invalid number of columns")
        self._shape = (n_rows, n_cols)
        super().__init__(n_rows, to_nullify=False)
        for i in range(n_rows):
            self._array[i] = Array(n_cols)

    def num_rows(self) -> int:
        return self._shape[0]

    def num_cols(self) -> int:
        return self._shape[1]

    def clear(self, value) -> None:
        for i in range(self._shape[0]):
            self._array[i].clear(value)

    def __getitem__(self, index: tuple) -> object:
        return self._array[index[0]][index[1]]

    def __setitem__(self, index: tuple, value: object) -> None:
        self._array[index[0]][index[1]] = value

    def __str__(self) -> str:
        return str([self._array[i] for i in range(self._shape[0])])
