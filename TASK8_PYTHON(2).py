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

top_employee = max(productivity_dict, key=productivity_dict.get)
print("Top Performer:", top_employee)

print("Employees below 4 hours productivity:")
for name, hours in productivity_dict.items():
    if hours < 4:
        print(name)