#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """waits until wait_random returns list of delays"""
    wait: List[float] = []
    for x in range(n):
        waited = await wait_random(max_delay)
        wait.append(waited)

    return sorted(wait)
