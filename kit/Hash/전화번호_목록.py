def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        check=phone_book[i]
        if check == phone_book[i+1][:len(check)]:
            return False
    return True


phone_book=["119", "97674223", "1195524421"]
print(solution(phone_book))