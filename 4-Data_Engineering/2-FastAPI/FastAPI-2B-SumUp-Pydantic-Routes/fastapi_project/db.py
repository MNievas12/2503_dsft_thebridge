from fastapi_project.schemas.post import Post
from fastapi_project.schemas.user import User


class DummyDatabase:
    users: dict[int, User] = {}
    posts: dict[int, Post] = {}


db = DummyDatabase()
