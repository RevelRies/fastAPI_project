from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return 'Special for Rekruto'

@app.get('/url_name/')
def get_item(name, message):
    return f'Hello {name}! {message}!'

if __name__ == '__main__':
    uvicorn.run('hello:app', port=4561, host='127.0.0.1', reload=True)
