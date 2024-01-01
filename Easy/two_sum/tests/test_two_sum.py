from typing import List, Optional

import pytest
import sys

from easy import TwoSum


class TestTwoSum:
    @pytest.mark.parametrize(
        "input_arg,target_num,expected_output",
        [
            (
                    [2, 7, 9, 11, 15],
                    9,
                    [0, 1]
            ),
            (
                    [2, 7, 9, 11, 19],
                    13,
                    [0, 3]
            ),
            (
                    [2, 7, 9, 11, 19],
                    28,
                    [2, 4]
            ),
            (
                    [2, 7, 9, 11, 19],
                    26,
                    [1, 4]
            ),
            (
                    [2, 7, 9, 11, 19],
                    21,
                    [0, 4]
            )
        ]
    )
    def test_two_sum_valid_input(
            self,
            two_sum: TwoSum,
            input_arg: List[int],
            expected_output: List[Optional[int]],
            target_num: Optional[int]
    ) -> None:
        assert two_sum.find_out_two_sum_elements(input_arg, target_num) == expected_output

    def test_two_sum_single_element_input(self, two_sum: TwoSum) -> None:
        assert two_sum.find_out_two_sum_elements([2], 9) == []

    def test_two_sum_no_valid_sum(self, two_sum: TwoSum) -> None:
        assert two_sum.find_out_two_sum_elements([2, 7, 9], 7) == []

    def test_invalid_datatype(self, two_sum: TwoSum):
        with pytest.raises(TypeError):
            two_sum.find_out_two_sum_elements([2, 7, 9], "")
        with pytest.raises(TypeError):
            two_sum.find_out_two_sum_elements([2, "7", 9], 9)
        with pytest.raises(TypeError):
            two_sum.find_out_two_sum_elements(1, 2)


if __name__ == "__main__":
    sys.exit(pytest.main())
