from collections import namedtuple, ChainMap, defaultdict


snape_log = {'Harry': 10, 'Hermione': 20}
mcgonagall_log = {'Harry': 5, 'Ron': 15}
flitwick_log = {'Luna': 25}

Student = namedtuple('Student', ['name', 'house', 'year'])
students = [
    Student('Harry', 'Gryffindor', 5),
    Student('Hermione', 'Gryffindor', 5),
    Student('Ron', 'Gryffindor', 5),
    Student('Luna', 'Ravenclaw', 4)
]


combined_log = ChainMap(snape_log, mcgonagall_log, flitwick_log)


name_to_house = {student.name: student.house for student in students}


house_points = defaultdict(int)


for name, house in name_to_house.items():
    if name in combined_log:
        house_points[house] += combined_log[name]


# top_house = max(house_points, key=house_points.get)
# print(top_house)
