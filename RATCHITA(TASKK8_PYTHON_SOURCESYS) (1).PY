reviews = [
    "GEN AI is powerful and GEN AI is HAVING A great future",
    "Python is powerful programming language used in GEN AI",
    "GEN AI and Python are the greatest future of upcoming world"
]

stopwords = {"is", "and", "are"}

word_count = {}

for review in reviews:
    review = review.lower()
    words = review.split()
    
    for word in words:
        if word not in stopwords:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

print("Word Frequency:", word_count)

unique_words = set(word_count.keys())
print("Unique Words:", unique_words)