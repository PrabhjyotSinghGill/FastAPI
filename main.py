from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit: int, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} PUBLISHED blogs from database'}
    else:
        return {'data': f'{limit} TOTAL blogs from database'}


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
    return request
    return{'data': f"Blog is created with title as {request.title}"}
