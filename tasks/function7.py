def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])
people_list = [("Alpha", 30), ("Bravo", 25), ("Charlie", 20)]
sorted_people = sort_by_age(people_list)
print(sorted_people)