import random
bot = int(input('Set range bottom'))
top = int(input('Set range top'))
print("You have a lot of money:$5000")
num = random.randint(bot, top)
print('Your code in ['+ str(bot) + ',' + str(top) + '] ')
money= 5000
i = 0
while i < 15:
    number = input("please input your code：")
    number = int(number)
    if i<10:
        if number > num:
            money = money - 500
            print("too big | balance:",money)
        elif number < num:
            money = money - 500
            print("too small | balance：",money)
        elif number==num:
            money = money + 3000
            print("congratualations The correct code is ：",num,"Reward--$3000，balance：",money)
            break
    elif i>=10:
        print("Clocked!!!")
        break
    i=i+1