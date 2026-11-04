import asyncio
async def main():
    print("Hello Friends.")
    await asyncio.sleep(5)
    print("How are you?")

asyncio.run(main())