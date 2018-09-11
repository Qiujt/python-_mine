result=0
counter=0

while counter<100:
    counter+=1
    if counter%2:       ##推荐简写##只有1和0两种情况，1为True,0为False
    #if counter%2==1:
        continue
    result+=counter
print(result)