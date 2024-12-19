test_cases = int(input())
while test_cases > 0:
    raw_data = input().split(" ")
    data = []
    for i in raw_data:
        data.append(int(i))
    num_power_bar = data[0]
    power_devices = 0
    while num_power_bar > 0:
        power_devices += data[num_power_bar - 1] - 1
        num_power_bar -= 1
    print(power_devices)
    test_cases -= 1