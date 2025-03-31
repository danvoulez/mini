from fastapi import APIRouter
router = APIRouter()

company = {"name": "VoulezVous", "logo": "vv.png"}

@router.put("/")
def update_company(data: dict):
    company.update(data)
    return company