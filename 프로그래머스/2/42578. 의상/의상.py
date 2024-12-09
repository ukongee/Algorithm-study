def solution(clothes):
    answer = 1
    dic = {}
    
    for _, i in clothes:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    for cnt in dic.values():
        answer *= (cnt + 1)
    
    return answer - 1