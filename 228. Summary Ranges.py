nums = []
start = nums[0] if len(nums) > 0 else [] 
stop = None
output = list()
lastoutput = []
for i in range(1, len(nums)):
    if nums[i] - 1 == nums[i-1]:
        stop = nums[i]
    else:
        output.append([start, stop])
        start = nums[i]
        stop = None
output.append([start, stop])
for i in output:
    if i[1]:
        lastoutput.append([f"{i[0]}->{i[1]}"])
    else:
        lastoutput.append([f"{i[0]}"])
