from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["Users"],
    responses={404: {"message": "Not found"}}
)

items_obj = [
    {'id': 1, 'name': 'item1'},
    {'id': 2, 'name': 'item2'},
    {'id': 3, 'name': 'item3'}
]


@router.get("/")
def items():
    return items_obj


@router.get("/items/{item_id}")
def read_item(item_id: int):
    result = [u for u in items_obj if u.get('id') == item_id]
    return result


@router.get("/abc")
def read_items():
    return {"message": "abc"}
