from app.models.user import User

from app.db import Base, engine


Base.metadata.create_all(engine)
