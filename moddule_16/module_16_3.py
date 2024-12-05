from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/')
async def home_page() -> dict:
    return {"message": "Главная страница"}


@app.get('/users')
async def get_users() -> dict:
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
) -> str:
    new_id = int(max(users)) + 1
    users[str(new_id)] = f'Имя: {username}, возраст {age}'
    return f"The user {new_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def change_user(
        user_id=Path(
            gt=0, le=100,
            description='Enter User ID',
            example='7'
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
) -> str:
    if users.get(f'{user_id}') is not None:
        users[user_id] = f'Имя: {username}, возраст {age}'
        return f"The user {user_id} is updated"
    else:
        return f"The user {user_id} is not found"


@app.delete('/user/{user_id}')
async def delete_user(
        user_id=Path(
            gt=0, le=100,
            description='Enter User ID',
            example='7'
        )
) -> str:
    if users.get(f'{user_id}') is not None:
        users.pop(f'{user_id}')
        return f'The user {user_id} is deleted'
    else:
        return f'The user {user_id} is not found'
