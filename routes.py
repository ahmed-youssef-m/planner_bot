from datetime import datetime

from fastapi import APIRouter, HTTPException
from starlette.responses import HTMLResponse
from config import WEDDING_VIBES, INVITATION_TEMPLATES, html_file_path
from gemini import send_message
from models import BudgetInput, InvitationInput, ChatInput, GuestCountInput, VibeInput, WeddingDateInput, \
    UserCoordinates
from services import process_budget, process_search_venues, store_wedding_detail, store_user_session

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def serve_html():
    if not html_file_path.exists():
        return HTMLResponse(content="<h1>Error: index.html not found</h1>", status_code=404)

    html_content = html_file_path.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)


@router.get("/welcome/{user_id}/{user_name}")
def welcome_user(user_id: str, user_name: str):
    store_user_session(user_id, user_name)
    return {"message": f"Welcome {user_name}! I am your assistant bot to help you plan your wedding."}


@router.post("/ask_ai")
def ask_ai(data: ChatInput):
    try:
        if not data.user_input.strip():
            raise HTTPException(status_code=400, detail="User input cannot be empty.")
        return {"response": send_message(data.user_input)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {e}")


@router.get("/ask_wedding_date")
def ask_wedding_date():
    return {"message": "Start planning your dream day now! 💍🎊 When is your wedding date?"}


@router.post("/set_wedding_date")
def set_wedding_date(data: WeddingDateInput):
    store_wedding_detail(data.user_id, "wedding_date", datetime.combine(data.wedding_date, datetime.min.time()))
    return {"message": f"Great! Now, what is your wedding budget?"}


@router.post("/set_budget")
def set_budget(data: BudgetInput):
    store_wedding_detail(data.user_id, "budget", data.budget)
    return {"allocations": process_budget(data.budget)}


@router.get("/ask_vibes")
def ask_vibes():
    return {"message": "What is your preferred wedding vibe?", "vibes": WEDDING_VIBES}


@router.post("/set_vibe")
def set_vibe(data: VibeInput):
    store_wedding_detail(data.user_id, "vibe", data.vibe)
    return {"message": f"'{data.vibe}' is a great choice! Now, how many guests will you invite?"}


@router.post("/select_venue")
def select_venue(data: UserCoordinates, data_1: GuestCountInput):
    store_wedding_detail(data_1.user_id, "guest_count", data_1.guest_count)
    return process_search_venues(data)


@router.get("/get_invitation_templates")
def get_invitation_templates():
    return {
        "message": "Choose from our beautifully designed invitation templates.",
        "templates": INVITATION_TEMPLATES
    }


@router.post("/set_invitation")
def set_invitation(data: InvitationInput):
    return {"message": f"'{data.template_name}' template is a great choice! Now you're ready to send it."}


@router.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon set."}
