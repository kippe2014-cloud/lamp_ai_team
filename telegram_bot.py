from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import csv
from datetime import datetime
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key не найден")

# функция сохранения клиента
def save_client(update):

    name = update.message.from_user.first_name
    username = update.message.from_user.username
    message = update.message.text
    date = datetime.now()

    with open("clients.csv", "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow([date, name, username, message])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["Каталог"],
        ["Цена"],
        ["Доставка"],
        ["Связаться с мастером"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Здравствуйте 👋\n"
        "Я консультант магазина светильников.\n"
        "Выберите раздел:",
        reply_markup=reply_markup
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        await update.message.reply_text(f"ID фото: {file_id}")
        return

    save_client(update)

    text = update.message.text.lower()
    # сохраняем клиента
    save_client(update)

    text = update.message.text.lower()

    if "каталог" in text:

        await update.message.reply_text("Наши светильники:")

        await update.message.reply_photo(
            photo="https://via.placeholder.com/500",
            caption="Светильник CHORON\nЦена: 6500 ₽"
        )

        await update.message.reply_photo(
            photo="https://png.pngtree.com/thumb_back/fh260/background/20230610/pngtree-picture-of-a-blue-bird-on-a-black-background-image_2937385.jpg",
            caption="Светильник YAKUT\nЦена: 7200 ₽"
        )

    elif "цена" in text:

        await update.message.reply_text(
            "💡 Цена наших светильников:\n\n"
            "от 3000 ₽ до 12000 ₽"
        )


    # elif "доставка" in text:

     #  await update.message.reply_text(
      #      "🚚 Доставка:\n\n"
       #     "СДЭК\n"
        #    "Почта России\n\n"
         #   "Отправляем по всей России."
        #)

    elif "связаться" in text:

        await update.message.reply_text(
            "Напишите мастеру:\n"
            "@Filin_zx"
        )

    else:

        await update.message.reply_text(
            "Выберите кнопку в меню."
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Бот запущен...")

app.run_polling()
