#!/usr/bin/env python3

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    for x in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
