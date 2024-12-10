def solution(phone_book):
    
#     phone_book.sort(key=lambda x: int(x))
    
#     for idx, num in enumerate(phone_book):
#         dic = {}
#         for idx2 in range(idx + 1, len(phone_book)):
#             if len(phone_book[idx2]) > len(num):
#                 # 슬라이싱은 비효율적
#                 dic[phone_book[idx2][:3]] = 0

#         if num in dic:
#             return False
#     return True
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True