import random

print('********猜数字游戏********')
print('\n')
print('请在0到20之间猜一个数字：')
guess = int(input())
secret = random.randint(0, 20)
while guess != secret:
    if guess > 20 or guess < 0:
        print('你输入的数字不在范围内！！！')
        print("请重新输入：")
        guess = int(input())

    else:
        print('你猜错了 ')
        if guess > secret:
            print('大了大了\n')
            guess = int(input("再猜再猜："))
        if guess < secret:
            print('小了小了\n')
            guess = int(input('再猜再猜：'))
        if guess == secret:
            print('恭喜你猜对了！！！')
            break
print('游戏结束！！！')



