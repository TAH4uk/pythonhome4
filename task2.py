# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.

data = open("icecream.txt", "r", encoding = "utf-8")
ice = data.readlines()
data.close

str1 = set(ice[0].replace("\n", "").split(", "))
str2= set(ice[1].replace("\n", "").split(", "))

print(str1.difference(str2))