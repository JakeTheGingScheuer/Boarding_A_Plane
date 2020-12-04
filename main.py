from src.plane import Plane


def run():
    number_of_succesful_boards = 0
    plane_tickets = Plane.create_list_of_all_seats(100)
    for i in range(0, 1000):
        plane = Plane(plane_tickets, 100)
        plane.board()
        if plane.successful_board:
            number_of_succesful_boards += 1

    probability = (number_of_succesful_boards/1000)*100
    print("\nThe probability over the course of 1000 boardings of the last passenger getting their correct seat is {:0.2f}%.\n".format(probability))


run()
