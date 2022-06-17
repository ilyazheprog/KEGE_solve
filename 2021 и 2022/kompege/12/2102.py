'''
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. 
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки цифр.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w, 
вторая проверяет, встречается ли цепочка v в строке исполнителя Редактор. Если она 
встречается, то команда возвращает логическое значение «истина», в противном случае 
возвращает значение «ложь». Дана программа для исполнителя Редактор:
НАЧАЛО
  ПОКА нашлось (11)
    ЕСЛИ нашлось(112)
      ТО заменить (112, 7)
      ИНАЧЕ заменить (11, 3)
  КОНЕЦ ПОКА
КОНЕЦ
Исходная строка содержит 12 единиц и 4 двойки, других цифр нет, точный порядок 
расположения цифр неизвестен. Какую наибольшую сумму цифр может иметь строка, 
которая получится после выполнения программы?
'''
# https://prnt.sc/G4S3GpABRYc5


strin = '112' * 4 + '1' * (12 - 8)

# 4 => 7
# 2 => 3
# очевидно, что выгоднее 4 => 7 , т.е. (112->7)


while '11' in strin:
    if '112' in strin:
        strin = strin.replace('112', '7', 1)
    else:
        strin = strin.replace('11', '3', 1)


print(sum(map(int, strin)))
