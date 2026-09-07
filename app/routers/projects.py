from fastapi import APIRouter, Depends
from sqlalchemy import asc
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Project
from app.schemas import ProjectOut

router = APIRouter(prefix="/api/projects", tags=["projects"])


@router.get("", response_model=list[ProjectOut])
def list_projects(db: Session = Depends(get_db)):
    return (
        db.query(Project)
        .order_by(Project.featured.desc(), asc(Project.sort_order))
        .all()
    )


@router.get("/{slug}", response_model=ProjectOut)
def get_project(slug: str, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.slug == slug).first()
    if not project:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="Project not found")
    return project
