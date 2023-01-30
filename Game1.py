class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


class Player(Character):
    def attack(self, enemy):
        enemy.hp -= self.damage
        print(
            f"{self.name} hits {enemy.name}!\n{enemy.name}'s health is now {enemy.hp}.")


class Enemy(Character):
    def attack(self, player):
        player.hp -= self.damage
        print(
            f"{self.name} hits {player.name}!\n{player.name}'s health is now {player.hp}.")


elf = Character("Elf", 100, 5)
knight = Character("Knight", 300, 50)
witch = Character("Witch", 200, 20)
spectre = Character("Spectre", 150, 60)
king = Character("King", 400, 90)

character_options = {
    1: elf,
    2: knight,
    3: witch,
    4: spectre,
    5: king,
}

print("1) Elf\n2) Knight\n3) Witch\n4) Spectre\n5) King\nPlease choose your character:")
character = int(input())
player = Player(character_options[character].name,
                character_options[character].hp, character_options[character].damage)

ogre = Enemy("Ogre", 500, 50)

while True:
    player.attack(ogre)
    if ogre.hp <= 0:
        print("The Ogre has lost.")
        break
    ogre.attack(player)
    if player.hp <= 0:
        print("You have fallen.")
        break
