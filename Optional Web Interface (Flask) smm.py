from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        mood = predict_mood(text)
        result = recommendation(mood)
        return render_template("index.html", mood=mood, result=result)

    return render_template("index.html")

app.run(debug=True)