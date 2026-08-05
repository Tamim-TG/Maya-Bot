from fastapi import FastAPI, Request
from telegram import Update
from bot import app as telegram_app

app = FastAPI()


@app.get("/")
async def home():
    return {
        "status": "ok",
        "bot": "Maya 🌸"
    }


@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    update = Update.de_json(data, telegram_app.bot)

    await telegram_app.process_update(update)

    return {"ok": True}