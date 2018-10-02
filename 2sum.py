
class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """
        dict = {}
        for i in range(len(numbers)):
            #dict[numbers[i]] = i
            #print (dict)
            if target_sum - numbers[i] in dict.keys() and dict[target_sum - numbers[i]] != i : #ensure not itself; [2,5,4] sum=10 should be false 但是有可能两个5
                return (dict[target_sum - numbers[i]], i)
            dict[numbers[i]] = i #should be here; incase [5,5] 第二个5把第一个覆盖掉 导致return false             
        return None 

            

print(TwoSum.find_two_sum([3, 1, 5, 7, 5, 9], 10))

# class Solution:
#     def twoSum(self, nums, target):
#         hash_table = {}
#         for i in range(0, len(nums)):
#             difference = target - nums[i]
#             if difference in hash_table and hash_table[difference] != i:
#                 return [hash_table[difference], i]
#             hash_table[nums[i]] = i