from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8714262946:AAFFBdfBH50ljGp1zBqPHwW6ViJJrnt2oNk"

ADMIN_ID = 7991716262

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    text = f"""
پیام جدید 📩

اسم: {user.first_name}
آیدی: {user.id}

پیام:
{update.message.text}
"""

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=text
    )

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.reply_to_message:

        old_text = update.message.reply_to_message.text

        lines = old_text.split("\n")

        for line in lines:

            if "آیدی:" in line:

                user_id = int(line.replace("آیدی:", "").strip())

                await context.bot.send_message(
                    chat_id=user_id,
                    text=update.message.text
                )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message)
)

app.add_handler(
    MessageHandler(filters.REPLY, reply_message)
)

print("Bot Running...")

app.run_polling()