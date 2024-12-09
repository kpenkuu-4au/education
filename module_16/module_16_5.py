from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int = None
    username: str
    age: int


users = []


@app.get('/')
async def home_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/user/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    index_user = None
    for user in range(len(users)):
        if users[user].id == user_id:
            index_user = user
    if index_user is not None:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[index_user]})
    raise HTTPException(status_code=404, detail="User not found")


@app.post('/user/{username}/{age}')
async def new_user(
        username: str = Path(
            min_length=5,
            max_length=20,
            description='Enter username',
            example='User1'
        ),
        age: int = Path(
            gt=18,
            le=120,
            description='Enter age',
            example=25
        )
) -> User:
    if not users:
        users.append(User(id=1, username=username, age=age))
        return users[0]
    else:
        users.append(User(id=users[-1].id + 1, username=username, age=age))
        return users[-1]


@app.put('/user/{user_id}/{username}/{age}')
async def change_user(
        user_id: int = Path(
            gt=0,
            le=100,
            description='Enter User ID',
            example=5
        ),
        username: str = Path(
            min_length=5,
            max_length=20,
            description='Enter username',
            example='User1'
        ),
        age: int = Path(
            gt=18,
            le=120,
            description='Enter age',
            example=5
        )
) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: int = Path(
            gt=0,
            le=100,
            description='Enter User ID',
            example=5
        )
) -> User:
    del_index = None
    del_user = None
    for user in range(len(users)):
        if users[user].id == user_id:
            del_index = user
            del_user = User(
                id=users[user].id,
                username=users[user].username,
                age=users[user].age
            )
    if del_user is not None:
        users.pop(del_index)
        return del_user
    raise HTTPException(status_code=404, detail="User was not found")
