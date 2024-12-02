def solution(participant, completion):
    answer = ''
    dic = {}
    
    for i in participant:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    
    for i in completion:
        if i in dic:
            if dic[i] == 1:
                dic.pop(i)
            else:
                dic[i] = dic[i] - 1
    
    for i in dic:
        for _ in range(dic[i]):
            answer += i
        
    
    return answer