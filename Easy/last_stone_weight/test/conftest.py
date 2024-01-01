import pytest

import LatStoneWeight


@pytest.fixture()
def last_stone_weight() -> LatStoneWeight:
    return LatStoneWeight()
