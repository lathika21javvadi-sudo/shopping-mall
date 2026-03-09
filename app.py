from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/stores")
def stores():
    return jsonify({
        "stores": [
            {"name": "Fashion Hub", "desc": "Latest trends in fashion"},
            {"name": "Tech World", "desc": "Electronics and gadgets"},
            {"name": "Kids Planet", "desc": "Toys and clothing"},
            {"name": "Home Style", "desc": "Furniture and décor"}
        ]
    })

@app.route("/dining")
def dining():
    return jsonify({
        "dining": [
            {"name": "Food Court", "desc": "Fast food and international chains"},
            {"name": "Rooftop Grill", "desc": "Fine dining with a view"},
            {"name": "Coffee Corner", "desc": "Coffee, snacks, and desserts"}
        ]
    })

@app.route("/cinema")
def cinema():
    return jsonify({
        "cinema": [
            {"movie": "Dune 3", "time": "4:00 PM"},
            {"movie": "Kung Fu Panda 5", "time": "6:30 PM"},
            {"movie": "Avengers: Secret Wars", "time": "9:00 PM"}
        ]
    })

@app.route("/offers")
def offers():
    return jsonify({
        "offers": [
            {"title": "50% Off at Fashion Hub", "valid": "March 2026"},
            {"title": "Buy 1 Get 1 at Kids Planet", "valid": "This Week"},
            {"title": "20% Off Electronics at Tech World", "valid": "Today Only"}
        ]
    })

@app.route("/")
def home():
    return "Lathika shopping Mall Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    