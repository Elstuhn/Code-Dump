def determinant(M):
    if len(M) == 1:
        return M[0][0]

    total = 0
    for column, element in enumerate(M[0]):
        print(element)
        K = [x[:column] + x[column + 1:] for x in M[1:]]
        s = 1 if column % 2 == 0 else -1
        total += s * element * determinant(K)
    return total
