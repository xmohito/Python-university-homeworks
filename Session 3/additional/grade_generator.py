import random
from collections import Counter

students_surnames = ['Smith', 'Smith', 'Williams', 'Brown', 'Jones']

surname_counts = Counter(students_surnames)
unique_surnames = []

for surname, count in surname_counts.items():
    if count == 1:
        unique_surnames.append(surname)
    else:
        for i in range(count):
            unique_surnames.append(f"{surname}{i + 1}")

grades = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
gradebook = {surname: random.choice(grades) for surname in unique_surnames}

with open('gradebook_note.txt', 'w') as file:
    for index, (student, grade) in enumerate(gradebook.items(), start=1):
        file.write(f'{index}. {student} : {grade}\n')


