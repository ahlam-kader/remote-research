import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    async with sse_client("http://localhost:8001/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("1. initialize : OK")
            tools = await session.list_tools()
            print("2. tools :", [t.name for t in tools.tools])
            res = await session.read_resource("papers://folders")
            print("3. papers://folders :\n" + res.contents[0].text)

asyncio.run(main())
