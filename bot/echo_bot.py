"""
Primeira versão é um bot-éco.

features:
    - comandos para gerenciar o bot [formato de ssid, dígitos na senha,email destino, quantidade e modelo padrão, etc]
    - comandos em mensagem também, parecido com linguagem natural, eventualmente.
    - botões para criar etiquetas 2.4ghz e 5ghz.
    - ao finalizar, enviar uma amostra da primeira e última etiqueta e uma mensagem que o email foi enviado.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
import token_config as cfg
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=cfg.token)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'ajuda'])
async def send_welcome(message: types.Message):
    """
    Esse handler vai ser chamado quando o usuário enviar o comando `/start` ou `/ajuda`
    """
    await message.reply(
"Olá!\nEu sou o Criador de Etiquetas! Para interagir comigo, \
selecione um dos comandos disponíveis no ícone [ / ] abaixo."
)

# text é verdadeiro para o corpo da mensagem inteira.
@dp.message_handler(text=['eco', 'Eco'])
async def responder(message: types.Message):
    await message.reply("você disse \"eco.\"")

# text_contains é verdadeiro caso o string ao menos faça parte do corpo da mensagem.
@dp.message_handler(text_contains='ex1')
@dp.message_handler(text_contains='ex2')
async def text_contains_any_handler(message: types.Message):
    await message.answer("Essa mensagem contém ex1 ou ex2")

@dp.message_handler(text=['oi'])
async def responder(message: types.Message):
    await message.reply("Oi gatão!")

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#     #await message.reply(message.text) # responde marcando uma mensagem específicamente.
#     await message.answer(message.text) # responde normalmente na próxima linha

### inline keyboard ###
@dp.message_handler(commands='gerar_etiquetas')
async def etiqueta_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=5)
    # row_width padrão é 3, mantido para clareza.

    opcao_e_dados = {
        'apenas 2.4GHz': '2.4GHz',
        '2.4 e 5GHz': '5GHz'
    }
    # in real life for the callback_data the callback data factory should be used
    # here the raw string is used for the simplicity
    row_btns = (types.InlineKeyboardButton(escolha, callback_data=tech) for escolha, tech in opcao_e_dados.items())

    keyboard_markup.row(*row_btns)

    await message.reply("Etiquetas de qual tecnologia?", reply_markup=keyboard_markup)

# Pode usar vários "registradores". O Handler vai executar aquele que for verdadeiro.
@dp.callback_query_handler(text='2.4GHz')  # se cb.tech == '2.4GHz'
@dp.callback_query_handler(text='5GHz')    # se cb.tech == '5GHz'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    # always answer callback queries, even if you have nothing to say
    await query.answer(f'Você escolheu {answer_data!r}')

    if answer_data == '2.4GHz':
        text = 'Gerando etiquetas 2.4GHz!'
    elif answer_data == '5GHz':
        text = 'Gerando etiquetas 5GHz!'
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await bot.send_message(query.from_user.id, text)


# @dp.message_handler(commands=['start', 'help'])
# async def ask_how_r_u(message: types.Message):

#     _keyboard = [
#         [types.KeyboardButton('Fine')], 
#         [types.KeyboardButton('Not bad')],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=_keyboard)

#     await message.reply("Hi!\nHow are you?", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
