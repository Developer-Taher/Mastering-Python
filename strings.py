# =====================================
# Complete Guide to Python Strings
# Comprehensive Tutorial and Reference
# =====================================

"""
What are Strings?
Strings are sequences of characters (letters, numbers, symbols) used to represent text.
They are one of the most important data types in Python and are used everywhere in programming.
Think of them as digital text that computers can read, manipulate, and display.

Examples: "Hello", 'Python', "123", "user@email.com", "Welcome to programming!"
"""

import string
import re
import sys
from datetime import datetime

print("=" * 70)
print("🐍 Complete Guide to Python Strings")
print("=" * 70)

print("\n" + "=" * 50)
print("1️⃣ Introduction to Strings")
print("=" * 50)

print("""
📝 What are Strings?
✅ Sequences of characters (text)
✅ Enclosed in quotes: 'single' or "double"
✅ Can contain letters, numbers, symbols, spaces
✅ Immutable (cannot be changed after creation)
✅ One of the most used data types in programming

🎯 Common Uses:
• Store names, messages, emails
• Display information to users
• Process text data
• Build user interfaces
• Handle file paths and URLs
""")

print("\n" + "=" * 50)
print("2️⃣ Creating Strings - Different Quote Types")
print("=" * 50)

print("\n📋 Ways to Create Strings")
print("-" * 25)

# Single quotes
single_quote_string = 'Hello, World!'
print(f"Single quotes: {single_quote_string}")

# Double quotes
double_quote_string = "Python is awesome!"
print(f"Double quotes: {double_quote_string}")

# Triple single quotes (multiline)
triple_single = '''This is a
multiline string
using triple single quotes'''
print(f"Triple single quotes:\n{triple_single}")

# Triple double quotes (multiline)
triple_double = """This is also a
multiline string
using triple double quotes"""
print(f"Triple double quotes:\n{triple_double}")

# When to use which quotes
print(f"\n💡 When to use different quote types:")
print("✅ Single quotes: General purpose, most common")
print("✅ Double quotes: When string contains single quotes")
print("✅ Triple quotes: Multiline strings or docstrings")

# Examples of quote usage
apostrophe_example = "I can't believe it's working!"  # Double quotes for apostrophe
quote_example = 'He said "Hello there!"'  # Single quotes for double quotes inside
mixed_example = '''He said "I can't do it" loudly.'''  # Triple for both

print(f"\nExamples:")
print(f"Apostrophe: {apostrophe_example}")
print(f"Quote inside: {quote_example}")
print(f"Mixed quotes: {mixed_example}")

print("\n" + "=" * 50)
print("3️⃣ String Characters and Unicode")
print("=" * 50)

print("\n🌍 Character Types and Unicode")
print("-" * 30)

# Basic characters
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
spaces = "   "  # Different types of spaces

print(f"Letters: {letters}")
print(f"Numbers: {numbers}")
print(f"Symbols: {symbols}")
print(f"Spaces: '{spaces}'")

# Unicode characters
unicode_examples = "Hello 🌍 Python 🐍 Programming 💻"
arabic_text = "مرحباً بالعالم"
chinese_text = "你好世界"
emoji_string = "😀😂😍🚀🌟⭐🎉🎯"

print(f"\nUnicode Examples:")
print(f"Mixed with emojis: {unicode_examples}")
print(f"Arabic text: {arabic_text}")
print(f"Chinese text: {chinese_text}")
print(f"Emojis: {emoji_string}")

# Special characters with escape sequences
escape_examples = {
    "\\n": "New line",
    "\\t": "Tab",
    "\\r": "Carriage return",
    "\\\\": "Backslash",
    "\\'": "Single quote",
    '\\"': "Double quote"
}

print(f"\nEscape Sequences:")
for escape, description in escape_examples.items():
    print(f"  {escape} → {description}")

# Demonstration of escape sequences
print(f"\nEscape Sequence Examples:")
print("Line 1\nLine 2\nLine 3")  # New lines
print("Column1\tColumn2\tColumn3")  # Tabs
print("Path: C:\\Users\\Python\\file.txt")  # Backslashes
print('She said: "I\'m learning Python"')  # Mixed quotes

print("\n" + "=" * 50)
print("4️⃣ String Indexing and Slicing")
print("=" * 50)

print("\n📍 Accessing Individual Characters")
print("-" * 33)

# Sample string for indexing
sample_string = "Python Programming"
print(f"Sample string: '{sample_string}'")
print(f"Length: {len(sample_string)} characters")

# Positive indexing
print(f"\n🔢 Positive Indexing (left to right):")
for i in range(len(sample_string)):
    print(f"  Index {i:2d}: '{sample_string[i]}'")

# Negative indexing
print(f"\n🔄 Negative Indexing (right to left):")
for i in range(1, len(sample_string) + 1):
    print(f"  Index -{i:2d}: '{sample_string[-i]}'")

# Basic slicing examples
print(f"\n✂️ String Slicing Examples:")
text = "Hello Python World"
print(f"Original: '{text}'")
print(f"text[0:5]:     '{text[0:5]}'     # First 5 characters")
print(f"text[6:12]:    '{text[6:12]}'    # Characters 6-11")
print(f"text[:5]:      '{text[:5]}'      # From start to index 5")
print(f"text[6:]:      '{text[6:]}'      # From index 6 to end")
print(f"text[:]:       '{text[:]}'       # Entire string")
print(f"text[-5:]:     '{text[-5:]}'     # Last 5 characters")
print(f"text[:-5]:     '{text[:-5]}'     # All except last 5")

# Advanced slicing with step
print(f"\n⚡ Advanced Slicing with Step:")
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"Original: '{alphabet}'")
print(f"alphabet[::2]:   '{alphabet[::2]}'   # Every 2nd character")
print(f"alphabet[::3]:   '{alphabet[::3]}'   # Every 3rd character")
print(f"alphabet[::-1]:  '{alphabet[::-1]}'  # Reverse string")
print(f"alphabet[2:8:2]: '{alphabet[2:8:2]}' # From 2 to 8, step 2")

print("\n" + "=" * 50)
print("5️⃣ String Methods - Basic Operations")
print("=" * 50)

print("\n🔧 Essential String Methods")
print("-" * 26)

# Sample text for methods
demo_text = "  Hello Python Programming World  "
print(f"Demo text: '{demo_text}'")

# Case methods
print(f"\n📝 Case Conversion Methods:")
print(f"upper():      '{demo_text.upper()}'")
print(f"lower():      '{demo_text.lower()}'")
print(f"title():      '{demo_text.title()}'")
print(f"capitalize(): '{demo_text.capitalize()}'")
print(f"swapcase():   '{demo_text.swapcase()}'")

# Whitespace methods
print(f"\n🧹 Whitespace Methods:")
print(f"strip():      '{demo_text.strip()}'")
print(f"lstrip():     '{demo_text.lstrip()}'")
print(f"rstrip():     '{demo_text.rstrip()}'")

# Search methods
print(f"\n🔍 Search Methods:")
search_text = "Python is great, Python is powerful"
print(f"Text: '{search_text}'")
print(f"find('Python'):       {search_text.find('Python')}")
print(f"rfind('Python'):      {search_text.rfind('Python')}")
print(f"index('is'):          {search_text.index('is')}")
print(f"count('Python'):      {search_text.count('Python')}")
print(f"startswith('Python'): {search_text.startswith('Python')}")
print(f"endswith('powerful'):  {search_text.endswith('powerful')}")

# Boolean check methods
print(f"\n✅ Boolean Check Methods:")
test_strings = ["Hello123", "12345", "hello", "HELLO", "Hello World", "   "]
methods = [
    ("isalnum()", lambda s: s.isalnum()),
    ("isalpha()", lambda s: s.isalpha()),
    ("isdigit()", lambda s: s.isdigit()),
    ("islower()", lambda s: s.islower()),
    ("isupper()", lambda s: s.isupper()),
    ("isspace()", lambda s: s.isspace())
]

for test_str in test_strings:
    print(f"\n  Testing: '{test_str}'")
    for method_name, method_func in methods:
        result = method_func(test_str)
        print(f"    {method_name:12} → {result}")

print("\n" + "=" * 50)
print("6️⃣ String Methods - Advanced Operations")
print("=" * 50)

print("\n🚀 Advanced String Manipulation")
print("-" * 31)

# Replace methods
print("🔄 Replace and Modify Methods:")
original = "I love Java. Java is great. Java programming is fun."
print(f"Original: '{original}'")
print(f"replace('Java', 'Python'): '{original.replace('Java', 'Python')}'")
print(f"replace('Java', 'Python', 2): '{original.replace('Java', 'Python', 2)}'")

# Split and join methods
print(f"\n✂️ Split Methods:")
sentence = "apple,banana,orange,grape,mango"
words = "Hello world Python programming"
print(f"Sentence: '{sentence}'")
print(f"split(','): {sentence.split(',')}")
print(f"Words: '{words}'")
print(f"split(): {words.split()}")

# Join method
print(f"\n🔗 Join Method:")
word_list = ["Python", "is", "awesome", "and", "powerful"]
separators = ["", " ", "-", " | ", " → "]
print(f"Word list: {word_list}")
for sep in separators:
    joined = sep.join(word_list)
    print(f"join('{sep}'): '{joined}'")

# Alignment methods
print(f"\n📐 Alignment Methods:")
text = "Python"
width = 20
print(f"Original: '{text}'")
print(f"center({width}):     '{text.center(width)}'")
print(f"ljust({width}):      '{text.ljust(width)}'")
print(f"rjust({width}):      '{text.rjust(width)}'")
print(f"center({width}, '*'): '{text.center(width, '*')}'")
print(f"ljust({width}, '-'):  '{text.ljust(width, '-')}'")
print(f"rjust({width}, '+'):  '{text.rjust(width, '+')}'")

# Zero padding
print(f"\n🔢 Zero Padding:")
numbers = ["42", "123", "7", "9999"]
for num in numbers:
    print(f"'{num}'.zfill(6): '{num.zfill(6)}'")

print("\n" + "=" * 50)
print("7️⃣ String Formatting - Old vs New")
print("=" * 50)

print("\n🎨 String Formatting Methods")
print("-" * 27)

# Variables for formatting examples
name = "Alice"
age = 25
salary = 75000.50
pi = 3.14159265359

print("📊 Formatting Examples with Data:")
print(f"Name: {name}, Age: {age}, Salary: ${salary}, Pi: {pi}")

# Old style % formatting
print(f"\n📜 Old Style (% formatting):")
old_style_examples = [
    ("Basic: %s is %d years old", (name, age)),
    ("Float: Pi is approximately %.2f", (pi,)),
    ("Money: Salary is $%.2f", (salary,)),
    ("Padded: %10s|%5d|%8.2f", (name, age, salary))
]

for format_str, values in old_style_examples:
    result = format_str % values
    print(f"  '{format_str}' → '{result}'")

# .format() method
print(f"\n🔧 .format() Method:")
format_examples = [
    ("Basic: {} is {} years old", [name, age]),
    ("Positional: {0} earns ${1:.2f}", [name, salary]),
    ("Named: {person} is {years} years old", {"person": name, "years": age}),
    ("Aligned: {:<10}|{:>5}|{:^10.2f}", [name, age, salary])
]

for format_str, values in format_examples:
    if isinstance(values, dict):
        result = format_str.format(**values)
    else:
        result = format_str.format(*values)
    print(f"  '{format_str}' → '{result}'")

# f-strings (modern way)
print(f"\n🚀 f-strings (Modern Python 3.6+):")
print(f"  Basic: f'{name} is {age} years old' → '{name} is {age} years old'")
print(f"  Math: f'2 + 2 = {{2 + 2}}' → '2 + 2 = {2 + 2}'")
print(f"  Formatting: f'Pi: {{pi:.3f}}' → 'Pi: {pi:.3f}'")
print(f"  Alignment: f'{{name:<10}}|{{age:>5}}|{{salary:^12.2f}}' → '{name:<10}|{age:>5}|{salary:^12.2f}'")

# Advanced f-string examples
print(f"\n⚡ Advanced f-string Features:")
data = {"users": 1500, "active": 1200}
print(f"  Expressions: f'Active: {{data[\"active\"]/data[\"users\"]*100:.1f}}%' → 'Active: {data['active']/data['users']*100:.1f}%'")

current_time = datetime.now()
print(f"  Date formatting: f'Today: {{current_time:%Y-%m-%d %H:%M}}' → 'Today: {current_time:%Y-%m-%d %H:%M}'")

print("\n" + "=" * 50)
print("8️⃣ String Concatenation Methods")
print("=" * 50)

print("\n🔗 Ways to Combine Strings")
print("-" * 26)

# Basic concatenation
first_name = "John"
last_name = "Doe"
age = 30

print("🔤 Basic Concatenation Methods:")

# Plus operator
plus_result = first_name + " " + last_name
print(f"Plus operator: '{first_name}' + ' ' + '{last_name}' → '{plus_result}'")

# Join method
join_result = " ".join([first_name, last_name])
print(f"Join method: ' '.join(['{first_name}', '{last_name}']) → '{join_result}'")

# Format methods
format_result = "{} {}".format(first_name, last_name)
print(f"Format method: '{{}} {{}}'.format('{first_name}', '{last_name}') → '{format_result}'")

# f-string
f_string_result = f"{first_name} {last_name}"
print(f"f-string: f'{{first_name}} {{last_name}}' → '{f_string_result}'")

# Performance comparison
import timeit

def test_plus_concatenation():
    result = first_name + " " + last_name + " is " + str(age) + " years old"
    return result

def test_join_concatenation():
    result = " ".join([first_name, last_name, "is", str(age), "years", "old"])
    return result

def test_format_concatenation():
    result = "{} {} is {} years old".format(first_name, last_name, age)
    return result

def test_f_string_concatenation():
    result = f"{first_name} {last_name} is {age} years old"
    return result

print(f"\n⚡ Performance Comparison (1000 iterations):")
methods = [
    ("Plus operator", test_plus_concatenation),
    ("Join method", test_join_concatenation),
    ("Format method", test_format_concatenation),
    ("f-string", test_f_string_concatenation)
]

times = []
for method_name, method_func in methods:
    time_taken = timeit.timeit(method_func, number=1000)
    times.append((method_name, time_taken))
    print(f"  {method_name:15}: {time_taken:.6f} seconds")

# Find fastest method
fastest = min(times, key=lambda x: x[1])
print(f"\n🏆 Fastest method: {fastest[0]}")

print("\n" + "=" * 50)
print("9️⃣ String Validation and Cleaning")
print("=" * 50)

print("\n🧹 String Validation and Cleaning Techniques")
print("-" * 42)

# Email validation example
def validate_email(email):
    """Simple email validation"""
    if "@" not in email:
        return False, "Missing @ symbol"
    if email.count("@") != 1:
        return False, "Multiple @ symbols"
    if email.startswith("@") or email.endswith("@"):
        return False, "@ cannot be at start or end"
    if ".." in email:
        return False, "Consecutive dots not allowed"
    return True, "Valid email format"

print("📧 Email Validation Examples:")
test_emails = [
    "user@example.com",
    "invalid.email",
    "user@@example.com",
    "@invalid.com",
    "user@.com",
    "valid.user@example.co.uk"
]

for email in test_emails:
    is_valid, message = validate_email(email)
    status = "✅" if is_valid else "❌"
    print(f"  {status} '{email}' → {message}")

# Phone number cleaning
def clean_phone_number(phone):
    """Clean and format phone number"""
    # Remove all non-digit characters
    digits_only = ''.join(char for char in phone if char.isdigit())
    
    if len(digits_only) == 10:
        # Format as (XXX) XXX-XXXX
        return f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    elif len(digits_only) == 11 and digits_only.startswith('1'):
        # Remove leading 1 and format
        return f"({digits_only[1:4]}) {digits_only[4:7]}-{digits_only[7:]}"
    else:
        return "Invalid phone number"

print(f"\n📱 Phone Number Cleaning:")
test_phones = [
    "123-456-7890",
    "(123) 456-7890",
    "1-123-456-7890",
    "123.456.7890",
    "1234567890",
    "123-45-6789"  # Invalid
]

for phone in test_phones:
    cleaned = clean_phone_number(phone)
    print(f"  '{phone}' → '{cleaned}'")

# Text cleaning function
def clean_text(text):
    """Comprehensive text cleaning"""
    # Remove extra whitespace
    cleaned = ' '.join(text.split())
    
    # Remove special characters (keep only letters, numbers, spaces)
    cleaned = ''.join(char for char in cleaned if char.isalnum() or char.isspace())
    
    # Convert to title case
    cleaned = cleaned.title()
    
    return cleaned

print(f"\n🧼 Text Cleaning Examples:")
messy_texts = [
    "  hello    world!!!  ",
    "Python@#$Programming*&^",
    "tHiS    iS   mEsSeD    uP tExT!@#",
    "   remove...extra   spaces   "
]

for messy_text in messy_texts:
    cleaned = clean_text(messy_text)
    print(f"  '{messy_text}' → '{cleaned}'")

print("\n" + "=" * 50)
print("🔟 Advanced String Operations")
print("=" * 50)

print("\n🎯 Advanced String Techniques")
print("-" * 27)

# String encoding and decoding
print("🔐 String Encoding/Decoding:")
original_text = "Hello, 世界! 🌍"
print(f"Original: '{original_text}'")

# Different encodings
encodings = ['utf-8', 'ascii', 'latin-1']
for encoding in encodings:
    try:
        encoded = original_text.encode(encoding)
        decoded = encoded.decode(encoding)
        print(f"  {encoding:8}: {encoded} → '{decoded}'")
    except UnicodeEncodeError as e:
        print(f"  {encoding:8}: Error - {e}")

# String translations
print(f"\n🔄 String Translation:")
# Create translation table
translation_table = str.maketrans("aeiou", "12345")
test_text = "Hello World"
translated = test_text.translate(translation_table)
print(f"Original: '{test_text}'")
print(f"Translated (a→1, e→2, i→3, o→4, u→5): '{translated}'")

# Remove characters
remove_table = str.maketrans("", "", "aeiou")
removed = test_text.translate(remove_table)
print(f"Vowels removed: '{removed}'")

# Regular expressions with strings
print(f"\n🔍 Regular Expressions:")
import re

text_with_numbers = "Call me at 123-456-7890 or email user@example.com"
print(f"Text: '{text_with_numbers}'")

# Find phone numbers
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, text_with_numbers)
print(f"Phone numbers found: {phones}")

# Find email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text_with_numbers)
print(f"Email addresses found: {emails}")

# String compression
print(f"\n📦 String Compression Example:")
def simple_compression(text):
    """Simple run-length encoding"""
    if not text:
        return ""
    
    compressed = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}" if count > 1 else current_char)
            current_char = char
            count = 1
    
    compressed.append(f"{current_char}{count}" if count > 1 else current_char)
    return ''.join(compressed)

compression_examples = [
    "aabbbcccc",
    "abcdef",
    "aaabbbaaa",
    "aabbccddee"
]

for example in compression_examples:
    compressed = simple_compression(example)
    print(f"  '{example}' → '{compressed}'")

print("\n" + "=" * 50)
print("1️⃣1️⃣ String Performance and Memory")
print("=" * 50)

print("\n⚡ String Performance Analysis")
print("-" * 28)

# Memory usage comparison
print("💾 Memory Usage Analysis:")
short_string = "Hello"
long_string = "Hello" * 1000
very_long_string = "A" * 10000

strings_to_analyze = [
    ("Short string", short_string),
    ("Long string", long_string),
    ("Very long string", very_long_string)
]

for name, string_obj in strings_to_analyze:
    memory_size = sys.getsizeof(string_obj)
    char_count = len(string_obj)
    print(f"  {name:17}: {char_count:6d} chars, {memory_size:6d} bytes")

# String concatenation performance
print(f"\n🔄 Concatenation Performance:")

def test_string_concatenation_plus(n=1000):
    """Test + operator concatenation"""
    result = ""
    for i in range(n):
        result += "a"
    return result

def test_string_concatenation_join(n=1000):
    """Test join method concatenation"""
    chars = ["a" for _ in range(n)]
    return "".join(chars)

def test_string_concatenation_list(n=1000):
    """Test list append and join"""
    chars = []
    for i in range(n):
        chars.append("a")
    return "".join(chars)

n = 1000
methods = [
    ("Plus operator", lambda: test_string_concatenation_plus(n)),
    ("Join method", lambda: test_string_concatenation_join(n)),
    ("List + join", lambda: test_string_concatenation_list(n))
]

for method_name, method_func in methods:
    time_taken = timeit.timeit(method_func, number=100)
    print(f"  {method_name:15}: {time_taken:.6f} seconds")

# String interning
print(f"\n🔗 String Interning:")
a = "hello"
b = "hello"
c = "hel" + "lo"
d = "".join(["h", "e", "l", "l", "o"])

print(f"a = 'hello'")
print(f"b = 'hello'")
print(f"c = 'hel' + 'lo'")
print(f"d = ''.join(['h', 'e', 'l', 'l', 'o'])")
print(f"")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"a is d: {a is d}")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")
print(f"id(d): {id(d)}")

print("\n" + "=" * 50)
print("1️⃣2️⃣ Practical String Applications")
print("=" * 50)

print("\n🛠️ Real-World String Applications")
print("-" * 32)

# Password strength checker
def check_password_strength(password):
    """Check password strength"""
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Include lowercase letters")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include uppercase letters")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include numbers")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    else:
        feedback.append("Include special characters")
    
    strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
    strength = strength_levels[min(score, 4)]
    
    return strength, score, feedback

print("🔐 Password Strength Checker:")
test_passwords = [
    "123",
    "password",
    "Password123",
    "MyStr0ng!Pass",
    "A1b2C3!@#"
]

for pwd in test_passwords:
    strength, score, feedback = check_password_strength(pwd)
    print(f"  '{pwd}' → {strength} ({score}/5)")
    if feedback:
        print(f"    Suggestions: {', '.join(feedback)}")

# URL parser
def parse_url(url):
    """Simple URL parser"""
    result = {
        "protocol": "",
        "domain": "",
        "path": "",
        "query": "",
        "fragment": ""
    }
    
    # Remove protocol
    if "://" in url:
        protocol, remainder = url.split("://", 1)
        result["protocol"] = protocol
    else:
        remainder = url
    
    # Split by #
    if "#" in remainder:
        remainder, fragment = remainder.split("#", 1)
        result["fragment"] = fragment
    
    # Split by ?
    if "?" in remainder:
        remainder, query = remainder.split("?", 1)
        result["query"] = query
    
    # Split domain and path
    if "/" in remainder:
        domain, path = remainder.split("/", 1)
        result["domain"] = domain
        result["path"] = "/" + path
    else:
        result["domain"] = remainder
        result["path"] = "/"
    
    return result

print(f"\n🌐 URL Parser:")
test_urls = [
    "https://www.example.com",
    "https://www.example.com/path/to/page",
    "https://www.example.com/search?q=python&sort=date",
    "https://www.example.com/page#section1"
]

for url in test_urls:
    parsed = parse_url(url)
    print(f"  URL: {url}")
    for key, value in parsed.items():
        if value:
            print(f"    {key}: {value}")

# CSV parser (simple)
def parse_csv_line(line):
    """Simple CSV line parser"""
    fields = []
    current_field = ""
    in_quotes = False
    
    for char in line:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            fields.append(current_field.strip())
            current_field = ""
        else:
            current_field += char
    
    fields.append(current_field.strip())
    return fields

print(f"\n📊 CSV Parser:")
csv_lines = [
    'John,25,Engineer',
    'Alice,"Software Developer",30',
    '"Smith, John",35,"Manager, IT"',
    'Bob,"Data Scientist, Senior",28'
]

for line in csv_lines:
    parsed = parse_csv_line(line)
    print(f"  '{line}' → {parsed}")

# Log file analyzer
def analyze_log_entry(log_line):
    """Analyze a log file entry"""
    # Expected format: [TIMESTAMP] LEVEL: MESSAGE
    if not log_line.strip():
        return None
    
    try:
        # Extract timestamp
        if log_line.startswith('['):
            end_bracket = log_line.find(']')
            timestamp = log_line[1:end_bracket]
            remainder = log_line[end_bracket + 1:].strip()
        else:
            timestamp = "Unknown"
            remainder = log_line
        
        # Extract level
        if ':' in remainder:
            level, message = remainder.split(':', 1)
            level = level.strip()
            message = message.strip()
        else:
            level = "INFO"
            message = remainder
        
        return {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }
    except:
        return {"error": "Could not parse log entry"}

print(f"\n📋 Log File Analyzer:")
log_entries = [
    "[2024-01-15 10:30:15] INFO: Application started successfully",
    "[2024-01-15 10:30:20] WARNING: Low memory detected",
    "[2024-01-15 10:30:25] ERROR: Database connection failed",
    "[2024-01-15 10:30:30] DEBUG: Processing user request",
    "Invalid log entry without proper format"
]

for entry in log_entries:
    parsed = analyze_log_entry(entry)
    print(f"  Entry: '{entry[:50]}{'...' if len(entry) > 50 else ''}'")
    if parsed:
        if "error" not in parsed:
            print(f"    Time: {parsed['timestamp']}")
            print(f"    Level: {parsed['level']}")
            print(f"    Message: {parsed['message']}")
        else:
            print(f"    {parsed['error']}")

print("\n" + "=" * 50)
print("1️⃣3️⃣ String Algorithms and Patterns")
print("=" * 50)

print("\n🧮 String Algorithms")
print("-" * 19)

# Palindrome checker
def is_palindrome(text):
    """Check if text is a palindrome"""
    # Clean text: remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

print("🔄 Palindrome Checker:")
palindrome_tests = [
    "racecar",
    "A man a plan a canal Panama",
    "race a car",
    "hello",
    "Madam",
    "Was it a car or a cat I saw"
]

for test in palindrome_tests:
    result = is_palindrome(test)
    status = "✅" if result else "❌"
    print(f"  {status} '{test}' → {result}")

# Anagram checker
def are_anagrams(str1, str2):
    """Check if two strings are anagrams"""
    # Clean and sort characters
    clean1 = ''.join(char.lower() for char in str1 if char.isalnum())
    clean2 = ''.join(char.lower() for char in str2 if char.isalnum())
    return sorted(clean1) == sorted(clean2)

print(f"\n🔀 Anagram Checker:")
anagram_pairs = [
    ("listen", "silent"),
    ("evil", "vile"),
    ("a gentleman", "elegant man"),
    ("conversation", "voices rant on"),
    ("hello", "world")
]

for str1, str2 in anagram_pairs:
    result = are_anagrams(str1, str2)
    status = "✅" if result else "❌"
    print(f"  {status} '{str1}' & '{str2}' → {result}")

# String similarity (Levenshtein distance)
def levenshtein_distance(str1, str2):
    """Calculate Levenshtein distance between two strings"""
    if len(str1) < len(str2):
        return levenshtein_distance(str2, str1)
    
    if len(str2) == 0:
        return len(str1)
    
    previous_row = list(range(len(str2) + 1))
    for i, c1 in enumerate(str1):
        current_row = [i + 1]
        for j, c2 in enumerate(str2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

print(f"\n📏 String Similarity (Edit Distance):")
similarity_tests = [
    ("kitten", "sitting"),
    ("saturday", "sunday"),
    ("hello", "hallo"),
    ("python", "java"),
    ("programming", "programing")
]

for str1, str2 in similarity_tests:
    distance = levenshtein_distance(str1, str2)
    max_len = max(len(str1), len(str2))
    similarity = (1 - distance / max_len) * 100 if max_len > 0 else 100
    print(f"  '{str1}' & '{str2}' → Distance: {distance}, Similarity: {similarity:.1f}%")

# Pattern matching
def find_pattern_occurrences(text, pattern):
    """Find all occurrences of pattern in text"""
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences

print(f"\n🔍 Pattern Matching:")
search_text = "The quick brown fox jumps over the lazy dog. The fox is quick."
patterns = ["the", "fox", "quick", "cat"]

print(f"Text: '{search_text}'")
for pattern in patterns:
    occurrences = find_pattern_occurrences(search_text.lower(), pattern)
    print(f"  Pattern '{pattern}': {len(occurrences)} occurrences at positions {occurrences}")

print("\n" + "=" * 50)
print("1️⃣4️⃣ String Security and Validation")
print("=" * 50)

print("\n🔒 String Security Considerations")
print("-" * 31)

# Input sanitization
def sanitize_input(user_input):
    """Sanitize user input for basic security"""
    # Remove potential HTML/script tags
    dangerous_patterns = ['<script', '</script>', '<iframe', '</iframe>', 'javascript:', 'on']
    
    sanitized = user_input
    for pattern in dangerous_patterns:
        sanitized = sanitized.replace(pattern.lower(), '')
        sanitized = sanitized.replace(pattern.upper(), '')
    
    # Remove excessive whitespace
    sanitized = ' '.join(sanitized.split())
    
    # Limit length
    if len(sanitized) > 1000:
        sanitized = sanitized[:1000] + "..."
    
    return sanitized

print("🛡️ Input Sanitization:")
dangerous_inputs = [
    "Hello <script>alert('hack')</script> World",
    "Normal text input",
    "JavaScript:void(0)",
    "Click <iframe src='evil.com'></iframe> here",
    "A" * 1100  # Very long input
]

for dangerous_input in dangerous_inputs:
    sanitized = sanitize_input(dangerous_input)
    print(f"  Original: '{dangerous_input[:50]}{'...' if len(dangerous_input) > 50 else ''}'")
    print(f"  Sanitized: '{sanitized[:50]}{'...' if len(sanitized) > 50 else ''}'")
    print()

# SQL injection prevention (basic example)
def safe_sql_like_query(table, column, search_term):
    """Example of safer SQL-like string construction"""
    # Escape special characters
    escaped_term = search_term.replace("'", "''").replace(";", "")
    
    # Use parameterized query style (simulation)
    query_template = "SELECT * FROM {} WHERE {} LIKE '%{}%'"
    
    # Basic validation
    if not table.isalnum() or not column.isalnum():
        return "Error: Invalid table or column name"
    
    return query_template.format(table, column, escaped_term)

print("🗄️ SQL Injection Prevention Example:")
sql_tests = [
    ("users", "name", "John"),
    ("users", "name", "'; DROP TABLE users; --"),
    ("products", "description", "laptop"),
    ("invalid_table!", "name", "test")
]

for table, column, search in sql_tests:
    result = safe_sql_like_query(table, column, search)
    print(f"  Query: {table}.{column} LIKE '{search}'")
    print(f"  Result: {result}")
    print()

print("\n" + "=" * 50)
print("1️⃣5️⃣ String Best Practices")
print("=" * 50)

print("\n💡 String Best Practices Guide")
print("-" * 29)

print("""
🎯 Performance Best Practices:
✅ Use f-strings for formatting (fastest and most readable)
✅ Use join() for concatenating many strings
✅ Avoid += in loops for string building
✅ Use string methods instead of regular expressions when possible
✅ Cache frequently used string operations

🔒 Security Best Practices:
✅ Always validate and sanitize user input
✅ Use parameterized queries for SQL
✅ Escape special characters when needed
✅ Set reasonable length limits on inputs
✅ Be careful with eval() and exec() on strings

📝 Code Quality Best Practices:
✅ Use meaningful variable names
✅ Keep string literals in constants when reused
✅ Document string format expectations
✅ Use type hints for string parameters
✅ Handle encoding/decoding explicitly

🌐 Internationalization Best Practices:
✅ Use Unicode (UTF-8) by default
✅ Be aware of locale-specific operations
✅ Test with non-ASCII characters
✅ Consider right-to-left languages
✅ Use locale-aware string comparisons when needed
""")

# Example of good string practices
print("\n📋 Example: Well-Structured String Class")

class StringValidator:
    """Example of good string handling practices"""
    
    # Constants
    MAX_LENGTH = 1000
    ALLOWED_CHARS = string.ascii_letters + string.digits + " .-_@"
    
    def __init__(self, value: str):
        self.value = self._validate_and_clean(value)
    
    def _validate_and_clean(self, value: str) -> str:
        """Validate and clean input string"""
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        
        # Clean whitespace
        cleaned = value.strip()
        
        # Check length
        if len(cleaned) > self.MAX_LENGTH:
            raise ValueError(f"String too long (max {self.MAX_LENGTH} characters)")
        
        # Check allowed characters
        for char in cleaned:
            if char not in self.ALLOWED_CHARS:
                raise ValueError(f"Invalid character: '{char}'")
        
        return cleaned
    
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return f"StringValidator('{self.value}')"
    
    def is_email_like(self) -> bool:
        """Check if string looks like an email"""
        return "@" in self.value and "." in self.value.split("@")[-1]
    
    def capitalize_words(self) -> str:
        """Capitalize each word"""
        return " ".join(word.capitalize() for word in self.value.split())

print("Testing StringValidator:")
test_values = [
    "john.doe@example.com",
    "hello world",
    "Test String 123",
    "invalid@char!",  # This will fail
]

for test_val in test_values[:3]:  # Skip the invalid one for demo
    try:
        sv = StringValidator(test_val)
        print(f"  Value: {sv}")
        print(f"  Email-like: {sv.is_email_like()}")
        print(f"  Capitalized: {sv.capitalize_words()}")
        print()
    except (ValueError, TypeError) as e:
        print(f"  Error with '{test_val}': {e}")

print("\n" + "=" * 50)
print("1️⃣6️⃣ String Testing and Debugging")
print("=" * 50)

print("\n🧪 String Testing Strategies")
print("-" * 26)

def comprehensive_string_test(func, test_cases):
    """Test a string function with various cases"""
    print(f"Testing function: {func.__name__}")
    
    for i, (input_val, expected) in enumerate(test_cases, 1):
        try:
            result = func(input_val)
            status = "✅ PASS" if result == expected else "❌ FAIL"
            print(f"  Test {i}: {status}")
            print(f"    Input: '{input_val}'")
            print(f"    Expected: {expected}")
            print(f"    Got: {result}")
        except Exception as e:
            print(f"  Test {i}: ❌ ERROR - {e}")
        print()

# Example function to test
def reverse_words(text):
    """Reverse the order of words in a string"""
    return " ".join(text.split()[::-1])

print("🔄 Testing reverse_words function:")
test_cases = [
    ("hello world", "world hello"),
    ("Python is awesome", "awesome is Python"),
    ("", ""),
    ("single", "single"),
    ("  extra   spaces  ", "spaces extra")
]

comprehensive_string_test(reverse_words, test_cases)

# String debugging helper
def debug_string(s, label="String"):
    """Debug helper for string analysis"""
    print(f"🔍 {label} Debug Info:")
    print(f"  Value: '{s}'")
    print(f"  Type: {type(s)}")
    print(f"  Length: {len(s)}")
    print(f"  Memory: {sys.getsizeof(s)} bytes")
    print(f"  Is ASCII: {s.isascii()}")
    print(f"  Encoding: {s.encode('utf-8')}")
    
    if s:
        print(f"  First char: '{s[0]}' (ord: {ord(s[0])})")
        print(f"  Last char: '{s[-1]}' (ord: {ord(s[-1])})")
    
    # Character analysis
    char_types = {
        "letters": sum(1 for c in s if c.isalpha()),
        "digits": sum(1 for c in s if c.isdigit()),
        "spaces": sum(1 for c in s if c.isspace()),
        "symbols": sum(1 for c in s if not c.isalnum() and not c.isspace())
    }
    print(f"  Character breakdown: {char_types}")

print("🔍 String Debugging Example:")
debug_string("Hello, 世界! 123 🌍", "Mixed String")

print("\n" + "=" * 50)
print("1️⃣7️⃣ Practice Exercises")
print("=" * 50)

print("\n🏋️ String Practice Challenges")
print("-" * 28)

print("""
Challenge 1: Create a function that counts vowels and consonants
Challenge 2: Build a simple word frequency counter
Challenge 3: Implement a basic spell checker
Challenge 4: Create a text statistics analyzer
Challenge 5: Build a simple template engine
""")

# Challenge 1: Vowel and consonant counter
def count_vowels_consonants(text):
    """Count vowels and consonants in text"""
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

print("Challenge 1 - Vowel/Consonant Counter:")
test_sentences = [
    "Hello World",
    "Python Programming",
    "The quick brown fox"
]

for sentence in test_sentences:
    vowels, consonants = count_vowels_consonants(sentence)
    print(f"  '{sentence}' → Vowels: {vowels}, Consonants: {consonants}")

# Challenge 2: Word frequency counter
def word_frequency(text):
    """Count frequency of each word"""
    # Clean and split text
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        # Remove punctuation
        clean_word = ''.join(char for char in word if char.isalnum())
        if clean_word:
            frequency[clean_word] = frequency.get(clean_word, 0) + 1
    
    return frequency

print(f"\nChallenge 2 - Word Frequency Counter:")
sample_text = "The quick brown fox jumps over the lazy dog. The dog was very lazy."
frequencies = word_frequency(sample_text)
print(f"Text: '{sample_text}'")
print("Word frequencies:")
for word, count in sorted(frequencies.items()):
    print(f"  '{word}': {count}")

# Challenge 3: Simple spell checker
def simple_spell_check(word, dictionary):
    """Simple spell checker with suggestions"""
    if word.lower() in [d.lower() for d in dictionary]:
        return True, []
    
    # Find similar words (simple approach)
    suggestions = []
    for dict_word in dictionary:
        if abs(len(word) - len(dict_word)) <= 2:
            distance = levenshtein_distance(word.lower(), dict_word.lower())
            if distance <= 2:
                suggestions.append((dict_word, distance))
    
    # Sort by distance and return top 3
    suggestions.sort(key=lambda x: x[1])
    return False, [word for word, _ in suggestions[:3]]

print(f"\nChallenge 3 - Simple Spell Checker:")
mini_dictionary = ["hello", "world", "python", "programming", "computer", "science"]
test_words = ["hello", "wrold", "pythom", "programing", "xyz"]

for word in test_words:
    is_correct, suggestions = simple_spell_check(word, mini_dictionary)
    if is_correct:
        print(f"  '{word}' ✅ Correct")
    else:
        print(f"  '{word}' ❌ Incorrect - Suggestions: {suggestions}")

print("\n" + "=" * 70)
print("🎉 Congratulations! You've completed the Python Strings Guide!")
print("🏆 You now have comprehensive knowledge of string manipulation!")
print("=" * 70)

print(f"""
🎯 What You've Mastered:

✅ String creation and quote types
✅ Character encoding and Unicode
✅ Indexing and slicing techniques
✅ All essential string methods
✅ String formatting (old and modern)
✅ Concatenation performance
✅ Validation and cleaning
✅ Advanced string operations
✅ Security considerations
✅ Performance optimization
✅ Real-world applications
✅ String algorithms and patterns
✅ Best practices and debugging

🚀 Next Steps:
1. Practice with real text data
2. Build text processing applications
3. Learn regular expressions
4. Explore natural language processing
5. Work with APIs that return text data

💡 Remember:
- Strings are immutable in Python
- f-strings are the modern way to format
- Always validate user input
- Performance matters with large text data
- Unicode handling is important for global apps

Keep practicing and building! 🐍✨
""")

# Quick reference card
print(f"""
📋 Strings Quick Reference:

Creating:
'text' or "text"          # Basic strings
'''multiline'''           # Multiline strings
f"Hello {name}"          # f-strings (best)

Common Methods:
str.upper(), .lower()     # Case conversion
str.strip()              # Remove whitespace
str.split()              # Split to list
str.join(list)           # Join list to string
str.replace(old, new)    # Replace text
str.find(sub)            # Find position
str.startswith(prefix)   # Check start
str.endswith(suffix)     # Check end

Formatting:
f"{{var}}"                # f-string (recommended)
"{{}}".format(var)        # .format() method
"%s" % var               # % formatting (old)

Safety:
Always validate input
Use parameterized queries
Escape special characters
Set length limits
""")

# End of comprehensive string guide