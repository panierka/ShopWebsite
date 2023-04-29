import asyncio
from surrealdb import Surreal
from dotenv import load_dotenv, find_dotenv
import os


class DbContext:
    db: Surreal

    def __init__(self, url, auth, namespace, database):
        self.url = url
        self.auth = auth
        self.namespace = namespace
        self.database = database

    async def __aenter__(self):
        self.db = Surreal()
        await self.db.connect(self.url)
        await self.db.signin(self.auth)
        await self.db.use(self.namespace, self.database)
        return self

    async def __aexit__(self, *args):
        asyncio.ensure_future(self.db.close())


class DbContextFactory:
    def __init__(self, url, auth, namespace, database):
        self.url = url
        self.auth = auth
        self.namespace = namespace
        self.database = database

    def get_context(self):
        db = DbContext(self.url, self.auth, self.namespace, self.database)
        return db


load_dotenv(find_dotenv())
url = os.getenv('DB_URL')

auth = {
    'user': os.getenv('DB_USER'),
    'pass': os.getenv('DB_PASS')
}

db_factory = DbContextFactory(url, auth, namespace='test', database='test')
