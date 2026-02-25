logs = [
    "101,Ratchita,9,2",
    "102,Arjun,8,5",
    "103,Meena,10,1",
    "104,Kiran,7,3"
]

productivity_dict = {}

for log in logs:
    data = log.split(",")
    
    emp_id = int(data[0])
    name = data[1]
    login_hours = int(data[2])
    idle_hours = int(data[3])
    
    productivity = login_hours - idle_hours
    productivity_dict[name] = productivity

print("Productivity Report:", productivity_dict)

# Top Performer
top_employee = max(productivity_dict, key=productivity_dict.get)
print("Top Performer:", top_employee)

# Average Productivity (NEW FEATURE)
average_productivity = sum(productivity_dict.values()) / len(productivity_dict)
print("Average Productivity:", average_productivity)

# Performance Rating (NEW FEATURE)
print("\nPerformance Ratings:")
for name, hours in productivity_dict.items():
    if hours >= 7:
        rating = "High Performer"
    elif hours >= 4:
        rating = "Medium Performer"
    else:
        rating = "Low Performer"
    
    print(name, "->", rating)

# Employees below 4 hours
print("\nEmployees below 4 hours productivity:")
for name, hours in productivity_dict.items():
    if hours < 4:
        print(name)