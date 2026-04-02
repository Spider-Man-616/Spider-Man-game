#File Name: Spider-Man: Saving Gwen Stacy
#Spider-Man game. I'll give a full plot description later
#File Author: Sahaj Ranadey
#last Edited: 23/03/2026

#imports (Libraries)

import random
import time

#Global Variables

spider_man_health = 100
print_delay = 0.1


#Functions

def typewriter(text, delay=print_delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def get_input(prompt="> "):
    global spider_man_health
    user = input(prompt)

    if user == "Q":
        print("\nRestarting game...\n")
        spider_man_health = 100
        main_menu()

    return user

def main_menu():
    global player_name
    print("---------------------------")
    typewriter("Spider-Man: Saving Gwen Stacy")
    print("---------------------------")
    print()
    typewriter("How to play:")
    typewriter("As you encounter the battle functions, they will start to explain themselves.")
    typewriter("If at any point you wish to quit? Just input 'Q' and the game will restart.")
    print()

    while True:
        try:
            print("Which Spider-Man would you like to be?")
            print("Type 1 for Peter Parker, 2 for Peter Parker, or 3 for Peter Parker: ")
            player_choice = int(get_input())
            if player_choice == 1 or player_choice == 2 or player_choice == 3:
                player_name = "Peter Parker"
                break
            else:
                print("Try again and pick 1, 2, or 3. Because you have to be Peter Parker.")
        except ValueError:
            print("Invalid input.")

    while True:
            try:
                print(f"Hi {player_name} press 1 to start your journey, or 2 to quit.")
                user_input = int(get_input())
                if user_input == 1:
                        typewriter("Empire State University")
                        typewriter("The haunting sound of an explosion rumbles through the campus of Empire State University.")
                        typewriter("Teenagers sprint in panic, professors hide, and through it all? You slip away from the crowd.")
                        typewriter("Subtly, you slip out of your civilian clothes to reveal the suit underneath.")
                        typewriter("Red and blue spandex. Shimmering in the gleaming sun. An odd suit, but one that the citizens of the city now love.")
                        print()
                        typewriter("Why?")
                        print()
                        typewriter("Simple.")
                        print()
                        typewriter("You're a hero.")
                        print()
                        typewriter("In fact? You're THE Hero.")
                        print()
                        typewriter("You")
                        print()
                        print()
                        typewriter("Are")
                        print()
                        print()
                        typewriter("Spider-Man")
                        area_01()
                elif user_input == 2:
                    print("Fine. Don't play. Bye. Nerd.")
                    exit()
                else:
                    print("Invalid Option.")
            except ValueError:
                print("Invalid input.")

def riddle_fight():
    print("Mysterio appears in a cloud of smoke...")
    print("Answer 3 riddles to escape his illusion.")

    riddles = {
        "I swing through the city but I am not a bird. Who am I?": "spider-man",
        "I shoot but I am not a gun. What am I?": "web",
        "I protect Peter Parker's identity while he swings. What am I?": "mask",
        "What warns me of danger before it happens?": "spider sense"
    }

    correct = 0

    while True:
        if correct >= 5:
            print("You broke Mysterio's illusion!")
            area_02()
            return

        question = random.choice(list(riddles.keys()))
        answer = riddles[question]

        print()
        print(question)
        user_answer = get_input("> ").lower()

        if user_answer == answer:
            print("Correct.")
            correct += 1
        else:
            print("Wrong. You are trapped in the illusion.")
            return

def pattern_recognition():
    print("Chameleon is disguising himself...")
    print("Memorize the pattern.")
    print("Use: P (Peter), MJ (MJ), M (May), S (Spider-Man)")
    print("Get 5 correct to win.")
    print()

    options = ["P", "MJ", "M", "S"]
    pattern = []

    successes = 0

    while True:
        if successes == 5:
            print("You exposed Chameleon!")
            print("Press 'THREE' to continue or 'ONE' to retry.")
            
            choice = get_input("> ").upper()
            if choice == "ONE":
                pattern_recognition()
            elif choice == "THREE":
                area_03()
            return

        pattern.append(random.choice(options))

        print("Memorize:")
        for item in pattern:
            print(item, end=" ", flush=True)
            time.sleep(0.7)

        time.sleep(1)

        # clear screen effect (simple version)
        print("\n" * 20)

        user_input = get_input("Repeat the pattern (space separated): ").upper().split()

        if user_input == pattern:
            print("Correct.")
            successes += 1
        else:
            print("Wrong. Chameleon fooled you.")
            print("Press run again to restart.")
            return

def dodge_mechanic():
    delay = random.randint(2, 5)
    time.sleep(delay)
    print("DODGE")
    start_time = time.time()
    action = get_input("> ").upper()
    end_time = time.time()
    reaction_time = end_time - start_time

    if action == "D" and reaction_time < 1.5:
        print("You dodged successfully!")
        return True
    elif action == "D" and reaction_time >= 1.5:
        print("Too slow. Scorpion stung you. Your final moments flash before your eyes as death embraces you.")
        return False
    else:
        print("You were frozen in place. You couldn't dodge. You die instantly.")
        return False

def dodge_timing():
#function for area 1
    print("Here are the instructions as to how you will play this area of the game.")
    print("When the word 'DODGE' pops up on your screen? You have 1.5 seconds to input the letter 'D'.")
    print("If you're too late? You die and you lose the game.")
    print("After dodging 5 times? You win and move on.")
    print()
    print("----------------------------------------------------------------------------------------")

    successes = 0
    delay = 5
    time.sleep(delay)
    print("Ready? (Y or N):")
    ready = get_input().upper()
    if ready == "Y":
        for round in range(5):
            if not dodge_mechanic():
                print("You lost. Press run again to start again.")
                break
            else:
                successes += 1
    elif ready == "N":
        print("Press run again to start again.")
        main_menu()
        return
    else:
        print("Invalid input. Try again.")

    if successes == 5:
        print("You dodged for the fifth time, and then an opening appeared.")
        print("With a fierce crack, your fist landed against his jaw, dislocating it.")
        print("You win. Press 'TWO' to progress to the next area. Press 'ONE' to repeat this. Press 'Q' to quit.")
        progression = input().upper()
        if progression == "ONE":
            dodge_timing()
        elif progression == "TWO":
            area_02()
        elif progression == "Q":
            print("Press run again to start again.")
            main_menu()
            return
        else:
            print("invalid input. Try again.")

def battle():
    global spider_man_health

    enemy_name = "Rhino"
    enemy_health = 120

    print("----------------------------------")
    print(f"A massive shadow crashes through the street...")
    print(f"{enemy_name} charges toward you!")
    print("----------------------------------")

    while enemy_health > 0 and spider_man_health > 0:
        print()
        print(f"Your Health: {spider_man_health}")
        print(f"{enemy_name} Health: {enemy_health}")
        print()
        print("Choose your action:")
        print("1 - Punch")
        print("2 - Web Attack")
        print("3 - Dodge")

        choice = input("> ")

        if choice == "1":
            damage = random.randint(10, 20)
            enemy_health -= damage
            print(f"You swing in and punch Rhino for {damage} damage!")

        elif choice == "2":
            damage = random.randint(5, 25)
            enemy_health -= damage
            print(f"You shoot webs and strike Rhino for {damage} damage!")

        elif choice == "3":
            print("Get ready to dodge!")
            if dodge_mechanic():#Instead of completely having them seperate, I thought having this dodge function here as well would be cool.
                print("You avoided Rhino's charge and countered!")
                counter = random.randint(10, 15)
                enemy_health -= counter
                print(f"You dealt {counter} counter damage!")
                continue
            else:
                spider_man_health = 0
                break

        else:
            print("Invalid move! You hesitated...")

        # Rhino attacks back
        if enemy_health > 0:
            enemy_damage = random.randint(8, 18)
            spider_man_health -= enemy_damage
            print(f"Rhino smashes into you for {enemy_damage} damage!")

    # Outcome
    if spider_man_health > 0:
        print("With one final blow, Rhino crashes into the ground!")
        print("You win the battle.")
        print()
        print("Press 'ONE' to return to Area 1.")
        print("Press 'TWO' to fight Rhino again.")
        print("Press 'THREE' to continue to Area 3.")
        print("Press 'Q' to quit.")

        progression = get_input("> ").upper()

        if progression == "ONE":
            area_01()

        elif progression == "TWO":
            battle()

        elif progression == "THREE":
            area_03()

        elif progression == "Q":
            print("Press run again to start again.")
            main_menu()
            return

        else:
            print("Invalid input. Try again.")
            battle()

    else:
        print("Rhino stands victorious...")
        print("You have been defeated.")
        print("Press Run Again to play again")
        main_menu()
        return


def round_repeating():
    global spider_man_health

    enemy_name = "Doctor Octopus"
    enemy_health = 150
    rounds = 3

    print("----------------------------------")
    print(f"{enemy_name} emerges, metal arms clashing wildly...")
    print("You must survive multiple rounds to defeat him!")
    print("----------------------------------")

    for current_round in range(1, rounds + 1):
        print(f"\n--- ROUND {current_round} ---\n")

        while enemy_health > 0 and spider_man_health > 0:
            print(f"Your Health: {spider_man_health}")
            print(f"{enemy_name} Health: {enemy_health}")
            print()
            print("Choose your action:")
            print("1 - Punch")
            print("2 - Web Attack")
            print("3 - Dodge")

            choice = get_input("> ")

            if choice == "1":
                damage = random.randint(12, 22)
                enemy_health -= damage
                print(f"You strike Doc Ock for {damage} damage!")

            elif choice == "2":
                damage = random.randint(8, 28)
                enemy_health -= damage
                print(f"Your webs hit for {damage} damage!")

            elif choice == "3":
                print("Get ready to dodge!")
                if dodge_mechanic():
                    counter = random.randint(10, 18)
                    enemy_health -= counter
                    print(f"Counter successful! You deal {counter} damage!")
                    continue
                else:
                    spider_man_health = 0
                    break

            else:
                print("Invalid move! You hesitate...")

            # Enemy attack
            if enemy_health > 0:
                enemy_damage = random.randint(10, 20)
                spider_man_health -= enemy_damage
                print(f"Doctor Octopus strikes you for {enemy_damage} damage!")

        if spider_man_health <= 0:
            print("Doctor Octopus has defeated you...")
            print("Press run again to restart.")
            return

        # Reset enemy health slightly each round (makes it feel like phases)
        if current_round < rounds:
            print(f"\nDoc Ock retreats briefly... but comes back stronger!")
            enemy_health = 100 + (current_round * 20)

    print("\nWith a final blow, Doctor Octopus collapses!")
    print("You win the fight!")

    print("Press 'FOUR' to continue to the next area or 'ONE' to replay.")
    progression = get_input("> ").upper()

    if progression == "ONE":
        round_repeating()
    elif progression == "FOUR":
        area_04()
    else:
        print("Invalid input. Returning to menu.")
def final_boss():
    global spider_man_health

    print("----------------------------------")
    print("The Green Goblin descends from above...")
    print("Laughing maniacally as chaos erupts around you.")
    print("This is it. The final battle.")
    print("----------------------------------")

    phases_completed = 0

    while spider_man_health > 0 and phases_completed < 5:

        print(f"\n--- PHASE {phases_completed + 1} ---\n")

        # Phase 1: Riddle (Mysterio style)
        if phases_completed == 0:
            print("The world distorts... illusions surround you.")
            riddles = {
                "I swing through the city but I am not a bird. Who am I?": "spider-man",
                "I shoot but I am not a gun. What am I?": "web",
                "What warns me of danger before it happens?": "spider sense"
            }

            for question, answer in riddles.items():
                print(question)
                user = get_input("> ").lower()
                if user != answer:
                    print("You failed to break the illusion...")
                    spider_man_health = 0
                    break

            if spider_man_health > 0:
                print("You shattered the illusion!")
                phases_completed += 1

        # Phase 2: Pattern Recognition (Chameleon style)
        elif phases_completed == 1:
            print("The Goblin creates clones... which one is real?")
            options = ["P", "MJ", "M", "S"]
            pattern = [random.choice(options) for _ in range(3)]

            print("Memorize:")
            for item in pattern:
                print(item, end=" ", flush=True)
                time.sleep(0.7)

            time.sleep(1)
            print("\n" * 20)

            user_input = get_input("Repeat the pattern: ").upper().split()

            if user_input == pattern:
                print("You identified the real Goblin!")
                phases_completed += 1
            else:
                print("You were tricked by illusions...")
                spider_man_health = 0

        # Phase 3: Dodge sequence (Scorpion style)
        elif phases_completed == 2:
            print("Pumpkin bombs rain from the sky!")
            dodges = 0

            for _ in range(3):
                if dodge_mechanic():
                    dodges += 1
                else:
                    spider_man_health = 0
                    break

            if dodges == 3:
                print("You dodged every explosion!")
                phases_completed += 1

        # Phase 4: Combat (Rhino style)
        elif phases_completed == 3:
            print("The Goblin attacks directly!")
            enemy_health = 80

            while enemy_health > 0 and spider_man_health > 0:
                print(f"Your Health: {spider_man_health}")
                print(f"Goblin Health: {enemy_health}")
                print("1 - Punch | 2 - Web | 3 - Dodge")

                choice = get_input("> ")

                if choice == "1":
                    dmg = random.randint(10, 20)
                    enemy_health -= dmg
                    print(f"You deal {dmg} damage!")

                elif choice == "2":
                    dmg = random.randint(8, 25)
                    enemy_health -= dmg
                    print(f"Web attack hits for {dmg}!")

                elif choice == "3":
                    if dodge_mechanic():
                        counter = random.randint(10, 15)
                        enemy_health -= counter
                        print(f"Counter for {counter} damage!")
                        continue
                    else:
                        spider_man_health = 0
                        break

                else:
                    print("Invalid move!")

                if enemy_health > 0:
                    dmg = random.randint(10, 18)
                    spider_man_health -= dmg
                    print(f"Goblin hits you for {dmg}!")

            if spider_man_health > 0:
                print("You overpower the Goblin!")
                phases_completed += 1

        # Phase 5: Final Round (Doc Ock style endurance)
        elif phases_completed == 4:
            print("FINAL PHASE: The Goblin goes berserk!")
            enemy_health = 100

            while enemy_health > 0 and spider_man_health > 0:
                print(f"Your Health: {spider_man_health}")
                print(f"Goblin Health: {enemy_health}")

                action = random.choice(["attack", "dodge"])

                if action == "dodge":
                    print("Incoming deadly strike!")
                    if not dodge_mechanic():
                        spider_man_health = 0
                        break
                else:
                    dmg = random.randint(12, 22)
                    enemy_health -= dmg
                    print(f"You strike for {dmg}!")

                    if enemy_health > 0:
                        enemy_dmg = random.randint(12, 22)
                        spider_man_health -= enemy_dmg
                        print(f"Goblin hits for {enemy_dmg}!")

            if spider_man_health > 0:
                phases_completed += 1

    # Final outcome
    if spider_man_health > 0:
        print("\nWith one final swing, you defeat the Green Goblin.")
        print("The city is safe. Gwen Stacy is saved.")
        print("You are truly... Spider-Man.")
    else:
        print("\nThe Green Goblin stands victorious...")
        print("The city falls into chaos.")
        print("Press run again to try again.")

#these are all the specialized battle functions for each of the fights in the game.

#---------------------------------------------------------------------------

def area_01():
    


    print("Scorpion")
    dodge_timing()

def area_02():




    print("Rhino in Times Square")
    battle()
def area_03():




    print("Mysterio in Wall Street")
    riddle_fight()
def area_04():



    print("The Chameleon in Central Park")
    pattern_recognition()
def area_05():




    print("Aunt May's home in Queens")
    round_repeating()
def final_area():




    print("Brooklyn Bridge")
    final_boss()
#these are all the settings for each fight. All the locations. 

#---------------------------------------------------------------------------

#main routine

main_menu()