from fastapi import APIRouter

router = APIRouter()


@router.get('/skills')
def get_skills():
    skills_data = [
        {'slNo': 1, 'skill': 'popo', 'remarks': 'expert'},
        {'slNo': 2, 'skill': 'Python', 'remarks': 'beginner'},
        {'slNo': 3, 'skill': 'MS Word', 'remarks': 'expert'}
    ]
    return skills_data

@router.get('/anantha')
def get_skills():
    skills_data = [
        "welcome to phils"
    ]
    return skills_data