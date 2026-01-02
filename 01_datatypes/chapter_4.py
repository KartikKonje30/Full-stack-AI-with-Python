
# Float data type 

ideal_temperature = 22.5
current_temperature = 18.3

print(f"Ideal Temperature: {ideal_temperature}°C")
print(f"Current Temperature: {current_temperature}°C")

# Arithmetic Operations with Float

temp_difference = ideal_temperature - current_temperature
print(f"Temperature Difference: {temp_difference}°C")

# Working with float precision
precise_value = 0.1 + 0.2
print(f"0.1 + 0.2 = {precise_value}")  
# Note: Due to floating-point precision, this may not exactly equal 0.3

# You can see the float limit and precision using the sys module/package

import sys
print(f"Maximum float value: {sys.float_info}")

# This shows the maximum representable float value in Python
# But the float representation may vary based on your system architecture.
# Depends on your machine, ram, os, etc.

# To help with precision issues, you can use the decimal module

from decimal import Decimal
precise_decimal = Decimal('0.1') + Decimal('0.2')
print(f"Using Decimal for precision: 0.1 + 0.2 = {precise_decimal}")

# The decimal module provides support for fast correctly-rounded decimal floating point arithmetic.

# Their is also one more datatype called complex numbers in python

# Complex Numbers :-

# Complex numbers are represented as a + bj, where a is the real part and b is the imaginary part.
# You can perform arithmetic operations on complex numbers as well
# Most commonly used in scientific computations
# where fractions of numbers are involved

complex_num1 = 2 + 3j
complex_num2 = 1 + 4j
complex_sum = complex_num1 + complex_num2
print(f"Complex Number 1: {complex_num1}")
print(f"Complex Number 2: {complex_num2}")
print(f"Sum of Complex Numbers: {complex_sum}")

# You can access real and imaginary parts
print(f"Real part of complex_num1: {complex_num1.real}")
print(f"Imaginary part of complex_num1: {complex_num1.imag}")
