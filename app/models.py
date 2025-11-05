from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Método de Serialização: Converte o objeto Task em um dicionário."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }