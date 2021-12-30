# from typing import Optional, List
#
# from fastapi import FastAPI, Query, Path, Body
# from enum import Enum
#
# from pydantic import Field
# from pydantic.main import BaseModel
# from uuid import UUID
# app = FastAPI()
#
#
# class EnvServer(str, Enum):
#     sit = "sit"
#     uat = "uat"
#     prod = "prod"
#
#
#
#
# # @app.get("/")
# # async def root():
# #     return {"message": "Hello World"}
# #
# #
# # @app.get("/items/{item_id}")
# # async def read_item(item_id: int):
# #     return {"item_id": item_id}
# #
# #
# # @app.get("/users/me")
# # async def read_user_me():
# #     return {"user_id": "the current user"}
# #
# #
# # @app.get("/users/{user_id}")
# # async def read_user(user_id: str):
# #     return {"user_id": user_id}
# #
# #
# # @app.get("/models/{env}")
# # async def get_server_env(env: EnvServer):
# #     if env.value == EnvServer.sit:
# #         return {"ENV": EnvServer.sit, "Config": EnvServer, "message": "Testing ENV !"}
# #     if env.value == EnvServer.uat:
# #         return {"ENV": EnvServer.uat, "Config": EnvServer, "message": "Staging ENV !"}
# #     if env.value == EnvServer.prod:
# #         return {"ENV": EnvServer.prod, "Config": EnvServer, "message": "PROD ENV !"}
# #
# #     return {"ENV": "not found", "message": "Error"}
#
# #
# # @app.get("/item/{item_ids}")
# # async def read_user_item(item_ids: str, needy: str):
# #     item = {"item_id": item_ids, "needy": needy}
# #     return item
# #
# #
# # @app.get("/items/{item_ids}")
# # async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
# #     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
# #     return item
# #
# # fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# #
# #
# # @app.get("/items/")
# # async def read_item(skip: int = 0, limit: int = 10):
# #     return fake_items_db[skip : skip + limit]
#
#
# class Image(BaseModel):
#     url: str
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(..., gt=1000, description="The price must be greater than zero")
#     tax: Optional[float] = None
#     # tags: list = []
#     # image: Optional[List[Image]] = None
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             }
#         }
#
#
# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None
#
#
#
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     price_with_tax = item.price + item.tax
#     item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
#
# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}
#
#
# @app.put("/items_/{item_id}")
# async def create_item(item_id: int, item: Item, q: Optional[str] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result
#
#
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query("fixedquery", min_length=3, max_length=50, regex="^fixedquery$",
#                                               )):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
#
# @app.get("/items_list/")
# async def read_items(q: Optional[List[str]] = Query(None,
#                                                     title="Query string",
#                                                     description="Query string for the items to search in the database that have a good match"
#                                                     )):
#     query_items = {"q": q}
#     return query_items
#
#
# @app.get("/items_valid/{item_id}")
# async def read_items(
#     *, item_id: int = Path(..., title="The ID of the item to get", gt=1, le=100), q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results
#
#
# @app.put("/items_multi/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
#     q: Optional[str] = None,
#     item: Optional[Item] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results
#
# import uuid
# @app.put("/items_body/{item_id}")
# async def update_item(item_id: int, item: Item, user: User, importance: int = Body(...)):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance, "test": uuid.uuid4()}
#     return results

#
# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer
#
# app = FastAPI()
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
#
# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}


# from database import Base
# from datetime import datetime, timedelta
# from typing import Optional
#
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
#
# from passlib.context import CryptContext
#
# from pydantic import BaseModel
#
# # to get a string like this run:
# # openssl rand -hex 32
# SECRET_KEY = "4b60e888dc1abccaf7c75c93c4ea15119a0c0964c8fce7abaf04553ead7cdffb"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
#
#
# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     }
# }
#
#
# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
#
# class TokenData(BaseModel):
#     username: Optional[str] = None
#
#
# class User(Base):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None
#
#
# class UserInDB(User):
#     hashed_password: str
#
#
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
# app = FastAPI()
#
#
#
# def verify_password(plain_password, hashed_password):
#
#     return pwd_context.verify(plain_password, hashed_password)
#
#
#
#
# def get_password_hash(password):
#
#     return pwd_context.hash(password)
#
#
#
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#
#
#
# def authenticate_user(fake_db, username: str, password: str):
#
#     user = get_user(fake_db, username)
#
#     if not user:
#
#         return False
#
#     if not verify_password(password, user.hashed_password):
#
#         return False
#
#     return user
#
#
#
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
#
#
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user
#
#
# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
#
#
# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
#
#
# @app.get("/users/me/", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user
#
#
# @app.get("/users/me/items/")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
from sql_app.models import Income
from sql_app.crud import update_summary
import datetime

models.Base.metadata.create_all(bind=engine)




app = FastAPI()


class IncomePatch(BaseModel):
    amount: Optional[float]
    deposit_account: Optional[str]
    date: Optional[datetime.datetime]
    comments: Optional[str]


class ExpensePatch(BaseModel):
    amount: Optional[float]
    budget: Optional[str]
    date: Optional[datetime.datetime]
    comments: Optional[str]


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/income/{user_id}", response_model=schemas.AddIncome)
def create_income_for_user(
        user_id: int, income: schemas.AddIncome, db: Session = Depends(get_db)
):
    return crud.create_income(db=db, income=income, user_id=user_id)


@app.get("/users/income/{user_id}")
def get_income_of_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user:
        return crud.get_income(db=db, user_id=user_id)
    else:
        return None


@app.patch("/users/income/{user_id}/{income_id}")
def patch_income_of_user(income_id: int, user_id: int, item: IncomePatch, db: Session = Depends(get_db)):
    instance = crud.get_income_for_update(db, user_id, income_id)
    for k, v in item:
        if instance.customer_id == user_id:
            if k == 'amount':
                instance.amount = v
            if k == 'date':
                instance.date = v
            if k == 'comments':
                instance.comments = v
            if k == 'deposit_account':
                instance.deposit_account = v
    db.commit()
    update_summary(db, user_id)
    return instance


@app.delete("/users/income/{user_id}/{income_id}")
def delete_income(income_id: int, user_id: int, db: Session = Depends(get_db)):
    instance = crud.delete_income(db, user_id, income_id)
    if instance:
        return True
    else:
        return False


@app.post("/users/expense/{user_id}")
def create_expense_for_user(user_id: int, expense: schemas.AddExpense, db: Session = Depends(get_db)):
    return crud.create_expense(db=db, expense=expense, user_id=user_id)


@app.get("/users/expense/{user_id}")
def get_expense_of_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user:
        return crud.get_expense(db=db, user_id=user_id)
    else:
        return None


@app.patch("/users/expense/{user_id}/{expense_id}")
def patch_expense_of_user(expense_id: int, user_id: int, item: ExpensePatch, db: Session = Depends(get_db)):
    instance = crud.get_expense_for_update(db, user_id, expense_id)
    for k, v in item:
        if instance.customer_id == user_id:
            if k == 'amount':
                instance.amount = v
            if k == 'date':
                instance.date = v
            if k == 'comments':
                instance.comments = v
            if k == 'budget':
                instance.budget = v
    db.commit()
    update_summary(db, user_id)
    return item


@app.delete("/users/expense/{user_id}/{expense_id}")
def delete_expense(expense_id: int, user_id: int, db: Session = Depends(get_db)):
    instance = crud.delete_expense(db, user_id, expense_id)
    if instance:
        return True
    else:
        return False


@app.get("/users/monthly/summary/{user_id}")
def get_monthly_summary(user_id: int, db: Session = Depends(get_db)):
    values = crud.get_summary(db, user_id)
    return values


