import datetime
from typing import List, Optional


from pydantic import BaseModel


class UserBase(BaseModel):

    email: str


class UserCreate(UserBase):

    password: str
    phone_number: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class IncomeBase(BaseModel):
    deposit_account: str
    amount: float
    date: datetime.datetime
    comments: str


class AddIncome(IncomeBase):

    class Config:
        orm_mode = True


class ExpenseBase(BaseModel):
    amount: float
    comments: str
    date: datetime.datetime
    budget: str


class AddExpense(ExpenseBase):
    class Config:
        orm_mode = True





