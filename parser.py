# библиотеки
import requests
from bs4 import BeautifulSoup

# сайт с курсом валют
RESOURCE = 'https://www.sravni.ru/valjuty/info/btc-rub-1/'
# не бот, а физический юзер
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
# для корректной работы
headers = headers

# запрос всего кода страницы
full_page = requests.get(RESOURCE, headers)

# парситься будет за счет библиотеки BeautifulSoup
soup = BeautifulSoup(full_page.content, 'html.parser')

# выборка по нужному классу
for heading in soup.find_all("div", {"class": "course-name"}):
    cost_str = heading.text

# удаление лишних символов и перевод в число
cost = cost_str.replace('R','').replace('U','').replace('B','').replace(' ','').replace("\n","")
cost = float(cost)


# курс валют
out = "1 BTC = " + str(cost) + " RUB \nДанные обновляются раз в день\n"
print(out)

cost = float(cost)

# получение значения от пользовтеля и перевод в число
enter = input("Укажите сумму в рублях или в BTC\nПример 3500 или 0.00237\n")
enter = enter.replace(',','.')
enter = float(enter)



# если биток
if enter > 1:
	btc = round(1/cost*enter, 8)
	if btc >= 0.0002 and btc <= 0.1:
		custom_out = str(enter) + " RUB = " + str(btc) + " BTC"
		print(custom_out)	
	else:
		print("Сумма должна быть в интервале от 0.0002 до 0.1 BTC")		
# если рубли
else:
	rub = round(cost*enter, 2)
	if enter >= 0.0002 and enter <= 0.1:
		custom_out = str(enter) + " BTC = " + str(rub) + " RUB"
		print(custom_out)	
	else:
		print("Сумма должна быть в интервале от 0.0002 до 0.1 BTC")