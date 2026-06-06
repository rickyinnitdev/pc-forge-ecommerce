from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class Token(BaseModel):
    access_token: str
    token_type: str


class AdminLogin(BaseModel):
    email: EmailStr
    password: str


class ProductBase(BaseModel):
    name: str
    category: str
    price: float = Field(gt=0)
    description: str
    image_url: str
    stock_quantity: int = Field(ge=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    description: Optional[str] = None
    image_url: Optional[str] = None
    stock_quantity: Optional[int] = Field(default=None, ge=0)


class ProductOut(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class CartItemUpdate(BaseModel):
    quantity: int = Field(gt=0)


class CartItemOut(BaseModel):
    id: int
    session_id: str
    quantity: int
    product: ProductOut

    class Config:
        from_attributes = True


class CheckoutRequest(BaseModel):
    session_id: str
    customer_name: str
    customer_email: EmailStr
    address: str
    city: str
    zip_code: str


class OrderItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float
    product: ProductOut

    class Config:
        from_attributes = True


class OrderOut(BaseModel):
    id: int
    customer_name: str
    customer_email: EmailStr
    address: str
    city: str
    zip_code: str
    status: str
    total_amount: float
    created_at: datetime
    items: List[OrderItemOut]

    class Config:
        from_attributes = True


class OrderStatusUpdate(BaseModel):
    status: str


class DashboardMetrics(BaseModel):
    total_sales: float
    total_orders: int
    total_products: int
    low_stock_count: int
