
my_list = [1, 3, 7, 4, 5, 3, 6, 8]
def quick_sort(list):
    if len(list) == 1:
        return list
    pivot = list[0]
    i = 1
    j = len(list) - 1
    while not i >= j:
        switch = False 
        while not switch:
            if list[i] > list[0] or i == j:
                switch = True
            else:
                i = i + 1
        reset = False
        while not reset:
            if list[j] < list[0] or i == j:
                reset = True
            else :
                j = j - 1
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
    temp = list[i - 1]
    list[i - 1] = list[0]
    list[0] = temp
    list1 = list[:i]
    list2 = list[i:]
    return quick_sort(list1) + quick_sort(list2)

print(quick_sort(my_list))

    
                
        
