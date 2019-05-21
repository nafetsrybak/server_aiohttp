import asyncio
from aiohttp import web
#import math

from libs.PositionGenerator import PositionGenerator
from libs.helpers import *


async def calc(request):
    args = request.query
    
    generator = PositionGenerator(int(args['mult1']),int(args['mult1']))
    generator.generate(int(args['from']), int(args['to']))
    positions = unzip_positions(generator.get_generated())
    
    return web.Response(body=str(positions) + '<br><a href="/">Back</a>', content_type='text/html')

async def handler(request):
    f = open('html/form.html', encoding='utf8')
    return web.Response(text=f.read(), content_type='text/html', charset='utf-8')   

loop = asyncio.ProactorEventLoop()
asyncio.set_event_loop(loop)
app = web.Application(loop=loop)
app.router.add_route('GET', '/calc', calc)
app.router.add_route('GET', '/', handler)


web.run_app(app, host='localhost', port=80)