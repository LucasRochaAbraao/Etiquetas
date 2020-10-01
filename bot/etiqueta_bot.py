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
selecione um dos comandos disponíveis no ícone [ / ] abaixo.")

@dp.message_handler(commands=['gerar_etiquetas'])
async def ask_how_r_u(message: types.Message):

    _keyboard = [
        [types.KeyboardButton('Apenas 2.4GHz (bgn)')], 
        [types.KeyboardButton('2.4GHz e 5GHz (ac)')],
        [types.KeyboardButton('Patrimônio')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=_keyboard, one_time_keyboard=True)

    await message.reply("Qual estilo de etiquetas você gostaria de gerar?", reply_markup=keyboard)

# text é verdadeiro para o corpo da mensagem inteira.
@dp.message_handler(text='Apenas 2.4GHz (bgn)')
async def responder(message: types.Message):
    await message.answer("Você escolheu a opção 2.4GHz (bgn).\nGerando 300 etiquetas....\nEnviadas por email!")


# text é verdadeiro para o corpo da mensagem inteira.
@dp.message_handler(text='2.4GHz e 5GHz (ac)')
async def responder(message: types.Message):
    await message.answer("Você escolheu a opção 2.4GHz com 5GHz (AC).\nGerando 300 etiquetas....\nEnviadas por email!")

# text é verdadeiro para o corpo da mensagem inteira.
@dp.message_handler(text='Patrimônio')
async def responder(message: types.Message):
    await message.answer("Você escolheu a opção de etiquetas de patrimônio!\nGerando 150 etiquetas....\nEnviadas por email!")

@dp.message_handler() # qualquer mensagem que não foi resolvida com os outros handlers
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    #await message.reply(message.text) # responde marcando uma mensagem específicamente.
    await message.answer("Não entendi... Para gerar etiquetas, digite:\n/gerar_etiquetas") # responde normalmente na próxima linha

# # text_contains é verdadeiro caso o string ao menos faça parte do corpo da mensagem.
# @dp.message_handler(text_contains='ex1')
# @dp.message_handler(text_contains='ex2')
# async def text_contains_any_handler(message: types.Message):
#     await message.answer("Essa mensagem contém ex1 ou ex2")

# @dp.message_handler(text=['oi'])
# async def responder(message: types.Message):
#     await message.reply("Falae!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
