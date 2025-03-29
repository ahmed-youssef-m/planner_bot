# # weddings_collection = connect_to_mongodb("weddings")
#
# # weddings_collection.update_one(
# #     {"user_id": "test_user"},
# #     {"$set": {
# #         "wedding_date": datetime.combine(date(2025, 5, 1), datetime.min.time()),  # Convert date to datetime
# #         "budget": 6000,
# #         "vibe": "Modern Chic",
# #         "guest_count": 30
# #     }},
# #     upsert=True
# # )
# # print("Test wedding details inserted!")
#
#
# test_data = UserCoordinates(
#     user_id="test_user",
#     latitude=30.096235507792155,
#     longitude=31.09650550263469,
#     max_distance=200000  # 200 km
# )
#
# result = process_search_venues(test_data)
# print(result)