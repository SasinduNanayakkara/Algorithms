from ast import List
import heapq

listItem = [5, 7, 9, 1, 3, 2, 4, 6, 8]

heapq.heapify(listItem) # convert list to heap

print("the created heap : ", end="")
print(list(listItem))

heapq.heappush(listItem, 10) # add an element to heap

print("the modified heap : ", end="")
print(list(listItem))

heapq.heappush(listItem, 7) # add an element to heap

print("the modified heap : ", end="")
print(list(listItem))

print("the smallest element : ", end="")
print(heapq.heappop(listItem)) # remove the smallest element from heap

