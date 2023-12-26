from typing import Optional

from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"message": "Not found"}}
)

users_obj = [
    {'id': 1, 'name': 'john'},
    {'id': 2, 'name': 'jame'},
    {'id': 3, 'name': 'jj'}
]


@router.get("/")
def users():
    return users_obj


@router.get("/users/{user_id}")
def read_item(user_id: int):
    result = [u for u in users_obj if u.get('id') == user_id]
    return result


@router.get("/abc")
def read_users():
    return {"message": "abc"}
