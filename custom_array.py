"""Custom implementation of array."""
import ctypes


class Array:
    """A custom array class."""

    def __init__(self, size: int) -> None:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Invalid size")
        self._size = size
        CtypesArrayClass = ctypes.py_object * size
        self._array = CtypesArrayClass()
        self.nullify()

    def __len__(self) -> int:
        return self._size

    def length(self) -> int:
        return self._size

    def nullify(self) -> None:
        self.clear(None)

    def clear(self, value) -> None:
        for i in range(self._size):
            self._array[i] = value

    def __getitem__(self, index: int) -> object:
        return self._array[index]

    def getitem(self, index: int) -> object:
        return self._array[index]

    def __setitem__(self, index: int, value: object) -> None:
        self._array[index] = value

    def setitem(self, index: int, value: object) -> None:
        self._array[index] = value

    def iterator(self) -> iter:
        return (self._array[i] for i in range(self._size))

    def __iter__(self) -> iter:
        return self.iterator()

    def __str__(self) -> str:
        return str([self._array[i] for i in range(self._size)])
