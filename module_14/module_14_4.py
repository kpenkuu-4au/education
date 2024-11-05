from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import crud_functions

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
calc_button = KeyboardButton(text='Рассчитать')
info_button = KeyboardButton(text='Информация')
buy_button = KeyboardButton(text='Купить')
kb.add(calc_button)
kb.add(info_button)
kb.add(buy_button)
kb_inline = InlineKeyboardMarkup()
calories_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formula_button = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
catalog_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ]
)
kb_inline.add(calories_button)
kb_inline.add(formula_button)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


crud_functions.initiate_db()
products = crud_functions.get_all_products()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inline)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in products:
        await message.answer(f'Продукт: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        with open('pill.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=catalog_buttons)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес(кг) + 6, 25 x рост(см) – 5 х возраст(г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await  message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
    await message.answer(f'Ваша норма {calories} калорий')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
