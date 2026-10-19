"""Functions for calculating steps in exchanging currency. """


def exchange_money(budget, exchange_rate):
    """Calculate estimated value after exchange.

    Parameters:
        budget (float): The amount of money you are planning to exchange.
        exchange_rate (float): The unit value of the foreign currency.

    Returns:
        float: The exchanged value of the foreign currency you can receive.

    This function calculates and returns the (estimated) value of the exchanged currency.

    """
    exchanging_value = budget / exchange_rate
    return float(exchanging_value)
def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange.

    Parameters:
        budget (float): The amount of money you own.
        exchanging_value (float): The amount of your money you want to exchange now.

    Returns:
        float: The amount left of your starting currency after the exchange

    Examples:
        >>> get_change(127.5, 120.0)
        7.5

        >>> get_change(300.75, 150.25)
        150.50

    This function calculates and returns the amount of money left over from the budget
    after an exchange.

    """

    currency_left = float(budget - exchanging_value)
    return float(currency_left)


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of currency at current denomination.

    Parameters:
        denomination (int): The value of a single unit (bill).
        number_of_bills (int): The total number of units (bills).

    Returns:
        int: Calculated value of the units (bills).

    This function calculates and returns the total value of the bills (excluding fractional amounts).

    """

    total_value = denomination * number_of_bills
    return total_value


def get_number_of_bills(amount, denomination):
    """Calculate the number of currency units (bills) within the amount.

    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single unit (bill).

    Returns:
        int: The number of units (bills) that can be obtained from the amount.

    This function calculates and returns the number pf currency units (bills) that can
    be obtained from the given amount. Whole bills only - no fractional amounts.

    """
    value_of_bills = amount / denomination
    return int(value_of_bills)
    


def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills.

    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single unit (bill).

    Returns:
        float: The amount that is "leftover", given the current denomination.

    This function calculates and returns the leftover amount that cannot be
    returned from starting amount, due to the currency denomination.

    """

    leftover_amount = amount % denomination
    return float(leftover_amount)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency.

    Parameters:
        budget (float): The amount of your money you are planning to exchange.
        exchange_rate (float): The unit value of the foreign currency.
        spread (int): The percentage that is taken as an exchange fee.
        denomination (int) The value of a single unit (bill).

    Returns:
        int: The maximum value you can get in the new currency.


    Note:
        The currency denomination is a whole number and cannot be sub-divided.

    This function calculates and returns the maximum value of the new currency after
    determining the exchange rate plus the spread.
    """

    number_of_bills = (budget / (exchange_rate + exchange_rate * (spread/100))) // denomination
    return int(number_of_bills * denomination)

# ==========================================
# CÁC HÀM TRONG BÀI TẬP CURRENCY EXCHANGE
# ==========================================

def exchange_money(budget, exchange_rate):
    """Estimate value after exchange."""
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange."""
    return float(budget - exchanging_value)


def get_value_of_bills(denomination, number_of_bills):
    """Calculate value of bills."""
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate number of bills."""
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills."""
    return float(amount % denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency."""
    actual_exchange_rate = exchange_rate * (1 + spread / 100)
    number_of_bills = (budget / actual_exchange_rate) // denomination
    return int(number_of_bills * denomination)


# Kiểm Thử


    
    # 1. Test exchange_money
res_1 = exchange_money(100000, 0.8)
print(f"exchange_money(-> Kết quả: {res_1}")


    # 2. Test get_change
res_2 = get_change(463000, 5000)
print(f"get_change -> Kết quả: {res_2}")


    # 3. Test get_value_of_bills
res_3 = get_value_of_bills(10000, 128)
print(f"get_value_of_bills -> Kết quả: {res_3}")


    # 4. Test get_number_of_bills
res_4 = get_number_of_bills(163270, 50000)
print(f"get_number_of_bills-> Kết quả: {res_4}")

    # 5. Test get_leftover_of_bills
res_5 = get_leftover_of_bills(10.1, 10)
print(f"get_leftover_of_bills-> Kết quả: {res_5}" )


    # 6. Test exchangeable_value
res_6 = exchangeable_value(100000, 10.61, 10, 1)
print(f"exchangeable_value-> Kết quả: {res_6}")