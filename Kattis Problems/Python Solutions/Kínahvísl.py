initial = input()
final = input()
different_count = 1
for i in range(len(initial)):
    if initial[i] != final[i]:
        different_count += 1
    else: pass
print(different_count)