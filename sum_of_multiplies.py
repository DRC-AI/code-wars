def solution(number):
    
    mylist = list(range(0,number,3)) + list(range(0,number,5))
    
    mylist = list(dict.fromkeys(mylist))
    
    return sum(mylist)

print(solution(10))
