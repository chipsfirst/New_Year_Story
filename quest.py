import random

client_data = []
character = input("Добро пожаловать в Новогодний квест! Как вас зовут?: ")
client_data.append(character)
location = input("Откуда вы к нам?: ")
client_data.append(location)
print("-------------------------------------------------------------")
print(input('Отличные новости, ' + client_data[0] + '! Двери нашей резиденции откроются совсем скоро. Хотите посмотреть карту?:'))

#TODO сделать карту

print(input("К сожалению, волшебные двери неконтролируемо открываются каждый раз в новом месте. Открывайте! "
            "Просто напишите слово (открыть)"))


data_maps = ["Снежная площадь",
             "Ледяной дворец",
             "Фабрика игрушек",
             "Конфетный двор",
             "Еловые поля",
             ]
random_maps = random.choice(data_maps)

print("Вы попали в интересное место:" + random_maps)
if random_maps == data_maps[0]:
    print("Вы очутились на Снежной площади, главной площади нашей страны. Здесь стоит самая большая елка, которая "
          "возвышается над всем городом")
elif random_maps == data_maps[1]:
    print("Вы попали в Ледяной дворец")
elif random_maps == data_maps[2]:
    print("Вы забежали на Фабрику игрушек")
elif random_maps == data_maps[3]:
    print("Вы залетели на Конфетный двор")
elif random_maps == data_maps[4]:
    print("Вы приземлились на Еловые поля")
