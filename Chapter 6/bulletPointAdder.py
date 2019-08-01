import pyperclip

list_of_points = pyperclip.paste()
list_of_points = list_of_points.split("\n")
list_of_points_with_star = []
for x in list_of_points:
    str1 = "* " + x
    list_of_points_with_star.append(str1)

str2 = "\n".join(list_of_points_with_star)
pyperclip.copy(str2)



