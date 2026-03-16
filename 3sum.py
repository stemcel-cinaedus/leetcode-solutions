snums = sorted(nums)
valid_nums = list()
i = 0
while i < len(snums) - 2:
            if i > 0:
                if snums[i] == snums[i - 1]:
                    i+=1
            if i < len(nums) - 1:
                    lh = i + 1
            rh = len(snums) - 1
            while lh < rh:
                        if snums[lh] + snums[rh] + snums[i] == 0:
                            valid_nums.append([snums[i], snums[lh], snums[rh]])
                            lh +=1
                            rh -=1
                        elif snums[lh] + snums[rh] + snums[i] > 0:
                            rh -=1
                        elif snums[lh] + snums[rh] + snums[i] < 0:
                            lh +=1
            i +=1
print(valid_nums)
