from database import connect_to_mongodb, VENUES_COLLECTION_NAME
from venues_data import venues_details
from pymongo import MongoClient
from datetime import datetime


def create_index(collection):
    """Creates a 2dsphere index for geospatial queries."""
    try:
        collection.create_index([("location", "2dsphere")])
        print("2dsphere index created successfully.")
    except Exception as e:
        print(f"Error creating index: {e}")


def convert_date(date_str):
    """Converts date string (DD-MM-YYYY) to a datetime object."""
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print(f"Invalid date format: {date_str}")
        return None


def insert_venue(collection, venue):
    """Processes and inserts a venue into MongoDB."""
    required_fields = ["name", "longitude", "latitude", "price", "capacity", "address", "phone_number", "venue_type"]

    if not all(field in venue and venue[field] for field in required_fields):
        print(f"Skipping venue due to missing required fields: {venue.get('name', 'Unknown')}")
        return

    venue_data = {
        "name": venue["name"],
        "location": {
            "type": "Point",
            "coordinates": [float(venue["longitude"]), float(venue["latitude"])]
        },
        "available_dates": [convert_date(date) for date in venue.get("available_dates", []) if convert_date(date)],
        "price": int(venue["price"]),
        "vibes": venue.get("vibes", []),
        "capacity": int(venue["capacity"]),
        "images": venue.get("images", []),
        "videos": venue.get("videos", []),
        "amenities": venue.get("amenities", []),
        "address": venue["address"],
        "phone_number": venue["phone_number"],
        "other_contacts": venue.get("other_contacts", []),
        "venue_type": venue["venue_type"],
    }

    try:
        collection.insert_one(venue_data)
        print(f"Venue '{venue['name']}' inserted successfully.")
    except Exception as e:
        print(f"Error inserting venue '{venue['name']}': {e}")


if __name__ == "__main__":
    venues_collection = connect_to_mongodb(VENUES_COLLECTION_NAME)

    if venues_collection is not None:
        create_index(venues_collection)

        for venue in venues_details:
            insert_venue(venues_collection, venue)
