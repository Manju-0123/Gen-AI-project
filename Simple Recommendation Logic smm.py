def recommendation(mood):

    if mood == "happy":
        return "Recommended: Party songs / Fun videos"

    elif mood == "sad":
        return "Recommended: Motivational videos"

    elif mood == "angry":
        return "Recommended: Meditation music"

    else:
        return "Recommended: Trending content"

mood = predict_mood(user_input)
print(recommendation(mood))