from sqlalchemy import ARRAY, Boolean, Column, DateTime, Integer, String, Text, func

from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    tech_stack = Column(ARRAY(String), nullable=False, default=list)
    category = Column(String, nullable=False)
    organization = Column(String, nullable=True)
    year = Column(String, nullable=False)
    link_url = Column(String, nullable=True)
    link_label = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    image_credit_name = Column(String, nullable=True)
    image_credit_url = Column(String, nullable=True)
    featured = Column(Boolean, default=False, nullable=False)
    sort_order = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
