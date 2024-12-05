from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int = None
    username: str
    age: int


users = []


@app.get('/')
async def home_page() -> str:
    return "Главная страница"


@app.get('/users')
async def get_users() -> list:
    return users


@app.post('/user/{username}/{age}')
async def new_user(
        username: str = Path(
            min_length=5,
            max_length=20,
            description='Enter username',
            example='Ivan123'
        ),
        age: int = Path(
            gt=18,
            le=120,
            description='Enter age',
            example='25'
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
            example='5'
        ),
        username: str = Path(
            min_length=5,
            max_length=20,
            description='Enter username',
            example='Ivan123'
        ),
        age: int = Path(
            gt=18,
            le=120,
            description='Enter age',
            example='25'
        )
) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
        else:
            raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: int = Path(
            gt=0,
            le=100,
            description='Enter User ID',
            example='5'
        )
) -> User:
    for user in range(len(users) - 1):
        if users[user].id == user_id:
            del_user = users.pop(user)
            return del_user
        else:
            raise HTTPException(status_code=404, detail="User was not found")
