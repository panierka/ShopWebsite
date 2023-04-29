from fastapi import FastAPI
import uvicorn
from routers import shop_items, users


app = FastAPI()
app.include_router(shop_items.router)
app.include_router(users.router)


@app.get('/message')
def get_message():
    return {
        'message': 'test'
    }


if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=False)
