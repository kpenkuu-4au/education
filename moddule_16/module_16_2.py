from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/')
async def home_page() -> dict:
    return {"message": "Главная страница"}


@app.get('/user/admin')
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get('/user/{user_id}')
async def user_root(user_id: int = Path(gt=0, le=100, description='Enter User ID', example='7')) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get('/user/{username}/{age}')
async def user_info(
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
) -> dict:
    return {"Информация о пользователе": f"Имя: {username}, Возраст: {age}"}
