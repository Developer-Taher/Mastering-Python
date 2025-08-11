# =====================================
# Complete Guide to Python Data Types
# Comprehensive Tutorial and Reference
# =====================================

"""
What are Data Types?
Data types are classifications that specify what kind of value can be stored in a variable.
In Python, everything is an object, and each object has a specific type.
Examples: text, numbers, lists, dictionaries, etc.
"""

import sys
import time
from datetime import datetime

print("=" * 70)
print("🐍 Complete Guide to Python Data Types")
print("=" * 70)

print("\n" + "=" * 50)
print("1️⃣ Introduction to Data Types")
print("=" * 50)

print("""
🎯 In Python:
✅ Everything is an object
✅ Python determines type automatically
✅ Types can be converted between each other
✅ Use type() to check the type
""")

# type() function - the foundation for checking data types
print("\n📋 type() function - to check any data type:")
print("type(object)  # returns the data type")

print("\n" + "=" * 50)
print("2️⃣ Integers (int)")
print("=" * 50)

print("\n🔢 Integers - int")
print("-" * 17)

# Examples of integers
positive_int = 19
large_int = 100
negative_int = -50
zero = 0

print(f"Positive number: {positive_int} - Type: {type(positive_int)}")
print(f"Large number: {large_int} - Type: {type(large_int)}")
print(f"Negative number: {negative_int} - Type: {type(negative_int)}")
print(f"Zero: {zero} - Type: {type(zero)}")

# Integer properties
print("\n💡 Integer properties:")
big_number = 999999999999999999999999999999
print(f"Very big number: {big_number}")
print(f"Its type: {type(big_number)}")
print(f"Size in bytes: {sys.getsizeof(big_number)} bytes")

# Operations on integers
print(f"\nArithmetic operations:")
print(f"Addition: {positive_int} + {large_int} = {positive_int + large_int}")
print(f"Multiplication: {positive_int} * {large_int} = {positive_int * large_int}")
print(f"Division: {large_int} / {positive_int} = {large_int / positive_int} - Type: {type(large_int / positive_int)}")
print(f"Floor division: {large_int} // {positive_int} = {large_int // positive_int} - Type: {type(large_int // positive_int)}")

# Different number systems
print(f"\n🔣 Different number systems:")
decimal_num = 255
binary_num = 0b11111111  # Binary system
octal_num = 0o377        # Octal system
hex_num = 0xFF           # Hexadecimal system

print(f"Decimal: {decimal_num}")
print(f"Binary: {binary_num} (0b11111111)")
print(f"Octal: {octal_num} (0o377)")
print(f"Hexadecimal: {hex_num} (0xFF)")
print(f"All equal: {decimal_num == binary_num == octal_num == hex_num}")

print("\n" + "=" * 50)
print("3️⃣ Floating Point Numbers (float)")
print("=" * 50)

print("\n🔢 Floating point numbers - float")
print("-" * 33)

# Examples of floats
simple_float = 10.5
precise_float = 1.92
negative_float = -21.92
scientific_notation = 1.5e3  # 1.5 × 10³ = 1500
very_small = 1.5e-3          # 1.5 × 10⁻³ = 0.0015

print(f"Simple float: {simple_float} - Type: {type(simple_float)}")
print(f"Precise float: {precise_float} - Type: {type(precise_float)}")
print(f"Negative float: {negative_float} - Type: {type(negative_float)}")
print(f"Scientific notation (large): {scientific_notation} - Type: {type(scientific_notation)}")
print(f"Scientific notation (small): {very_small} - Type: {type(very_small)}")

# Float precision issues
print(f"\n⚠️ Float precision issues:")
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"Is 0.1 + 0.2 == 0.3? {result == 0.3}")
print(f"Solution: using round() → {round(result, 1) == 0.3}")

# Advanced math operations
import math
print(f"\n🧮 Advanced mathematical operations:")
number = 16.25
print(f"Number: {number}")
print(f"Square root: {math.sqrt(number):.3f}")
print(f"Ceiling: {math.ceil(number)}")
print(f"Floor: {math.floor(number)}")
print(f"Absolute value: {abs(-number)}")

# Special float values
print(f"\n🌟 Special float values:")
infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(f"Infinity: {infinity} - Type: {type(infinity)}")
print(f"Negative infinity: {negative_infinity}")
print(f"Not a Number (NaN): {not_a_number}")
print(f"Is inf > 1000000? {infinity > 1000000}")

print("\n" + "=" * 50)
print("4️⃣ Strings (str)")
print("=" * 50)

print("\n📝 Strings - str")
print("-" * 15)

# Examples of strings
simple_string = 'I love Python'
double_quotes = "This is a string with double quotes"
multiline_string = """This is a
multiline string
that can span multiple lines"""
empty_string = ""
unicode_string = "Hello 🐍 Python! 😊"

print(f"Simple string: '{simple_string}' - Type: {type(simple_string)}")
print(f"Double quotes: \"{double_quotes}\"")
print(f"Multiline string:\n{multiline_string}")
print(f"Empty string: '{empty_string}' - Length: {len(empty_string)}")
print(f"Unicode string: '{unicode_string}'")

# String properties
text = "Python Programming"
print(f"\n🔍 String properties:")
print(f"Text: '{text}'")
print(f"Length: {len(text)} characters")
print(f"Uppercase: '{text.upper()}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Title case: '{text.title()}'")
print(f"Starts with Python? {text.startswith('Python')}")
print(f"Ends with ing? {text.endswith('ing')}")

# String indexing
print(f"\n📌 String indexing:")
word = "Python"
print(f"Word: '{word}'")
print(f"First character [0]: '{word[0]}'")
print(f"Last character [-1]: '{word[-1]}'")
print(f"Slice [1:4]: '{word[1:4]}'")
print(f"Every second character [::2]: '{word[::2]}'")
print(f"Reverse [::-1]: '{word[::-1]}'")

# String splitting and joining
sentence = "Python is an amazing programming language"
print(f"\n✂️ String splitting and joining:")
print(f"Sentence: '{sentence}'")
words = sentence.split()
print(f"Words: {words}")
rejoined = " - ".join(words)
print(f"Rejoined: '{rejoined}'")

# String formatting
name = "John"
age = 25
print(f"\n🎨 String formatting:")
print(f"f-string: Hello {name}, you are {age} years old")
print("format(): Hello {}, you are {} years old".format(name, age))
#print("% formatting: Hello %s, you are %d years old" % (name, age))

print("\n" + "=" * 50)
print("5️⃣ Lists (list)")
print("=" * 50)

print("\n📋 Lists - list")
print("-" * 15)

# Examples of lists
numbers = [1, 2, 3, 45, 6, 3]
mixed_list = [1, "text", 3.14, True, None]
nested_list = [[1, 2], [3, 4], [5, 6]]
empty_list = []

print(f"Number list: {numbers} - Type: {type(numbers)}")
print(f"Mixed list: {mixed_list}")
print(f"Nested list: {nested_list}")
print(f"Empty list: {empty_list} - Length: {len(empty_list)}")

# List operations
fruits = ["apple", "orange", "banana"]
print(f"\n🍎 List operations:")
print(f"Original list: {fruits}")

# Adding elements
fruits.append("grape")
print(f"After append('grape'): {fruits}")

fruits.insert(1, "strawberry")
print(f"After insert(1, 'strawberry'): {fruits}")

# Removing elements
removed = fruits.pop()
print(f"After pop(): {fruits}, removed element: {removed}")

fruits.remove("orange")
print(f"After remove('orange'): {fruits}")

# Indexing and slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\n📍 List indexing and slicing:")
print(f"List: {numbers}")
print(f"First element [0]: {numbers[0]}")
print(f"Last element [-1]: {numbers[-1]}")
print(f"First 5 elements [:5]: {numbers[:5]}")
print(f"Last 3 elements [-3:]: {numbers[-3:]}")
print(f"Every second element [::2]: {numbers[::2]}")

# Useful list methods
data = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n🔧 Useful list methods:")
print(f"Data: {data}")
print(f"Length: {len(data)}")
print(f"Sum: {sum(data)}")
print(f"Maximum: {max(data)}")
print(f"Minimum: {min(data)}")
print(f"Count of 1: {data.count(1)}")
print(f"Index of 5: {data.index(5)}")

# List copying
original = [1, 2, 3]
shallow_copy = original.copy()
deep_copy = original[:]
reference = original

print(f"\n📄 List copying:")
original.append(4)
print(f"Original after modification: {original}")
print(f"Shallow copy: {shallow_copy}")
print(f"Deep copy: {deep_copy}")
print(f"Reference: {reference}")

print("\n" + "=" * 50)
print("6️⃣ Tuples (tuple)")
print("=" * 50)

print("\n📦 Tuples - tuple")
print("-" * 17)

# Examples of tuples
coordinates = (1, 2, 3, 4, 5)
mixed_tuple = (1, "text", 3.14, True)
single_item = (42,)  # Comma is important for single-item tuple
empty_tuple = ()
nested_tuple = ((1, 2), (3, 4), (5, 6))

print(f"Coordinates: {coordinates} - Type: {type(coordinates)}")
print(f"Mixed tuple: {mixed_tuple}")
print(f"Single item: {single_item}")
print(f"Empty tuple: {empty_tuple}")
print(f"Nested tuple: {nested_tuple}")

# Tuple properties
point = (10, 20)
print(f"\n🔒 Tuple properties (immutable):")
print(f"Point: {point}")
print(f"X coordinate: {point[0]}")
print(f"Y coordinate: {point[1]}")

# Attempting to modify tuple (will cause error)
print("# point[0] = 30  # TypeError! Tuples are immutable")

# Tuple unpacking
person = ("John", 25, "Engineer")
name, age, job = person
print(f"\n📤 Tuple unpacking:")
print(f"Name: {name}, Age: {age}, Job: {job}")

# Practical uses of tuples
def get_name_age():
    return "Sarah", 30

result = get_name_age()
print(f"Function result: {result} - Type: {type(result)}")

# Performance comparison between lists and tuples
import timeit

list_data = [1, 2, 3, 4, 5] * 1000
tuple_data = tuple(list_data)

list_time = timeit.timeit(lambda: list_data[500], number=1000000)
tuple_time = timeit.timeit(lambda: tuple_data[500], number=1000000)

print(f"\n⚡ Performance comparison:")
print(f"List access time: {list_time:.6f} seconds")
print(f"Tuple access time: {tuple_time:.6f} seconds")
print(f"Tuple is {list_time/tuple_time:.2f}x faster")

print("\n" + "=" * 50)
print("7️⃣ Dictionaries (dict)")
print("=" * 50)

print("\n📚 Dictionaries - dict")
print("-" * 21)

# Examples of dictionaries
student = {"name": "John", "age": 20, "city": "New York"}
mixed_dict = {"number": 1, "text": "hello", "list": [1, 2, 3]}
empty_dict = {}
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 22}
}

print(f"Student: {student} - Type: {type(student)}")
print(f"Mixed dict: {mixed_dict}")
print(f"Empty dict: {empty_dict}")
print(f"Nested dict: {nested_dict}")

# Accessing values
print(f"\n🔍 Accessing values:")
print(f"Student name: {student['name']}")
print(f"Student age: {student.get('age')}")
print(f"Salary (not found): {student.get('salary', 'Not specified')}")

# Adding and modifying values
student["salary"] = 5000
student["age"] = 21
print(f"After modification: {student}")

# Dictionary operations
grades = {"math": 95, "physics": 88, "chemistry": 92}
print(f"\n📊 Dictionary operations:")
print(f"Grades: {grades}")
print(f"Subjects: {list(grades.keys())}")
print(f"Scores: {list(grades.values())}")
print(f"Items: {list(grades.items())}")

# Iterating over dictionary
print(f"\n🔄 Iterating over dictionary:")
for subject, grade in grades.items():
    print(f"  {subject}: {grade}")

# Merging dictionaries
personal_info = {"name": "Sarah", "age": 25}
contact_info = {"phone": "123456", "email": "sarah@email.com"}

# Python 3.9+
combined = personal_info | contact_info
print(f"\nMerged dictionaries: {combined}")

# Alternative method
combined2 = {**personal_info, **contact_info}
print(f"Alternative merge: {combined2}")

print("\n" + "=" * 50)
print("8️⃣ Boolean Values (bool)")
print("=" * 50)

print("\n✅ Boolean values - bool")
print("-" * 24)

# Basic boolean values
true_value = True
false_value = False
comparison_result = (2 == 3)

print(f"True: {true_value} - Type: {type(true_value)}")
print(f"False: {false_value} - Type: {type(false_value)}")
print(f"Comparison result 2==3: {comparison_result} - Type: {type(comparison_result)}")

# Converting to boolean
print(f"\n🔄 Converting to boolean:")
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('text'): {bool('text')}")
print(f"bool(''): {bool('')}")
print(f"bool([1,2,3]): {bool([1,2,3])}")
print(f"bool([]): {bool([])}")
print(f"bool(None): {bool(None)}")

# Boolean operations
a = True
b = False
print(f"\n🧮 Boolean operations:")
print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")
print(f"not b: {not b}")

# Comparisons
x = 10
y = 5
print(f"\n⚖️ Comparisons:")
print(f"x = {x}, y = {y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Boolean values in conditions
age = 18
has_license = True

if age >= 18 and has_license:
    result = "Can drive"
else:
    result = "Cannot drive"

print(f"\n🚗 Practical example:")
print(f"Age: {age}, Has license: {has_license}")
print(f"Result: {result}")

print("\n" + "=" * 50)
print("9️⃣ Other Important Data Types")
print("=" * 50)

# None - null value
print("\n🔳 None - null value")
print("-" * 19)
nothing = None
print(f"Null value: {nothing} - Type: {type(nothing)}")
print(f"bool(None): {bool(nothing)}")
print(f"None == None: {nothing == None}")
print(f"None is None: {nothing is None}")

# bytes - binary data
print("\n💾 bytes - binary data")
print("-" * 21)
text_bytes = "Hello".encode('utf-8')
print(f"Text as bytes: {text_bytes}")
print(f"Type: {type(text_bytes)}")
print(f"Back to text: {text_bytes.decode('utf-8')}")

# set - collections without duplicates
print("\n🎯 set - collections (no duplicates)")
print("-" * 33)
numbers_set = {1, 2, 3, 4, 5, 1, 2, 3}  # Duplicates will be removed
print(f"Set: {numbers_set} - Type: {type(numbers_set)}")

fruits_set = {"apple", "orange", "banana", "apple"}
print(f"Fruits set: {fruits_set}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

print("\n" + "=" * 50)
print("🔟 Type Conversion")
print("=" * 50)

print("\n🔄 Type conversion")
print("-" * 17)

# Converting to integers
print("Converting to int:")
print(f"int('123'): {int('123')}")
print(f"int(45.67): {int(45.67)}")
print(f"int(True): {int(True)}")
print(f"int(False): {int(False)}")

# Converting to floats
print(f"\nConverting to float:")
print(f"float('123.45'): {float('123.45')}")
print(f"float(100): {float(100)}")
print(f"float(True): {float(True)}")

# Converting to strings
print(f"\nConverting to str:")
print(f"str(123): '{str(123)}'")
print(f"str(45.67): '{str(45.67)}'")
print(f"str(True): '{str(True)}'")
print(f"str([1,2,3]): '{str([1,2,3])}'")

# Converting to lists
print(f"\nConverting to list:")
print(f"list('Python'): {list('Python')}")
print(f"list((1,2,3)): {list((1,2,3))}")
print(f"list({{1,2,3}}): {list({1,2,3})}")

# Converting to tuples
print(f"\nConverting to tuple:")
print(f"tuple([1,2,3]): {tuple([1,2,3])}")
print(f"tuple('Python'): {tuple('Python')}")

# Common conversion errors
print(f"\n❌ Common conversion errors:")
print("# int('12.5')  # ValueError! Cannot convert float string to int directly")
print("# Solution: int(float('12.5'))")
print(f"Solution: {int(float('12.5'))}")

print("\n" + "=" * 50)
print("1️⃣1️⃣ Comprehensive Practical Examples")
print("=" * 50)

# Example 1: Student management system
print("\n🎓 Example 1: Student Management System")
print("-" * 38)

class StudentManager:
    def __init__(self):
        self.students = {}  # dict
        self.next_id = 1    # int
    
    def add_student(self, name, age, grades):
        student_data = {
            "name": name,           # str
            "age": age,            # int
            "grades": grades,       # list
            "average": sum(grades) / len(grades),  # float
            "active": True             # bool
        }
        self.students[self.next_id] = student_data
        self.next_id += 1
        return self.next_id - 1
    
    def get_student_info(self, student_id):
        if student_id in self.students:
            return self.students[student_id]
        return None  # None type

# Using the system
manager = StudentManager()
student_id = manager.add_student("John Smith", 20, [85, 90, 88, 92])
student_info = manager.get_student_info(student_id)

print(f"Student ID: {student_id} - Type: {type(student_id)}")
print(f"Student info: {student_info}")
print(f"Info type: {type(student_info)}")

for key, value in student_info.items():
    print(f"  {key}: {value} - Type: {type(value)}")

# Example 2: Shopping system
print(f"\n🛒 Example 2: Shopping System")
print("-" * 30)

# Store products
products = {
    "apple": {"price": 5.50, "quantity": 100},    # float, int
    "banana": {"price": 3.25, "quantity": 150},
    "orange": {"price": 4.75, "quantity": 80}
}

# Shopping cart
shopping_cart = []  # list

def add_to_cart(product_name, quantity):
    """Add product to cart"""
    if product_name in products:
        if products[product_name]["quantity"] >= quantity:
            cart_item = {
                "product": product_name,      # str
                "quantity": quantity,          # int
                "price": products[product_name]["price"],  # float
                "total": products[product_name]["price"] * quantity  # float
            }
            shopping_cart.append(cart_item)
            products[product_name]["quantity"] -= quantity
            return True  # bool
        else:
            print(f"Requested quantity not available. Available: {products[product_name]['quantity']}")
            return False  # bool
    else:
        print(f"Product '{product_name}' not found")
        return False  # bool

def calculate_total():
    """Calculate total cost"""
    total = 0.0  # float
    for item in shopping_cart:  # Iterate over list
        total += item["total"]  # Add float
    return total

# Using the shopping system
print("Available products:")
for product, details in products.items():
    print(f"  {product}: ${details['price']} - Available: {details['quantity']}")

# Add products to cart
add_to_cart("apple", 5)
add_to_cart("banana", 3)
add_to_cart("orange", 200)  # More than available

print(f"\nShopping cart:")
for item in shopping_cart:
    print(f"  {item['product']}: {item['quantity']} × ${item['price']} = ${item['total']}")

total_cost = calculate_total()
print(f"\nTotal cost: ${total_cost} - Type: {type(total_cost)}")

# Example 3: Data analysis
print(f"\n📊 Example 3: Student Data Analysis")
print("-" * 35)

# Sample student data
students_data = [
    ("John", 85, True),      # tuple: (str, int, bool)
    ("Sarah", 92, True),
    ("Mike", 78, False),
    ("Emma", 96, True),
    ("Alex", 81, True)
]

def analyze_students_data(data):
    """Analyze student data"""
    total_students = len(data)          # int
    active_students = []                # list
    grades = []                         # list
    
    for name, grade, is_active in data:  # unpacking tuple
        if is_active:                    # bool check
            active_students.append(name)  # str
            grades.append(grade)         # int
    
    if grades:  # Check if list is not empty
        average_grade = sum(grades) / len(grades)  # float
        max_grade = max(grades)                    # int
        min_grade = min(grades)                    # int
    else:
        average_grade = max_grade = min_grade = 0
    
    analysis = {
        "total_students": total_students,
        "active_students": len(active_students),
        "active_names": active_students,
        "average_grade": round(average_grade, 2),
        "highest_grade": max_grade,
        "lowest_grade": min_grade,
        "success_rate": f"{(len(active_students)/total_students)*100:.1f}%"
    }
    
    return analysis

# Analyze the data
analysis_result = analyze_students_data(students_data)

print("Analysis results:")
for key, value in analysis_result.items():
    print(f"  {key}: {value} - Type: {type(value)}")

print("\n" + "=" * 50)
print("1️⃣2️⃣ Common Errors and Solutions")
print("=" * 50)

print("\n❌ Common errors and solutions")
print("-" * 30)

print("1. Mixing types in operations:")
print("❌ Error: '5' + 3")
print("✅ Solution: int('5') + 3 or '5' + str(3)")
print(f"   Result: {int('5') + 3} or {'5' + str(3)}")

print("\n2. Forgetting conversion in comparisons:")
age_input = "25"  # From user input as string
print(f"❌ Error: '{age_input}' > 18 = {age_input > '18'} (string comparison!)")
print(f"✅ Solution: int('{age_input}') > 18 = {int(age_input) > 18}")

print("\n3. Using == instead of is with None:")
value = None
print(f"✅ Correct: value is None = {value is None}")
print(f"⚠️ Works but not best: value == None = {value == None}")

print("\n4. Modifying tuple (immutable):")
coordinates = (10, 20)
print("❌ Error: coordinates[0] = 30  # TypeError!")
print("✅ Solution: create new tuple")
new_coordinates = (30, coordinates[1])
print(f"   Old: {coordinates}, New: {new_coordinates}")

print("\n5. Mixing list and tuple in indexing:")
mixed_data = [(1, 2), (3, 4), (5, 6)]  # list of tuples
print(f"Data: {mixed_data}")
print(f"Access first element: {mixed_data[0]}")  # tuple
print(f"Access first element of first tuple: {mixed_data[0][0]}")  # int

print("\n" + "=" * 50)
print("1️⃣3️⃣ Performance and Memory Tips")
print("=" * 50)

print("\n⚡ Performance tips")
print("-" * 17)

# Memory usage comparison
import sys

# Lists vs tuples
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(f"List memory size: {sys.getsizeof(list_data)} bytes")
print(f"Tuple memory size: {sys.getsizeof(tuple_data)} bytes")
print(f"Tuple saves: {sys.getsizeof(list_data) - sys.getsizeof(tuple_data)} bytes")

# Strings vs lists for large text
text = "Python" * 1000
text_list = ["Python"] * 1000

print(f"\nRepeated string size: {sys.getsizeof(text)} bytes")
print(f"String list size: {sys.getsizeof(text_list)} bytes")

# Using sets for fast searching
large_list = list(range(10000))
large_set = set(range(10000))

# Measure search time
import timeit

list_search_time = timeit.timeit(lambda: 9999 in large_list, number=1000)
set_search_time = timeit.timeit(lambda: 9999 in large_set, number=1000)

print(f"\nList search time: {list_search_time:.6f} seconds")
print(f"Set search time: {set_search_time:.6f} seconds")
print(f"Set is {list_search_time/set_search_time:.0f}x faster")

print("\n💡 Memory tips:")
print("✅ Use tuple instead of list for fixed data")
print("✅ Use set for fast searching")
print("✅ Use dict for key-based lookups")
print("✅ Avoid unnecessary copying of large lists")

print("\n" + "=" * 50)
print("1️⃣4️⃣ Data Type Inspection Tools")
print("=" * 50)

print("\n🔍 Inspection and checking tools")
print("-" * 30)

def analyze_variable(var, name="variable"):
    """Comprehensive analysis of any variable"""
    print(f"\n📋 Analysis of {name}:")
    print(f"  Value: {var}")
    print(f"  Type: {type(var)}")
    print(f"  Type name: {type(var).__name__}")
    
    # Type checking
    if isinstance(var, int):
        print(f"  Integer - Absolute value: {abs(var)}")
        print(f"  Binary: {bin(var)}")
        print(f"  Hexadecimal: {hex(var)}")
    
    elif isinstance(var, float):
        print(f"  Float - Rounded: {round(var, 2)}")
        print(f"  Integer part: {int(var)}")
        print(f"  Is integer? {var.is_integer()}")
    
    elif isinstance(var, str):
        print(f"  String - Length: {len(var)} characters")
        print(f"  Is digit? {var.isdigit()}")
        print(f"  Is alpha? {var.isalpha()}")
        print(f"  Is alphanumeric? {var.isalnum()}")
    
    elif isinstance(var, (list, tuple)):
        print(f"  Sequence - Length: {len(var)}")
        if var:
            print(f"  First element: {var[0]} - Type: {type(var[0])}")
            print(f"  Last element: {var[-1]} - Type: {type(var[-1])}")
    
    elif isinstance(var, dict):
        print(f"  Dictionary - Number of keys: {len(var)}")
        if var:
            print(f"  Keys: {list(var.keys())}")
    
    elif isinstance(var, bool):
        print(f"  Boolean - Numeric value: {int(var)}")
    
    elif var is None:
        print(f"  Null value")
    
    print(f"  Memory size: {sys.getsizeof(var)} bytes")
    print(f"  Boolean value: {bool(var)}")

# Test the tool
test_variables = [
    (42, "integer"),
    (3.14159, "float"),
    ("Python is awesome", "string"),
    ([1, 2, 3, "text"], "mixed list"),
    ((10, 20), "coordinate tuple"),
    ({"name": "John", "age": 25}, "person dict"),
    (True, "boolean value"),
    (None, "null value"),
    ({1, 2, 3, 4}, "number set")
]

for var, description in test_variables:
    analyze_variable(var, description)

print("\n" + "=" * 50)
print("1️⃣5️⃣ Practical Exercises")
print("=" * 50)

print("\n🏋️ Practice exercises")
print("-" * 19)

def exercise_1():
    """Exercise 1: Data classification"""
    print("Exercise 1: Classify mixed data list")
    
    mixed_data = [1, "text", 3.14, True, [1, 2], None, {"key": "value"}, (1, 2)]
    
    classified = {
        "numbers": [],
        "strings": [],
        "lists": [],
        "dictionaries": [],
        "booleans": [],
        "null_values": [],
        "others": []
    }
    
    for item in mixed_data:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            classified["numbers"].append(item)
        elif isinstance(item, str):
            classified["strings"].append(item)
        elif isinstance(item, list):
            classified["lists"].append(item)
        elif isinstance(item, dict):
            classified["dictionaries"].append(item)
        elif isinstance(item, bool):
            classified["booleans"].append(item)
        elif item is None:
            classified["null_values"].append(item)
        else:
            classified["others"].append(item)
    
    print(f"Original data: {mixed_data}")
    for category, items in classified.items():
        if items:
            print(f"  {category}: {items}")

def exercise_2():
    """Exercise 2: Smart data type converter"""
    print("\nExercise 2: Smart data type converter")
    
    def smart_convert(value, target_type):
        """Smart converter for data types"""
        try:
            if target_type == "int":
                if isinstance(value, str) and '.' in value:
                    return int(float(value))  # Convert "12.5" to 12
                return int(value)
            elif target_type == "float":
                return float(value)
            elif target_type == "str":
                return str(value)
            elif target_type == "bool":
                if isinstance(value, str):
                    return value.lower() in ['true', '1', 'yes']
                return bool(value)
            elif target_type == "list":
                if isinstance(value, str):
                    return list(value)  # "abc" -> ['a', 'b', 'c']
                return list(value)
            else:
                return None
        except (ValueError, TypeError):
            return None
    
    test_cases = [
        ("123", "int"),
        ("12.5", "int"),
        ("45.67", "float"),
        (True, "str"),
        ("true", "bool"),
        ("Python", "list"),
        ([1, 2, 3], "str")
    ]
    
    for value, target in test_cases:
        result = smart_convert(value, target)
        print(f"  {value} ({type(value).__name__}) → {target}: {result} ({type(result).__name__})")

def exercise_3():
    """Exercise 3: Advanced data storage system"""
    print("\nExercise 3: Advanced data storage system")
    
    class DataStore:
        def __init__(self):
            self.data = {
                "integers": [],
                "floats": [],
                "strings": [],
                "lists": [],
                "dicts": [],
                "booleans": [],
                "others": []
            }
        
        def add(self, value):
            """Add value to appropriate store"""
            if isinstance(value, int) and not isinstance(value, bool):
                self.data["integers"].append(value)
            elif isinstance(value, float):
                self.data["floats"].append(value)
            elif isinstance(value, str):
                self.data["strings"].append(value)
            elif isinstance(value, list):
                self.data["lists"].append(value)
            elif isinstance(value, dict):
                self.data["dicts"].append(value)
            elif isinstance(value, bool):
                self.data["booleans"].append(value)
            else:
                self.data["others"].append(value)
        
        def get_stats(self):
            """Get storage statistics"""
            stats = {}
            for data_type, values in self.data.items():
                if values:
                    stats[data_type] = {
                        "count": len(values),
                        "sample": values[0] if values else None
                    }
            return stats
        
        def get_by_type(self, data_type):
            """Get data by type"""
            return self.data.get(data_type, [])
    
    # Test the system
    store = DataStore()
    
    sample_data = [
        42, 3.14, "hello", [1, 2, 3], {"name": "test"}, 
        True, False, 99, 2.71, "Python", None
    ]
    
    for item in sample_data:
        store.add(item)
    
    print(f"  Added data: {sample_data}")
    print(f"  Storage statistics:")
    for data_type, stats in store.get_stats().items():
        print(f"    {data_type}: {stats['count']} items, sample: {stats['sample']}")

# Run exercises
exercise_1()
exercise_2()
exercise_3()

print("\n" + "=" * 50)
print("1️⃣6️⃣ Comprehensive Summary")
print("=" * 50)

print(f"""
🎯 Python Data Types Summary:

📊 Basic Types:
┌─────────────┬─────────────┬──────────────┬─────────────────┐
│ Type        │ Symbol      │ Mutable      │ Example         │
├─────────────┼─────────────┼──────────────┼─────────────────┤
│ Integer     │ int         │ ❌           │ 42, -10, 0      │
│ Float       │ float       │ ❌           │ 3.14, -2.5      │
│ String      │ str         │ ❌           │ "hello", 'text' │
│ List        │ list        │ ✅           │ [1, 2, 3]       │
│ Tuple       │ tuple       │ ❌           │ (1, 2, 3)       │
│ Dictionary  │ dict        │ ✅           │ {{"a": 1}}        │
│ Boolean     │ bool        │ ❌           │ True, False     │
│ Set         │ set         │ ✅           │ {{1, 2, 3}}       │
│ None        │ NoneType    │ ❌           │ None            │
└─────────────┴─────────────┴──────────────┴─────────────────┘

🔧 Type checking methods:
✅ type(obj) - gives exact type
✅ isinstance(obj, type) - checks type
✅ obj.__class__.__name__ - type name as string

🔄 Conversion rules:
✅ Use int(), float(), str(), list(), tuple()
✅ Validate data before conversion
❌ Avoid direct conversion of float strings to int

⚡ Performance tips:
✅ tuple is faster than list for reading
✅ set is faster for searching than list
✅ dict is faster for key-based access
✅ f-strings are faster than + for strings

🚨 Common mistakes:
❌ Mixing types in operations
❌ Forgetting conversion from inputs
❌ Trying to modify tuple or str
❌ Using == instead of is with None

💡 Best practices:
✅ Use clear variable names
✅ Check types when needed
✅ Use appropriate type for the task
✅ Document data types in functions
""")

def final_demonstration():
    """Final comprehensive demonstration of all data types"""
    print("\n🎬 Final demonstration - all types together")
    print("-" * 45)
    
    # Create comprehensive example
    comprehensive_data = {
        "personal_info": {
            "name": "John Doe",                    # str
            "age": 28,                            # int
            "salary": 8500.75,                    # float
            "married": True,                      # bool
            "children": None                      # NoneType
        },
        "skills": ["Python", "JavaScript", "SQL"],  # list
        "coordinates": (24.7136, 46.6753),              # tuple
        "projects": {                                 # dict
            "project1": {"duration": 6, "completed": True},
            "project2": {"duration": 3, "completed": False}
        },
        "languages": {"English", "Spanish", "French"}, # set
        "resume": b"resume.pdf"                     # bytes
    }
    
    def explore_data(data, level=0):
        """Explore data interactively"""
        indent = "  " * level
        
        for key, value in data.items():
            print(f"{indent}🔑 {key}: {value}")
            print(f"{indent}   📝 Type: {type(value).__name__}")
            
            if isinstance(value, dict) and level < 2:
                print(f"{indent}   📂 Contents:")
                explore_data(value, level + 1)
            elif isinstance(value, (list, tuple, set)):
                print(f"{indent}   📊 Elements: {len(value)}")
                if value:
                    print(f"{indent}   🔍 Element type: {type(next(iter(value))).__name__}")
            elif isinstance(value, str):
                print(f"{indent}   📏 Length: {len(value)} characters")
            elif isinstance(value, (int, float)):
                print(f"{indent}   🔢 Even number: {value % 2 == 0}")
            
            print()
    
    explore_data(comprehensive_data)
    
    # Final statistics
    type_count = {}
    
    def count_types(obj):
        """Count data types in structure"""
        type_name = type(obj).__name__
        type_count[type_name] = type_count.get(type_name, 0) + 1
        
        if isinstance(obj, dict):
            for value in obj.values():
                count_types(value)
        elif isinstance(obj, (list, tuple, set)):
            for item in obj:
                count_types(item)
    
    count_types(comprehensive_data)
    
    print("📈 Type statistics in example:")
    for type_name, count in sorted(type_count.items()):
        print(f"   {type_name}: {count} occurrences")

# Run final demonstration
final_demonstration()

print("\n" + "=" * 70)
print("🎉 Complete Python Data Types Guide Finished!")
print("💻 You're now ready to use all data types effectively")
print("=" * 70)

# Quick reference for developers
print(f"""
📚 Quick reference:
type(obj)           # check type
isinstance(obj, t)  # verify type  
int/float/str()     # convert
len(obj)           # length
bool(obj)          # boolean value

⭐ Remember: Python is dynamic - types are determined at runtime!
""")

# End of file