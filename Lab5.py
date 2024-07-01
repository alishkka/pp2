import re

def match_ab_zero_or_more_b(string):
    pattern = r'ab*'
    match = re.fullmatch(pattern, string)
    return match is not None

# Test
print(match_ab_zero_or_more_b("a"))  # True
print(match_ab_zero_or_more_b("ab"))  # True
print(match_ab_zero_or_more_b("abbb"))  # True
print(match_ab_zero_or_more_b("ac"))  # False

import re

def match_ab_two_to_three_b(string):
    pattern = r'ab{2,3}'
    match = re.fullmatch(pattern, string)
    return match is not None

# Test
print(match_ab_two_to_three_b("abb"))  # True
print(match_ab_two_to_three_b("abbb"))  # True
print(match_ab_two_to_three_b("abbbb"))  # False
print(match_ab_two_to_three_b("a"))  # False

import re

def find_lowercase_sequences_with_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    matches = re.findall(pattern, string)
    return matches

# Test
print(find_lowercase_sequences_with_underscore("abc_def ghi_jkl"))  # ['abc_def', 'ghi_jkl']

import re

def find_upper_followed_by_lower(string):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, string)
    return matches

# Test
print(find_upper_followed_by_lower("Hello World"))  # ['Hello', 'World']

import re

def match_a_followed_by_anything_ending_b(string):
    pattern = r'a.*b'
    match = re.fullmatch(pattern, string)
    return match is not None

# Test
print(match_a_followed_by_anything_ending_b("aXYZb"))  # True
print(match_a_followed_by_anything_ending_b("ab"))  # True
print(match_a_followed_by_anything_ending_b("aXYZc"))  # False

import re

def replace_space_comma_dot_with_colon(string):
    pattern = r'[ ,.]'
    result = re.sub(pattern, ':', string)
    return result

# Test
print(replace_space_comma_dot_with_colon("Hello, world. How are you?"))  # Hello:world:How:are:you?

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Test
print(snake_to_camel("hello_world_example"))  # helloWorldExample

import re

def split_at_uppercase(string):
    pattern = r'(?=[A-Z])'
    result = re.split(pattern, string)
    return [s for s in result if s]

# Test
print(split_at_uppercase("HelloWorldExample"))  # ['Hello', 'World', 'Example']

import re

def insert_spaces_between_capitals(string):
    pattern = r'(?<!^)(?=[A-Z])'
    result = re.sub(pattern, ' ', string)
    return result

# Test
print(insert_spaces_between_capitals("HelloWorldExample"))  # Hello World Example

import re

def camel_to_snake(camel_str):
    pattern = r'(?<!^)(?=[A-Z])'
    result = re.sub(pattern, '_', camel_str).lower()
    return result

# Test
print(camel_to_snake("helloWorldExample"))  # hello_world_example
