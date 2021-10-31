class Day5():

    def check_number(number: int):
        number_string = str(number)
        number_1 = int(number_string[0])
        number_2 = int(number_string[1])

        if number_1 == number_2 or number_1 + number_2 == 10:
            return True
        else:
            return False

    def check_number_2(number: int):
        number_string = str(number)
        sum_even = 0
        sum_odd = 0
        list_even = []
        list_odd = []

        for i in range(len(number_string)):
            member = int(number_string[i])
            if i % 2 == 0:
                sum_even += member
                list_even.append(member)
            else:
                sum_odd += member
                list_odd.append(member)

        list_odd.sort()
        list_even.sort()

        if sum_odd == sum_even or list_even == list_odd:
            return True
        else:
            return False