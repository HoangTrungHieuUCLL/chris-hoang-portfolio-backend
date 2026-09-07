from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class ProjectOut(BaseModel):
    id: int
    slug: str
    name: str
    description: str
    tech_stack: list[str]
    category: str
    organization: str | None
    year: str
    link_url: str | None
    link_label: str | None
    image_url: str | None
    image_credit_name: str | None
    image_credit_url: str | None
    featured: bool

    class Config:
        from_attributes = True


class ContactMessageIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: EmailStr
    message: str = Field(min_length=1, max_length=4000)


class ContactMessageOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True
