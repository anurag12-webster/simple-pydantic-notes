from fastapi import(
    FastAPI,
    Depends
)
from pydantic import(
    BaseModel,
    EmailStr
)
import uvicorn

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str


class Settings(BaseModel):
    app_name: str = "Fastapi APP"
    admin_email: str = "anurag@ak.com"

def get_settings():
    return Settings()

@app.post("/signup")
def signup(user:UserSignup):
    return {'messgae': 'User created successfully', 'user': user}

@app.get("/settings")
def get_app_setting(settings: Settings= Depends(get_settings)):
    return settings

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)