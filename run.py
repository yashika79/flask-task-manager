from app import create_app,db
from app.models import Task,User
from flask_migrate import Migrate

app=create_app()

migrate = Migrate(app, db)


with app.app_context():
    print("Database URL:", db.engine.url)
    print("Models registered:", list(db.metadata.tables.keys()))

    # db.create_all()

    print("Tables in database:", db.inspect(db.engine).get_table_names())

if __name__=="__main__":
    app.run(debug=True)