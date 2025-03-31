from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def get_cashflow(from_date: str = None, to_date: str = None):
    return {
        "entrada": 18000,
        "saida": 5600,
        "saldo": 12400,
        "periodo": {"from": from_date, "to": to_date}
    }