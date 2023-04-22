from surrealdb import Surreal
from dotenv import load_dotenv
import os
from db_context import DbContextFactory, DbContext

load_dotenv('.env')
url = os.getenv('DB_URL')

auth = {
    'user': os.getenv('DB_USER'),
    'pass': os.getenv('DB_PASS')
}

db_factory = DbContextFactory(url, auth)


async def get_all_items():
    async with db_factory.get_context() as ctx:
        items = await ctx.db.select('item')
        return items
