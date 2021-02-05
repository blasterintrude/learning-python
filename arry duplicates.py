source_list = [1, 726, 726, 726, 123, 124, 2709, 2007, 123]
blank_list = []
for number in source_list:
    if number not in blank_list:
          blank_list.append(number)

print(blank_list)