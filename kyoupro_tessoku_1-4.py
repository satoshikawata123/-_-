n = int(input())
binary = bin(n)[2:]       # "0b" を除去
binary = binary.zfill(10) # 10桁になるように左を0で埋める
print(binary)
