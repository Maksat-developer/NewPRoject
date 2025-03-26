import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = "7615967263:AAEfwC3oiCV03R_LLjvmbubIGuvBzl-d5c8"
CHANNEL_ID = "-1002458595342"  # Убедись, что этот chat_id правильный

bot = telebot.TeleBot(TOKEN)

HABR_URL = "https://habr.com/ru/all/"
KEYWORDS = ["Linux", "Линукс"]

def get_habr_articles():
    """Функция парсит статьи с Хабра по ключевым словам."""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }
    response = requests.get(HABR_URL, headers=headers)

    if response.status_code != 200:
        print(f"Ошибка при запросе к Хабру: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    articles = soup.find_all("article")
    news_list = []

    for article in articles:
        title_tag = article.find("h2")
        title = title_tag.text.strip() if title_tag else "Нет заголовка"

        link_tag = title_tag.find("a") if title_tag else None
        link = "https://habr.com" + link_tag["href"] if link_tag and "href" in link_tag.attrs else "Нет ссылки"

        desc_tag = article.find("div", class_="article-formatted-body")
        description = desc_tag.text.strip()[:300] if desc_tag else "Нет описания"

        img_tag = article.find("img")
        image = img_tag["src"] if img_tag and "src" in img_tag.attrs else None

        # Фильтрация по ключевым словам
        if any(word.lower() in title.lower() or word.lower() in description.lower() for word in KEYWORDS):
            news_list.append({
                "title": title,
                "link": link,
                "description": description,
                "image": image
            })

    return news_list

def send_news_to_telegram():
    """Функция отправляет найденные статьи в канал Telegram"""
    news_list = get_habr_articles()

    print(f"Отправка в канал: {CHANNEL_ID}")  # Лог для проверки

    if not news_list:
        try:
            bot.send_message(CHANNEL_ID)
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
        return

    for news in news_list:
        message = f"📰 *{news['title']}*\n\n{news['description']}...\n\n🔗 [Читать полностью]({news['link']})"

        try:
            if news["image"]:
                bot.send_photo(CHANNEL_ID, photo=news["image"], caption=message, parse_mode="Markdown")
            else:
                bot.send_message(CHANNEL_ID, message, parse_mode="Markdown")
            print(f"✅ Отправлено: {news['title']}")
        except Exception as e:
            print(f"❌ Ошибка при отправке сообщения: {e}")

# === Отправляем новости сразу при запуске ===
send_news_to_telegram()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я отправляю новости про Linux в канал.")

@bot.message_handler(content_types=['text'])
def forward_message_to_channel(message):
    """Пересылает текстовые сообщения в канал"""
    try:
        bot.send_message(CHANNEL_ID, message.text)  # Отправка в канал
        bot.send_message(message.chat.id, "Сообщение отправлено в канал!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

# === Бот работает постоянно ===
bot.polling(non_stop=True)
