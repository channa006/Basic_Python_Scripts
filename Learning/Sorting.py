# Sorting Lists , Tuples and Objects

# # Ascending Order
# li = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# so_li = sorted(li)

# li.sort()

# print('Sorted Variable: \t', so_li)
# print('Sorted Variable: \t', li)

# Reverse the Order
# li = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# so_li = sorted(li, reverse=True)

# li.sort(reverse=True)

# print('Sorted Variable: \t', so_li)
# print('Sorted Variable: \t', li)


# Tuples
# li = (9, 8, 7, 6, 5, 4, 3, 2, 1)
# so_li = sorted(li)

# print('Tuple: \t', so_li)


li = [-1, -5, -4, 3, 2, 1]
so_li = sorted(li, key=abs)

print('Tuple :\t', so_li)
