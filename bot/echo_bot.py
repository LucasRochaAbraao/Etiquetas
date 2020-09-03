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


@dp.message_handler(commands=['start', 'help', 'iniciar', 'ajuda'])
async def send_welcome(message: types.Message):
    """
    Esse handler vai ser chamado quando o usuário enviar o comando `/start`, `/help`, `/iniciar` ou `/ajuda`
    """
    await message.reply("Olá!\nEu sou o Criador de Etiquetas! Estou à disposição.")

# text é verdadeiro para o corpo da mensagem inteira.
@dp.message_handler(text=['eco', 'Eco'])
async def responder(message: types.Message):
    await message.reply("você disse \"eco.\""")

# text_contains é verdadeiro caso o string ao menos faça parte do corpo da mensagem.
@dp.message_handler(text_contains='ex1')
@dp.message_handler(text_contains='ex2')
async def text_contains_any_handler(message: types.Message):
    await message.answer("Essa mensagem contém ex1 ou ex2")

@dp.message_handler(text=['oi'])
async def responder(message: types.Message):
    await message.reply("Oi gatão!")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    #await message.reply(message.text) # responde marcando uma mensagem específicamente.
    await message.answer(message.text) # responde normalmente na próxima linha


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)