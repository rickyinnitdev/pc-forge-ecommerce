from sqlalchemy.orm import Session

from app.auth import get_password_hash
from app.models import Product, User


SAMPLE_PRODUCTS = [
    {
        "name": "CyberPowerPC Gamer Supreme RTX 4070",
        "category": "Gaming PCs",
        "price": 1899.99,
        "description": "High-performance gaming desktop with Intel Core i7, RTX 4070, 32GB RAM, and 1TB NVMe SSD.",
        "image_url": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 14,
    },
    {
        "name": "MSI Aegis R2 Gaming Tower",
        "category": "Gaming PCs",
        "price": 2099.00,
        "description": "Premium gaming PC with liquid cooling, Intel Core i9, RTX 4080, and fast DDR5 memory.",
        "image_url": "https://images.unsplash.com/photo-1593640408182-31c70c8268f5?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 9,
    },
    {
        "name": "NZXT Player One Prime",
        "category": "Gaming PCs",
        "price": 1599.50,
        "description": "Compact gaming setup featuring Ryzen 7 processor, RTX 4060 Ti, and 16GB RAM for smooth gameplay.",
        "image_url": "https://images.unsplash.com/photo-1624705002806-5d72df19c3f0?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 21,
    },
    {
        "name": "ASUS ROG Strix G16 Battle Station",
        "category": "Gaming PCs",
        "price": 2399.99,
        "description": "Extreme gaming rig with RTX 4090 graphics, Intel i9 processor, RGB chassis, and advanced cooling.",
        "image_url": "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 6,
    },
    {
        "name": "Dell OptiPlex 7010 Office Desktop",
        "category": "Office PCs",
        "price": 749.99,
        "description": "Reliable office desktop with Intel i5 CPU, 16GB RAM, and 512GB SSD for daily productivity.",
        "image_url": "https://images.unsplash.com/photo-1517336714739-489689fd1ca8?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 30,
    },
    {
        "name": "HP ProDesk 400 G9 Workstation",
        "category": "Office PCs",
        "price": 899.00,
        "description": "Business-class workstation designed for multitasking, reports, and video meetings.",
        "image_url": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 25,
    },
    {
        "name": "Lenovo ThinkCentre M90s",
        "category": "Office PCs",
        "price": 979.00,
        "description": "Compact and quiet office desktop with strong performance for accounting and admin tasks.",
        "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 18,
    },
    {
        "name": "NVIDIA GeForce RTX 4070 Ti Super",
        "category": "Components",
        "price": 799.00,
        "description": "Latest generation GPU for high-refresh 1440p gaming, ray tracing, and streaming workflows.",
        "image_url": "https://images.unsplash.com/photo-1591489378430-ef2f4c626b35?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 40,
    },
    {
        "name": "AMD Ryzen 7 7800X3D Processor",
        "category": "Components",
        "price": 399.00,
        "description": "Top-rated gaming CPU with 3D V-Cache technology, excellent efficiency, and strong frame rates.",
        "image_url": "https://images.unsplash.com/photo-1555617778-02518510b9fa?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 52,
    },
    {
        "name": "Corsair Vengeance DDR5 32GB Kit",
        "category": "Components",
        "price": 149.99,
        "description": "High-speed DDR5 memory kit, ideal for gaming rigs and creative workloads.",
        "image_url": "https://images.unsplash.com/photo-1562976540-1502c2145186?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 64,
    },
    {
        "name": "LG UltraGear 27-inch QHD Monitor",
        "category": "Accessories",
        "price": 329.99,
        "description": "27-inch gaming monitor with 165Hz refresh rate and IPS panel for smooth, vivid visuals.",
        "image_url": "https://images.unsplash.com/photo-1527443195645-1133f7f28990?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 20,
    },
    {
        "name": "Logitech G Pro Mechanical Keyboard",
        "category": "Accessories",
        "price": 129.99,
        "description": "Tournament-grade mechanical keyboard with fast switches and durable compact frame.",
        "image_url": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?auto=format&fit=crop&w=1200&q=80",
        "stock_quantity": 34,
    },
]


def seed_initial_data(db: Session) -> None:
    admin_email = "admin@pcforge.com"
    existing_admin = db.query(User).filter(User.email == admin_email).first()
    if not existing_admin:
        admin = User(
            email=admin_email,
            full_name="Store Admin",
            hashed_password=get_password_hash("Admin@12345"),
            role="admin",
        )
        db.add(admin)

    product_count = db.query(Product).count()
    if product_count == 0:
        for product_data in SAMPLE_PRODUCTS:
            db.add(Product(**product_data))

    db.commit()
