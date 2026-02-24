class Model:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy

    def __repr__(self):
        return f"{self.name} - {self.accuracy}%"


models = [
    Model("BERT", 92),
    Model("GPT", 95),
    Model("LSTM", 89)
]

ranked = sorted(models, key=lambda m: m.accuracy, reverse=True)

print("Model Ranking:")
for model in ranked:
    print(model)