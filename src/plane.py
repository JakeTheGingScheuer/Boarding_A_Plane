from src.random_wrapper import RandomWrapper


class Plane:
    def __init__(self, passenger_assignments, plane_size, random_wrapper=None):
        self.passengers_assignments = passenger_assignments
        self.available_seats = self._create_list_of_all_seats(plane_size)
        self.correct_placements = 0
        self.successful_board = False
        self.random_wrapper = random_wrapper or RandomWrapper()

    def board(self):
        for passenger in self.passengers_assignments:
            seat_chosen = passenger
            if self.is_first_passenger(passenger):
                seat_chosen = self.pick_random_seat()
            self.take_seat(seat_chosen, passenger)
        return self.successful_board

    def pick_random_seat(self):
        total_available_seats = len(self.available_seats)
        random_pick = self.random_wrapper.random_number(total_available_seats)
        random_seat = self.available_seats[random_pick]
        return random_seat

    def is_first_passenger(self, passenger):
        return passenger == self.passengers_assignments[0]

    def is_last_passenger(self, passenger):
        return passenger == self.passengers_assignments[len(self.passengers_assignments)-1]

    def take_seat(self, seat, passenger):
        try:
            self.available_seats.remove(seat)
            if passenger == seat:
                self.correct_placements = self.correct_placements+1
                if self.is_last_passenger(passenger):
                    self.successful_board = True

        except ValueError:
            new_seat = self.pick_random_seat()
            self.take_seat(new_seat, passenger)


    @staticmethod
    def _create_list_of_all_seats(plane_size):
        all_seats = []
        for i in range(plane_size):
            all_seats.append(i+1)
        return all_seats
