# Copyright 2022 John Reese
# Licensed under the MIT License

import warnings
warnings.simplefilter("once")

import asyncio


async def sleepy():
    return await asyncio.sleep(0)