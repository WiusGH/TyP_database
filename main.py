from flask import Flask, render_template, jsonify
from models import db, User, Post, Comment, Review
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin1234@localhost/typ_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/users')
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'e-mail': user.email} for user in users]
    return jsonify(user_list)


@app.route('/api/posts')
def get_posts():
    posts = Post.query.all()
    post_list = [{'id': post.id, 'title': post.title, 'content': post.content, 'date': post.date} for post in posts]
    return jsonify(post_list)


@app.route('/api/comments')
def get_comments():
    comments = Comment.query.all()
    comment_list = [{'id': comment.id, 'comment': comment.comment, 'date': comment.date} for comment in comments]
    return jsonify(comment_list)


@app.route('/api/reviews')
def get_reviews():
    reviews = Review.query.all()
    review_list = [{'id': review.id, 'review': review.review, 'rating': review.rating} for review in reviews]
    return jsonify(review_list)


if __name__ == '__main__':
    app.run(debug=True)
