from fastapi import APIRouter
router = APIRouter()

expenses = []

@router.post("/")
def create_expense(item: dict):
    expenses.append(item)
    return item

@router.get("/")
def list_expenses():
    return expenses