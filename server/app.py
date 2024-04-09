# server/app.py

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# Sample route to retrieve all users
@app.route('/users')
def get_users():
    users = User.query.all()
    user_list = [{"id": user.id, "username": user.username} for user in users]
    return jsonify(user_list)

# Sample route to retrieve all games
@app.route('/games')
def get_games():
    games = Game.query.all()
    game_list = [{"id": game.id, "title": game.title} for game in games]
    return jsonify(game_list)

# Sample route to retrieve all reviews
@app.route('/reviews')
def get_reviews():
    reviews = Review.query.all()
    review_list = [{"id": review.id, "content": review.content} for review in reviews]
    return jsonify(review_list)

@app.route('/')
def index():
    return "Index for Game/Review/User API"

# start building your API here

if __name__ == '__main__':
    app.run(port=5555, debug=True)
