#!/usr/bin/env python3

import asyncio
import random


async def async_generator():
    for x in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
