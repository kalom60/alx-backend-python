#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """waits until wait_random returns list of delays"""
    wait: List[float] = []
    for x in range(n):
        waited = await task_wait_random(max_delay)
        wait.append(waited)

    return sorted(wait)
