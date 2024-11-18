import sys

# 입력이 파일처럼 처리되므로 sys.stdin을 사용
for line in sys.stdin:
    print(line.strip())