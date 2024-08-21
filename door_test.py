import pytest

from door import Door, DoorLock

@pytest.fixture
def a_door():
    """

    :return:
    """
    return Door(DoorLock(), 'green')

def test_initial(a_door):
    """

    :param a_door:
    :return:
    """
    assert a_door.color == 'green'

def test_get_set_color(a_door):
    """

    :param a_door:
    :return:
    """
    a_door.color = 'red'
    assert a_door.color == 'red'

def test_door_open(a_door):
    """

    :param a_door:
    :return:
    """
    a_door.open_the_door()
    assert a_door.door_is_open

def test_door_close(a_door):
    """

    :param a_door:
    :return:
    """
    a_door.close_the_door()
    assert a_door.door_is_open is False

def test_door_locking(a_door):
    """

    :param a_door:
    :return:
    """
    a_door.lock_the_door()
    assert a_door._door_is_locked

def test_door_unlock(a_door):
    """

    :param a_door:
    :return:
    """
    a_door.unlock_the_door()
    assert a_door._door_is_locked is False
