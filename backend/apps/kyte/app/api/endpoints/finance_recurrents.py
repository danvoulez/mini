from fastapi import APIRouter
router = APIRouter()

recurrents = [{"nome": "Aluguel", "valor": 1500, "tipo": "mensal"}]

@router.get("/")
def list_recurrents():
    return recurrents

@router.post("/")
def add_recurrent(data: dict):
    recurrents.append(data)
    return data