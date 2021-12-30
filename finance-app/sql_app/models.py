from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    phone_number = Column(String(50))
    hashed_password = Column(String(255))
    is_super_user = Column(Boolean, default=False)
    created_at = Column(DATETIME, default=now())
    updated_at = Column(DATETIME, nullable=True)
    created_by = Column(String(255), default='system')
    last_login_at = Column(DATETIME, nullable=True, default=None)
    is_active = Column(Boolean, default=True)


class Income(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    deposit_account = Column(String(100), nullable=True)
    date = Column(DATETIME, default=now)
    comments = Column(String(255), nullable=True)


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    budget = Column(String(100), nullable=True)
    comments = Column(String(255), nullable=True)
    date = Column(DATETIME, default=now)


class MonthlySummary(Base):
    __tablename__ = "monthlysummarys"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    total_income = Column(Float)
    total_expense = Column(Float)
    remaining_balance = Column(Float)
    month = Column(String(30))

