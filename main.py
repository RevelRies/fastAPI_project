from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hellow Word'}

@app.get('/url_name/')
def get_item(name, message):
    return f'Hello {name}! {message}!'


if __name__ == '__main__':
    uvicorn.run('hello:app', port=8000, host='127.3.5.1', reload=True)