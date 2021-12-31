from homework_11.hw.hw2 import Order, Morning_discount, Elder_discount


def test_morning_case():
    """Testing Morning context"""
    order_1 = Order(100, Morning_discount())
    assert order_1.final_price() == 75


def test_elder_context():
    """Testing Elder context"""
    order_2 = Order(100, Elder_discount())
    assert order_2.final_price() == 10
