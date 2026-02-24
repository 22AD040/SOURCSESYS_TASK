import ai_utils  

text = "  GEN AI is the Future Scope in this world  "

cleaned = ai_utils.clean_text(text)
count = ai_utils.word_count(cleaned)

print("Cleaned:", cleaned)
print("Word Count:", count)