from flask_sqlalchemy import SQLAlchemy
import logging as lg
from api_modele_demo import db

# Create database connection object

class Channel(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True) 
    url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    language = db.Column(db.String(200), nullable=True)
    subjects = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)

    def json(self):
        return {
            'title': self.title, 
            'url': self.url,
            'description': self.description,
            'language': self.language,
            'subjects': self.subjects,
            'image_url': self.image_url,
            }

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

def init_db():
    db.drop_all()
    db.create_all()
    Channel(
        title = "Tech_With_Time",
        description = "Learn programming, software engineering, machine learning and everything tech from this channel. With a special emphasis on python and javascript my channel aims to give you free resources so that you can learn to code and dive into the software engineering and programming industry. My goal is to provide the highest quality programming and tech videos on the internet! ",
        url = "https://www.youtube.com/c/TechWithTim/featured",
        language = "English",
        subjects = '["Flask","Python"]',
        image_url = "https://yt3.ggpht.com/ytc/AKedOLQXx-JXf1NsSUtVHcYhx4B4MaIYE0m7I_H0GHmu-w=s900-c-k-c0x00ffffff-no-rj"
        ).save_to_db()
    Channel(
        title = "Docstring",
        description = "Tutoriels, trucs & astuces, bonnes pratiques autour du langage Python, de différents framework (Django, Qt for Python...) et du développement en général.",
        url = "https://www.youtube.com/c/Docstring/featured",
        language = "French",
        subjects = '["Python"]',
        image_url = "https://yt3.ggpht.com/3sXh0-ipDGiHgBRTle8sbGLjKm6p0PENZAeoo2-H_w3NxOLXLI7Khw2ZEi7olJNs2kMNEcql=s900-c-k-c0x00ffffff-no-rj"
        ).save_to_db()
    Channel(
        title = "ArjanCodes",
        description =  "On this channel, I post videos about programming and software design to help you take your coding skills to the next level. I'm an entrepreneur and a university lecturer in computer science, with more than 20 years of experience in software development and design. If you're a software developer and you want to improve your development skills, and learn more about programming in general, make sure to subscribe for helpful videos.",
        url = "https://www.youtube.com/c/ArjanCodes/featured",
        language = "English",
        subjects = '["Python","POO"]',
        image_url = "https://yt3.ggpht.com/PF_5a9pF_CurRWcBpGxAvYv-uMc6bsK_LYpmgHDMDnG5tTzHbYU7Jz55pU_QXm1f0nVLTmlzZw=s900-c-k-c0x00ffffff-no-rj"
        ).save_to_db()

    lg.warning('Database initialized!')


