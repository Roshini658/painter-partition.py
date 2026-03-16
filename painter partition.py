def painters_partition(boards,painters):# "Painter's partition min partitition takes maximum time"  brute force code using "Linear Search" this code is same exact pattern as "Capacity to ship packages,books allocation,split array sum"
    if painters>len(boards):#if painters more than boards
        return -1#not possible
    start=max(boards)#minimum time needed
    end=sum(boards)#maximum time if one painter paints all
    ans=-1
    for time in range(start,end+1):#try every possible maximum time
        count=1#first painter
        total=0#boards painted by current painter
        for b in boards:#check every board
            if total+b>time:#if work exceeds time limit
                count+=1#assign next painter
                total=b#start with this board
            else:#if within limit
                total+=b#add board to current painter
        if count<=painters:#if boards can be painted
            ans=time#this is maximum time
    return ans#if not possible
boards=[10,20,30,40]#length of boards
painters=2#number of painters
print(painters_partition(boards,painters))#print answer
