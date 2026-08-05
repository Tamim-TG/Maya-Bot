from telegram import Update
from telegram.ext import (
    Application,
    ContextTypes,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN, TRIGGERS
from gemini import ask_gemini
from memory import get_memory, save_memory


def should_reply(text: str) -> bool:
    text = text.lower()
    return any(trigger.lower() in text for trigger in TRIGGERS)


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    text = update.message.text or ""

    if not should_reply(text):
        return

    user_id = update.effective_user.id

    memory = get_memory(user_id)

    reply = ask_gemini(text, memory)

    save_memory(user_id, reply)

    await update.message.reply_text(reply)


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        message_handler,
    )
)


if __name__ == "__main__":
    print("🌸 Maya Started...")
    app.run_polling()