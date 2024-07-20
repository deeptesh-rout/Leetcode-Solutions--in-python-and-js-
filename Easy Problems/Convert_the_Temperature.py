# You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

# Return the array ans. Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def convertTemperature(self, celsius):
        temp = []
        temp.append(celsius + 273.15)
        temp.append(celsius * 1.80 + 32.00)

        return temp


celsius = Solution()
degree = celsius.convertTemperature(10.56)

degree_formatted = list(map(lambda x: '{:.5f}'.format(x), degree))

print(degree_formatted)
