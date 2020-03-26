import random


def spin_lottery(number_of_balls=50, number_of_picks=10):
    """
    Select random unique numbers from a given number of balls

    :param number_of_balls: optional number of balls
    :param number_of_picks: optional number of picks

    :return: sorted list of unique selected numbers
    """
    lottery_numbers = {
        idx
        for idx in range(1, (number_of_balls + 1))
    }
    selected_numbers = random.sample(lottery_numbers, number_of_picks)

    return sorted(selected_numbers)


if __name__ == "__main__":
    print('Lottery picks: {}'.format(spin_lottery()))
