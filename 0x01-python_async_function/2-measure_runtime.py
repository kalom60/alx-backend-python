#!/usr/bin/env python3
"""Measure the runtime"""

from asyncio import run
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return the runtime"""
    begin = time.time()
    run(wait_n(n, max_delay))
    end = time.time()
    return (end - begin) / n
