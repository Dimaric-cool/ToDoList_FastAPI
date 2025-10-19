#  Точка входа в приложение

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.routes import todo
from app.routes import auth

app = FastAPI(title="ToDo API", description="API для управления списком задач", debug=True)

# Подключение маршрутов
app.include_router(auth.router)
app.include_router(todo.router)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)