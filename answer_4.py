

def ads_pairs(_list):
    count = 0 
    for i in range(len(_list)):
        for j in range(i+1,len(_list)):
            if _list[i]+_list[j] % 30 == 30:
                count += 1
    return count

if __name__ == "__main__":
    _list1 = [30,30,30]
    _list2 = [15,10,75,50,20]
    print(ads_pairs(_list1))
    print(ads_pairs(_list2))
