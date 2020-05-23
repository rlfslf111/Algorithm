import sys
input = sys.stdin.readline

# 전위 순회 (root, 왼쪽, 오른쪽)
def preorder(root):
    stack = []
    stack.append(root)
    result = ''
    while stack:
        data = stack.pop()
        result += data

        # 오른쪽 자식
        if tree[data][1] != '.':
            stack.append(tree[data][1])

        # 왼쪽 자식
        if tree[data][0] != '.':
            stack.append(tree[data][0])

    return result

# 중위 순회 (왼쪽, root, 오른쪽)
def inorder(root):
    stack = []
    result = ''
    data = root
    stack.append(root)
    while 1:

        # 왼쪽부터 root로 순회
        while tree[data][0] != '.':
            if data not in result:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break

        if stack:
            data = stack.pop()
            result += data
            if tree[data][1] != '.':
                stack.append(tree[data][1])
                data = tree[data][1]
        else:
            break

    return result

#후위 순회 (왼쪽, 오른쪽, root)
def postorder(root):
    stack = []
    result = ''
    data = root
    stack.append(root)

    while 1:

        #왼쪽 자식 확인
        while tree[data][0] != '.':
            if tree[data][0] not in result:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break

        # 오른족 자식의 유무를 위해 pop하지 않고 저장
        last_data = stack[-1]

        # 오른쪽 자식 확인
        if tree[last_data][1] == '.':
            result += stack.pop()

            if stack:
                data = stack[-1]
            else:
                # stack 이 비어있으면 종료
                break
        else:
            # 오른쪽에 자식이 존재한다면,
            if tree[data][1] not in result:
                stack.append(tree[data][1])
                data = tree[data][1]
            else:
                # 오른쪽 자식이 이미 나왔다면 현재의 노드를 출력한다.
                result += stack.pop()
                if stack:
                    data = stack[-1]
                else:
                    break
    return result

N = int(input().strip())
tree = {}
for i in range(N):
    inp = input().strip().split(' ')
    tree[inp[0]] = [inp[1],inp[2]]

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))