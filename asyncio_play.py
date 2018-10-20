import asyncio
import random

async def hw(a):
    rn = random.randint(1,5)
    await asyncio.sleep(rn)
    print("Running {} for {}".format(a,rn))

async def parallelstuff():
    tasks=[]
    for x in range(12):
        print("scheduling job:{}".format(x))
        tasks.append(asyncio.ensure_future(hw(x)))
    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(parallelstuff())
loop.close()