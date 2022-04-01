if __name__ == '__main__':
    V = 10
    N = 2

    size = [1, 10]
    value = [100, 900]
    maxvalue = []
    choice = []

    for k in range(0, V + 1):
        maxvalue.append(0)
        choice.append(-1)

    for s in range(0, N-1 + 1):
        for t in range(size[s], V + 1):
            temp = maxvalue[t - size[s]] + value[s]
            if temp > maxvalue[t]:
                maxvalue[t] = temp
                choice[t] = s

    k = V
    while choice[k] >= 0:
        # print(choice[k])
        k = k - size[choice[k]]

    print(maxvalue[V])