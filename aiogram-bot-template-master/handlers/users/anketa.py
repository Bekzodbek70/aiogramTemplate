from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import Personaldata

@dp.message_handler(Command('anketa'), state=None)
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting")
    await Personaldata.fullname.set()

@dp.message_handler(state=Personaldata.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname=message.text
    # await state.update_data(name=fullName)
    await state.update_data(
        {"name": fullname}
    )
    await message.answer("Email manzil kiriting")
    await Personaldata.next() #keyingi holatga o'tish uchun<------->
    # agarda biror bir handler komanda yopilmagan bo'lsa keyingi holatga o'tmaydi
    # await Personaldata.email.set() -------> biror bir qadamni tashlab o'tishimizda ishlatiladi'

@dp.message_handler(state=Personaldata.email)
async def answer_email(message: types.Message, state: FSMContext):
    email=message.text
    await state.update_data(
        {"email": email}
    )

    await message.answer("Telefon raqamingizni kiriting")
    await Personaldata.next()

@dp.message_handler(state=Personaldata.phone)
async def answer_phone(message: types.Message, state: FSMContext):
    phone=message.text
    await state.update_data(
        {"phone": phone}
    )

    #Ma'lumotlarni qayta o'qiymiz

    data= await state.get_data()
    name=data.get("name")
    email=data.get("email")
    phone=data.get("phone")

    msg="Quyidagi ma'lumotlar qabul qilindi:\n"
    msg+=f"Ismingiz - {name}\n"
    msg+=f"Emailingiz - {email}\n"
    msg+=f"Telefon raqamingiz -{phone}"
    await message.answer(msg)

    await state.finish() #holatdan chiqish

