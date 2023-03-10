def jump_search(arr, var):
    n = len(var)
    jump = int(n**0.5) # menghitung jump dengan pangkat 0.5 (akar)
    left = 0
    right = 0

    # mencari blok tempat nama bisa berada
    while right < n and var[right] <= arr:
        left = right
        right += jump

    # pencarian pada blok yang tepat
    for i in range(left, min(right, n)):
        if isinstance(var[i], list):
            if var[i][-1] >= arr:
                for j in range(len(var[i])):
                    if var[i][j] == arr:
                        return i, j
            else:
                continue
        elif var[i] == arr:
            return i, None

    return None

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Mencari nama "Avivah" dan "Wibi"
names = ["Arsel", "Avivah", "Daiva", "Wahyu", "Wibi"]
for arr in names:
    index = jump_search(arr, var)
    if index is not None:
        if index[1] is not None:
            print("{} ditemukan pada index {} pada kolom {}".format(arr, index[0], index[1]))
        else:
            print("{} ditemukan pada index {}".format(arr, index[0]))
    else:
        print("{} tidak ditemukan".format(arr))