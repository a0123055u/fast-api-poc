from sqlalchemy.orm import Session

from .import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    phone_number = user.phone_number
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password, phone_number=phone_number, )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_income(db: Session, income: schemas.AddIncome, user_id: int):
    amount = income.amount
    dep_acct = income.deposit_account
    date = income.date
    comments = income.comments
    user_id_ = get_user(db, user_id)
    if user_id_:
        db_income = models.Income(customer_id=user_id, amount=amount, deposit_account=dep_acct, comments=comments,
                                  date=date)
        db.add(db_income)
        db.commit()
        db.refresh(db_income)
        update_summary(db, user_id)
        return db_income
    else:
        return None


def get_income(db: Session, user_id: int):
    return db.query(models.Income).filter(models.Income.customer_id == user_id).all()


def get_income_for_update(db: Session, user_id: int, income_id: int):
    return db.query(models.Income).get(income_id)


def delete_income(db: Session, user_id: int, income_id: int):
    print("income_id--", income_id)
    print("customer_id--", user_id)
    instance = db.query(models.Income).get(income_id)
    print(instance.customer_id, user_id)
    if instance.customer_id == user_id:
        db.delete(instance)
        db.commit()
        update_summary(db, user_id)
        return True
    else:
        return False


def create_expense(db: Session, expense: schemas.AddExpense, user_id: int):
    amount = expense.amount
    budget = expense.budget
    date = expense.date
    comments = expense.comments
    user_id_ = get_user(db, user_id)
    if user_id_:
        db_expense = models.Expense(customer_id=user_id, amount=amount, budget=budget, comments=comments, date=date)
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        update_summary(db, user_id)
        return db_expense
    else:
        return None


def get_expense(db: Session, user_id: int):
    return db.query(models.Expense).filter(models.Expense.customer_id == user_id).all()


def get_expense_for_update(db: Session, user_id: int, expense_id: int):
    return db.query(models.Expense).get(expense_id)


def delete_expense(db: Session, user_id: int, expense_id: int):
    print("expense_id--", expense_id)
    print("customer_id--", user_id)
    instance = db.query(models.Expense).get(expense_id)
    print("OBJ id ", instance.id)
    print(instance.customer_id, user_id)
    if instance.customer_id == user_id:
        db.delete(instance)
        db.commit()
        update_summary(db, user_id)
        return True
    else:
        return False


def update_summary(db: Session, user_id: int):
    incomes = db.query(models.Income).filter(models.Income.customer_id == user_id).all()
    user_income = 0
    user_expense = 0
    for x in incomes:
        user_income += x.amount
        print(x)
    expenses = db.query(models.Expense).filter(models.Expense.customer_id == user_id).all()
    for x in expenses:
        user_expense += x.amount
        print(x)
    balance = user_income - user_expense
    db_summary = models.MonthlySummary(total_income=user_income, total_expense=user_expense, month="test",
                                       remaining_balance=balance, customer_id=user_id)
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)
    return db_summary
    pass


def get_summary(db: Session, user_id: int):
    qry = db.query(models.MonthlySummary).filter(models.MonthlySummary.customer_id == user_id).all()
    length = len(qry)
    instance = qry[length - 1] if length > 0 else None
    if instance:
        return instance
    else:
        return None
