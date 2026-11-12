# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):

    # Outline (write your plan here first):
    #   Loop through each item in `nums`, as
    #   well as every other number.
    #
    #   If their sum is `target`, then return the
    #   indexes: (a, b)

    for a_index in range( len(nums) ):
        
        for b_index in range(a_index+1, len(nums) ):

            a = nums[a_index]
            b = nums[b_index]

            if a + b == target: return [ a_index, b_index ]
    pass


def max_profit(prices):
    # Outline:
    #   Loop through the prices, and find
    #   the index of the lowest cost.
    #
    #   Then, loop through the rest of the list,
    #   getting the maximum value greater than the minimum

    minimum: None | int = None

    for i in range( len(prices) ):

        if minimum is None:
            minimum = i
        else:
            if prices[i] < prices[minimum]:
                minimum = i

    if minimum is None: return 0

    maximum: None | int = None

    for i in range(minimum+1, len(prices)):
        if maximum is None:
            maximum = i
        else:
            if prices[i] > prices[maximum]:
                maximum = i
    
    if maximum is None: return 0

    return prices[maximum] - prices[minimum]


def max_subarray(nums):
    # Outline:
    #   Generate a list of all the different
    #   possible maximum values, based on
    #   varying start and end indexes.
    #
    #   Then, loop through all the maximum
    #   values, and return the largest.

    maximums = []
    maximum = None

    for start in range( len(nums) ):
        for end in range( start, len(nums)):
            maximums.append( sum(nums[start:end+1]) )


    for total in maximums:
        if maximum is None or total > maximum:
            maximum = total

    return maximum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   Loop through each character in the string.
    #
    #   If it's an opening bracket, add it to the
    #   stack
    #
    #   If it's a closing bracket, and there are
    #   brackets still in the stack, return False
    #   if the last one is not the same type as the
    #   current one
    # 
    #   If the closing bracket is the same type as
    #   the last opening bracket, it is safe to
    #   remove it from the stack.abs
    # 
    #   At the end, if there are still brackets in
    #   the stack, then they have not been closed
    #   properly (return False). If it's empty,
    #   return True

    brackets: list[str] = []

    open_bracket = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in s:

        if char in "([{":
            brackets.append(char)
            continue

        if char in ")]}":
            if len(brackets) == 0 or brackets[-1] != open_bracket[char]:
                return False
            
            brackets.pop()
    
    return True if len(brackets) == 0 else False


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
