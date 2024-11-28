while True:
    input_num = input()

    if input_num == '0':
        break

    else:
        if input_num == input_num[::-1]:
            print('yes')
        else:
            print('no')