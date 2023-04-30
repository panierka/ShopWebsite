from db.db_context import db_factory
from fastapi import APIRouter
from db.models.user_accounts_models import *
from datetime import datetime

router = APIRouter()


@router.post('/add-user')
async def add_user(form: NewAccountForm):
    new_user = UserAccount(
        email=form.email,
        join_time=datetime.now().strftime('%m/%d/%Y %H:%M')
    )
    async with db_factory.get_context() as ctx:
        await ctx.db.create('user', new_user.dict())


@router.post('/user-exists')
async def does_user_exist(user_identifier: UserAccountIdentifier):
    email = user_identifier.email
    query = 'SELECT count(email="{}") FROM user GROUP ALL;'.format(email)
    async with db_factory.get_context() as ctx:
        results = await ctx.db.query(query)
        count = results[0]['result'][0]['count']
        return {
            'unique': count > 0
        }
