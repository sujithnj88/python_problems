from typing import List, Optional


class TwoSum:
    @staticmethod
    def find_out_two_sum_elements(numbers: List[int], target: int) -> List[Optional[int]]:
        """
        Iterate over each element in the list and return the list of indexes which gives expected target sum.
        """
        iterated_data = {}
        sum_indices = []

        for i, value in enumerate(numbers):
            remaining = target - value

            if remaining in iterated_data:
                sum_indices.extend([iterated_data[remaining], i])
                break
            else:
                iterated_data[value] = i

        return sum_indices
