from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from db_config import session, engine
import db_models
from sqlalchemy.orm import Session

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

db_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to FastAPI Tutorial"

products = [
    Product(id=1, name="Laptop", description="A high performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=599.99, quantity=20),
    Product(id=3, name="Headphones", description="Noise cancelling headphones", price=199.99, quantity=15),
    Product(id=4, name="Monitor", description="4K UHD Monitor", price=299.99, quantity=8),
    Product(id=5, name="Keyboard", description="Mechanical keyboard", price=89.99, quantity=25),
    Product(id=6, name="Mouse", description="Wireless mouse", price=49.99, quantity=30)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(db_models.Product).count
    if count == 0:
        for p in products:
            db.add(db_models.Product(**p.model_dump()))
        db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(db_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product Not Found"

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(db_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        db.query(db_models.Product).filter(db_models.Product.id == id).update(product.model_dump())
        db.commit()
        return "Product Updated Successfully"
    return "Product Not Found"

@app.delete("/products")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted"
    return "Product not found"