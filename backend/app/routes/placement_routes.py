from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models import User

from app.schemas import (
    PlacementCreate,
    PlacementUpdate,
    PlacementResponse
)

from app.middleware.admin_middleware import (
    get_current_admin
)

from app.services.placement_service import (
    create_placement,
    get_placements,
    get_placement,
    update_placement,
    delete_placement
)


router = APIRouter(
    prefix="/placements",
    tags=["Placements"]
)


# =========================
# CREATE
# ADMIN ONLY
# =========================

@router.post(
    "",
    response_model=PlacementResponse
)
def add_placement(
    placement: PlacementCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return create_placement(
        placement,
        db
    )


# =========================
# GET ALL
# PUBLIC
# =========================

@router.get(
    "",
    response_model=list[PlacementResponse]
)
def placements(
    db: Session = Depends(get_db)
):
    return get_placements(db)


# =========================
# GET ONE
# PUBLIC
# =========================

@router.get(
    "/{placement_id}",
    response_model=PlacementResponse
)
def placement(
    placement_id: int,
    db: Session = Depends(get_db)
):
    return get_placement(
        placement_id,
        db
    )


# =========================
# UPDATE
# ADMIN ONLY
# =========================

@router.put(
    "/{placement_id}",
    response_model=PlacementResponse
)
def edit_placement(
    placement_id: int,
    placement_data: PlacementUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return update_placement(
        placement_id,
        placement_data,
        db
    )


# =========================
# DELETE
# ADMIN ONLY
# =========================

@router.delete(
    "/{placement_id}"
)
def remove_placement(
    placement_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return delete_placement(
        placement_id,
        db
    )