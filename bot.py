import logging
import settings
import ephem as ephe
import datetime
from pprint import pprint
from telegram.ext import Updater , CommandHandler , MessageHandler, Filters
logging.basicConfig(filename='bot.log', level=logging.INFO)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_plane(update, context):
    print('planet_rub')
    user_text = str(update.message.text)

    user_text_2=user_text.split(' ')

    #print(user_text_2[1])
    now= datetime.datetime.now()
    a =str(now.year)+'/'+str(now.month)+'/'+str(now.day)
    print('data =',a)
    if user_text_2[1]== 'Mars':
        mars=ephe.Mars(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Mercury':
        mars=ephe.Mercury(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Venus':
        mars=ephe.Venus(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Jupiter':
        mars=ephe.Jupiter(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Saturn':
        mars=ephe.Saturn(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Uranus':
        mars=ephe.Uranus(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))


    elif user_text_2[1]== 'Neptune':
        mars=ephe.Neptune(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Pluto':
        mars=ephe.Pluto(a)
        constellation =  ephe.constellation (mars)
        update.message.reply_text((constellation))

    elif user_text_2[1]== 'Sun':
        #print('the Sun_rubb',a)

        mars=ephe.Sun(a)
        #print(dir(ephe))
        constellation =  ephe.constellation (mars)#ephem.constellation(mars)
        #print(constellation,'\t ' ,type(constellation) )

        update.message.reply_text((constellation))


    elif user_text_2[1]== 'Moon':
        mars=ephe.Moon(a)
        constellation = ephem.constellation(mars)
        update.message.reply_text(constellation)
    else:
        update.message.reply_text('я не знаю это планеты ')


    #a_name_palnet=ephem.star(str(user_text_2[1]))
    #print(a_name_palnet.name)


    #bb=getattr(ephem, str(user_text_2[1]))
    #a1=(bb)
    #print(a)

    #bb_new=bb(a)

    #pprint('!!!!=',[name for _0, _1, name in ephem._libastro.builtin_planets()])
    #b=(ephem._libastro.builtin_planets())


    #print(a)
    #for ar in b:
        #print(ar)

    #if user_text_2 == 'Mars':
        #mars = ephem.Mars(a)
    #elif user_text_2 == 'Mars':





    #pprint('!!!!=',ephem._libastro.builtin_planets())
    #update.message.reply_text('user_text=',user_text)


    #pass

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def main():
    print('run bbot')
    #print(dir(ephe))


    mybot=Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_plane))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":

    main()
