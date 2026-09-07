from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ContactMessage
from app.schemas import ContactMessageIn, ContactMessageOut

router = APIRouter(prefix="/api/contact", tags=["contact"])


@router.post("", response_model=ContactMessageOut, status_code=201)
def submit_contact_message(payload: ContactMessageIn, db: Session = Depends(get_db)):
    message = ContactMessage(
        name=payload.name, email=payload.email, message=payload.message
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message
