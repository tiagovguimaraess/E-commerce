from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

class Product(BaseModel):
    Id: Optional[str]
    Name: str
    Value: float
    Descripition: str
    Available: bool

banco: List[Product] = []

@app.post('/product')
def CreateProduct(product: Product):
    product.Id = str(uuid4())
    banco.append(product)
    return {'Registered product.'}

@app.get('/product')
def product():
    return banco

@app.get('/product/{Id}')
def ObtainProduct(Id: str):
    for product in banco:
        if product.Id == Id:
            return product
    return {'Product not found'}

@app.delete('/product/deletar/{Id}')
def ProductDelete(Id: str):
    position = -1
    for index, product in enumerate(banco):
        if product.Id == Id:
            position = index
            break
    if position != -1:
        banco.pop(position)
        return {'Product deletado.'}
    else:
        return {'Product not found'}


