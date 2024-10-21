import random

bullets = ["fake", "real", "fake", "real", "real","fake","fake","real","fake"]
random.shuffle(bullets)  # Shuffle the bullets

# items = ["k","s","k","s"]
# random.shuffle(items)

items = ["k", "s"]
random.shuffle(items)
def power():


    return items.pop(random.randint(0,len(items)-1))

def gun():
    return bullets.pop(random.randint(0, len(bullets) - 1))



person = ["player1" , "player2"]
player = person[0]

player1hp = 3
player2hp = 3
pl1itm = 1
pl2itm = 1
while player2hp > 0 and player1hp > 0 and len(bullets) > 0:
    if player == "player1":
        print(f'{player} turn')
        damage = 1
        if pl1itm > 0 :
            pic = input("gonna us(e item (k,s) or (p)-->")
            # pic = power()
            if pic == "k":
                damage = 2
                pl1itm -= 1

                print(f'{player} use knife')
            elif pic == "s":
                print(f'{player} use soda')
                player1hp += 1
                pl1itm -= 1
                print(f'{player1hp} hp now')
            else:
                print(f'{player}skipped items')
        pc = input('shoot or re-->')


        if pc == "s" :
            opt = gun()
            if opt == "real":
                player2hp -= 1*damage
                print("💣 on  2")
                print(f'remaning bullets {bullets}')

                print(f'😎 ❤:{player2hp}')
            elif opt == "fake":

                player = "player2"
                print("🔫 fake")
                print(f'😎 ❤:{player2hp}')
                print(f'remaning bullets {bullets}')

        elif pc == "re":
            opt = gun()
            if opt == "real":
                player1hp -= 1*damage

                player = "player2"
                print("💣 on playr1 face self")
                print(f'🤣 ❤:{player1hp}')
                print(f'remaning bullets {bullets}')
            elif opt == "fake":
                print("😇")
                print(f'🤣 ❤:{player1hp}')
                print(f'remaning bullets {bullets}')






    if player == "player2":
        print("player2 turn")

        damage = 1
        if pl2itm > 0:
            pic = input("gonna us(e item (k,s) or (p)-->")
            # pic = power()
            if pic == "k":
                damage = 2
                print(f'{player} use knife')
                pl2itm -= 1
            elif pic == "s":
                print(f'{player} use soda')
                player2hp += 1
                pl2itm -= 1
                print(f'{player2hp} hp now')
            else:
                print(f'{player}skipped')
        pc = input('shoot or re-->')

        if pc == "s":
            opt = gun()
            if opt == "real":
                player1hp -= 1*damage
                print("💣 on  1")

                print(f'🤣 ❤:{player1hp}')
                print(f'remaning bullets {bullets}')
            elif opt == "fake":

                player = "player1"
                print("🔫 fake")
                print(f'🤣 ❤:{player1hp}')
                print(f'remaning bullets {bullets}')

        # if pc == "s" :
        #     opt = gun()
        #     if opt == "real":
        #         player1hp -= 1
        #         print("💣 on 1")
        #
        #         print(f'🤣 ❤:{player1hp}')
        #     elif opt == "fake":
        #
        #         player = "player1"
        #         print("🔫 fake 1")
        #
        #         print(f'🤣 ❤:{player1hp}')

        elif pc == "re":
            opt = gun()
            if opt == "real":
                player2hp -= 1
                player = "player1"
                print("💣 on 2 self")
                print(f'😎 ❤:{player2hp}')
                print(f'remaning bullets {bullets}')
            elif opt == "fake":
                print("😇")
                print(f'😎 ❤:{player2hp}')
                print(f'remaning bullets {bullets}')

    if len(bullets) == 0:
        print("out of bulltets 🛠")
        print(f' 🤣💚 is{player1hp} and 😎❤ is{player2hp}')
        break

    if player1hp == 0:
        print("player2 win 😎🥇")
    elif player2hp == 0:
        print("player1 win 🤣🥇")








