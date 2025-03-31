from fastapi import APIRouter
router = APIRouter()

ui_settings = {
    "theme": "dark",
    "timezone": "Europe/Lisbon",
    "language": "pt-PT"
}

@router.get("/")
def get_ui_settings():
    return ui_settings

@router.put("/")
def update_ui_settings(new: dict):
    ui_settings.update(new)
    return ui_settings