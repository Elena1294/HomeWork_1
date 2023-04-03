try:
    my_age = int(input("Сколько Вам лет? "))
    print ("Ваш возраст: " + str(my_age)) 
except ValueError: 
    print("Это не число.")
try:
    my_age = my_age + 1
    print ("Ваш возраст+1: " + str(my_age))
except ValueError: 
    print("Это не число.")

