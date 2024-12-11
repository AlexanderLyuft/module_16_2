            # Домашнее задание по теме "Валидация данных".


from fastapi import FastAPI, Path
from pydantic import constr, conint
from typing import Annotated

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[conint(ge=1, le=100),
                        Path(..., description="Enter User ID")]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[constr(min_length=5, max_length=20),
                        Path(..., description="Enter username")],
    age: Annotated[conint(ge=18, le=120),
                   Path(..., description="Enter age")]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}



