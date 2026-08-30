from fastapi import FastAPI, Request
from telegram import Update
from bot import app as telegram_app

app = FastAPI()


@app.on_event("startup")
async def startup():
    await telegram_app.initialize()
    await telegram_app.start()
    await telegram_app.bot.set_webhook(
        url="https://maya-bot.fly.dev/webhook"
    )


@app.on_event("shutdown")
async def shutdown():
    await telegram_app.bot.delete_webhook()
    await telegram_app.stop()
    await telegram_app.shutdown()


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