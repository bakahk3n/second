min_sleep = int(input())
max_sleep = int(input())
total_sleep_hour = int(input())

if total_sleep_hour > max_sleep:
    print("Excess")
else:
    if total_sleep_hour >= min_sleep:
        print("Normal")
    else:
        print("Deficiency")
