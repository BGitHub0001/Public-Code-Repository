class Character:
    def __init__(self, name, hp, attack1, attack2, attack3):
        self.name = name
        self.hp = hp
        self.attacks = [attack1, attack2, attack3]


class Player(Character):
    def choose_attack(self):
        print("Choose an attack:")
        for i, attack in enumerate(self.attacks, start=1):
            print(f"{i}) {attack.name} (Damage: {attack.damage})")
        attack_choice = int(input())
        return self.attacks[attack_choice - 1]


class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


elf = Character("Elf", 100, Attack("Quick Strike", 5), Attack(
    "Double Strike", 10), Attack("Triple Strike", 15))
knight = Character("Knight", 300, Attack("Power Strike", 50),
                   Attack("Shield Bash", 30), Attack("Charge", 40))
witch = Character("Witch", 200, Attack("Fireball", 20), Attack(
    "Ice Shards", 25), Attack("Lightning Bolt", 30))
spectre = Character("Spectre", 150, Attack("Ghostly Strike", 60),
                    Attack("Possession", 50), Attack("Haunt", 40))
king = Character("King", 400, Attack("Royal Strike", 90), Attack(
    "King's Guard", 70), Attack("Crown Strike", 80))

character_options = {
    1: elf,
    2: knight,
    3: witch,
    4: spectre,
    5: king,
}

print("1) Elf\n2) Knight\n3) Witch\n4) Spectre\n5) King\nPlease choose your character:")
character = int(input())
player = Player(character_options[character].name, character_options[character].hp, character_options[character].attacks[0],
                character_options[character].attacks[1], character_options[character].attacks[2])

ogre = Character("Ogre", 500, Attack("Ogre Smash", 50),
                 Attack("Ogre Charge", 40), Attack("Ogre Swipe", 30))

while True:
    player_attack = player.choose_attack()
    ogre.hp -= player_attack.damage
    print(f"{player.name} hits {ogre.name} with {player_attack.name}!\n{ogre.name}'s health is now {ogre.hp}.")

    if ogre.hp <= 0:
        print("The Ogre has lost.")
        break

    ogre_attack = ogre.attacks[0]  # The ogre always uses its first attack
    player.hp -= ogre_attack.damage
    print(f"{ogre.name} hits {player.name} with {ogre_attack.name}!\n{player.name}'s health is now {player.hp}.")

    if player.hp <= 0:
        print("You have fallen.")
        break
