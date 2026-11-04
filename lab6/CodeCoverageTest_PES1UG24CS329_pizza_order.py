"""Tests targeting complete executable-line coverage of pizza_order.py."""

import pytest

from pizza_order import delivery_status, order_discount, pizza_price


def test_pizza_price_rejects_unknown_size():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra-large", 1, False)


def test_pizza_price_rejects_negative_toppings():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)


def test_pizza_price_more_than_three_toppings_with_cheese_burst():
    assert pizza_price("large", 5, True) == 500 + 3 * 40 + 2 * 30 + 100


def test_pizza_price_small_cheese_burst_is_rejected():
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 3, True)


def test_discount_below_minimum_total_is_zero():
    assert order_discount(299, "tuesday", True) == 0


def test_tuesday_student_discount():
    assert order_discount(500, "tuesday", True) == 300


def test_weekend_student_discount():
    assert order_discount(500, "saturday", True) == 50


def test_regular_weekday_student_discount():
    assert order_discount(500, "monday", True) == 100


def test_delivery_too_far():
    assert delivery_status(20, 10.1) == "not deliverable"


def test_delivery_on_time():
    assert delivery_status(30, 10) == "on time"


def test_delivery_late():
    assert delivery_status(45, 5) == "late"


def test_delivery_free_pizza():
    assert delivery_status(46, 5) == "free pizza"
