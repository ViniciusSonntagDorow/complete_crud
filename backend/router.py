from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import ProductCreate, ProductUpdate, ProductResponse
from typing import List
from crud import (
    get_products,
    get_product,
    create_product,
    delete_product,
    update_product,
)


router = APIRouter()


@router.get("/products/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    return get_products(db)


@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.post("/products/", response_model=ProductResponse)
def create_one_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)


@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_one_product(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_one_product(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    db_product = update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
