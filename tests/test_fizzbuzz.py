import pytest

from src.FizzBuzz import FizzBuzz


class TestFizzBuzz:

    @pytest.fixture
    def subject(self):
        return FizzBuzz()

    def test_when_given_1_returns_1_as_string(self, subject):
        actual = subject.run(1)
        assert actual == "1"

    def test_when_given_3_returns_fizz(self, subject):
        actual = subject.run(3)
        assert actual == "fizz"

    def test_when_given_5_returns_buzz(self, subject):
        actual = subject.run(5)
        assert actual == "buzz"

    def test_when_given_6_returns_fizz(self, subject):
        actual = subject.run(6)
        assert actual == "fizz"

    def test_when_given_9_returns_fizz(self, subject):
        actual = subject.run(9)
        assert actual == "fizz"

    def test_when_given_10_returns_buzz(self, subject):
        actual = subject.run(10)
        assert actual == "buzz"

    def test_when_given_15_returns_fizzbuzz(self, subject):
        actual = subject.run(15)
        assert actual == "fizzbuzz"
