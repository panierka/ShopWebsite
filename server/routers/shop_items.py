from dotenv import load_dotenv, find_dotenv
import os
from db_context import DbContextFactory
from datetime import datetime
from fastapi import APIRouter

router = APIRouter()

load_dotenv(find_dotenv())
url = os.getenv('DB_URL')

auth = {
    'user': os.getenv('DB_USER'),
    'pass': os.getenv('DB_PASS')
}

db_factory = DbContextFactory(url, auth, namespace='test', database='test')


@router.get('/get-items')
async def get_all_items():
    async with db_factory.get_context() as ctx:
        items = await ctx.db.select('item')
        return items
