#### Activity Selection Greedy Approach I ####

def greedy_activity_selection(activity):
    activity.sort(key=lambda x:x[1])
    count=1
    last_activity=activity[0][1]
    
    for i in range(1, len(activity)):
        if activity[i][0]>=last_activity:
            count+=1
            last_activity=activity[i][1]
    return count
array = [(2,4),(3,5),(0,6),(5,7),(8,9),(1,3)]
print(greedy_activity_selection(array))