import pytest
from gamers import Gamer


def test_Task_1_name_and_age_check():
    gamer = Gamer("John", 14, "JohnForever", "john@gmail.com")
    assert hasattr(gamer, 'name'), "Task 1 is not completed. The 'Gamer' class does not contain the 'name' attribute"
    assert hasattr(gamer, 'age'), "Task 1 is not completed. The 'Gamer' class does not contain the 'age' attribute"


def test_Task_2_add_nickname():
    gamer = Gamer("John", 14, "JohnForever", "john@gmail.com")
    assert hasattr(gamer, 'nickname'), "Task 2 is not completed. The 'Gamer' class does not contain the 'nickname' attribute"


def test_Task_3_add_email():
    gamer = Gamer("John", 14, "JohnForever", "john@gmail.com")
    assert hasattr(gamer, 'email'), "Task 3 is not completed. The 'Gamer' class does not contain the 'email' attribute"


def test_Task_4_change_message(capsys):
    gamer = Gamer("John", 14, "JohnForever", "john@gmail.com")
    gamer.introduce()
    captured = capsys.readouterr()
    expected_output = "Hi, my name is John, I'm 14 years old. You can always reach out by sending an email to john@gmail.com. Look for me in the game by nickname JohnForever."
    assert expected_output in captured.out, f"Task 4 has not been completed. Expected message: {expected_output}, What we got is: {captured.out}"


if __name__ == "__main__":
    pytest.main(["-v"])
