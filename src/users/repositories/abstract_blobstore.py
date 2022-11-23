from abc import ABC, abstractmethod
from typing import Type, TypeVar

from general_types.typesafe_representations import URI


T = TypeVar("T")


class IBlobStore(ABC):
    @abstractmethod
    def raw_load_sync(self, location: URI) -> bytes:
        pass

    @abstractmethod
    async def raw_load_async(self, location: URI) -> bytes:
        pass

    @abstractmethod
    async def load_object_async(self, location: URI, expected_type: Type[T]) -> T:
        """
        Loads objects of the given type

        Args:
            location: Resource Location
            expected_type: Expected type to be loaded
        Returns:
            Requested object
        Raises:
            FileNotFoundError
            TypeError
        """
        pass

    @abstractmethod
    async def store_object_async(self, object_: object, location: URI) -> URI:
        """
        Stores an object at the given URI

        Args:
            object_: Object to be stored
            location: URI identifier of where it is stored

        Returns:
            The Stored object
        """
        pass

    @abstractmethod
    def delete_object_async(self, location: URI):
        pass

    @abstractmethod
    def load_object_sync(self, location: URI, expected_type: Type[T]) -> T:
        """
        Loads objects of the given type

        Args:
            location: Resource Location
            expected_type: Expected type to be loaded
        Returns:
            Requested object
        Raises:
            FileNotFoundError
            TypeError
        """
        pass

    @abstractmethod
    def store_object_sync(self, object_: object, location: URI) -> URI:
        """
        Stores an object at the given URI

        Args:
            object_: Object to be stored
            location: URI identifier of where it is stored

        Returns:
            The Stored object
        """
        pass

    @abstractmethod
    def delete_object_sync(self, location: URI):
        pass
