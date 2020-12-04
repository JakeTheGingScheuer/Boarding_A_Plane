import pytest

from src.FizzBuzz import FizzBuzz


class TestFizzBuzz:

    @pytest.fixture
    def subject(self):
        return FizzBuzz()

    def test_when_given_1_returns_1_as_string(self, subject):
        actual = subject.run(1)
        assert actual == "1"
