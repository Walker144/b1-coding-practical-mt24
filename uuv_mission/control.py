class Controller:
    def __init__(self, proportional_gain: float, derivative_gain: float):
        self.__proportional_gain = proportional_gain
        self.__derivative_gain = derivative_gain
        self.__previous_error = 0
        self.__error = 0

    def set_proportional_gain(self, gain : float):
        self.__proportional_gain = gain

    def get_proportional_gain(self):
        return self.__proportional_gain

    def set_derivative_gain(self, gain: float):
        self.__derivative_gain = gain

    def get_derivative_gain(self):
        return self.__derivative_gain

    def calculate_error(self, reference, current_value):
        self.__previous_error = self.__error
        self.__error =  reference - current_value

    def calculate_action(self):
        return self.__proportional_gain * self.__error + self.__derivative_gain * (self.__error - self.__previous_error)
