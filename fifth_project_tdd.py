"""
@author: periwinkleFTW
@date: Jun 2, 2021
This class is going to calculate how many years will it take to generate passive for a given income from renting apts.
"""
import math


class Calculator:
    def __init__(self, passive_income_desired_yearly, yearly_savings, starting_year,
                 price_of_one_apt, price_of_renting_one_apt):
        if isinstance(starting_year, int):
            self._passive_income_desired_yearly = passive_income_desired_yearly
            self._yearly_savings = yearly_savings
            self._starting_year = starting_year
            self._years_needed = starting_year
            self._price_of_one_apt = price_of_one_apt
            self._price_of_renting_one_apt = price_of_renting_one_apt
            self._answer = dict()
            self._calculate()
        else:
            raise TypeError('Please input int for year')

    def _calculate(self):
        apt_number_owned = 0
        income_reached = 0
        while self._passive_income_desired_yearly >= (apt_number_owned *
                                                      self._price_of_renting_one_apt):
            frac, whole = math.modf((self._yearly_savings + income_reached) /
                                    self._price_of_one_apt)

            if whole >= 2:
                apt_number_owned += whole
                income_reached = (self._yearly_savings + income_reached) - (whole *
                                                                            self._price_of_one_apt)
                income_reached += (apt_number_owned * self._price_of_renting_one_apt)

            elif whole >= 1:
                apt_number_owned += whole
                income_reached = frac * self._price_of_one_apt
                income_reached += (apt_number_owned * self._price_of_renting_one_apt)

            else:
                income_reached += self._yearly_savings

            self._answer[self._starting_year] = [apt_number_owned, round(income_reached)]
            self._starting_year += 1

    def get_results(self):
        return self._answer

    def get_years_needed(self):
        return (self._starting_year - 1) - self._years_needed

    def get_apartments_needed(self):
        key = max(self._answer, key=int)
        value = self._answer[key]
        number_of_apartments = value[0]
        return number_of_apartments

    def get_net_worth(self):
        return self.get_apartments_needed() * self._price_of_one_apt

    def print_results(self):
        for k, v in self._answer.items():
            print(f'Year number: {k}, Apt number owned: {int(v[0])}, Passive income: ${round(v[1])}')
        print(f'You can reach your passive income of ${self._passive_income_desired_yearly}, '
              f'but it will take {self.get_years_needed()} years,\n'
              f'Your net worth is: ${self.get_net_worth()}')


calculator_obj_one = Calculator(150000, 70000, 2019, 80000, 6666)
calculator_obj_one.print_results()