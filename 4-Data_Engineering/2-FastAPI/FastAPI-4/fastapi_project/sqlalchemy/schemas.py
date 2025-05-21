from datetime import datetime

from pydantic import BaseModel, Field

# Pydantic for the schemas


class PostBase(BaseModel):
    title: str
    content: str
    publication_date: datetime = Field(
        default_factory=datetime.now
    )  # default_factory to initiate the time by default

    class Config:  # Config subclass
        # from_attributes = False would use Pydantic parsing data from dictionaries
        # example: d["title"]
        # from_attributes = True would use Pydantic parsing data using dot notation
        # example: o.title
        from_attributes = True


# To modify the title and content of a post
class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


# To create a post we need PostBase like it is
class PostCreate(PostBase):
    pass


# To post a post we include an id (not decided by the user)
class PostRead(PostBase):
    id: int
