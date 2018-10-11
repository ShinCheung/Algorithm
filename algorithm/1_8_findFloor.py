#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 电梯停在哪一层能让此次乘坐电梯的所有乘客爬楼梯层数之和最少

# 如果电梯停在第i层
# i层以上：N3个乘客的目的楼层
# i层：N2个乘客的目的楼层
# i层以下：N1个乘客的目的楼层
# 所有乘客总共要爬Y层

# 如果停在i-1层
# 所有目的地在第i层及以上的乘客都需要多爬1层，总共需要多爬N2+N3层
# 所有目的地在第i-1层及以下的乘客可以少爬1层，总共可以少爬N1层
# 因此乘客总共需要爬的层数是Y-N1+(N2+N3) = Y-(N1-N2-N3)

# 如果停在i+1层
# 所有目的地在第i层及以下的乘客都需要多爬1层，总共需要多爬N1+N2层
# 所有目的地在第i+1层及以上的乘客可以少爬1层，总共可以少爬N3层
# 因此乘客总共需要爬的层数是Y+(N1+N2)-N3 = Y-(N3-N1-N2)

# 当N1>N2+N3，停在i-1层好，乘客走的层数减少(N1-N2-N3)
# 当N3>N1+N2，停在i+1层号，乘客走的层数减少(N3-N1-N2)
# other，停在i层好，注：此处的other = N1<=N2+N3 and N3<=N1+N2

def findFloor(alist):
    for i in range(len(alist)):
        N1 = sum(alist[:i])	# [:] 前闭后开
        N2 = alist[i]
        N3 = sum(alist[i+1:])
        if N1 + N2 - N3 >= 0 and N2 + N3 - N1 >= 0:
            return i

test = [4,0,3,2,1,0,4,0,8]
print(findFloor(test))