from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hellow Word'}

@app.get('/url_name/')
def get_item(name, message):
    return f'Hello {name}! {message}!'


