from dotenv import load_dotenv, find_dotenv
import os
from db.db_context import DbContextFactory, DbContext
from datetime import datetime
from fastapi import APIRouter
from surrealdb import Surreal
import asyncio

router = APIRouter()

load_dotenv(find_dotenv())
url = os.getenv('DB_URL')

auth = {
    'user': os.getenv('DB_USER'),
    'pass': os.getenv('DB_PASS')
}

db_factory = DbContextFactory(url, auth, namespace='test', database='test')


@router.get('/get-items', response_model=list[dict])
async def get_all_items():
    async with db_factory.get_context() as ctx:
        ctx: DbContext
        items = await ctx.db.select('item')
        return items
