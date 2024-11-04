# Dylan Stitt
# Unit 3 Lab 4
# Binary Search

def binarySearch(target, nums, pointer=0):
    if len(nums) == 1 and nums[0] == target:
        return pointer
    elif len(nums) == 1 and nums[0] != target:
        return None

    ind = len(nums)//2
    left = nums[:ind]
    right = nums[ind:]

    if target < nums[ind]:
        return binarySearch(target, left, pointer)
    else:
        return binarySearch(target, right, pointer=ind+pointer)

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    test1 = binarySearch(2, nums)
    print("\n\nTest 1 - search for 2")
    print(f"Your returned index: {test1}")
    print(f"Test passed? {test1 == 1}\n\n")

    test2 = binarySearch(7, nums)
    print("Test 2 - search for 7")
    print(f"Your returned index: {test2}")
    print(f"Test passed? {test2 == 6}\n\n")

    test3 = binarySearch(9, nums)
    print("Test 3 - search for 9")
    print(f"Your returned index: {test3}")
    print(f"Test passed? {test3 == 8}\n\n")

    test4 = binarySearch(99, nums)
    print("Test 4 - number doesn't exist")
    print(f"Your returned index: {test4}")
    print(f"Test passed? {test4 == None}\n\n")

if __name__ == '__main__':
    main()
