import asyncio


async def start_strongman(name, power):
    print(f'Cилач {name} начал соревнования.')
    ball = 1
    for item in range(5):
        print(f'Силач {name} поднял {ball}')
        await asyncio.sleep(1 / power)
        ball += 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    print("Старт соревнования")
    strongman1 = asyncio.create_task(start_strongman('Иван', 1.5))
    strongman2 = asyncio.create_task(start_strongman('Данила', 2))
    strongman3 = asyncio.create_task(start_strongman('Кирилл', 2.5))
    await strongman1
    await strongman2
    await strongman3
    print('Финиш соревнования')


asyncio.run(start_tournament())
