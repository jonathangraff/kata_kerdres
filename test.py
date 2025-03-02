from main import get_winner_and_winning_price


def test_classic():
    bids = {
        "Alice": [5],
        "Bob": [10, 20, 50],
        "David": [40, 60],
        "Charles": [15, 35],
    }
    reserve_price = 45
    assert get_winner_and_winning_price(bids, reserve_price) == ("David", 50)


def test_with_empty_list():
    bids = {
        "Alice": [],
        "Bob": [10, 20, 50],
        "David": [40, 60],
        "Charles": [15, 35],
    }
    reserve_price = 45
    assert get_winner_and_winning_price(bids, reserve_price) == ("David", 50)


def test_with_only_empty_list():
    bids = {
        "Alice": [],
        "Bob": [],
        "David": [],
        "Charles": [],
    }
    reserve_price = 50
    assert get_winner_and_winning_price(bids, reserve_price) == (None, 50)


def test_with_no_winner():
    bids = {
        "Alice": [],
        "Bob": [10, 20, 50],
        "David": [40, 60],
        "Charles": [15, 35],
    }
    reserve_price = 80
    assert get_winner_and_winning_price(bids, reserve_price) == (None, 80)


def test_with_winning_price_is_reserve_price():
    bids = {
        "Alice": [],
        "Bob": [10, 20, 50],
        "David": [40, 60],
        "Charles": [15, 35],
    }
    reserve_price = 55
    assert get_winner_and_winning_price(bids, reserve_price) == ('David', 55)