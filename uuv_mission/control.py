class Controller:
    def __init__(self, proportional_gain, derivative_gain):
        self.__proportional_gain = float(proportional_gain)
        self.__derivative_gain = float(derivative_gain)s
        self.__previous_error = 0
        self.__error = 0

    def calculate_error(self, reference, current_value):
        self.__previous_error = self.__error
        self.__error =  reference - current_value

    def calculate_action(self):
        return self.__proportional_gain * self.__error + self.__derivative_gain * (self.__error - self.__previous_error)
