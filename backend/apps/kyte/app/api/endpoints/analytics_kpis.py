from fastapi import APIRouter
router = APIRouter()

@router.get("/kpis")
def get_kpis(from_date: str = None, to_date: str = None):
    return {
        "faturamento_liquido": 15600,
        "ticket_medio": 52.2,
        "mais_vendidos": ["Camiseta", "Cueca", "Shorts"],
        "clientes_fieis": ["João", "Maria"],
        "custo_operacional": 3120,
        "vendas_por_canal": {"WhatsApp": 22, "Balcão": 18, "Instagram": 9}
    }