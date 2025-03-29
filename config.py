from pathlib import Path

html_file_path = Path(__file__).parent / "index.html"

BUDGET_ALLOCATION = {
    "Venue": 0.35,  # (Hotels, banquet halls, outdoor spaces)
    "Food": 0.20,  # (Catering, buffet, or plated dinner)
    "Entertainment": 0.10,  # (DJ, band, or singer)
    "Bride_groom_attire": 0.08,  # (Wedding dress & groom's suit)
    "Makeup_hair": 0.05,  # (Makeup artist & hairstylist)
    "Photography_videography": 0.10,  # (Photographer & videographer)
    "Session_photo_place": 0.04,  # (Special location for photoshoot)
    "Getting_ready_place": 0.05,  # (Hotel room or bridal suite)
    "Miscellaneous": 0.03  # (Unexpected expenses, gifts, etc.)
}

WEDDING_VIBES = [
    {"name": "Classic Elegance", "image": "https://example.com/classic.jpg"},
    {"name": "Rustic Charm", "image": "https://example.com/rustic.jpg"},
    {"name": "Modern Chic", "image": "https://example.com/modern.jpg"},
    {"name": "Bohemian", "image": "https://example.com/boho.jpg"},
    {"name": "Romantic Fairytale", "image": "https://example.com/fairytale.jpg"}
]

INVITATION_TEMPLATES = [
    {"name": "Elegant Gold", "image": "https://example.com/elegant_gold.jpg"},
    {"name": "Floral Romance", "image": "https://example.com/floral_romance.jpg"},
    {"name": "Modern Minimalist", "image": "https://example.com/modern_minimalist.jpg"},
    {"name": "Rustic Charm", "image": "https://example.com/rustic_charm.jpg"},
    {"name": "Vintage Classic", "image": "https://example.com/vintage_classic.jpg"}
]

sys_instruct = (
    "You're an AI wedding planner. Keep responses concise and to the point. "
    "Start by asking for the wedding date, budget, and theme preferences in a brief, engaging way."
    "IF you asked any question answer it shortly"
)