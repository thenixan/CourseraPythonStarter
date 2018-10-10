roubles = int(input())
kopecks = int(input())
count = int(input())

price = roubles * 100 + kopecks

amount = price * count

print(amount // 100, amount % 100)
