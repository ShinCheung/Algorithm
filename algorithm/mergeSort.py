#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import merge

def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist)//2
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    # return merge(left, right)
    return list(merge(left, right))
 
# def merge(left, right):
#     l, r = 0, 0
#     result = []
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     result.extend(left[l:])
#     result.extend(right[r:])
#     return result

alist = [54,26,93,17,77,31,44,55,20]
print(mergeSort(alist))
