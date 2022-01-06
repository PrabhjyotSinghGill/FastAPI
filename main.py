from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog/{id}')
def index(id:int):
    #only get 10 published blogs
    return {'data':id}
    if published:
        return{'data':f'{limit} PUBLISHED blogs from the database'}
    else:
        return{'data':f'{limit} ALL blogs from the database'}


@app.get('/blog/unpublished')
def unpublished():
    return{'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return{'data': f"Blog is created with title as {request.title}"}
