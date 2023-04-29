from db.db_context import db_factory, DbContext
from fastapi import APIRouter

router = APIRouter()


@router.post('/add-user')
def add_user(item):
    print(item)
