from surrealdb import Surreal


class DbContext:
    db: Surreal

    def __init__(self, url, auth):
        self.url = url
        self.auth = auth

    async def __aenter__(self):
        self.db = Surreal()
        await self.db.connect(self.url)
        await self.db.signin(self.auth)
        await self.db.use('test', 'test')
        return self

    async def __aexit__(self, *args):
        await self.db.close()


class DbContextFactory:
    def __init__(self, url, auth):
        self.url = url
        self.auth = auth

    def get_context(self):
        db = DbContext(self.url, self.auth)
        return db
