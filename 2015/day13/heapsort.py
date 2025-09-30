def heapalgorithm(n: int, A: list) -> list:
    c = list()
    for i in range(n):
        c.append(0)

    yield A

    i = 0  # index
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                A[0], A[i] = A[i], A[0]
            else:
                A[c[i]], A[i] = A[i], A[c[i]]

            yield A

            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
