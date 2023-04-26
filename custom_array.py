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
        return (self._array[i] for i in range(self._size))

    def __str__(self) -> str:
        return str([self._array[i] for i in range(self._size)])

    def __repr__(self) -> str:
        return str(self)


class Array2D(Array):
    """A custom 2D array class."""

    def __init__(self, shape: tuple) -> None:
        if not isinstance(shape, tuple) or len(shape) != 2:
            raise ValueError("Invalid shape")
        self._shape = shape
        super().__init__(shape[0])
        for i in range(shape[0]):
            self._array[i] = Array(shape[1])

    def __getitem__(self, index: tuple) -> object:
        return self._array[index[0]][index[1]]

    def __setitem__(self, index: tuple, value: object) -> None:
        self._array[index[0]][index[1]] = value

    def __iter__(self):
        return (self._array[i] for i in range(self._shape[0]))

    def __str__(self) -> str:
        return str([self._array[i] for i in range(self._shape[0])])
