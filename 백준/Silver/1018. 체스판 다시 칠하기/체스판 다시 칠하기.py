n,m = map(int,input().split())

mtr = list()
cnt = list()

for i in range(n):
    mtr.append(input())
    
for a in range(n-7):
    
# 8*8로 자르기 위해, -7해준다
    for b in range(m-7):
        
        # 흰색으로 시작
        w_index = 0 
        # 검은색으로 시작
        b_index = 0 
        
        # 시작지점
        for i in range(a, a+8):
            
            # 시작지점
            for j in range(b, b+8): 
                
                # 짝수인 경우
                if (i + j) % 2 == 0:
                    
                    # W가 아니면, 즉 B이면
                    if mtr[i][j] != 'W':
                    
                        # W로 칠하는 갯수
                        w_index += 1 
                    
                    # W일 때
                    else: 
                        # B로 칠하는 갯수
                        b_index += 1 
                
                # 홀수인 경우
                else:
                    
                    # W가 아니면, 즉 B이면
                    if mtr[i][j] != 'W':
                        # B로 칠하는 갯수
                        b_index += 1
                    
                    else:
                        # W로 칠하는 갯수
                        w_index +=1 
        
        # W로 시작할 때 경우의 수                
        cnt.append(w_index) 
        
        # B로 시작할 때 경우의 수
        cnt.append(b_index) 

print(min(cnt))