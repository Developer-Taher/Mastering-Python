# =====================================
# Complete Guide to Python Tuples
# Comprehensive Tutorial and Reference
# =====================================

"""
What are Tuples?
Tuples are ordered, immutable collections of items in Python.
They are one of the fundamental data structures used for storing sequences.
Tuples cannot be modified after creation, making them perfect for fixed data.

Examples: (1, 2, 3), ('apple', 'banana'), (1, 'hello', 3.14, True), ()
"""

import sys
import timeit
import random
import itertools
import operator
from collections import Counter, namedtuple
from functools import reduce
import copy

print("=" * 70)
print("📦 Complete Guide to Python Tuples")
print("=" * 70)

print("\n" + "=" * 50)
print("1️⃣ Introduction to Tuples")
print("=" * 50)

print("""
📝 What are Tuples?
✅ Ordered collections of items
✅ Immutable (cannot be changed after creation)
✅ Allow duplicate elements
✅ Can contain mixed data types
✅ Indexed by integers starting from 0
✅ Hashable (can be used as dictionary keys)

🎯 Common Uses:
• Store coordinates (x, y, z)
• Return multiple values from functions
• Store database records
• Dictionary keys when you need composite keys
• Configuration settings that shouldn't change
• Represent fixed collections of related data

🆚 Tuples vs Lists:
Tuples: Immutable, Hashable, Slightly faster, Fixed size
Lists:  Mutable,   Unhashable, More flexible, Dynamic size
""")

print("\n" + "=" * 50)
print("2️⃣ Creating Tuples - Different Methods")
print("=" * 50)

print("\n📦 Ways to Create Tuples")
print("-" * 24)

# Empty tuple
empty_tuple1 = ()
empty_tuple2 = tuple()
print(f"Empty tuples:")
print(f"  () → {empty_tuple1}")
print(f"  tuple() → {empty_tuple2}")

# Tuple with initial values
numbers = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True, None)
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(f"\nTuples with initial values:")
print(f"  Numbers: {numbers}")
print(f"  Mixed types: {mixed_tuple}")
print(f"  Nested: {nested_tuple}")

# Single element tuple (note the comma!)
single_element1 = (42,)  # Correct way
single_element2 = tuple([42])  # Alternative way
not_a_tuple = (42)  # This is just parentheses around an integer!
print(f"\nSingle element tuples:")
print(f"  (42,) → {single_element1} (type: {type(single_element1).__name__})")
print(f"  tuple([42]) → {single_element2} (type: {type(single_element2).__name__})")
print(f"  (42) → {not_a_tuple} (type: {type(not_a_tuple).__name__}) ⚠️ Not a tuple!")

# Tuple from string
string_tuple = tuple("Python")
print(f"\nFrom string: tuple('Python') → {string_tuple}")

# Tuple from range
range_tuple = tuple(range(5))
range_tuple2 = tuple(range(2, 10, 2))
print(f"From range:")
print(f"  tuple(range(5)) → {range_tuple}")
print(f"  tuple(range(2, 10, 2)) → {range_tuple2}")

# Tuple from list
list_data = [1, 2, 3, 4, 5]
tuple_from_list = tuple(list_data)
print(f"From list: tuple({list_data}) → {tuple_from_list}")

# Tuple multiplication
repeated = (0,) * 5
repeated_tuple = ("hello",) * 3
print(f"\nRepeated elements:")
print(f"  (0,) * 5 → {repeated}")
print(f"  ('hello',) * 3 → {repeated_tuple}")

# Tuple packing (without parentheses)
packed_tuple = 1, 2, 3, "hello"
print(f"\nTuple packing: 1, 2, 3, 'hello' → {packed_tuple}")

# Tuple unpacking
a, b, c, d = packed_tuple
print(f"Tuple unpacking: a={a}, b={b}, c={c}, d={d}")

print("\n" + "=" * 50)
print("3️⃣ Tuple Indexing and Slicing")
print("=" * 50)

print("\n📍 Accessing Tuple Elements")
print("-" * 27)

# Sample tuple for indexing
colors = ("red", "green", "blue", "yellow", "orange")
print(f"Sample tuple: {colors}")
print(f"Length: {len(colors)} elements")

# Positive indexing
print(f"\n🔢 Positive Indexing (left to right):")
for i in range(len(colors)):
    print(f"  Index {i}: colors[{i}] = '{colors[i]}'")

# Negative indexing
print(f"\n🔄 Negative Indexing (right to left):")
for i in range(1, len(colors) + 1):
    print(f"  Index -{i}: colors[-{i}] = '{colors[-i]}'")

# Slicing examples
print(f"\n✂️ Tuple Slicing Examples:")
numbers = tuple(range(10))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Numbers: {numbers}")
print(f"numbers[2:7]:     {numbers[2:7]}     # Elements from index 2 to 6")
print(f"numbers[:5]:      {numbers[:5]}      # First 5 elements")
print(f"numbers[5:]:      {numbers[5:]}      # From index 5 to end")
print(f"numbers[:]:       {numbers[:]}       # Entire tuple (copy)")
print(f"numbers[-3:]:     {numbers[-3:]}     # Last 3 elements")
print(f"numbers[:-3]:     {numbers[:-3]}     # All except last 3")

# Advanced slicing with step
print(f"\n⚡ Advanced Slicing with Step:")
alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
print(f"Alphabet: {alphabet}")
print(f"alphabet[::2]:     {alphabet[::2]}     # Every 2nd element")
print(f"alphabet[1::2]:    {alphabet[1::2]}    # Every 2nd starting from index 1")
print(f"alphabet[::-1]:    {alphabet[::-1]}    # Reverse tuple")
print(f"alphabet[::3]:     {alphabet[::3]}     # Every 3rd element")
print(f"alphabet[2:10:2]:  {alphabet[2:10:2]}  # From 2 to 10, step 2")

print("\n" + "=" * 50)
print("4️⃣ Basic Tuple Operations")
print("=" * 50)

print("\n🔧 Essential Tuple Operations")
print("-" * 28)

# Length and membership
sample_tuple = (1, 2, 3, 2, 4, 2, 5)
print(f"Sample tuple: {sample_tuple}")
print(f"len(sample_tuple): {len(sample_tuple)}")
print(f"2 in sample_tuple: {2 in sample_tuple}")
print(f"6 in sample_tuple: {6 in sample_tuple}")
print(f"2 not in sample_tuple: {2 not in sample_tuple}")

# Counting and finding
print(f"\n🔍 Counting and Finding:")
print(f"sample_tuple.count(2): {sample_tuple.count(2)}")
print(f"sample_tuple.index(2): {sample_tuple.index(2)}")  # First occurrence

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(f"\n🔗 Tuple Concatenation:")
print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")
print(f"tuple1 + tuple2: {tuple1 + tuple2}")
print(f"tuple1 * 3: {tuple1 * 3}")

# Min, max, sum (for numeric tuples)
numeric_tuple = (3, 1, 4, 1, 5, 9, 2, 6)
print(f"\n📊 Numeric Operations:")
print(f"Tuple: {numeric_tuple}")
print(f"min(numeric_tuple): {min(numeric_tuple)}")
print(f"max(numeric_tuple): {max(numeric_tuple)}")
print(f"sum(numeric_tuple): {sum(numeric_tuple)}")

# Comparison operations
print(f"\n⚖️ Tuple Comparison:")
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
tuple_c = (1, 2, 3)
print(f"tuple_a: {tuple_a}")
print(f"tuple_b: {tuple_b}")
print(f"tuple_c: {tuple_c}")
print(f"tuple_a == tuple_c: {tuple_a == tuple_c}")
print(f"tuple_a < tuple_b: {tuple_a < tuple_b}")
print(f"tuple_a != tuple_b: {tuple_a != tuple_b}")

print("\n" + "=" * 50)
print("5️⃣ Tuple Methods and Properties")
print("=" * 50)

print("\n🛠️ Built-in Tuple Methods")
print("-" * 25)

# Tuple methods (only count and index!)
demo_tuple = (1, 2, 3, 2, 4, 2, 5, 2)
print(f"Demo tuple: {demo_tuple}")

# count() method
print(f"\n📊 count() method:")
print(f"demo_tuple.count(2): {demo_tuple.count(2)}")
print(f"demo_tuple.count(1): {demo_tuple.count(1)}")
print(f"demo_tuple.count(10): {demo_tuple.count(10)}")

# index() method
print(f"\n🔍 index() method:")
print(f"demo_tuple.index(2): {demo_tuple.index(2)}")  # First occurrence
print(f"demo_tuple.index(4): {demo_tuple.index(4)}")

# index() with start parameter
print(f"demo_tuple.index(2, 2): {demo_tuple.index(2, 2)}")  # Start from index 2
print(f"demo_tuple.index(2, 4): {demo_tuple.index(2, 4)}")  # Start from index 4

# Demonstrating immutability
print(f"\n🔒 Immutability Demonstration:")
original_tuple = (1, 2, 3)
print(f"Original tuple: {original_tuple}")
print(f"ID of original: {id(original_tuple)}")

# These operations create NEW tuples
extended_tuple = original_tuple + (4, 5)
repeated_tuple = original_tuple * 2
print(f"Extended tuple: {extended_tuple}")
print(f"ID of extended: {id(extended_tuple)}")
print(f"Repeated tuple: {repeated_tuple}")
print(f"Original unchanged: {original_tuple}")

print("\n" + "=" * 50)
print("6️⃣ Tuple Unpacking and Packing")
print("=" * 50)

print("\n📦 Tuple Packing and Unpacking")
print("-" * 30)

# Basic unpacking
print("📤 Basic Unpacking:")
point = (3, 4)
x, y = point
print(f"point = {point}")
print(f"x, y = point  # x={x}, y={y}")

# Multiple assignment
print(f"\n🔄 Multiple Assignment:")
name, age, city = "Alice", 25, "New York"
person = (name, age, city)
print(f"person = {person}")

# Swapping variables using tuples
print(f"\n🔀 Variable Swapping:")
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# Extended unpacking (Python 3+)
print(f"\n⭐ Extended Unpacking with *:")
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
first, second, *middle, last = numbers
print(f"numbers = {numbers}")
print(f"first, second, *middle, last = numbers")
print(f"  first={first}, second={second}")
print(f"  middle={middle}")
print(f"  last={last}")

# Unpacking in function calls
def calculate_distance(point1, point2):
    """Calculate distance between two points"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"\n📏 Unpacking in Functions:")
point1 = (0, 0)
point2 = (3, 4)
distance = calculate_distance(point1, point2)
print(f"Distance between {point1} and {point2}: {distance}")

# Returning multiple values
def get_name_age():
    """Return multiple values as tuple"""
    return "Bob", 30

print(f"\n↩️ Returning Multiple Values:")
name, age = get_name_age()
print(f"get_name_age() returned: name='{name}', age={age}")

# Enumerate with tuples
print(f"\n🔢 Enumerate with Tuples:")
colors = ("red", "green", "blue")
print(f"colors = {colors}")
for i, color in enumerate(colors):
    print(f"  Index {i}: {color}")

# Zip with tuples
print(f"\n🤝 Zip with Tuples:")
names = ("Alice", "Bob", "Charlie")
scores = (95, 87, 92)
print(f"names = {names}")
print(f"scores = {scores}")
print("Combined:")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

print("\n" + "=" * 50)
print("7️⃣ Named Tuples")
print("=" * 50)

print("\n🏷️ Named Tuples - Enhanced Tuples")
print("-" * 32)

# Creating named tuple
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', ['name', 'age', 'city'])

print("📋 Creating Named Tuple Classes:")
print("Point = namedtuple('Point', ['x', 'y'])")
print("Person = namedtuple('Person', ['name', 'age', 'city'])")

# Creating instances
p1 = Point(3, 4)
p2 = Point(x=1, y=2)
alice = Person("Alice", 25, "New York")

print(f"\n🏗️ Creating Named Tuple Instances:")
print(f"p1 = Point(3, 4) → {p1}")
print(f"p2 = Point(x=1, y=2) → {p2}")
print(f"alice = Person('Alice', 25, 'New York') → {alice}")

# Accessing elements
print(f"\n🔍 Accessing Named Tuple Elements:")
print(f"p1.x = {p1.x}, p1.y = {p1.y}")
print(f"alice.name = '{alice.name}', alice.age = {alice.age}")
print(f"p1[0] = {p1[0]}, p1[1] = {p1[1]}  # Still works like regular tuple")

# Named tuple methods
print(f"\n🛠️ Named Tuple Methods:")
print(f"alice._asdict(): {alice._asdict()}")
print(f"alice._fields: {alice._fields}")

# _replace method (creates new instance)
alice_older = alice._replace(age=26)
print(f"alice._replace(age=26): {alice_older}")
print(f"Original alice: {alice}")

# Named tuples are still tuples
print(f"\n✅ Named Tuples are Still Tuples:")
print(f"isinstance(p1, tuple): {isinstance(p1, tuple)}")
print(f"len(alice): {len(alice)}")
print(f"alice[0]: '{alice[0]}'")

# Named tuple with defaults (Python 3.7+)
try:
    Student = namedtuple('Student', ['name', 'grade', 'gpa'], defaults=[0.0])
    student1 = Student("John", "A")
    student2 = Student("Jane", "B", 3.5)
    print(f"\n🎓 Named Tuple with Defaults:")
    print(f"student1 = Student('John', 'A') → {student1}")
    print(f"student2 = Student('Jane', 'B', 3.5) → {student2}")
except TypeError:
    print(f"\n⚠️ Named tuple defaults require Python 3.7+")

print("\n" + "=" * 50)
print("8️⃣ Tuple Performance and Memory")
print("=" * 50)

print("\n⚡ Performance Analysis")
print("-" * 21)

# Memory comparison: tuple vs list
print("💾 Memory Usage Comparison:")
tuple_data = tuple(range(1000))
list_data = list(range(1000))

tuple_size = sys.getsizeof(tuple_data)
list_size = sys.getsizeof(list_data)

print(f"Tuple (1000 elements): {tuple_size:,} bytes")
print(f"List (1000 elements):  {list_size:,} bytes")
print(f"Memory difference:     {list_size - tuple_size:,} bytes ({(list_size/tuple_size-1)*100:.1f}% more for list)")

# Speed comparison: creation
print(f"\n⏱️ Creation Speed Comparison:")

def create_tuple(n=10000):
    return tuple(range(n))

def create_list(n=10000):
    return list(range(n))

n = 10000
tuple_time = timeit.timeit(lambda: create_tuple(n), number=1000)
list_time = timeit.timeit(lambda: create_list(n), number=1000)

print(f"Creating {n:,} elements (1000 iterations):")
print(f"  Tuple creation: {tuple_time:.6f} seconds")
print(f"  List creation:  {list_time:.6f} seconds")
print(f"  Speedup: {list_time/tuple_time:.2f}x faster for tuples")

# Access speed comparison
print(f"\n🏃 Element Access Speed:")
test_tuple = tuple(range(10000))
test_list = list(range(10000))

def access_tuple():
    return test_tuple[5000]

def access_list():
    return test_list[5000]

tuple_access_time = timeit.timeit(access_tuple, number=1000000)
list_access_time = timeit.timeit(access_list, number=1000000)

print(f"Accessing element 5000 (1M iterations):")
print(f"  Tuple access: {tuple_access_time:.6f} seconds")
print(f"  List access:  {list_access_time:.6f} seconds")

# Iteration speed
print(f"\n🔄 Iteration Speed:")

def iterate_tuple():
    total = 0
    for item in test_tuple:
        total += item
    return total

def iterate_list():
    total = 0
    for item in test_list:
        total += item
    return total

tuple_iter_time = timeit.timeit(iterate_tuple, number=100)
list_iter_time = timeit.timeit(iterate_list, number=100)

print(f"Iterating through 10,000 elements (100 iterations):")
print(f"  Tuple iteration: {tuple_iter_time:.6f} seconds")
print(f"  List iteration:  {list_iter_time:.6f} seconds")

print("\n" + "=" * 50)
print("9️⃣ Tuple as Dictionary Keys")
print("=" * 50)

print("\n🗝️ Using Tuples as Dictionary Keys")
print("-" * 34)

# Coordinate system example
print("🗺️ Coordinate System Example:")
chess_board = {}

# Setting up a chess board using tuple coordinates
pieces = {
    (0, 0): "Rook", (0, 7): "Rook",
    (0, 1): "Knight", (0, 6): "Knight",
    (0, 2): "Bishop", (0, 5): "Bishop",
    (0, 3): "Queen", (0, 4): "King",
}

print("Chess pieces (row, col): piece")
for position, piece in pieces.items():
    print(f"  {position}: {piece}")

# 3D coordinates
print(f"\n🌐 3D Point Storage:")
point_data = {
    (0, 0, 0): "Origin",
    (1, 0, 0): "X-axis unit",
    (0, 1, 0): "Y-axis unit",
    (0, 0, 1): "Z-axis unit",
    (1, 1, 1): "Corner point"
}

for coords, description in point_data.items():
    x, y, z = coords
    print(f"  Point({x}, {y}, {z}): {description}")

# Database-like records
print(f"\n🗄️ Database Records:")
student_grades = {
    ("Alice", "Math"): 95,
    ("Alice", "Science"): 87,
    ("Bob", "Math"): 78,
    ("Bob", "Science"): 92,
    ("Charlie", "Math"): 85,
    ("Charlie", "Science"): 90,
}

print("Student grades (name, subject): grade")
for (name, subject), grade in student_grades.items():
    print(f"  {name}, {subject}: {grade}")

# Why lists can't be keys
print(f"\n❌ Why Lists Cannot Be Dictionary Keys:")
print("Lists are mutable and therefore unhashable")
try:
    bad_dict = {[1, 2]: "value"}  # This will raise TypeError
except TypeError as e:
    print(f"Error with list as key: {e}")

# Tuples containing mutable objects also can't be keys
print(f"\nTuples with mutable objects also can't be keys:")
try:
    bad_dict = {(1, [2, 3]): "value"}  # This will also raise TypeError
except TypeError as e:
    print(f"Error with tuple containing list: {e}")

# Cache/memoization example
print(f"\n💾 Memoization with Tuple Keys:")

def fibonacci_memo():
    cache = {}
    
    def fib(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    
    return fib

# Function with multiple parameters
def distance_memo():
    cache = {}
    
    def distance(x1, y1, x2, y2):
        key = (x1, y1, x2, y2)
        if key in cache:
            return cache[key]
        
        result = ((x2-x1)**2 + (y2-y1)**2)**0.5
        cache[key] = result
        return result
    
    return distance

fib = fibonacci_memo()
dist = distance_memo()

print(f"fibonacci_memo(10): {fib(10)}")
print(f"distance(0, 0, 3, 4): {dist(0, 0, 3, 4)}")
print(f"distance(0, 0, 3, 4): {dist(0, 0, 3, 4)} # Cached result")

print("\n" + "=" * 50)
print("🔟 Advanced Tuple Techniques")
print("=" * 50)

print("\n🎯 Advanced Tuple Operations")
print("-" * 27)

# Nested tuple processing
print("🎭 Nested Tuple Processing:")
nested_data = (
    ("Alice", 25, "Engineer"),
    ("Bob", 30, "Designer"),
    ("Charlie", 35, "Manager")
)

print("Original nested tuple:")
for person in nested_data:
    name, age, job = person
    print(f"  {name}: {age} years old, {job}")

# Tuple comprehensions (generator expressions)
print(f"\n⚡ Generator Expressions (Tuple-like):")
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
squares_gen = (x**2 for x in numbers if x % 2 == 0)
squares_tuple = tuple(squares_gen)
print(f"Even squares: {squares_tuple}")

# Sorting tuples
print(f"\n📏 Sorting Tuples:")
students = [
    ("Alice", 85),
    ("Bob", 90),
    ("Charlie", 78),
    ("Diana", 95)
]

# Sort by name (first element)
by_name = sorted(students)
print(f"Sorted by name: {by_name}")

# Sort by grade (second element)
by_grade = sorted(students, key=lambda x: x[1])
print(f"Sorted by grade: {by_grade}")

# Sort by grade descending
by_grade_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by grade (desc): {by_grade_desc}")

# Tuple methods with custom functions
print(f"\n🔧 Advanced Tuple Processing:")

def process_records(records):
    """Process a tuple of records"""
    # Find highest grade
    best_student = max(records, key=lambda x: x[1])
    
    # Calculate average grade
    total_grade = sum(student[1] for student in records)
    avg_grade = total_grade / len(records)
    
    # Count students above average
    above_avg = sum(1 for student in records if student[1] > avg_grade)
    
    return best_student, avg_grade, above_avg

best, avg, above_count = process_records(students)
print(f"Best student: {best[0]} with grade {best[1]}")
print(f"Average grade: {avg:.1f}")
print(f"Students above average: {above_count}")

# Matrix operations with tuples
print(f"\n🔢 Matrix Operations with Tuples:")
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Transpose matrix
transposed = tuple(zip(*matrix))
print(f"Transposed:")
for row in transposed:
    print(f"  {row}")

# Flatten matrix
flattened = tuple(item for row in matrix for item in row)
print(f"Flattened: {flattened}")

print("\n" + "=" * 50)
print("1️⃣1️⃣ Real-World Applications")
print("=" * 50)

print("\n🛠️ Practical Tuple Applications")
print("-" * 30)

# RGB Color system
print("🎨 RGB Color System:")
class Color:
    def __init__(self, rgb_tuple):
        if len(rgb_tuple) != 3:
            raise ValueError("RGB tuple must have exactly 3 values")
        if not all(0 <= val <= 255 for val in rgb_tuple):
            raise ValueError("RGB values must be between 0 and 255")
        self.rgb = rgb_tuple
    
    def __str__(self):
        return f"Color{self.rgb}"
    
    def to_hex(self):
        return "#{:02x}{:02x}{:02x}".format(*self.rgb)
    
    def brightness(self):
        return sum(self.rgb) / 3

# Define some colors
red = Color((255, 0, 0))
green = Color((0, 255, 0))
blue = Color((0, 0, 255))
white = Color((255, 255, 255))

colors = [red, green, blue, white]
print("Color analysis:")
for color in colors:
    print(f"  {color}: Hex={color.to_hex()}, Brightness={color.brightness():.1f}")

# Geographic coordinates
print(f"\n🌍 Geographic Coordinate System:")
cities = {
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Tokyo": (35.6762, 139.6503),
    "Sydney": (-33.8688, 151.2093),
    "Cairo": (30.0444, 31.2357)
}

def calculate_distance(coord1, coord2):
    """Calculate approximate distance between two coordinates"""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Simplified distance calculation
    lat_diff = abs(lat1 - lat2)
    lon_diff = abs(lon1 - lon2)
    
    # Very rough approximation in km
    return ((lat_diff * 111)**2 + (lon_diff * 111)**2)**0.5

print("City coordinates:")
for city, coords in cities.items():
    lat, lon = coords
    print(f"  {city}: ({lat:.4f}, {lon:.4f})")

print(f"\nDistances from New York:")
ny_coords = cities["New York"]
for city, coords in cities.items():
    if city != "New York":
        distance = calculate_distance(ny_coords, coords)
        print(f"  to {city}: {distance:.0f} km")

# Database record system
print(f"\n🗄️ Database Record System:")
Employee = namedtuple('Employee', ['id', 'name', 'department', 'salary'])

employees = [
    Employee(1, "Alice Johnson", "Engineering", 75000),
    Employee(2, "Bob Smith", "Marketing", 65000),
    Employee(3, "Charlie Brown", "Engineering", 80000),
    Employee(4, "Diana Wilson", "HR", 60000),
    Employee(5, "Eve Davis", "Engineering", 72000),
]

def analyze_employees(employee_list):
    """Analyze employee data using tuple operations"""
    # Group by department
    by_department = {}
    for emp in employee_list:
        if emp.department not in by_department:
            by_department[emp.department] = []
        by_department[emp.department].append(emp)
    
    # Calculate statistics
    total_salary = sum(emp.salary for emp in employee_list)
    avg_salary = total_salary / len(employee_list)
    
    # Find highest paid employee
    highest_paid = max(employee_list, key=lambda emp: emp.salary)
    
    return by_department, avg_salary, highest_paid

departments, avg_sal, top_emp = analyze_employees(employees)

print("Employee Analysis:")
print(f"  Average salary: ${avg_sal:,.0f}")
print(f"  Highest paid: {top_emp.name} (${top_emp.salary:,})")
print("\nBy Department:")
for dept, emp_list in departments.items():
    dept_avg = sum(emp.salary for emp in emp_list) / len(emp_list)
    print(f"  {dept}: {len(emp_list)} employees, avg salary ${dept_avg:,.0f}")

print("\n" + "=" * 50)
print("1️⃣2️⃣ Best Practices")
print("=" * 50)

print("\n💡 Tuple Best Practices Guide")
print("-" * 27)

print("""
🎯 When to Use Tuples:
✅ Fixed collections that won't change (coordinates, RGB values)
✅ Multiple return values from functions
✅ Dictionary keys (when you need composite keys)
✅ Configuration settings
✅ Database records
✅ When you need immutability for safety

🎯 When NOT to Use Tuples:
❌ When you need to modify the collection after creation
❌ When you need methods like append, remove, sort
❌ When the collection size varies significantly
❌ When you need only one type of operation repeatedly

🔒 Immutability Best Practices:
✅ Use tuples to prevent accidental modifications
✅ Return tuples from functions to ensure data integrity
✅ Use named tuples for better readability
✅ Remember: immutability is shallow (nested mutable objects can change)

📝 Code Quality Best Practices:
✅ Use meaningful names for tuple elements
✅ Consider named tuples for complex data structures
✅ Document tuple structure in function docstrings
✅ Use tuple unpacking for cleaner code
✅ Validate tuple contents when accepting from external sources

⚡ Performance Best Practices:
✅ Use tuples for read-heavy operations
✅ Prefer tuples over lists for dictionary keys
✅ Use tuples for function signatures that won't change
✅ Consider memory efficiency: tuples use less memory than lists
✅ Use tuple packing/unpacking instead of indexing when possible
""")

print("\n" + "=" * 50)
print("1️⃣3️⃣ Common Pitfalls and Solutions")
print("=" * 50)

print("\n⚠️ Common Tuple Pitfalls")
print("-" * 23)

# Pitfall 1: Single element tuple syntax
print("🚨 Pitfall 1: Single Element Tuple Syntax")
print("❌ Wrong:")
not_tuple = (42)  # This is just an integer with parentheses
print(f"  (42) → {not_tuple}, type: {type(not_tuple).__name__}")

print("✅ Correct:")
single_tuple = (42,)  # Note the comma!
print(f"  (42,) → {single_tuple}, type: {type(single_tuple).__name__}")

# Pitfall 2: Modifying nested mutable objects
print(f"\n🚨 Pitfall 2: Nested Mutable Objects")
print("❌ Problem:")
tuple_with_list = (1, 2, [3, 4])
print(f"  Original: {tuple_with_list}")
tuple_with_list[2].append(5)  # This modifies the nested list!
print(f"  After modifying nested list: {tuple_with_list}")

print("✅ Solution: Use tuples all the way down")
immutable_nested = (1, 2, (3, 4))
print(f"  Fully immutable: {immutable_nested}")

# Pitfall 3: Trying to use list methods
print(f"\n🚨 Pitfall 3: Trying to Use List Methods")
demo_tuple = (1, 2, 3, 4, 5)
print(f"Demo tuple: {demo_tuple}")

print("❌ These don't work on tuples:")
methods_that_dont_work = ['append', 'remove', 'pop', 'sort', 'reverse', 'extend']
for method in methods_that_dont_work:
    if hasattr(demo_tuple, method):
        print(f"  {method}(): exists but may not work as expected")
    else:
        print(f"  {method}(): doesn't exist")

print("✅ Tuple alternatives:")
print(f"  Add element: {demo_tuple} + (6,) = {demo_tuple + (6,)}")
print(f"  Remove element: tuple(x for x in {demo_tuple} if x != 3) = {tuple(x for x in demo_tuple if x != 3)}")
print(f"  Sort: sorted({demo_tuple}) = {sorted(demo_tuple)} (returns list)")
print(f"  Reverse: {demo_tuple}[::-1] = {demo_tuple[::-1]}")

# Pitfall 4: Expecting mutability
print(f"\n🚨 Pitfall 4: Expecting Mutability")
print("❌ This will raise TypeError:")
try:
    test_tuple = (1, 2, 3)
    test_tuple[1] = 10
except TypeError as e:
    print(f"  {e}")

print("✅ Create new tuple instead:")
old_tuple = (1, 2, 3)
new_tuple = old_tuple[:1] + (10,) + old_tuple[2:]
print(f"  {old_tuple} → {new_tuple}")

print("\n" + "=" * 50)
print("1️⃣4️⃣ Practice Exercises")
print("=" * 50)

print("\n🏋️ Tuple Practice Challenges")
print("-" * 27)

print("""
Challenge 1: Create a function that finds the distance between two 3D points
Challenge 2: Implement a grade book using tuples as keys
Challenge 3: Create a function that rotates RGB colors
Challenge 4: Build a simple inventory system using named tuples
Challenge 5: Create a tuple-based matrix calculator
""")

# Challenge 1: 3D Distance Calculator
def distance_3d(point1, point2):
    """Calculate distance between two 3D points represented as tuples"""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

print("Challenge 1 - 3D Distance Calculator:")
p1 = (0, 0, 0)
p2 = (1, 1, 1)
p3 = (3, 4, 5)
print(f"Distance between {p1} and {p2}: {distance_3d(p1, p2):.2f}")
print(f"Distance between {p1} and {p3}: {distance_3d(p1, p3):.2f}")
print(f"Distance between {p2} and {p3}: {distance_3d(p2, p3):.2f}")

# Challenge 2: Grade Book System
class GradeBook:
    """Grade book using tuple keys (student, subject)"""
    
    def __init__(self):
        self.grades = {}
    
    def add_grade(self, student, subject, grade):
        """Add a grade for a student in a subject"""
        key = (student, subject)
        if key not in self.grades:
            self.grades[key] = []
        self.grades[key].append(grade)
    
    def get_student_average(self, student):
        """Get average grade for a student across all subjects"""
        student_grades = []
        for (s, subject), grades in self.grades.items():
            if s == student:
                student_grades.extend(grades)
        
        return sum(student_grades) / len(student_grades) if student_grades else 0
    
    def get_subject_average(self, subject):
        """Get average grade for a subject across all students"""
        subject_grades = []
        for (student, s), grades in self.grades.items():
            if s == subject:
                subject_grades.extend(grades)
        
        return sum(subject_grades) / len(subject_grades) if subject_grades else 0
    
    def get_student_grades(self, student):
        """Get all grades for a student"""
        result = {}
        for (s, subject), grades in self.grades.items():
            if s == student:
                result[subject] = grades
        return result

print(f"\nChallenge 2 - Grade Book System:")
gradebook = GradeBook()

# Add some grades
gradebook.add_grade("Alice", "Math", 95)
gradebook.add_grade("Alice", "Science", 87)
gradebook.add_grade("Bob", "Math", 78)
gradebook.add_grade("Bob", "Science", 92)
gradebook.add_grade("Alice", "Math", 88)

print("Grade book data:")
print(f"  Alice's Math grades: {gradebook.get_student_grades('Alice')['Math']}")
print(f"  Alice's average: {gradebook.get_student_average('Alice'):.1f}")
print(f"  Math average: {gradebook.get_subject_average('Math'):.1f}")

# Challenge 3: RGB Color Rotator
def rotate_rgb(rgb_tuple, steps=1):
    """Rotate RGB values by steps positions"""
    r, g, b = rgb_tuple
    colors = [r, g, b]
    
    # Rotate the list
    steps = steps % 3  # Handle steps > 3
    rotated = colors[steps:] + colors[:steps]
    
    return tuple(rotated)

print(f"\nChallenge 3 - RGB Color Rotator:")
original_color = (255, 128, 64)
print(f"Original RGB: {original_color}")
for i in range(1, 4):
    rotated = rotate_rgb(original_color, i)
    print(f"Rotated by {i}: {rotated}")

# Challenge 4: Inventory System
Item = namedtuple('Item', ['name', 'category', 'price', 'quantity'])

class Inventory:
    """Simple inventory system using named tuples"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, name, category, price, quantity):
        """Add an item to inventory"""
        item = Item(name, category, price, quantity)
        self.items.append(item)
    
    def find_item(self, name):
        """Find an item by name"""
        for item in self.items:
            if item.name == name:
                return item
        return None
    
    def get_by_category(self, category):
        """Get all items in a category"""
        return [item for item in self.items if item.category == category]
    
    def total_value(self):
        """Calculate total inventory value"""
        return sum(item.price * item.quantity for item in self.items)
    
    def low_stock(self, threshold=5):
        """Find items with low stock"""
        return [item for item in self.items if item.quantity <= threshold]

print(f"\nChallenge 4 - Inventory System:")
inventory = Inventory()
inventory.add_item("Laptop", "Electronics", 999.99, 10)
inventory.add_item("Mouse", "Electronics", 29.99, 25)
inventory.add_item("Desk", "Furniture", 199.99, 3)
inventory.add_item("Chair", "Furniture", 149.99, 2)

print(f"Total inventory value: ${inventory.total_value():,.2f}")
print("Electronics items:")
for item in inventory.get_by_category("Electronics"):
    print(f"  {item.name}: ${item.price}, qty: {item.quantity}")

print("Low stock items (≤ 5):")
for item in inventory.low_stock():
    print(f"  {item.name}: only {item.quantity} left")

# Challenge 5: Matrix Calculator
class TupleMatrix:
    """Matrix operations using tuples"""
    
    def __init__(self, matrix_tuple):
        """Initialize matrix from tuple of tuples"""
        self.matrix = matrix_tuple
        self.rows = len(matrix_tuple)
        self.cols = len(matrix_tuple[0]) if matrix_tuple else 0
    
    def __str__(self):
        """String representation of matrix"""
        result = "Matrix:\n"
        for row in self.matrix:
            result += "  " + str(row) + "\n"
        return result.strip()
    
    def transpose(self):
        """Return transposed matrix"""
        transposed = tuple(zip(*self.matrix))
        return TupleMatrix(transposed)
    
    def add(self, other):
        """Add two matrices"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions")
        
        result = tuple(
            tuple(self.matrix[i][j] + other.matrix[i][j] 
                  for j in range(self.cols))
            for i in range(self.rows)
        )
        return TupleMatrix(result)
    
    def multiply_scalar(self, scalar):
        """Multiply matrix by scalar"""
        result = tuple(
            tuple(self.matrix[i][j] * scalar 
                  for j in range(self.cols))
            for i in range(self.rows)
        )
        return TupleMatrix(result)

print(f"\nChallenge 5 - Matrix Calculator:")
matrix1 = TupleMatrix(((1, 2, 3), (4, 5, 6)))
matrix2 = TupleMatrix(((1, 1, 1), (2, 2, 2)))

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

print("\nMatrix 1 transposed:")
print(matrix1.transpose())

print("\nMatrix 1 + Matrix 2:")
print(matrix1.add(matrix2))

print("\nMatrix 1 * 3:")
print(matrix1.multiply_scalar(3))

print("\n" + "=" * 50)
print("1️⃣5️⃣ Performance Optimization Tips")
print("=" * 50)

print("\n⚡ Tuple Performance Optimization")
print("-" * 32)

# Memory efficiency demonstration
print("💾 Memory Efficiency Tips:")

# Tip 1: Use tuples for constant data
def demonstrate_memory_efficiency():
    """Demonstrate memory efficiency of tuples vs lists"""
    
    # Large datasets
    size = 10000
    tuple_data = tuple(range(size))
    list_data = list(range(size))
    
    tuple_size = sys.getsizeof(tuple_data)
    list_size = sys.getsizeof(list_data)
    
    print(f"  Data size: {size:,} elements")
    print(f"  Tuple memory: {tuple_size:,} bytes")
    print(f"  List memory: {list_size:,} bytes")
    print(f"  Memory saved: {list_size - tuple_size:,} bytes ({((list_size - tuple_size) / list_size * 100):.1f}%)")

demonstrate_memory_efficiency()

# Speed optimization tips
print(f"\n🏃 Speed Optimization Tips:")

# Tip 1: Tuple unpacking vs indexing
def compare_access_methods():
    """Compare tuple unpacking vs indexing"""
    coordinates = [(i, i+1, i+2) for i in range(1000)]
    
    def using_indexing():
        total = 0
        for coord in coordinates:
            total += coord[0] + coord[1] + coord[2]
        return total
    
    def using_unpacking():
        total = 0
        for x, y, z in coordinates:
            total += x + y + z
        return total
    
    index_time = timeit.timeit(using_indexing, number=1000)
    unpack_time = timeit.timeit(using_unpacking, number=1000)
    
    print(f"  Indexing method: {index_time:.6f} seconds")
    print(f"  Unpacking method: {unpack_time:.6f} seconds")
    if index_time > unpack_time:
        print(f"  Unpacking is {index_time/unpack_time:.1f}x faster")
    else:
        print(f"  Indexing is {unpack_time/index_time:.1f}x faster")

compare_access_methods()

# Tip 2: Named tuple vs regular class
print(f"\n🏷️ Named Tuple vs Class Performance:")

class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

PointTuple = namedtuple('Point', ['x', 'y'])

def create_regular_points(n=10000):
    return [RegularPoint(i, i+1) for i in range(n)]

def create_named_tuples(n=10000):
    return [PointTuple(i, i+1) for i in range(n)]

n = 10000
regular_time = timeit.timeit(lambda: create_regular_points(n), number=100)
tuple_time = timeit.timeit(lambda: create_named_tuples(n), number=100)

print(f"Creating {n:,} objects (100 iterations):")
print(f"  Regular class: {regular_time:.6f} seconds")
print(f"  Named tuple: {tuple_time:.6f} seconds")
if regular_time > tuple_time:
    print(f"  Named tuples are {regular_time/tuple_time:.1f}x faster")

print("\n" + "=" * 70)
print("🎉 Congratulations! You've completed the Python Tuples Guide!")
print("🏆 You now have comprehensive knowledge of tuple manipulation!")
print("=" * 70)

print(f"""
🎯 What You've Mastered:

✅ Tuple creation and initialization methods
✅ Understanding immutability and its implications
✅ Indexing, slicing, and element access
✅ Tuple packing and unpacking techniques
✅ Named tuples for structured data
✅ Using tuples as dictionary keys
✅ Performance advantages and memory efficiency
✅ Advanced tuple operations and algorithms
✅ Real-world applications and use cases
✅ Best practices and common pitfalls
✅ Performance optimization techniques

🚀 Next Steps:
1. Practice with tuple-based algorithms
2. Explore more advanced named tuple features
3. Learn about other immutable data structures
4. Study functional programming concepts
5. Build projects using tuple-based designs

💡 Key Takeaways:
- Tuples are immutable and perfect for fixed data
- Use tuples for coordinates, settings, and return values
- Named tuples provide structure while maintaining tuple benefits
- Tuples are hashable and can be dictionary keys
- Memory efficient and faster for read-only operations
- Immutability provides safety in concurrent programming
- Tuple unpacking makes code more readable and Pythonic

🔄 Tuple vs List Quick Decision Guide:
Use Tuples when:
- Data won't change after creation
- You need hashable keys for dictionaries
- Memory efficiency is important
- You're returning multiple values from functions
- You want to prevent accidental modifications

Use Lists when:
- You need to modify the collection
- Collection size varies significantly
- You need list-specific methods (append, remove, etc.)
- Building the collection incrementally

Keep practicing and building with tuples! 🐍✨
""")

# Quick reference card
print("""
📦 Tuples Quick Reference:

Creating:
()                        # Empty tuple
(1, 2, 3)                # Tuple with elements
(42,)                    # Single element (note comma!)
tuple([1, 2, 3])         # From list

Accessing:
t[0]                     # First element
t[-1]                    # Last element
t[1:3]                   # Slicing

Operations:
len(t)                   # Length
x in t                   # Membership
t1 + t2                  # Concatenation
t * 3                    # Repetition

Methods:
t.count(x)               # Count occurrences
t.index(x)               # Find index

Unpacking:
x, y = (1, 2)           # Basic unpacking
a, *b, c = (1,2,3,4,5)  # Extended unpacking

Named Tuples:
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x, p.y                # Attribute access
p._asdict()             # Convert to dict

As Dict Keys:
d = {(1, 2): 'value'}   # Tuple as key
d[(1, 2)]               # Access by tuple key
""")

print("\n" + "=" * 70)
print("📚 Happy Coding with Python Tuples! 🐍")
print("=" * 70)