# 1. 각 문장은 줄바꿈과 무관하게 오직 구두점 ('.', '?', '!')으로 구분된다.
# 2. 문장안에서 각 단어들은 공백 (' ')으로 구분된다.
# 3. 단어 중에서 이름이 되는 조건은 오직 첫 글자만 알파벳 대문자이고 나머지는 모두 알파벳 소문자인 단어 뿐이다. (예: "Annyung", "Hasae" 등)
# 3-1. 3번의 예외로 알파벳 대문자 한글자도 이름으로 간주한다. (예: 'A', 'B' 등)
# 3-2. 어떤 단어가 문장의 마지막이라서 구두점이 붙었을지라도, 3번 조건을 만족한다면 이름으로 간주한다. (예: "Yo!", "Bro?" 등)
# 대문자 65~90 소문자 97~122 마침표 = 46 물음표 = 63 느낌표 = 33

for t in range(1, int(input())+1):
    start = 0
    N = int(input())
    tmp = []
    sentence = input()

    # 마침표, 물음표, 느낌표를 기준으로 문장 나누기
    for x in range(len(sentence)):
        if ord(sentence[x]) == 46 or ord(sentence[x]) == 63 or ord(sentence[x]) == 33:
            tmp.append(sentence[start:x])
            start = x + 2

    ans = []
    for j in range(N):
        count = 0
        # 쪼갠 문장을 한 단어씩 나누기
        word = tmp[j].split()
        for a in range(len(word)):
            aa = list(word[a])
            # 첫 알파벳이 대문자라면
            if 65 <= ord(aa[0]) <= 90:
                small = 0
                for b in range(1, len(aa)):
                    if 97 <= ord(aa[b]) <= 122:
                        small += 1
                if small == len(aa) - 1:
                    count += 1
        ans.append(str(count))
    print('#{} {}'.format(t,' '.join(ans)))
