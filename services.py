from datetime import datetime
from config import BUDGET_ALLOCATION
from database import WEDDINGS_COLLECTION_NAME, SESSIONS_COLLECTION_NAME


def store_wedding_detail(user_id: str, field: str, value):
    """Stores or updates a wedding detail with the correct data type."""

    allowed_fields = ["wedding_date", "budget", "vibe", "guest_count"]

    if field not in allowed_fields:
        raise ValueError(f"Invalid field. Allowed fields: {', '.join(allowed_fields)}")

    # No conversion needed for date, it's already a `date` object
    if field in ["budget", "guest_count"]:
        try:
            value = int(value)  # Ensure integer type
            if value < 0:
                raise ValueError(f"{field.capitalize()} must be a positive number.")
        except ValueError:
            raise ValueError(f"Invalid value for {field}. It must be a positive integer.")

    # Connect to MongoDB
    weddings_collection: Collection = connect_to_mongodb(WEDDINGS_COLLECTION_NAME)

    # Update or insert the wedding detail
    weddings_collection.update_one(
        {"user_id": user_id},
        {"$set": {field: value}},
        upsert=True
    )

    return {"message": f"{field.capitalize()} updated successfully!"}


def get_wedding_detail(user_id: str, field: str):
    """Retrieves a wedding detail without altering the stored format."""

    allowed_fields = ["wedding_date", "budget", "vibe", "guest_count"]

    if field not in allowed_fields:
        raise ValueError(f"Invalid field. Allowed fields: {', '.join(allowed_fields)}.")

    # Connect to MongoDB
    weddings_collection = connect_to_mongodb(WEDDINGS_COLLECTION_NAME)
    result = weddings_collection.find_one({"user_id": user_id}, {field: 1, "_id": 0})

    if not result or field not in result:
        return {field: None}  # Explicitly return None for missing values

    return {field: result[field]}  # Return the value exactly as stored


def process_budget(budget):
    return {category: budget * percentage for category, percentage in BUDGET_ALLOCATION.items()}


from database import connect_to_mongodb, VENUES_COLLECTION_NAME
from datetime import date
from pymongo.collection import Collection
from typing import Dict, Any
from models import UserCoordinates


def process_search_venues(data: UserCoordinates) -> Dict[str, Any]:
    """Searches venues matching user's stored wedding details and geolocation within MongoDB."""

    venues_collection: Collection = connect_to_mongodb(VENUES_COLLECTION_NAME)

    # Retrieve stored wedding details
    wedding_date = get_wedding_detail(data.user_id, "wedding_date").get("wedding_date")
    budget = get_wedding_detail(data.user_id, "budget").get("budget")
    vibe = get_wedding_detail(data.user_id, "vibe").get("vibe")
    guest_count = get_wedding_detail(data.user_id, "guest_count").get("guest_count")

    # Constructing the geo query
    query: Dict[str, Any] = {
        "location": {
            "$geoWithin": {
                "$centerSphere": [[data.longitude, data.latitude], data.max_distance / 6371000]
            }
        }
    }

    failed_criteria = []

    # Ensure correct type-based queries
    if isinstance(wedding_date, date):  # Ensure we only search with a valid date object
        query["available_dates"] = {"$in": [wedding_date]}
    else:
        failed_criteria.append("wedding_date")

    if isinstance(budget, int):  # Ensure budget is an integer
        query["price"] = {"$lte": budget}
    else:
        failed_criteria.append("budget")

    if isinstance(vibe, str) and vibe.strip():  # Ensure vibe is a valid string
        query["vibes"] = {"$in": [vibe]}
    else:
        failed_criteria.append("vibe")

    if isinstance(guest_count, int):  # Ensure guest_count is an integer
        query["capacity"] = {"$gte": guest_count}
    else:
        failed_criteria.append("guest_count")

    try:
        # Search for venues in MongoDB
        results = list(venues_collection.find(query, {"_id": 0}))

        if not results:
            return {
                "message": f"No venues found matching the criteria. Failed criteria: {', '.join(failed_criteria) if failed_criteria else 'None'}"
            }

        return {
            "message": "Great! You're almost there! Now, please explore the venue options, manage the guest list, or select an invitation.",
            "venues": results
        }

    except Exception as e:
        return {"error": f"Error during search: {e}"}


def store_user_session(user_id: str, user_name: str):
    sessions_collection = connect_to_mongodb(SESSIONS_COLLECTION_NAME)

    session_data = {
        "user_id": user_id,
        "user_name": user_name,
        "last_active": datetime.utcnow(),
    }

    sessions_collection.update_one(
        {"user_id": user_id},
        {"$set": session_data},
        upsert=True
    )

    return {"message": f"Session stored for {user_name}."}
