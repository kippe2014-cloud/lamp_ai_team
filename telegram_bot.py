import os
import csv
from telegram import Update, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Получаем токен бота и ключ OpenAI из переменных окружения
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")  # если используешь AI

# Файл с клиентами
CLIENTS_FILE = "clients.csv"

# Файл с каталогом товаров (фото)
CATALOG_FOLDER = "catalog"  # создайте папку catalog и положите туда картинки товаров
CATALOG = [
    {"name": "Светильник 1", "filename": "001.jpg", "description": "Красивый светильник для дома"},
    {"name": "Светильник 2", "filename": "002.jpg", "description": "Настольная лампа стильная"},
]

# ----------------- КЛИЕНТЫ -----------------
def add_client(user_id, username):
    """Добавляем клиента в CSV если его там нет"""
    try:
        with open(CLIENTS_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if str(user_id) == row[0]:
                    return  # клиент уже есть
    except FileNotFoundError:
        pass  # файл ещё не создан

    # Добавляем нового клиента
    with open(CLIENTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([user_id, username])
        
# ----------------- КОМАНДЫ -----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_client(user.id, user.username)
    await update.message.reply_text(f"Привет, {user.first_name}! Добро пожаловать в магазин светильников.")

async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляем каталог товаров"""
    media = []
    for item in CATALOG:
        path = os.path.join(CATALOG_FOLDER, item["filename"])
        media.append(InputMediaPhoto(open(path, "rb"), caption=f"{item['name']}\n{item['description']}"))

    # Telegram позволяет отправлять до 10 фото за раз
    for i in range(0, len(media), 10):
        await update.message.reply_media_group(media[i:i+10])

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - начать\n/catalog - посмотреть каталог\n/help - помощь"
    )

# ----------------- MAIN -----------------
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("catalog", catalog))
    app.add_handler(CommandHandler("help", help_command))

    print("Бот запущен...")
    app.run_polling()
