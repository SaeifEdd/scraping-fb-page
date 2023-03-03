from sqlalchemy.orm import Session
import models, schemas
import services 

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: dict):
    db_post = models.Post(content = post['post_text'], likes = post['likes'])
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

    