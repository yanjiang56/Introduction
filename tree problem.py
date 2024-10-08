def maxheight(trees, M):
    low, high = 0, max(trees)
    while low <= high:
        mid = (low + high) // 2
        wood = sum(max(tree - mid, 0) for tree in trees)
        if wood >= M:
            low = mid + 1
        else:
            high = mid - 1

    return high


n = 4
m = 6
tree = [20, 15, 8, 17]

print(maxheight(tree, m))
