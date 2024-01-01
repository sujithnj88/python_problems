import pytest
import sys


class TestLastStoneWeight:
    @pytest.mark.parametrize(
        "stone_weight,expectation",
        [
            ([2, 7, 4, 1, 8, 1], 1)
            ]
        )
    def test_valid_case(self, last_stone_weight, stone_weight, expectation):
        assert last_stone_weight.find_weight(stone_weight) == expectation


if __name__ == "__main__":
    sys.exit(pytest.main())
