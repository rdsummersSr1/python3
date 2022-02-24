def exchange_money(budget, exchange_rate):
    """


    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    exchange_value = 0.0
    exchange_value = float(budget/exchange_rate)
    return exchange_value


def get_change(budget, exchanging_value):
    """


    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    remain_budget = 0.0
    remain_budget = float(budget - exchanging_value)
    return remain_budget
  
def get_value_of_bills(denomination, number_of_bills):
    """


    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    total_value = denomination * number_of_bills
    return total_value


def get_number_of_bills(budget, denomination):
    """


    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    num_bills = int( budget / denomination)
    return num_bills
 


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """


    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    1500, 0.84, 25, 40
    100000, 10.61, 10, 1
    8568, 1400, 0, 4017094016600, 363300
    1.20 10  10/100 x 1.2 = .12 1.2 + .12 = 1.32
    """
    print(budget, exchange_rate, spread, denomination)
    actual_exchange_rate  = exchange_rate * (1 + spread/100)
    max_v = budget / actual_exchange_rate
    max_v1 = int((max_v)/denomination)
    return max_v1*denomination
   


    
def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """


    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    0, 28, 229, 13
    """


    print(budget, exchange_rate, spread, denomination)
    actual_exchange_rate  = exchange_rate * (1 + spread/100)
    max_v = budget / actual_exchange_rate
    max_v1 = int((max_v)/denomination)
    print('1', max_v)
    max_v1 = max_v1*denomination
    print('2', int(max_v1))
    non_x = int(max_v - max_v1)
    return non_x