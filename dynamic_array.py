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
            self._resize(2 * self._capacity)

        self.__array[self._size] = item
        self._size += 1

    def __setitem__(self, index, item):
        if index < 0 or index >= self._size:
            raise IndexError('Invalid index')
        self.__array[index] = item

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError('Invalid index')
        return self.__array[index]
    
    def __iter__(self):
        ...
    

class DynamicArrayIterator:
    ...