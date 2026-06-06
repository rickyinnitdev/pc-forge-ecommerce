from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import CartItem, Product
from app.schemas import CartItemCreate, CartItemOut, CartItemUpdate


router = APIRouter(prefix="/cart", tags=["Cart"])


@router.get("/{session_id}", response_model=list[CartItemOut])
def get_cart(session_id: str, db: Session = Depends(get_db)):
    return db.query(CartItem).filter(CartItem.session_id == session_id).all()


@router.post("", response_model=CartItemOut, status_code=status.HTTP_201_CREATED)
def add_to_cart(payload: CartItemCreate, session_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    cart_item = (
        db.query(CartItem)
        .filter(CartItem.session_id == session_id, CartItem.product_id == payload.product_id)
        .first()
    )
    if cart_item:
        cart_item.quantity += payload.quantity
    else:
        cart_item = CartItem(session_id=session_id, product_id=payload.product_id, quantity=payload.quantity)
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)
    return cart_item


@router.put("/{cart_item_id}", response_model=CartItemOut)
def update_cart_item(cart_item_id: int, payload: CartItemUpdate, db: Session = Depends(get_db)):
    cart_item = db.query(CartItem).filter(CartItem.id == cart_item_id).first()
    if not cart_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart item not found")
    cart_item.quantity = payload.quantity
    db.commit()
    db.refresh(cart_item)
    return cart_item


@router.delete("/{cart_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_cart_item(cart_item_id: int, db: Session = Depends(get_db)):
    cart_item = db.query(CartItem).filter(CartItem.id == cart_item_id).first()
    if not cart_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart item not found")
    db.delete(cart_item)
    db.commit()
