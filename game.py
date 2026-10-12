import random
import time



class Character:
    _instances = []

    def __init__(self, name, health):
        self.name = name
        self.__health = health
        Character._instances.append(self)

    def __str__(self):
        return f"Hello, I am {self.name}"

    def do_task(self, health):
        self.__health -= health
        if self.__health <= 0:
            print(f"{self.name} died.")

    def get_health(self):
        return self.__health

    def is_alive(self):
        return self.__health > 0
   
    @classmethod
    def is_all_dead(cls):
        if not cls._instances:
            return True

        for obj in cls._instances:
            if obj.is_alive():
                return False

        return True

    @classmethod
    def all_characters(cls):
        if not cls._instances:
            print("No instances")

        for obj in cls._instances:
            print(f"{obj.name.title()} is a {type(obj).__name__}")


class Scout(Character):
    def __init__(self, name):
        super().__init__(name, health = 40)


class Blacksmith(Character):
    def __init__(self, name):
        super().__init__(name, health = 60)


class Healer(Character):
    def __init__(self, name):
        super().__init__(name, health = 45)


class Hunter(Character):
    def __init__(self, name):
        super().__init__(name, health = 50)



scenarios = [
    {"description": "Heavy rain has washed out the bridge. The river is brown and fast. Task: cross the river on a slippery fallen tree and tie a rope on the other side.",
     "health_cost": 10},
    {"description": "A pack of hyenas follows you at dusk and circles the camp. Task: drive the hyenas away from the camp.",
     "health_cost": 15},
    {"description": "A stone door blocks an old mountain pass and a storm is coming. Task: push the door open for the others.",
     "health_cost": 10},
    {"description": "Lightning has set the dry grass on fire. Task: run through the smoke and clear a safe path for the group.",
     "health_cost": 20},
    {"description": "A bandit camp sits beside the trail. Task: sneak past the bandits in the dark and find a safe way around.",
     "health_cost": 15},
    {"description": "The trail ends at a steep cliff and the rope is old. Task: climb the cliff and drop a rope for the others.",
     "health_cost": 15},
    {"description": "A fever spreads after the group drinks from a bad stream. Task: carry the medicine and the sick while pushing on through the night.",
     "health_cost": 20},
    {"description": "A rockslide buries the road. Task: dig and move the boulders for hours to open the way.",
     "health_cost": 15},
    {"description": "A freezing night falls on the high plateau and there is no wood. Task: keep watch all night and keep the group warm.",
     "health_cost": 20},
    {"description": "A giant of a man blocks the road and demands a fight. Task: fight the giant so the group can pass.",
     "health_cost": 25},
]


def main():
    global scenarios

    # Creating the characters
    characters = []
    while True:
        chars = input("Enter 4 character names(Separate them using a comma): ")
        chars = chars.split(",")
        if len(chars) == 4:
            break
        else:
            print("Please enter again.")

    ## To randomly assign roles to characters
    random.shuffle(chars)

    ## Shuffling the scenarios so that users can go different paths each time they play the game
    random.shuffle(scenarios)
    
    for idx, Subclass in enumerate(Character.__subclasses__()):
        instance = Subclass(chars[idx].lower())
        characters.append({"instance": instance, "name": instance.name, "role": Subclass.__name__.title()})
                        
    
    Character.all_characters()



    # Opening Narrator
    openings = ["\nThe floods have cut off a village in the highlands, and the people there are running out of time.\n",
               "Four travelers carry the only medicine that can save them.\n", 
               "Several trials stand between you and the village, and not everyone will make it.\n", 
               "Choose wisely, because every task has a price.\n"
               ]
    for sentence in openings:
        print(sentence)
        time.sleep(2)


    # Game progress
    win = True
    for idx, scenario in enumerate(scenarios):
        print(scenario["description"])
        print("\nChoose a person to do the task:")
        available_choices = []
        damage = scenario['health_cost']
        for idx, char in enumerate(characters):
            if char["instance"].is_alive():
                print(f"{idx}. {char['name']}")
                available_choices.append(str(idx))
        
        while True:
            user_choice = input(">")
            if user_choice in available_choices:
                break
            else:
                print("Please Enter a valid choice")
       
        match user_choice:
            case "0":
                characters[0]['instance'].do_task(damage)
            case "1":
                characters[1]['instance'].do_task(damage)
            case "2":
                characters[2]['instance'].do_task(damage)
            case "3":
                characters[3]['instance'].do_task(damage)

        print("\n")

        if Character.is_all_dead():
            print("All Characters are dead")
            win = False
            break

    
    # End
    if win:
        print("Congratulations! You have won the game")
    else:
        print("You Lose. All players are dead")


if "__main__" == __name__:
    main()



