def predict_mood(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    mood = model.predict(vec)
    return mood[0]

# Example
user_input = input("Enter your social media post: ")
print("Detected Mood:", predict_mood(user_input))