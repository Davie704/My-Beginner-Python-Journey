# Homework practice - String variables:

windows_serial_number = "abc-def-ghi-jkl"

new_var_1 = "abc"
new_var_2 = "def"
new_var_3 = "ghi"
new_var_4 = "jkl"

encoded_windows_serial_number = windows_serial_number.replace('abc', 'AAA').replace('def', 'DDD').replace('ghi', 'GGG').replace('jkl', 'JJJ')

print("This is the NEW encoded serial number : " + encoded_windows_serial_number)

