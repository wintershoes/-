from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    CORS(app) #允许跨域名访问

    db.init_app(app)

    from app.controllers import (
        user_controller,
        book_controller,
        reservation_controller,
        activity_controller,
        review_controller,
        score_controller
    )

    app.register_blueprint(user_controller.bp)
    # app.register_blueprint(book_controller.bp)
    # app.register_blueprint(reservation_controller.bp)
    # app.register_blueprint(activity_controller.bp)
    # app.register_blueprint(review_controller.bp)
    # app.register_blueprint(score_controller.bp)

    return app