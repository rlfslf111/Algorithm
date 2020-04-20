class Tree:
    def __init__(self):
        self.lst = [0]

    def sort(self,num):
        if num >= 2:
            if self.lst[num] < self.lst[num//2]:
                self.lst[num], self.lst[num // 2] = self.lst[num // 2], self.lst[num]
                self.sort(num // 2)

    def push(self, data):
        num = len(self.lst)
        self.lst.append(data)
        self.sort(num)

    def my_sum(self, node):
        if node <= 1:
            return self.lst[node]
        else:
            return self.lst[node] + self.my_sum(node // 2)

    def result(self):
        last = len(self.lst) - 1
        self.sum = 0
        if last >= 2:
            return self.my_sum(last // 2)
        else:
            return 0

for t in range(1,int(input())+1):
    N = int(input())
    tree = Tree()
    for i in map(int,input().split()):
        tree.push(i)
    print('#{} {}'.format(t,tree.result()))