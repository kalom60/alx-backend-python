#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    end = time.time()
    return end - start
