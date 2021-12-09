from codetiming import Timer
videocard = 1
money = 0
coin = 0


def menu():
    print("MENU\n(1) shop\n(2) mining\n(3) reverse ")
    print(f"money: {money} | coin: {coin} | videocard: {videocard}")
    xmenu = input("take: ")
    if xmenu == "1":
        shop()
    if xmenu == "2":
        mining()
    if xmenu == "3":
        reverse()
    if xmenu == "0":
        pass
    else:
        print("what?")
        menu()

def shop():
    global videocard, money
    print("SHOP\n(1) videocard -- 500 money\n(0) exit")
    xshop = input("take: ") 
    if xshop == "1":
        if money >= 500:
            money -= 500
            videocard += 1
            print(f"you buy videocard\n you have {videocard} videocard")
        else:
            print("you don't have money")
        shop()
    if xshop == "0":
        menu()
    else:
        print("what?")
        shop()

def reverse():
    global money, coin
    print(f"0.001 coin = 1 money\nyou money: {money} | you coin {coin}\n(1) exchange all\n(2) exchange partially\n(0)exit")
    xreverse = input("take: ")
    if xreverse == "1":
        money += int(coin * 1000)
        coin -= coin
        if coin <= 0:
            print("don't coin")
    if xreverse == "2":
        xtotal = float(input("how much do you want to exchange: "))
        if xtotal <= coin:
            newmoney = int(xtotal * 1000)
            print(f"you have: {newmoney} money")
            coin -= xtotal
            money += newmoney
        else:
            print("you don't have coin")
    if xreverse == "0":
        menu()
    else:
        print("What?")
        reverse()
    reverse()

def mining():
    global coin
    t = Timer()
    t.start()
    input("press what would stoped: ")
    final = round(t.stop())
    ming = (final * videocard) / 1000
    print(f"you have: {ming} coin")
    coin += ming
    menu()

menu()
