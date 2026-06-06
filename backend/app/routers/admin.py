from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.auth import get_current_admin
from app.database import get_db
from app.models import Order, Product
from app.schemas import DashboardMetrics, ProductOut


router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/dashboard", response_model=DashboardMetrics)
def get_dashboard_metrics(db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    total_sales = db.query(func.coalesce(func.sum(Order.total_amount), 0.0)).scalar() or 0.0
    total_orders = db.query(func.count(Order.id)).scalar() or 0
    total_products = db.query(func.count(Product.id)).scalar() or 0
    low_stock_count = db.query(func.count(Product.id)).filter(Product.stock_quantity < 10).scalar() or 0

    return DashboardMetrics(
        total_sales=float(total_sales),
        total_orders=int(total_orders),
        total_products=int(total_products),
        low_stock_count=int(low_stock_count),
    )


@router.get("/inventory", response_model=list[ProductOut])
def inventory(db: Session = Depends(get_db), _: str = Depends(get_current_admin)):
    return db.query(Product).order_by(Product.stock_quantity.asc()).all()
