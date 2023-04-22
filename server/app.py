from fastapi import FastAPI
import data_access as da

import uvicorn

app = FastAPI()


@app.get('/message')
def get_message():
    return {
        'message': 'test'
    }


@app.get('/get-items')
async def get_items():
    return await da.get_all_items()


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
