import heapq

list1 = [5, 7, 9, 1, 3, 2, 4, 6, 8]
list2 = [6, 9, 3, 1, 2, 4, 8, 5, 7]

heapq.heapify(list1)
heapq.heapify(list2)

print("the popped item using heappushpop() : ", end="") # remove the smallest element from heap
print(heapq.heappushpop(list1, 10))

print("the popped item using heapreplace() : ", end="") # remove the smallest element from heap
print(heapq.heapreplace(list2, 20))