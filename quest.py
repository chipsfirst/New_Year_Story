import random
import colorama
from colorama import Fore, Back, Style
from data_maps import data_maps
colorama.init()


client_data = []
steps = []
character = input(Fore.BLUE+"Добро пожаловать в Новогодний квест! Как вас зовут?: ")
client_data.append(character)
location = input("Откуда вы к нам?: ")
client_data.append(location)
print("------------------------------------------------------------------------------------")
question1 = input('Отличные новости, ' + client_data[0] + '! Двери нашей резиденции откроются совсем скоро. '
                                                    'Хотите посмотреть карту?:').title()
if question1 == "Да":
    delimiter = ", \n"
    output = delimiter.join(data_maps)
    print(output)
    print()
    print("**********************************************************************************************")
else:
    print("Попробуйте еще раз!")

