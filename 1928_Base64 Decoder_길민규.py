import base64

def decode(pre_decode):
    decoding = str(base64.b64decode(pre_decode))
    decode_list = []
    for i in decoding:
        decode_list.append(i)
    return ''.join(decode_list[2:-1])
test_case = int(input())
for x in range(test_case):
    pre_decode = input()
    print('#{} {}'.format(x+1,decode(pre_decode)))