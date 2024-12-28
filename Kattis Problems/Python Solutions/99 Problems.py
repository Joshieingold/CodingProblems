num = int(input())
answer = None
if num <= 99: # If the answer is the max then we already know the answer.
    answer = 99 
else:
    down = num # Mark down and up as our inital number
    up = num
    while str(down)[-2:] != "99":
        down -= 1
    while str(up)[-2:] != "99":
        up += 1
    down_distance = num - down
    up_distance = up - num

    if down_distance < up_distance:
        answer = down
    elif down_distance > up_distance:
        answer = up
    else:
        answer = up
print(answer)
