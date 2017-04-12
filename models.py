from run import db

class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    furniture_type = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Integer, nullable = False)
