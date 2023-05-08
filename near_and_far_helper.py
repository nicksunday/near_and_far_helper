#!/usr/bin/env python3

from random import randint


class NearAndFarMap():
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.selected_quests = []

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def generate_quests(self, player_count):
        quest_counter = (player_count * 3) + 1
        start = self.get_start()
        end = self.get_end()
        quest_list = []
        if str(start).isalpha():
            quest_list = list(range(ord(start), ord(end) + 1))
        else:
            quest_list = list(range(start, end + 1))
        while quest_counter > 0:
            random_quest = randint(0, len(quest_list) - 1)
            self.selected_quests.append(
                quest_list.pop(random_quest)
            )
            quest_counter -= 1
        self.selected_quests.sort()

    def print_quests(self):
        if not self.selected_quests:
            print("No quests generated yet.")
        else:
            print(f"\n    {self.name} Map Quests\n")
            for quest in self.selected_quests:
                if str(self.get_start()).isalpha():
                    print(f"\t\t{chr(quest)}")
                else:
                    print(f"\t\t{quest}")


def main():
    map_prompt = """
    Select A Map By Number:
    
        1) Glogo Caverns
        2) Broken Plains
        3) Crimson Forest
        4) Meteor Mountain
        5) Toxic Desert
        6) Cloudy Valley
        7) Dried Sea
        8) Fire Delta
        9) Rocktooth Isles
        10) Mammoth Jungle
        11) The Last Ruin
    
    Selection: """

    map_selection = int(input(map_prompt))

    if map_selection not in range(1,12):
        print("Please enter a number between 1 and 11 to pick a map.")
        map_selection = int(input(map_prompt))

    player_count_prompt = "\n    How many players? "

    player_count = int(input(player_count_prompt))

    match map_selection:
        case 1:
            chosen_map = NearAndFarMap("Glogo Caverns", "a", "p")
        case 2:
            chosen_map = NearAndFarMap("Broken Plains", 1, 16)
        case 3:
            chosen_map = NearAndFarMap("Crimson Forest", 17, 32)
        case 4:
            chosen_map = NearAndFarMap("Meteor Mountain", 33, 48)
        case 5:
            chosen_map = NearAndFarMap("Toxic Desert", 49, 64)
        case 6:
            chosen_map = NearAndFarMap("Cloudy Valley", 65, 80)
        case 7:
            chosen_map = NearAndFarMap("Dried Sea", 81, 96)
        case 8:
            chosen_map = NearAndFarMap("Fire Delta", 97, 112)
        case 9:
            chosen_map = NearAndFarMap("Rocktooth Isles", 113, 128)
        case 10:
            chosen_map = NearAndFarMap("Mammoth Jungle", 129, 145)
        case 11:
            chosen_map = NearAndFarMap("The Last Ruin", 146, 160)

    chosen_map.generate_quests(player_count)
    chosen_map.print_quests()

if __name__ == '__main__':
    main()
