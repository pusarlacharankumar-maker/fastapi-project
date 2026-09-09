from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Placement

from app.schemas.placement_schema import (
    PlacementCreate,
    PlacementUpdate
)


# =========================
# CREATE PLACEMENT
# =========================

def create_placement(
    placement_data: PlacementCreate,
    db: Session
):

    placement = Placement(
        company_name=placement_data.company_name,
        job_title=placement_data.job_title,
        location=placement_data.location,
        job_type=placement_data.job_type,
        description=placement_data.description,
        skills_required=placement_data.skills_required,
        salary=placement_data.salary,
        application_url=placement_data.application_url
    )

    db.add(placement)
    db.commit()
    db.refresh(placement)

    return placement


# =========================
# GET ALL PLACEMENTS
# =========================

def get_placements(
    db: Session
):

    return db.query(Placement).all()


# =========================
# GET ONE PLACEMENT
# =========================

def get_placement(
    placement_id: int,
    db: Session
):

    placement = db.query(Placement).filter(
        Placement.id == placement_id
    ).first()

    if placement is None:
        raise HTTPException(
            status_code=404,
            detail="Placement not found"
        )

    return placement


# =========================
# UPDATE PLACEMENT
# =========================

def update_placement(
    placement_id: int,
    placement_data: PlacementUpdate,
    db: Session
):

    placement = db.query(Placement).filter(
        Placement.id == placement_id
    ).first()

    if placement is None:
        raise HTTPException(
            status_code=404,
            detail="Placement not found"
        )

    placement.company_name = placement_data.company_name
    placement.job_title = placement_data.job_title
    placement.location = placement_data.location
    placement.job_type = placement_data.job_type
    placement.description = placement_data.description
    placement.skills_required = placement_data.skills_required
    placement.salary = placement_data.salary
    placement.application_url = placement_data.application_url

    db.commit()
    db.refresh(placement)

    return placement


# =========================
# DELETE PLACEMENT
# =========================

def delete_placement(
    placement_id: int,
    db: Session
):

    placement = db.query(Placement).filter(
        Placement.id == placement_id
    ).first()

    if placement is None:
        raise HTTPException(
            status_code=404,
            detail="Placement not found"
        )

    db.delete(placement)
    db.commit()

    return {
        "message": "Placement deleted successfully"
    }