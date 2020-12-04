from mock import MagicMock

from src.plane import Plane


class TestPlane:
    def test_when_a_plane_is_created_a_list_of_seats_is_generated_from_size_given(self):
        fake_passenger_assignments = [2, 1, 3, 5, 4]
        size_of_plane = 5
        subject = Plane(fake_passenger_assignments, size_of_plane)
        assert len(subject.available_seats) == 5

    def test_when_pick_random_seat_a_seat_is_chosen_from_the_available_seats(self):
        fake_passenger_assignments = [2, 1, 3, 5, 4]
        size_of_plane = 5
        subject = Plane(fake_passenger_assignments, size_of_plane)
        actual = subject.pick_random_seat()
        assert actual in subject.available_seats

    def test_when_take_seat_the_seat_is_removed_from_available_seats(self):
        fake_passenger_assignments = [2, 1, 3, 5, 4]
        size_of_plane = 5
        subject = Plane(fake_passenger_assignments, size_of_plane)
        subject.take_seat(3, 3)
        assert 3 not in subject.available_seats

    def test_when_seat_taken_is_correct_seat_correct_placements_increases(self):
        fake_passenger_assignments = [2, 1, 3, 5, 4]
        size_of_plane = 5
        subject = Plane(fake_passenger_assignments, size_of_plane)
        subject.take_seat(3, 3)
        assert subject.correct_placements == 1

    def test_when_seat_taken_is_incorrect_the_correct_placements_do_not_increase(self):
        fake_passenger_assignments = [2, 1, 3, 5, 4]
        size_of_plane = 5
        subject = Plane(fake_passenger_assignments, size_of_plane)
        subject.take_seat(3, 3)
        subject.take_seat(2, 5)
        assert subject.correct_placements == 1

    def test_when_take_seat_and_seat_is_incorrectly_taken_already_a_different_seat_is_chosen(self):
        fake_passenger_assignments = [2, 1, 3, 5, 4]
        size_of_plane = 5
        subject = Plane(fake_passenger_assignments, size_of_plane)
        subject.take_seat(3, 4)
        subject.take_seat(3, 3)
        assert subject.correct_placements == 0

    def test_is_first_passenger_returns_true_if_they_are_the_first(self):
        fake_passenger_assignments = [2, 1, 3, 5, 4]
        size_of_plane = 5
        subject = Plane(fake_passenger_assignments, size_of_plane)
        result = subject.is_first_passenger(subject.passengers_assignments[0])
        assert result is True

    def test_is_first_passenger_returns_false_if_they_are_not_the_first(self):
        fake_passenger_assignments = [2, 1, 3, 5, 4]
        size_of_plane = 5
        subject = Plane(fake_passenger_assignments, size_of_plane)
        result = subject.is_first_passenger(subject.passengers_assignments[1])
        assert result is False

    def test_board_given_first_person_picks_correct_board_was_successful(self):
        fake_passenger_assignments = [2, 1, 3, 5, 4]
        size_of_plane = 5
        mock_random = MagicMock()
        mock_random.random_number = MagicMock(return_value=1)
        subject = Plane(fake_passenger_assignments, size_of_plane, mock_random)
        subject.board()
        result = subject.successful_board
        assert result is True

