import re
p = input()
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d{1}\1)" 
regex_integer_in_range = r"^([1-9]\d{5})$"
print(bool(re.match(regex_integer_in_range, p)))
print(len(re.findall(regex_alternating_repetitive_digit_pair, p)))
