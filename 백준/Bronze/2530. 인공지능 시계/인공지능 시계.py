# 입력 받기
a, b, c = map(int, input().split())
d = int(input())

# 현재 시각을 초 단위로 변환
current_time_in_seconds = a * 3600 + b * 60 + c

# 요리 시간 더하기
end_time_in_seconds = current_time_in_seconds + d

# 시, 분, 초로 변환
end_hour = (end_time_in_seconds // 3600) % 24
end_minute = (end_time_in_seconds // 60) % 60
end_second = end_time_in_seconds % 60

# 출력
print(end_hour, end_minute, end_second)