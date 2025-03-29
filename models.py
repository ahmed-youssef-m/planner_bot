from datetime import date
from pydantic import BaseModel


class UserSession(BaseModel):
    user_id: str
    name: str


class ChatInput(BaseModel):
    user_id: str
    user_input: str


class WeddingDateInput(BaseModel):
    user_id: str
    wedding_date: date


class BudgetInput(BaseModel):
    user_id: str
    budget: float


class VibeInput(BaseModel):
    user_id:str
    vibe: str


class GuestCountInput(BaseModel):
    user_id: str
    guest_count: int


class UserCoordinates(BaseModel):
    user_id:str
    latitude: float
    longitude: float
    max_distance: int


class InvitationInput(BaseModel):
    user_id: str
    template_name: str
