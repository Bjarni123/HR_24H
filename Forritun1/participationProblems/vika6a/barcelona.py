bags_count, desired_bag = input().split()
bags_list = input().split()

if desired_bag == bags_list[0]:
    print("fyrst")
elif desired_bag == bags_list[1]:
    print("naestfyrst")
else:
    for bagidx in range(int(bags_count)):
        if bags_list[bagidx] == desired_bag:
            print(bagidx + 1, "fyrst")