from sqlalchemy.orm import Session
from schemas import ProductCreate, ProductUpdate
from models import ProductModels


def get_products(db: Session):
    """
    Get all products from the database
    """
    return db.query(ProductModels).all()


def get_product(db: Session, product_id: int):
    """
    Get a product by its id
    """
    return db.query(ProductModels).filter(ProductModels.id == product_id).first()


def create_product(db: Session, product: ProductCreate):
    """
    Create a new product, pydantic data is converted to ORM data
    """
    db_product = ProductModels(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    """
    Delete a product by its id
    """
    db_product = db.query(ProductModels).filter(ProductModels.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Update a product
    """
    db_product = db.query(ProductModels).filter(ProductModels.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.category is not None:
        db_product.category = product.category

    if product.email_seller is not None:
        db_product.email_seller = product.email_seller

    db.commit()
    db.refresh(db_product)
    return db_product
