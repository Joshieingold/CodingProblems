num_boxes, num_colours = map(int,input().split(" "))
num_removed = 0
for i in range(num_boxes):
    crayon_lst = list(input().split(" "))
    found_colors = []
    for j in crayon_lst:
        if j not in found_colors:
            found_colors.append(j)
            if crayon_lst.count(j) > 1:
                num_removed += crayon_lst.count(j) - 1
print(num_removed)
