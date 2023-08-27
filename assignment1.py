"""
Replace the contents of this module docstring with your own details
Name: Tang Jiahui
Date started: 25/8/2023
GitHub URL:
"""
import random

MENU = "Menu:\nL - List places\nR - Recommend random place\nA - Add new place\nM - Mark a place as visited\nQ - Quit"


def main():
    print("Travel Tracker 1.0 - by Tang Jiahui")
    places_names = []
    visited_places = []
    non_visited_places = []
    place = read_file(non_visited_places, places_names, visited_places)
    print(MENU)
    choice = input("").upper()
    while choice != "Q":
        if choice == "L":
            list_places(non_visited_places, places_names, visited_places)
        elif choice == "R":
            recommend(non_visited_places)
        elif choice == "A":
            add_new_place(non_visited_places, places_names)
        elif choice == "M":
            mark_visited(non_visited_places, places_names, visited_places)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input("").upper()
    new_places_names = []
    save_file(new_places_names, non_visited_places, place, visited_places)


def save_file(new_places_names, non_visited_places, place, visited_places):
    """Save the places to the csv file"""
    for i in range(0, len(non_visited_places)):
        new_places_names.append(non_visited_places[i])
    for i in range(0, len(visited_places)):
        new_places_names.append(visited_places[i])
    new_place_file = open("places.csv", "w")
    for line in range(0, len(new_places_names)):
        new_places_names[line][2] = str(new_places_names[line][2])
        new_place_file.writelines(new_places_names[line][0])
        for i in range(1, len(place)):
            new_place_file.write(",")
            new_place_file.writelines(new_places_names[line][i])
        new_place_file.writelines("\n")
    print(f"{len(new_places_names)} places saved to {new_place_file.name}")
    print(f"Have a nice day :)")
    new_place_file.close()


def read_file(non_visited_places, places_names, visited_places):
    """read the scv file and get the places"""
    places_file = open("places.csv", "r")
    for line in places_file.readlines():
        place = line.strip().split(",")
        place[2] = int(place[2])
        places_names.append(place)
        if place[3] == "n":
            non_visited_places.append(place)
        else:
            visited_places.append(place)
    print(f"{len(places_names)} places loaded from {places_file.name}")
    visited_places.sort(key=priority, reverse=False)
    non_visited_places.sort(key=priority, reverse=False)
    places_file.close()
    return place


def mark_visited(non_visited_places, places_names, visited_places):
    """mark the places as visited"""
    if len(non_visited_places) == 0:
        print("No unvisited places")
    else:
        list_places(non_visited_places, places_names, visited_places)
        print("Enter the number of a place to mark as visited")
        place_choice = input('')
        while True:
            if place_choice.isdigit() == False:
                print("Invalid input; enter a valid number")
            else:
                place_choice = int(place_choice)
                if place_choice <= 0:
                    print("Number must be > 0")
                elif place_choice > len(places_names):
                    print("Invalid place number")
                else:
                    break
            place_choice = input("")
        if len(places_names) >= place_choice > len(non_visited_places):
            print(f"You have already visited {visited_places[place_choice - len(places_names) - 1][0]}")
        else:
            visit_place = non_visited_places[place_choice - 1]
            visit_place[3] = "v"
            non_visited_places.remove(non_visited_places[place_choice - 1])
            visited_places.append(visit_place)
            visited_places.sort(key=priority, reverse=False)
            print(f"{visit_place[0]} in {visit_place[1]} visited!")


def add_new_place(non_visited_places, places_names):
    """add the new place"""
    add_place = []
    add_place_name = input("Name:")
    while add_place_name == "":
        print("Input can not be blank")
        add_place_name = input("Name:")
    add_place.append(add_place_name)
    add_country = input("Country:")
    while add_country == "":
        print("Input can not be blank")
        add_country = input("Country:")
    add_place.append(add_country)
    add_priority = int(input("Priority:"))
    while add_priority == "":
        print("Input can not be blank")
        add_priority = input("Priority:")
    add_place.append(add_priority)
    add_place.append("n")
    places_names.append(add_place)
    non_visited_places.append(add_place)
    non_visited_places.sort(key=priority, reverse=False)
    print(f"{add_place_name} in {add_country} (priority {add_priority}) added to Travel Tracker")


def recommend(non_visited_places):
    """make a random recommend"""
    if len(non_visited_places) == 0:
        print("No places left to visit!")
    else:
        print("Not sure where to visit next?")
        random_city_number = random.randint(0, len(non_visited_places) - 1)
        print(
            f"How about... {non_visited_places[random_city_number][0]} in {non_visited_places[random_city_number][1]}?")


def list_places(non_visited_places, places_names, visited_places):
    """display the list of the places"""
    longest_name = 0
    for i in range(0, len(places_names)):
        if len(places_names[i][0]) > longest_name:
            longest_name = len(places_names[i][0])
    longest_country_name = 0
    for i in range(0, len(places_names)):
        if len(places_names[i][1]) > longest_country_name:
            longest_country_name = len(places_names[i][1])
    longest_priority = 0
    for i in range(0, len(places_names)):
        if places_names[i][2] // 10 + 1 > longest_priority:
            longest_priority = places_names[i][2] // 10 + 1
    for i in range(0, len(non_visited_places)):
        print(
            f"*{i + 1}. {non_visited_places[i][0]:{longest_name}} in {non_visited_places[i][1]:{longest_country_name}} {non_visited_places[i][2]:>{longest_priority}}")
    for j in range(0, len(visited_places)):
        print(
            f" {i + 2 + j}. {visited_places[j][0]:{longest_name}} in {visited_places[j][1]:{longest_country_name}} {visited_places[j][2]:>{longest_priority}}")
    if len(non_visited_places) == 0:
        print(f"{len(places_names)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(places_names)} places. You still want to visit {len(non_visited_places)} places.")


def priority(place):
    """make a location for the list in the list"""
    return place[2]


if __name__ == '__main__':
    main()
