class LowMatchException(Exception):
    pass


class Candidate:
    def __init__(self, name, skills):
        self.name = name
        self.skills = set(skills)

    def match_skills(self, required_skills):
        matched = self.skills.intersection(required_skills)
        percent = (len(matched) / len(required_skills)) * 100
        
        if percent < 50:
            raise LowMatchException("Skill match below threshold!")
        
        return percent


required = {"Python", "SQL", "Machine Learning", "Deep Learning"}

c1 = Candidate("Ratchita", ["Python", "SQL", "Machine Learning"])
c2 = Candidate("Arjun", ["Java", "HTML"])

for candidate in [c1, c2]:
    try:
        match = candidate.match_skills(required)
        print(candidate.name, "Match %:", match)
    except LowMatchException as e:
        print(candidate.name, "Rejected:", e)