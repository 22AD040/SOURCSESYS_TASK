def validate_row(row):
    try:
        name = row["name"]
        age = int(row["age"])
        salary = float(row["salary"])

        if age <= 0 or salary <= 0:
            raise ValueError("Invalid age or salary")

        return True
    except Exception as e:
        print("Invalid Row:", row, "| Error:", e)
        return False


dataset = [
    {"name": "Ratchita", "age": "23", "salary": "50000"},
    {"name": "Arjun", "age": "-5", "salary": "40000"},
    {"name": "Meena", "age": "29", "salary": "-1000"}
]

valid_data = list(filter(lambda row: validate_row(row), dataset))

print("Valid Dataset:", valid_data)