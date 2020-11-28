list = ["level"]

# 첫번째 방법
isSame = False
for str in list:
    print(str)
    for j in range(len(str) // 2):
        #print(str[j])
        if str[j] == str[-1 - j]:
            isSame = True
        else:
            isSame = False
            break
    print("%s is %s" %(str , isSame))

print(isSame)

print("##########################")
# 두번째 방법
for str in list:
    print(str)
    # ::-1 수식은 문자열을 reversing 해준다.
    if str == str[::-1]:
        print("True")
    else:
        print("False")





