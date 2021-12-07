from homework_06.hw.counter import User


def test_negative_case():
    """Testing wrong cases"""
    assert User.get_created_instances() != -1  # 0
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() != 2  # 3


def test_positive_case():
    """Testing correct cases"""
    user, _, _ = User(), User(), User()
    assert user.reset_instances_counter() == 6  # 6
    assert user.get_created_instances() == 0
