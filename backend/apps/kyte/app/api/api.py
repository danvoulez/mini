
from app.api.endpoints import (
    settings_ui, settings_company, analytics_kpis,
    finance_expenses, finance_recurrents, finance_cashflow, finance_categories
)

api_router.include_router(settings_ui.router, prefix="/settings/ui", tags=["Settings"])
api_router.include_router(settings_company.router, prefix="/settings/company", tags=["Settings"])
api_router.include_router(analytics_kpis.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(finance_expenses.router, prefix="/finance/expenses", tags=["Finance"])
api_router.include_router(finance_recurrents.router, prefix="/finance/recurrents", tags=["Finance"])
api_router.include_router(finance_cashflow.router, prefix="/finance/cashflow", tags=["Finance"])
api_router.include_router(finance_categories.router, prefix="/finance/categories", tags=["Finance"])
