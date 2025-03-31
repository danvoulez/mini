from fastapi import APIRouter
router = APIRouter()

categories = ["Alimentação", "Tecnologia", "Fornecedores", "Marketing"]

@router.get("/")
def list_categories():
    return categories

@router.post("/")
def add_category(name: str):
    categories.append(name)
    return {"added": name}