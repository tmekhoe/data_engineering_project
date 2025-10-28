from sqlalchemy import create_engine, text

DATABASE_URL = "mysql+pymysql://myuser:mypassword@localhost:3306/mydatabase"

engine = create_engine(DATABASE_URL, echo=True, pool_size=5, max_overflow=10)

with engine.connect() as connection:
    result = connection.execute(text("SELECT VERSION()"))
print(f"Database version:{result.scalar()}")

# with engine.connect() as conn:
#     conn.execute(text("INSERT INTO users (username, email) VALUES (:username, :email)"),
#                  {"username":"test","email":"test@example.com"})
#     conn.commit()

from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, create_engine
from datetime import datetime

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False, unique=True),
    Column("email", String(100), nullable=False),
    Column("created_at", DateTime, default=datetime.utcnow),
)
