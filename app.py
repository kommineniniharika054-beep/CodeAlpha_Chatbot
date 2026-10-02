from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


responses = {
    "hello": "Hello! 👋 Welcome to the CodeAlpha Cloud Assistant. How can I help you?",
    "hi": "Hi! 👋 How can I help you today?",
    "hey": "Hey! 😊 What would you like to know?",

    "codealpha": "CodeAlpha provides internship opportunities where students can gain practical experience through project-based learning.",

    "internship": "CodeAlpha offers internship programs that help students develop practical technical skills through real-world projects.",

    "cloud": "Cloud computing allows applications, data, and services to be accessed through internet-based infrastructure such as AWS, Azure, and Google Cloud.",

    "python": "Python is a popular programming language used for web development, data analysis, automation, artificial intelligence, and many other applications.",

    "flask": "Flask is a lightweight Python web framework used to build web applications and APIs.",

    "project": "This chatbot is developed as Task 4 of the CodeAlpha Cloud Computing Internship.",

    "task": "This is Task 4 — Chatbot, developed as part of the CodeAlpha Cloud Computing Internship.",

    "features": "This chatbot provides instant responses, predefined question handling, keyword-based matching, a web chat interface, and a fallback response for unknown questions.",

    "thank": "You're welcome! 😊 I'm happy to help.",

    "thanks": "You're welcome! 😊",

    "bye": "Goodbye! 👋 Have a great day!",

    "help": "You can ask me about CodeAlpha, internships, cloud computing, Python, Flask, this project, or its features."
}


def get_response(message):

    message = message.lower().strip()

    if not message:
        return "Please type a question so I can help you. 😊"

    for keyword, response in responses.items():

        if keyword in message:
            return response

    return (
        "I'm sorry, I don't have an answer for that yet. 🤔 "
        "Try asking about CodeAlpha, internships, cloud computing, "
        "Python, Flask, or this project."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    bot_response = get_response(user_message)

    return jsonify({
        "response": bot_response
    })


if __name__ == "__main__":
    app.run(debug=True)