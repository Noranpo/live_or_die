import random

bullets = ["real", "real", "fake", "real", "real","fake","fake"]
random.shuffle(bullets)  # Shuffle the bullets
def gun():
    return bullets.pop(random.randint(0, len(bullets) - 1))



person = ["player1" , "player2"]
player = person[1]

player1hp = 3
player2hp = 3
while player2hp > 0 and player1hp > 0 and len(bullets) > 0:
    if player == "player1":
        print("player 1 turn")
        pc = input('shoot or re-->')

        if pc == "s" :
            opt = gun()
            if opt == "real":
                player2hp -= 1
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
                player1hp -= 1
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
        pc = input('shoot or re-->')

        if pc == "s":
            opt = gun()
            if opt == "real":
                player1hp -= 1
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
    if player1hp == 0:
        print("player2 win 😎🥇")
        break
    elif player2hp ==0:
        print("player1 win 🤣🥇")
        break
    elif len(bullets) == 0:
        print("out of bulltets 🛠")
        print(f' 🤣💚 is{player1hp} and 😎❤ is{player2hp}')
        break






