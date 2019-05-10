T = int(input())
for t in range(T):
    n, x = map(int , input().split())
    w = [int(i) for i in input().split()]
    adj = [[] for i in range(n + 1)]
    for i in range(1, n):
        u, v = map(int, input().split())
        adj[u].append(v);
        adj[v].append(u);
    root = 1
    gain = [0] * (n + 1)
    state = [0] * (n + 1)
    stack = []
    stack.append(root)
    state[root] = 1
    while(len(stack) != 0):
        flag = 0
        root = stack[-1]
        for i in adj[root]:
            if state[i] == 0:
                stack.append(i)
                state[i] = 1
                flag = 1
        if flag == 0:
            gain[root] = w[root - 1]
            for i in adj[root]:
                if state[i] == 2:
                    gain[root] += gain[i]
            gain[root] = max(gain[root], -x)
            state[root] = 2
            stack.pop()
    print(gain[1])