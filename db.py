from flask_sqlalchemy import SQLAlchemy

# DATABASE CONFIG
DATABASE_PATH = 'postgres://lcwsqlaqeedlfs:6fd3cb209bb18ac0d99eaae1d7a451e8e8e209e777aa720a90a00653973b9c9d@ec2-54-147-126-173.compute-1.amazonaws.com:5432/d55fftrn0iufhr'

db = SQLAlchemy()


# Setup db by providing the app and database path
def setup_db(app, database_path=DATABASE_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


# Drop all the tables and create them again
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
