from db.db_context import db_factory, DbContext
from fastapi import APIRouter
from db.models.user_accounts_models import *

router = APIRouter()


@router.post('/add-user')
def add_user(form: NewAccountForm):
    print('Email: {}'
          .format(form.email))