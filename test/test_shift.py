from bennibot.shift import getshift


def test_shift():
    assert len(getshift()) > 0
