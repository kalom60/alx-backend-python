#!/usr/bin/env python3
"""The basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for random number of seconds"""
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
