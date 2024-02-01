import telebot
from config import CURRENCY as currency, TOKEN
from utils import ConvertException, Convert

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id,
                     f"Привет, {message.chat.username}. Это бот, который будет выдавать вам актуальные курсы валют. "
                     f"Помощь по управлению ботом: \n/help")


@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Чтобы начать работу введите боту команду в следущем формате: \n<имя валюты> "
                                      "<в какую валюту перевести> <кол-во валюты>. \nДля того чтобы узнать "
                                      "доступные валюты, используйте: /currency \nПишите названия валюты в "
                                      "единственном числе!")


@bot.message_handler(commands=['currency'])
def handle_start_help(message):
    text = 'Доступные валюты:'
    for key in currency.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertException('Не правильное кол-во параметров')

        cu_fr, cu_to, amount = values

        result = Convert.convert(cu_fr, cu_to, amount)
    except ConvertException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        bot.reply_to(message, f"При конвертации {amount} {cu_fr} в {cu_to} получится {result}")


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)