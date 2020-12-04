class FizzBuzz:

    def run(self, input_number):
        if input_number % 15 == 0:
            return "fizzbuzz"
        if input_number % 3 == 0:
            return "fizz"
        if input_number % 5 == 0:
            return "buzz"
        return str(input_number)
