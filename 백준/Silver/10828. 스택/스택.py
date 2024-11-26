class Stack:
    def __init__(self):
        """스택 초기화"""
        self.stack = []

    def push(self, x):
        """스택에 정수 X 추가"""
        self.stack.append(x)

    def pop(self):
        """스택의 최상단 값을 제거하고 반환, 스택이 비어 있으면 -1 반환"""
        return self.stack.pop() if self.stack else -1

    def size(self):
        """스택의 크기 반환"""
        return len(self.stack)

    def empty(self):
        """스택이 비어 있으면 1, 아니면 0 반환"""
        return 1 if not self.stack else 0

    def top(self):
        """스택의 최상단 값을 반환, 비어 있으면 -1 반환"""
        return self.stack[-1] if self.stack else -1


# 명령을 처리하는 메인 함수
def process_commands(commands):
    stack = Stack()  # 스택 객체 생성
    output = []  # 결과를 저장할 리스트

    for command in commands:
        if command.startswith("push"):
            _, x = command.split()
            stack.push(int(x))
        elif command == "pop":
            output.append(stack.pop())
        elif command == "size":
            output.append(stack.size())
        elif command == "empty":
            output.append(stack.empty())
        elif command == "top":
            output.append(stack.top())

    return output


# 입력 처리
import sys
input = sys.stdin.read  # 빠른 입력
commands = input().splitlines()

n = int(commands[0])  # 명령의 개수
commands = commands[1:]  # 명령 리스트

# 명령 처리 및 출력
results = process_commands(commands)
sys.stdout.write("\n".join(map(str, results)) + "\n")