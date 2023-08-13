from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Skill])
def read_skills(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve skills.
    """
    if crud.user.is_superuser(current_user):
        skills = crud.skill.get_multi(db, skip=skip, limit=limit)
    else:
        skills = crud.skill.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return skills


@router.post("/", response_model=schemas.Skill)
def create_skill(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.SkillCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new skill.
    """
    skill = crud.skill.create_with_owner(db=db, obj_in=item_in, owner_id=current_user.id)
    return skill


@router.put("/{owner_id}", response_model=schemas.Skill)
def update_skill(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.SkillUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),

) -> Any:
    """
    Update an skill.
    """
    #skill = crud.skill.get(db=db, id=id)
    skill = crud.skill.get_multi_by_owner(
            db=db, owner_id=current_user.id,
        )
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    if not crud.user.is_superuser(current_user) and (skill.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    skill = crud.skill.update(db=db, db_obj=skill, obj_in=item_in)
    return skill


@router.get("/myskill", response_model=List[schemas.Skill])
def read_skill(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get the current user's skillsets.
    """
    skill = crud.skill.get_multi_by_owner(db=db,owner_id=current_user.id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    return skill



@router.delete("/{id}", response_model=schemas.Skill)
def delete_skill(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an skill.
    """
    skill = crud.skill.get(db=db, id=id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    if not crud.user.is_superuser(current_user) and (skill.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    skill = crud.skill.remove(db=db, id=id)
    return skill
