def solution(phone_number):
    answer = phone_number[-4:]
    star = '*'*(len(phone_number)-4)
    return star + answer