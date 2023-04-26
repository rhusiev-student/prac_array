"""
Dynamic array class.
"""

import ctypes

class DynamicArray:
    """
    A dynamic array class akin to a simplified Python list.
    """

    def __init__(self, initial_capacity = 1):
        self._size = 0
        self._capacity = initial_capacity
        self.__array = self._make_array(self._capacity)

        self.clear()

    def __len__(self):
        return self._size

    def capacity(self):
        """
        Returns capacity of array.
        """
        return self._capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def clear(self, value = None):
        """
        Sets all list items as None.
        """
        for i in range(self._capacity):
            self.__array[i] = value

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self.__array[i]

        self.__array = new_array
        self._capacity = new_capacity

    def push_back(self, item):
        """
        Pushes item into end of array.
        """
        if self._size == self._capacity:
            self._resize(int(1.25 * self._capacity) + 1)

        self.__array[self._size] = item
        self._size += 1

    def remove(self, index):
        """
        Remove element from array.
        """
        if index < 0 or index >= self._size:
            raise IndexError('Invalid index')

        for i in range(index, self._size):
            if i == self._size - 1:
                self[self._size - 1] = None
                break
            self[i] = self[i + 1]

        self._size -= 1
        self.shrink_to_fit()

    def shrink_to_fit(self):
        """
        Set capacity equals to logic size.
        """
        self._resize(self._size)

    def __setitem__(self, index, item):
        if index < 0 or index >= self._size:
            raise IndexError('Invalid index')
        self.__array[index] = item

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError('Invalid index')
        return self.__array[index]

    def __iter__(self):
        iterator = DynamicArrayIterator(self)
        return iter(iterator)


class DynamicArrayIterator:
    """
    Iterator class for DynamicArray
    """
    def __init__(self, dyn_array):
        if not isinstance(dyn_array, DynamicArray):
            raise TypeError("Must be instance of DynamicArray")

        self.__dyn_array = dyn_array

    def __iter__(self):
        for i in range(len(self.__dyn_array)):
            yield self.__dyn_array[i]

