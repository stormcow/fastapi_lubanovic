import asyncio

async def q():
    print('why cant programmers tell jokes?')
    await asyncio.sleep(3)
    
async def a ():
    print('timing')

async def main():
    await asyncio.gather(q(),a())
    
asyncio.run(main())