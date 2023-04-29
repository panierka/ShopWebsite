from db.db_context import db_factory, DbContext
from fastapi import APIRouter

router = APIRouter()


@router.get('/get-items', response_model=list[dict])
async def get_all_items():
    async with db_factory.get_context() as ctx:
        ctx: DbContext
        items = await ctx.db.select('item')
        return items
