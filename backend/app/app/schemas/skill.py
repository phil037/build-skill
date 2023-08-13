from typing import Optional

from pydantic import BaseModel


# Shared properties
class SkillBase(BaseModel):
    Python: Optional[int] = None
    OLGA: Optional[int] = None
    HYSYS: Optional[int] = None

# Properties to receive on item creation
class SkillCreate(SkillBase):
    Python: int
    OLGA: int
    HYSYS: int


# Properties to receive on item update
class SkillUpdate(SkillBase):
    pass


# Properties shared by models stored in DB
class SkillInDBBase(SkillBase):
    id: int
    owner_id: int
    Python: int
    OLGA: int
    HYSYS: int
    

    class Config:
        orm_mode = True


# Properties to return to client
class Skill(SkillInDBBase):
    pass


# Properties properties stored in DB
class SkillInDB(SkillInDBBase):
    pass
