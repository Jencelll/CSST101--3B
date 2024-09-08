# ai_agent.py

from logic_functions import and_operation, or_operation, not_operation, implies_operation
from predicate_logic import forall, exists

class SmartThermostat:
    def __init__(self, set_temp):
        """
        Initialize the thermostat with a desired temperature threshold.
        :param set_temp: The desired temperature threshold (float)
        """
        self.set_temp = set_temp

    def decide_action(self, current_temp):
        """
        Decide the action based on the current temperature.
        :param current_temp: The current temperature in the house (float)
        :return: Action to be taken ("Turn on heater" or "Do nothing")
        """
        if self.should_turn_on_heater(current_temp):
            return "Turn on heater"
        else:
            return "Do nothing"

    def should_turn_on_heater(self, current_temp):
        """
        Decide whether to turn on the heater based on the current temperature and the set temperature.
        :param current_temp: The current temperature in the house (float)
        :return: True if the heater should be turned on, otherwise False
        """
        return current_temp < self.set_temp

# Example usage
if __name__ == "__main__":
    thermostat = SmartThermostat(set_temp=21.0)  # Desired temperature is 21°C

    current_temp = 18.0  # Current temperature is 18°C
    print("Action:", thermostat.decide_action(current_temp))  # Output: "Turn on heater"

    current_temp = 22.0  # Current temperature is 22°C
    print("Action:", thermostat.decide_action(current_temp))  # Output: "Do nothing"
