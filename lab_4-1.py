# Author: ATN 11/12/21

colors = ["blue", "yellow", "orange", "red"]
print(colors)

colors.extend(["black", "white", "violet"])
print(colors)

print(colors.count('yellow'))

colors.insert(3, "indigo")
print(colors)

colors.clear()
print(colors)

print(colors.count("red"))
