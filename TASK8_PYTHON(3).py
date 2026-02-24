required_skills = {"Python", "Machine Learning", "SQL", "Deep Learning"}

candidate = ("Python", "SQL", "Deep Learning", "NLP")

candidate_set = set(candidate)

matched = required_skills.intersection(candidate_set)

match_percentage = (len(matched) / len(required_skills)) * 100

print("Matched Skills:", matched)
print("Match %:", match_percentage)