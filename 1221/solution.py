num_dict = {
    "ZRO":0, 
    "ONE":1, 
    "TWO":2, 
    "THR":3, 
    "FOR":4, 
    "FIV":5, 
    "SIX":6, 
    "SVN":7, 
    "EGT":8, 
    "NIN":9
}

TC = int(input())

for tc in range(TC):
    tc, n = input().split()
    n = int(n)    
    print(tc)

    numbers = list(input().split())
    for num_str in num_dict.keys():
        cnt = numbers.count(num_str)
        for i in range(cnt):
            print(num_str, end=" ")
    
    print("")