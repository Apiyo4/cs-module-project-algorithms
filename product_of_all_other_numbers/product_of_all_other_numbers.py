'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    mult =  1
    for i in arr:
        mult = mult * i
    print(mult)
    for i in range(0, len(arr)):
        arr[i] = int(mult / arr[i])
    return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

"""
Plan
    Create var mult
    Loop through array
        -Use * for multiplying array elements 
    Loop through array again
        -Use / for dividing mult with item in list
        -Use int to convert value to integers
    Return arr
"""


"""
Pseudocode
    Init mult with value 1
    Loop through the array 
        -Multiply mult with item in the list
    Loop through array again
        -Divide mult with item in the list
        -Convert the float value to int
    Return arr 

"""