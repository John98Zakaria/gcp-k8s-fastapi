import asyncio
import os
import pickle
from functools import partial
from pathlib import Path
from typing import Type

import aiofiles
import aiofiles.os

from general_types.typesafe_representations import URI
from users.repositories.abstract_blobstore import IBlobStore
from users.repositories.abstract_blobstore import T


class FileBlobStore(IBlobStore):
    def __init__(self, base_path: Path):
        self.base_path = base_path

    def raw_load_sync(self, location: URI) -> bytes:
        with open(self.base_path / location, mode="rb") as f:
            return f.read()

    async def raw_load_async(self, location: URI) -> bytes:
        async with aiofiles.open(self.base_path / location, mode="rb") as f:
            return await f.read()

    async def load_object_async(self, location: URI, expected_type: Type[T]) -> T:
        async with aiofiles.open(self.base_path / location, mode="rb") as f:
            raw_data: bytes = await f.read()
        maybe_data = pickle.loads(raw_data)
        if not isinstance(maybe_data, expected_type):
            raise TypeError(f"Expected type {expected_type} got {type(maybe_data)}")
        return maybe_data

    async def store_object_async(self, object_: object, location: URI) -> URI:
        data_path = self.base_path / location
        await asyncio.get_event_loop().run_in_executor(
            None, partial(data_path.parent.mkdir, exist_ok=True, parents=True)
        )
        async with aiofiles.open(data_path, mode="wb") as f:
            await f.write(pickle.dumps(object_))
        return location

    async def delete_object_async(self, location: URI):
        await aiofiles.os.remove(self.base_path / location)

    def load_object_sync(self, location: URI, expected_type: Type[T]) -> T:
        with open(self.base_path / location, mode="rb") as f:
            raw_data: bytes = f.read()
        maybe_data = pickle.loads(raw_data)
        if not isinstance(maybe_data, expected_type):
            raise TypeError(f"Expected type {expected_type} got {type(maybe_data)}")
        return maybe_data

    def store_object_sync(self, object_: object, location: URI) -> URI:
        data_path = self.base_path / location
        data_path.parent.mkdir(exist_ok=True, parents=True)
        with open(self.base_path / location, mode="wb") as f:
            f.write(pickle.dumps(object_))
        return location

    def delete_object_sync(self, location: URI):
        file_path = self.base_path / location
        os.remove(file_path)
