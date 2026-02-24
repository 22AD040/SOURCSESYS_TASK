employees = [
    ("101", "Ratchita", "9", "2", "Python,SQL,Machine Learning"),
    ("102", "Arjun", "8", "5", "Java,SQL"),
    ("103", "Meena", "10", "1", "Python,Deep Learning,SQL"),
    ("104", "Kiran", "6", "4", "Python"),
    ("101", "Ratchita", "9", "2", "Python,SQL,Machine Learning") 
]

feedback = {
    "101": "Amazing performance and excellent delivery",
    "102": "Work quality is poor and bad response",
    "103": "Great and powerful execution",
    "104": "Average work but not bad"
}

required_skills = {"Python", "SQL", "Machine Learning", "Deep Learning"}

positive_words = {"amazing", "excellent", "great", "powerful"}
negative_words = {"bad", "poor", "worst"}


cleaned_data = {}
seen_ids = set()

for emp in employees:
    emp_id = emp[0]
    name = emp[1]
    login_hours = int(emp[2])      
    idle_hours = int(emp[3])
    skills = emp[4].split(",")     
    
    if emp_id not in seen_ids:
        cleaned_data[emp_id] = {
            "name": name,
            "login": login_hours,
            "idle": idle_hours,
            "skills": set(skills)  
        }
        seen_ids.add(emp_id)

final_report = {}

for emp_id, data in cleaned_data.items():
    
    name = data["name"]
    login = data["login"]
    idle = data["idle"]
    skills = data["skills"]
    
    productivity = login - idle
    
    matched = skills.intersection(required_skills)
    skill_match_percent = (len(matched) / len(required_skills)) * 100
   
    review = feedback[emp_id].lower()
    words = review.split()
    
    pos_score = 0
    neg_score = 0
    
    for word in words:
        if word in positive_words:
            pos_score += 1
        elif word in negative_words:
            neg_score += 1
    
    if pos_score > neg_score:
        sentiment = "Positive"
    elif neg_score > pos_score:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    risk_level = "Low"
    i = 0
    
    while i < 1:
        if productivity < 4:
            risk_level = "High"
        elif productivity < 6:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        i += 1
    
    final_report[emp_id] = {
        "Name": name,
        "Productivity": productivity,
        "Skill Match %": skill_match_percent,
        "Sentiment": sentiment,
        "Risk Level": risk_level
    }



ranking = sorted(final_report.items(), 
                 key=lambda x: x[1]["Productivity"], 
                 reverse=True)


print("===== FINAL AI ANALYTICS REPORT =====\n")

for emp_id, details in ranking:
    print("Employee ID:", emp_id)
    for key, value in details.items():
        print(f"{key}: {value}")
    print("----------------------------------")



top_employee = ranking[0]
print(" TOP PERFORMER:", top_employee[1]["Name"])