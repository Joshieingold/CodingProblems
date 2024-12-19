num_problems = int(input())
for _ in range(num_problems):
    sum_num = 0
    even_num = 0
    odd_num = 0
    indexer, use_num = map(int, input().split())
    

    for i in range(1, use_num + 1):
        even_num += 2 * i

    for i in range(1, use_num + 1):
        odd_num += 2 * i - 1

    sum_num = sum(range(1, use_num + 1))
    
    print(indexer, sum_num, odd_num, even_num)
