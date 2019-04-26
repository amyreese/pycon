import asyncio
import random
from aiohttp import web

routes = web.RouteTableDef()


@routes.get(r"/randint/{number:\d+}")
async def randint(request):
    try:
        number = int(request.match_info["number"])
    except Exception:
        number = 20

    await asyncio.sleep(0.1)  # thinking

    value = random.randint(0, number)
    return web.Response(text=f"{value}\n")


app = web.Application()
app.add_routes(routes)
web.run_app(app)
