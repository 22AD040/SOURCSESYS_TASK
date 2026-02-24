users = [
    ("101", "Ratchita", "23"),
    ("102", "Arjun", "17"),
    ("101", "Ratchita", "23"),  
    ("103", "Meena", "29")
]

cleaned_users = {}
seen_ids = set()

for user in users:
    user_id = user[0]
    name = user[1]
    age = int(user[2])   
    
    if user_id not in seen_ids and age > 18:
        cleaned_users[user_id] = {
            "name": name,
            "age": age
        }
        seen_ids.add(user_id)

print("Cleaned Dataset:", cleaned_users)