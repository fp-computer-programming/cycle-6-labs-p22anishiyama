# Author: ATN 11/12/21

subjects = ["Theology II", "French IV", "Asian Studies"]
print(subjects)

subjects.append("Biology")
print(subjects)

print(subjects.index("Biology"))

subjects.sort()
print(subjects)

new_subjects = subjects.copy()

new_subjects.reverse()
print(new_subjects)
