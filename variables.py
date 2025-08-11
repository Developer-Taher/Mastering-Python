# =====================================
# Complete Guide to Python Variables
# Comprehensive Tutorial and Reference
# =====================================

"""
What are Variables?
Variables are named locations in memory that store data values.
They act as containers that hold information that can be used and manipulated in your program.
Think of them as labeled boxes where you can store different types of data.
"""

import keyword
import builtins
import sys
import gc

print("=" * 70)
print("🐍 Complete Guide to Python Variables")
print("=" * 70)

print("\n" + "=" * 50)
print("1️⃣ Introduction to Variables")
print("=" * 50)

print("""
🎯 What are Variables?
✅ Named storage locations in memory
✅ Hold data values that can change
✅ Act as references to objects in Python
✅ Everything in Python is an object

📝 Basic Syntax:
variable_name = value
""")

print("\n" + "=" * 50)
print("2️⃣ Variable Assignment Syntax")
print("=" * 50)

print("\n📋 Basic Assignment Patterns")
print("-" * 30)

# Basic value assignment
print("# Basic Values:")
x = 5                    # Integer
name = "Python"          # String
price = 99.99           # Float
is_active = True        # Boolean

print(f"x = {x} (type: {type(x).__name__})")
print(f"name = '{name}' (type: {type(name).__name__})")
print(f"price = {price} (type: {type(price).__name__})")
print(f"is_active = {is_active} (type: {type(is_active).__name__})")

# Expression assignment
print(f"\n# Expression Assignment:")
result = 5 + 3          # Mathematical expression
full_name = "John" + " " + "Doe"  # String concatenation
area = 3.14 * 5 * 5     # Circle area calculation

print(f"result = 5 + 3 = {result}")
print(f"full_name = 'John' + ' ' + 'Doe' = '{full_name}'")
print(f"area = 3.14 * 5 * 5 = {area}")

print("\n" + "=" * 50)
print("3️⃣ Data Structure Assignment")
print("=" * 50)

# List assignment
print("\n📋 List Assignment:")
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]

print(f"numbers = {numbers}")
print(f"mixed_list = {mixed_list}")
print(f"nested_list = {nested_list}")

# Dictionary assignment
print(f"\n📚 Dictionary Assignment:")
person = {"name": "John", "age": 30, "city": "New York"}
grades = {"math": 95, "science": 88, "english": 92}
complex_dict = {
    "user": {"name": "Alice", "email": "alice@email.com"},
    "settings": {"theme": "dark", "notifications": True}
}

print(f"person = {person}")
print(f"grades = {grades}")
print(f"complex_dict = {complex_dict}")

# Set assignment
print(f"\n🎯 Set Assignment:")
unique_numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}

print(f"unique_numbers = {unique_numbers}")
print(f"fruits = {fruits}")

# Tuple assignment
print(f"\n📦 Tuple Assignment:")
coordinates = (10, 20)
person_info = ("John", 25, "Engineer")
nested_tuple = ((1, 2), (3, 4))

print(f"coordinates = {coordinates}")
print(f"person_info = {person_info}")
print(f"nested_tuple = {nested_tuple}")

# Special values
print(f"\n🔳 Special Values:")
empty_value = None
nothing = None
default_setting = None

print(f"empty_value = {empty_value}")
print(f"nothing = {nothing}")
print(f"default_setting = {default_setting}")

print("\n" + "=" * 50)
print("4️⃣ Advanced Assignment Types")
print("=" * 50)

# Function assignment
print("\n🔧 Function Assignment:")
my_function = len  # Built-in function
string_upper = str.upper  # Method reference

print(f"my_function = len → my_function([1,2,3]) = {my_function([1,2,3])}")
print(f"string_upper = str.upper → string_upper('hello') = '{string_upper('hello')}'")

# Lambda function assignment
print(f"\n⚡ Lambda Function Assignment:")
square = lambda x: x * x
add_numbers = lambda a, b: a + b
is_even = lambda n: n % 2 == 0

print(f"square = lambda x: x * x → square(5) = {square(5)}")
print(f"add_numbers = lambda a, b: a + b → add_numbers(3, 4) = {add_numbers(3, 4)}")
print(f"is_even = lambda n: n % 2 == 0 → is_even(8) = {is_even(8)}")

# Class assignment
print(f"\n🏗️ Class Assignment:")
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

PersonClass = Person  # Class reference
john = Person("John")  # Object instance

print(f"PersonClass = Person (class reference)")
print(f"john = Person('John') → john.greet() = '{john.greet()}'")

# Module assignment
print(f"\n📦 Module Assignment:")
import math
import datetime as dt

math_module = math
date_module = dt

print(f"math_module = math → math_module.pi = {math_module.pi}")
print(f"date_module = datetime → date_module.datetime.now() = {date_module.datetime.now()}")

print("\n" + "=" * 50)
print("5️⃣ Multiple Assignment Techniques")
print("=" * 50)

# Multiple assignment
print("\n🔄 Multiple Assignment:")
a, b, c = 1, 2, 3
x = y = z = 10
first, second, third = "Python", "Java", "JavaScript"

print(f"a, b, c = 1, 2, 3 → a={a}, b={b}, c={c}")
print(f"x = y = z = 10 → x={x}, y={y}, z={z}")
print(f"first, second, third = languages → first='{first}', second='{second}', third='{third}'")

# Unpacking assignment
print(f"\n📤 Unpacking Assignment:")
numbers_tuple = (100, 200, 300)
num1, num2, num3 = numbers_tuple

point = {"x": 15, "y": 25}
coordinates_list = [1, 2, 3, 4, 5]
first_two, *rest = coordinates_list

print(f"num1, num2, num3 = (100, 200, 300) → num1={num1}, num2={num2}, num3={num3}")
print(f"first_two, *rest = [1,2,3,4,5] → first_two={first_two}, rest={rest}")

# Swapping variables
print(f"\n🔀 Variable Swapping:")
var1 = "Hello"
var2 = "World"
print(f"Before swap: var1='{var1}', var2='{var2}'")

var1, var2 = var2, var1  # Python swap
print(f"After swap: var1='{var1}', var2='{var2}'")

print("\n" + "=" * 50)
print("6️⃣ Variable Naming Conventions")
print("=" * 50)

print("\n📝 Naming Convention Examples")
print("-" * 30)

# Different naming styles
normal_variable = 'snake_case (recommended)'
camelCaseVariable = 'camelCase (not recommended in Python)'
PascalCaseVariable = 'PascalCase (for classes)'
CONSTANT_VARIABLE = 'UPPER_CASE (for constants)'

print(f"snake_case: {normal_variable}")
print(f"camelCase: {camelCaseVariable}")
print(f"PascalCase: {PascalCaseVariable}")
print(f"UPPER_CASE: {CONSTANT_VARIABLE}")

# Good variable names
print(f"\n✅ Good Variable Names:")
user_name = "john_doe"
total_price = 299.99
is_authenticated = True
user_list = ["alice", "bob", "charlie"]
max_attempts = 3

good_examples = [
    ("user_name", user_name),
    ("total_price", total_price),
    ("is_authenticated", is_authenticated),
    ("user_list", user_list),
    ("max_attempts", max_attempts)
]

for name, value in good_examples:
    print(f"  {name} = {value}")

# Bad variable names (examples only - not recommended)
print(f"\n❌ Bad Variable Names (avoid these):")
bad_examples = [
    "x",  # Too short, not descriptive
    "data",  # Too generic
    "temp",  # Unclear purpose
    "thing",  # Not descriptive
    "var1",  # Generic numbering
]

for bad_name in bad_examples:
    print(f"  {bad_name} - Too vague or unclear")

print("\n" + "=" * 50)
print("7️⃣ Variable Naming Rules")
print("=" * 50)

print("\n📏 Naming Rules and Restrictions")
print("-" * 32)

print("✅ Valid Variable Names:")
valid_names = [
    "variable_name",
    "myVariable",
    "_private_var",
    "__special_var__",
    "name123",
    "student_age",
    "PI_VALUE",
    "is_valid"
]

for name in valid_names:
    print(f"  ✓ {name}")

print(f"\n❌ Invalid Variable Names:")
invalid_examples = [
    ("123variable", "Cannot start with number"),
    ("my-variable", "Cannot contain hyphens"),
    ("my variable", "Cannot contain spaces"),
    ("@variable", "Cannot contain @ symbol"),
    ("if", "Cannot use reserved keywords"),
    ("class", "Cannot use reserved keywords"),
    ("def", "Cannot use reserved keywords")
]

for invalid_name, reason in invalid_examples:
    print(f"  ✗ {invalid_name} - {reason}")

# Demonstrate reserved keywords
print(f"\n🚫 Python Reserved Keywords:")
python_keywords = keyword.kwlist
print(f"Total keywords: {len(python_keywords)}")
print("Keywords:", ", ".join(python_keywords))

# Built-in function names to avoid
print(f"\n⚠️ Built-in Names to Avoid:")
builtin_names = [name for name in dir(builtins) if not name.startswith('_')]
print(f"Examples: {', '.join(builtin_names[:10])}... (and {len(builtin_names)-10} more)")

print("\n" + "=" * 50)
print("8️⃣ Variable Scope and Lifetime")
print("=" * 50)

print("\n🔍 Variable Scope Examples")
print("-" * 27)

# Global variable
global_var = "I'm a global variable"

def scope_demo():
    # Modifying global variable (declare global first)
    global global_var
    
    # Local variable
    local_var = "I'm a local variable"
    
    # Accessing global variable
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")
    
    # Modifying global variable
    global_var = "Modified global variable"

print(f"Before function call - Global: {global_var}")
scope_demo()
print(f"After function call - Global: {global_var}")

# Nested scope example
def outer_function():
    outer_var = "Outer variable"
    
    def inner_function():
        inner_var = "Inner variable"
        print(f"Inner function sees: {outer_var}, {inner_var}")
    
    inner_function()
    print(f"Outer function sees: {outer_var}")
    # print(inner_var)  # This would cause NameError

print(f"\n🏗️ Nested Scope Demo:")
outer_function()

print("\n" + "=" * 50)
print("9️⃣ Variable Memory Management")
print("=" * 50)

print("\n💾 Memory Management Examples")
print("-" * 28)

# Variable identity and memory
a = [1, 2, 3]
b = a  # Same object reference
c = [1, 2, 3]  # Different object

print(f"a = [1, 2, 3]")
print(f"b = a (reference)")
print(f"c = [1, 2, 3] (new object)")
print(f"")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")
print(f"")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"a == c: {a == c}")

# Mutable vs Immutable
print(f"\n🔄 Mutable vs Immutable:")
# Immutable example
x = 10
print(f"x = {x}, id(x) = {id(x)}")
x = 20
print(f"x = {x}, id(x) = {id(x)} (new object created)")

# Mutable example
my_list = [1, 2, 3]
print(f"my_list = {my_list}, id(my_list) = {id(my_list)}")
my_list.append(4)
print(f"my_list = {my_list}, id(my_list) = {id(my_list)} (same object modified)")

# Memory usage
print(f"\n📊 Memory Usage:")
small_int = 42
large_list = list(range(1000))
small_string = "hello"
large_string = "x" * 1000

memory_examples = [
    ("small_int", small_int),
    ("large_list", large_list),
    ("small_string", small_string),
    ("large_string", large_string)
]

for name, obj in memory_examples:
    print(f"{name}: {sys.getsizeof(obj)} bytes")

print("\n" + "=" * 50)
print("🔟 Variable Type Checking")
print("=" * 50)

print("\n🔍 Type Checking and Validation")
print("-" * 30)

def analyze_variable(var_name, var_value):
    """Comprehensive variable analysis"""
    print(f"\n📋 Variable Analysis: {var_name}")
    print(f"  Value: {var_value}")
    print(f"  Type: {type(var_value).__name__}")
    print(f"  Type (full): {type(var_value)}")
    print(f"  Memory ID: {id(var_value)}")
    print(f"  Memory Size: {sys.getsizeof(var_value)} bytes")
    print(f"  Is Mutable: {not isinstance(var_value, (int, float, str, tuple, frozenset, bool, type(None)))}")
    print(f"  Boolean Value: {bool(var_value)}")
    
    # Type-specific information
    if isinstance(var_value, (list, tuple, str)):
        print(f"  Length: {len(var_value)}")
    elif isinstance(var_value, dict):
        print(f"  Keys: {len(var_value)}")
    elif isinstance(var_value, set):
        print(f"  Elements: {len(var_value)}")

# Test different variable types
test_variables = [
    ("integer_var", 42),
    ("float_var", 3.14159),
    ("string_var", "Hello Python"),
    ("list_var", [1, 2, 3, 4]),
    ("dict_var", {"name": "John", "age": 30}),
    ("tuple_var", (10, 20, 30)),
    ("set_var", {1, 2, 3, 4}),
    ("bool_var", True),
    ("none_var", None)
]

for name, value in test_variables:
    analyze_variable(name, value)

print("\n" + "=" * 50)
print("1️⃣1️⃣ Common Variable Mistakes")
print("=" * 50)

print("\n❌ Common Mistakes and Solutions")
print("-" * 30)

print("1. Using Reserved Keywords:")
print("❌ Bad:")
print("# class = 'MyClass'  # SyntaxError!")
print("# def = 'my function'  # SyntaxError!")
print("✅ Good:")
class_name = 'MyClass'
function_def = 'my function'
print(f"class_name = '{class_name}'")
print(f"function_def = '{function_def}'")

print(f"\n2. Overwriting Built-in Functions:")
print("❌ Bad:")
print("# list = [1, 2, 3]  # Overwrites built-in list()")
print("# str = 'hello'     # Overwrites built-in str()")
print("✅ Good:")
my_list = [1, 2, 3]
my_string = 'hello'
print(f"my_list = {my_list}")
print(f"my_string = '{my_string}'")

print(f"\n3. Unclear Variable Names:")
print("❌ Bad:")
print("# x = 'john@email.com'")
print("# data = [1, 2, 3, 4, 5]")
print("# temp = calculate_something()")
print("✅ Good:")
user_email = 'john@email.com'
test_scores = [1, 2, 3, 4, 5]
calculation_result = "some_result"
print(f"user_email = '{user_email}'")
print(f"test_scores = {test_scores}")
print(f"calculation_result = '{calculation_result}'")

print(f"\n4. Mutable Default Arguments:")
print("❌ Bad:")
print("# def add_item(item, my_list=[]):  # Dangerous!")
print("#     my_list.append(item)")
print("#     return my_list")
print("✅ Good:")
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

result1 = add_item("first")
result2 = add_item("second")
print(f"Safe function result1: {result1}")
print(f"Safe function result2: {result2}")

print("\n" + "=" * 50)
print("1️⃣2️⃣ Advanced Variable Techniques")
print("=" * 50)

print("\n🚀 Advanced Techniques")
print("-" * 21)

# Variable annotations (type hints)
print("1. Type Hints (Python 3.5+):")
name: str = "John"
age: int = 30
scores: list[int] = [85, 90, 95]
user_data: dict[str, any] = {"name": "Alice", "active": True}

print(f"name: str = '{name}'")
print(f"age: int = {age}")
print(f"scores: list[int] = {scores}")
print(f"user_data: dict[str, any] = {user_data}")

# Dynamic variable creation
print(f"\n2. Dynamic Variable Creation:")
variables = {}
for i in range(3):
    variables[f'dynamic_var_{i}'] = i * 10

for var_name, var_value in variables.items():
    print(f"{var_name} = {var_value}")

# Using globals() and locals()
print(f"\n3. Using globals() and locals():")
global_example = "I'm global"

def local_demo():
    local_example = "I'm local"
    print(f"Local variables: {list(locals().keys())}")

print(f"Some global variables: {list(globals().keys())[:5]}...")
local_demo()

# Variable unpacking with *
print(f"\n4. Advanced Unpacking:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first, second, *middle, second_last, last = numbers

print(f"first = {first}")
print(f"second = {second}")
print(f"middle = {middle}")
print(f"second_last = {second_last}")
print(f"last = {last}")

# Dictionary unpacking
person_info = {"name": "John", "age": 30, "city": "New York"}
other_info = {"job": "Engineer", "salary": 75000}
complete_info = {**person_info, **other_info}

print(f"\nDictionary unpacking:")
print(f"person_info = {person_info}")
print(f"other_info = {other_info}")
print(f"complete_info = {complete_info}")

print("\n" + "=" * 50)
print("1️⃣3️⃣ Variable Best Practices")
print("=" * 50)

print("\n💡 Best Practices Guide")
print("-" * 23)

print("""
🎯 Naming Best Practices:
✅ Use descriptive names: user_email instead of e
✅ Use snake_case for variables and functions
✅ Use UPPER_CASE for constants
✅ Use PascalCase for classes
✅ Prefix private variables with underscore: _private_var
✅ Use is_ or has_ for boolean variables: is_active, has_permission

🔧 Assignment Best Practices:
✅ Initialize variables close to where they're used
✅ Use meaningful default values
✅ Group related variable assignments
✅ Use tuple unpacking for multiple return values
✅ Avoid deep nesting in variable structures

⚡ Performance Best Practices:
✅ Reuse variables when appropriate
✅ Use local variables in loops (faster access)
✅ Avoid global variables in performance-critical code
✅ Use appropriate data structures for your use case
✅ Consider memory usage for large datasets

🔒 Safety Best Practices:
✅ Don't modify mutable default arguments
✅ Be careful with mutable objects and references
✅ Use type hints for better code documentation
✅ Validate input data before assignment
✅ Handle None values explicitly
""")

print("\n" + "=" * 50)
print("1️⃣4️⃣ Practical Variable Examples")
print("=" * 50)

print("\n🛠️ Real-World Variable Usage")
print("-" * 28)

# Example 1: Configuration management
print("Example 1: Configuration Management")
# Application configuration
APP_NAME = "MyWebApp"  # Constant
APP_VERSION = "1.2.3"  # Constant
DEBUG_MODE = True       # Boolean flag

# Database configuration
db_config = {
    "host": "localhost",
    "port": 5432,
    "database": "myapp_db",
    "username": "admin",
    "password": "secure_password"
}

# User settings
user_preferences = {
    "theme": "dark",
    "language": "en",
    "notifications_enabled": True,
    "max_items_per_page": 25
}

print(f"App: {APP_NAME} v{APP_VERSION} (Debug: {DEBUG_MODE})")
print(f"Database: {db_config['host']}:{db_config['port']}")
print(f"User theme: {user_preferences['theme']}")

# Example 2: Data processing
print(f"\nExample 2: Data Processing Pipeline")
# Raw data
raw_sales_data = [
    {"product": "Laptop", "price": 999.99, "quantity": 5},
    {"product": "Mouse", "price": 29.99, "quantity": 15},
    {"product": "Keyboard", "price": 79.99, "quantity": 8}
]

# Processing variables
total_revenue = 0
total_items_sold = 0
product_revenues = {}

# Process data
for sale in raw_sales_data:
    product_name = sale["product"]
    item_revenue = sale["price"] * sale["quantity"]
    
    total_revenue += item_revenue
    total_items_sold += sale["quantity"]
    product_revenues[product_name] = item_revenue

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Items Sold: {total_items_sold}")
print(f"Revenue by Product: {product_revenues}")

# Example 3: User management system
print(f"\nExample 3: User Management System")
class UserManager:
    def __init__(self):
        self.users = {}  # Dictionary to store users
        self.next_user_id = 1  # Auto-increment ID
        self.active_sessions = set()  # Set of active session IDs
        
    def create_user(self, username, email, role="user"):
        user_id = self.next_user_id
        user_data = {
            "id": user_id,
            "username": username,
            "email": email,
            "role": role,
            "created_at": "2024-01-01",  # Simplified
            "is_active": True
        }
        
        self.users[user_id] = user_data
        self.next_user_id += 1
        
        return user_id
    
    def get_user_stats(self):
        total_users = len(self.users)
        active_users = sum(1 for user in self.users.values() if user["is_active"])
        admin_users = sum(1 for user in self.users.values() if user["role"] == "admin")
        
        return {
            "total": total_users,
            "active": active_users,
            "admins": admin_users,
            "active_sessions": len(self.active_sessions)
        }

# Using the user manager
user_manager = UserManager()
john_id = user_manager.create_user("john_doe", "john@email.com", "admin")
alice_id = user_manager.create_user("alice_smith", "alice@email.com")
bob_id = user_manager.create_user("bob_jones", "bob@email.com")

user_stats = user_manager.get_user_stats()
print(f"User Management Stats: {user_stats}")

print("\n" + "=" * 50)
print("1️⃣5️⃣ Variable Performance Analysis")
print("=" * 50)

print("\n⚡ Performance Considerations")
print("-" * 27)

import timeit

# Test 1: Local vs Global variable access
global_counter = 0

def test_global_access():
    global global_counter
    for i in range(1000):
        global_counter += 1

def test_local_access():
    local_counter = 0
    for i in range(1000):
        local_counter += 1
    return local_counter

# Measure performance
global_time = timeit.timeit(test_global_access, number=1000)
local_time = timeit.timeit(test_local_access, number=1000)

print(f"Global variable access: {global_time:.6f} seconds")
print(f"Local variable access: {local_time:.6f} seconds")
print(f"Local is {global_time/local_time:.2f}x faster")

# Test 2: Variable assignment vs multiple lookups
def test_repeated_lookups():
    data = {"key": {"nested": {"value": 42}}}
    total = 0
    for i in range(1000):
        total += data["key"]["nested"]["value"]
    return total

def test_variable_assignment():
    data = {"key": {"nested": {"value": 42}}}
    value = data["key"]["nested"]["value"]  # Assign once
    total = 0
    for i in range(1000):
        total += value
    return total

lookup_time = timeit.timeit(test_repeated_lookups, number=1000)
assignment_time = timeit.timeit(test_variable_assignment, number=1000)

print(f"\nRepeated lookups: {lookup_time:.6f} seconds")
print(f"Variable assignment: {assignment_time:.6f} seconds")
print(f"Assignment is {lookup_time/assignment_time:.2f}x faster")

print("\n" + "=" * 50)
print("1️⃣6️⃣ Variable Debugging Tools")
print("=" * 50)

print("\n🔧 Debugging and Inspection Tools")
print("-" * 31)

def debug_variables():
    """Demonstrate variable debugging techniques"""
    
    # Local variables for debugging
    user_name = "John Doe"
    user_age = 30
    user_scores = [85, 90, 95, 88]
    user_active = True
    
    print("🔍 Variable Debugging Session:")
    print(f"Current function: {debug_variables.__name__}")
    print(f"Local variables: {list(locals().keys())}")
    
    # Inspect each variable
    for var_name, var_value in locals().items():
        if not var_name.startswith('__'):  # Skip internal variables
            print(f"  {var_name}: {var_value} ({type(var_value).__name__})")

debug_variables()

# Variable existence checking
print(f"\n✅ Variable Existence Checking:")
def check_variable_exists(var_name):
    return var_name in globals() or var_name in locals()

test_vars = ["user_name", "undefined_var", "APP_NAME"]
for var in test_vars:
    exists = var in globals()
    print(f"Variable '{var}' exists: {exists}")

print("\n" + "=" * 70)
print("🎉 Complete Python Variables Guide Finished!")
print("💻 You're now ready to use variables effectively in Python")
print("=" * 70)

# Quick reference summary
print(f"""
📚 Quick Variable Reference:

Basic Assignment:
variable_name = value

Multiple Assignment:
a, b, c = 1, 2, 3
x = y = z = 10

Type Hints:
name: str = "John"
age: int = 30

Naming Rules:
✅ snake_case (recommended)
✅ Descriptive names
✅ No reserved keywords
❌ No numbers at start
❌ No special characters (except _)

Best Practices:
✅ Use meaningful names
✅ Initialize close to usage
✅ Avoid global variables
✅ Use type hints for clarity
✅ Follow naming conventions

Memory Management:
- Variables are references to objects
- Use id() to check object identity
- Use is for identity comparison
- Use == for value comparison

Common Mistakes to Avoid:
❌ Using reserved keywords as variable names
❌ Overwriting built-in functions
❌ Using unclear single-letter names
❌ Modifying mutable default arguments
❌ Creating unnecessary global variables
""")

# Additional practical exercises
print("\n" + "=" * 50)
print("1️⃣7️⃣ Practice Exercises")
print("=" * 50)

print("\n🏋️ Variable Practice Exercises")
print("-" * 28)

def exercise_1():
    """Exercise 1: Variable naming correction"""
    print("Exercise 1: Fix the variable names")
    print("❌ Bad names → ✅ Good names")
    
    # Bad examples and their corrections
    corrections = [
        ("x", "user_age"),
        ("data", "student_grades"),
        ("temp", "temperature_celsius"),
        ("list", "shopping_items"),
        ("str", "user_message"),
        ("123name", "user_name_123"),
        ("my-var", "my_variable"),
        ("class", "class_name")
    ]
    
    for bad, good in corrections:
        print(f"  '{bad}' → '{good}'")

def exercise_2():
    """Exercise 2: Variable assignment patterns"""
    print("\nExercise 2: Practice different assignment patterns")
    
    # Multiple assignment
    name, age, city = "Alice", 28, "Boston"
    print(f"Multiple assignment: name={name}, age={age}, city={city}")
    
    # Swap variables
    a, b = 10, 20
    print(f"Before swap: a={a}, b={b}")
    a, b = b, a
    print(f"After swap: a={a}, b={b}")
    
    # Unpacking with *
    numbers = [1, 2, 3, 4, 5, 6]
    first, *middle, last = numbers
    print(f"Unpacking: first={first}, middle={middle}, last={last}")
    
    # Dictionary unpacking
    person = {"name": "Bob", "age": 25}
    details = {"job": "Developer", "city": "Seattle"}
    complete = {**person, **details}
    print(f"Dict unpacking: {complete}")

def exercise_3():
    """Exercise 3: Variable scope understanding"""
    print("\nExercise 3: Understanding variable scope")
    
    global_var = "I'm global"
    
    def outer_function():
        outer_var = "I'm in outer function"
        
        def inner_function():
            inner_var = "I'm in inner function"
            print(f"  Inner sees: {global_var}, {outer_var}, {inner_var}")
        
        inner_function()
        print(f"  Outer sees: {global_var}, {outer_var}")
    
    print(f"  Global sees: {global_var}")
    outer_function()

def exercise_4():
    """Exercise 4: Variable type checking and validation"""
    print("\nExercise 4: Variable validation system")
    
    def validate_variable(name, value, expected_type):
        """Validate if variable matches expected type"""
        actual_type = type(value).__name__
        is_valid = isinstance(value, expected_type)
        
        status = "✅ Valid" if is_valid else "❌ Invalid"
        print(f"  {name}: {value} - Expected: {expected_type.__name__}, Got: {actual_type} - {status}")
        
        return is_valid
    
    # Test cases
    test_cases = [
        ("user_name", "John", str),
        ("user_age", 25, int),
        ("user_scores", [85, 90, 95], list),
        ("is_active", True, bool),
        ("invalid_age", "twenty-five", int),  # This should fail
        ("user_data", {"name": "Alice"}, dict)
    ]
    
    print("  Variable validation results:")
    for name, value, expected_type in test_cases:
        validate_variable(name, value, expected_type)

def exercise_5():
    """Exercise 5: Advanced variable manipulation"""
    print("\nExercise 5: Advanced variable operations")
    
    # Dynamic variable creation
    variables = {}
    data_types = [int, str, list, dict, bool]
    sample_values = [42, "hello", [1, 2, 3], {"key": "value"}, True]
    
    for i, (data_type, value) in enumerate(zip(data_types, sample_values)):
        var_name = f"dynamic_{data_type.__name__}_{i}"
        variables[var_name] = value
    
    print("  Dynamically created variables:")
    for var_name, var_value in variables.items():
        print(f"    {var_name} = {var_value} ({type(var_value).__name__})")
    
    # Variable statistics
    type_counts = {}
    total_memory = 0
    
    for var_value in variables.values():
        var_type = type(var_value).__name__
        type_counts[var_type] = type_counts.get(var_type, 0) + 1
        total_memory += sys.getsizeof(var_value)
    
    print(f"\n  Variable statistics:")
    print(f"    Total variables: {len(variables)}")
    print(f"    Type distribution: {type_counts}")
    print(f"    Total memory usage: {total_memory} bytes")

# Run all exercises
exercise_1()
exercise_2()
exercise_3()
exercise_4()
exercise_5()

print("\n" + "=" * 50)
print("1️⃣8️⃣ Variable Troubleshooting Guide")
print("=" * 50)

print("\n🔧 Common Variable Problems and Solutions")
print("-" * 37)

def troubleshooting_demo():
    """Demonstrate common variable issues and solutions"""
    
    print("Problem 1: NameError - Variable not defined")
    print("❌ Error code:")
    print("# print(undefined_variable)  # NameError!")
    print("✅ Solution:")
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"  Caught error: {e}")
        print("  Fix: Define the variable before using it")
        undefined_variable = "Now I'm defined!"
        print(f"  Result: {undefined_variable}")
    
    print(f"\nProblem 2: Mutable default argument")
    print("❌ Problematic code:")
    def bad_function(item, my_list=[]):
        my_list.append(item)
        return my_list
    
    result1 = bad_function("first")
    result2 = bad_function("second")
    print(f"  First call: {result1}")
    print(f"  Second call: {result2}  # Unexpected!")
    
    print("✅ Fixed version:")
    def good_function(item, my_list=None):
        if my_list is None:
            my_list = []
        my_list.append(item)
        return my_list
    
    result3 = good_function("first")
    result4 = good_function("second")
    print(f"  First call: {result3}")
    print(f"  Second call: {result4}  # Expected!")
    
    print(f"\nProblem 3: Variable shadowing")
    print("❌ Confusing code:")
    name = "Global Name"
    
    def confusing_function():
        print(f"  Before assignment: {name}")  # This would cause UnboundLocalError
        # Uncommenting the next line would cause an error:
        # name = "Local Name"
    
    print("✅ Clear version:")
    def clear_function():
        global name
        print(f"  Global name: {name}")
        local_name = "Local Name"
        print(f"  Local name: {local_name}")
    
    clear_function()
    
    print(f"\nProblem 4: Reference vs Copy confusion")
    print("❌ Unexpected behavior:")
    original_list = [1, 2, 3]
    copied_list = original_list  # This is a reference, not a copy!
    copied_list.append(4)
    print(f"  Original: {original_list}  # Modified unexpectedly!")
    print(f"  Copied: {copied_list}")
    
    print("✅ Correct copying:")
    original_list2 = [1, 2, 3]
    actual_copy = original_list2.copy()  # or original_list2[:]
    actual_copy.append(4)
    print(f"  Original: {original_list2}  # Unchanged")
    print(f"  Copy: {actual_copy}")

troubleshooting_demo()

print("\n" + "=" * 50)
print("1️⃣9️⃣ Variable Performance Optimization")
print("=" * 50)

print("\n⚡ Performance Optimization Tips")
print("-" * 30)

def performance_tips():
    """Demonstrate variable performance optimization techniques"""
    
    print("Tip 1: Use local variables in loops")
    # Slow version with global lookup
    global_data = {"value": 42}
    
    def slow_loop():
        total = 0
        for i in range(1000):
            total += global_data["value"]  # Global lookup each time
        return total
    
    # Fast version with local variable
    def fast_loop():
        value = global_data["value"]  # Lookup once, store locally
        total = 0
        for i in range(1000):
            total += value  # Local variable access
        return total
    
    slow_time = timeit.timeit(slow_loop, number=1000)
    fast_time = timeit.timeit(fast_loop, number=1000)
    
    print(f"  Slow (global lookup): {slow_time:.6f} seconds")
    print(f"  Fast (local variable): {fast_time:.6f} seconds")
    print(f"  Improvement: {slow_time/fast_time:.2f}x faster")
    
    print(f"\nTip 2: Reuse variables appropriately")
    # Memory-efficient variable reuse
    def process_data_efficiently():
        result_data = []
        
        # Reuse temporary variables
        for i in range(5):
            temp_value = i * 2  # Reuse temp_value
            processed_item = f"Item_{temp_value}"
            result_data.append(processed_item)
        
        return result_data
    
    efficient_result = process_data_efficiently()
    print(f"  Efficient processing result: {efficient_result}")
    
    print(f"\nTip 3: Choose appropriate data structures")
    # List vs Set for membership testing
    large_list = list(range(1000))
    large_set = set(range(1000))
    
    def test_list_membership():
        return 999 in large_list
    
    def test_set_membership():
        return 999 in large_set
    
    list_time = timeit.timeit(test_list_membership, number=10000)
    set_time = timeit.timeit(test_set_membership, number=10000)
    
    print(f"  List membership test: {list_time:.6f} seconds")
    print(f"  Set membership test: {set_time:.6f} seconds")
    print(f"  Set is {list_time/set_time:.0f}x faster for membership testing")

performance_tips()

print("\n" + "=" * 50)
print("2️⃣0️⃣ Final Variable Mastery Test")
print("=" * 50)

print("\n🎓 Variable Mastery Challenge")
print("-" * 27)

def variable_mastery_test():
    """A comprehensive test of variable knowledge"""
    
    print("Challenge: Create a complete variable management system")
    
    class VariableManager:
        """Advanced variable management system"""
        
        def __init__(self):
            self._variables = {}  # Private variable storage
            self._history = []    # Track variable changes
            self._type_counts = {}  # Count variables by type
        
        def set_variable(self, name: str, value, description: str = ""):
            """Set a variable with validation and history tracking"""
            # Validate variable name
            if not self._is_valid_name(name):
                raise ValueError(f"Invalid variable name: {name}")
            
            # Store old value for history
            old_value = self._variables.get(name, "UNDEFINED")
            
            # Set new value
            self._variables[name] = {
                "value": value,
                "type": type(value).__name__,
                "description": description,
                "memory_size": sys.getsizeof(value),
                "created_at": "2024-01-01"  # Simplified timestamp
            }
            
            # Update type counts
            var_type = type(value).__name__
            self._type_counts[var_type] = self._type_counts.get(var_type, 0) + 1
            
            # Add to history
            self._history.append({
                "name": name,
                "old_value": old_value,
                "new_value": value,
                "action": "SET"
            })
        
        def get_variable(self, name: str):
            """Get a variable value"""
            if name not in self._variables:
                raise NameError(f"Variable '{name}' is not defined")
            return self._variables[name]["value"]
        
        def delete_variable(self, name: str):
            """Delete a variable"""
            if name not in self._variables:
                raise NameError(f"Variable '{name}' is not defined")
            
            old_value = self._variables[name]["value"]
            var_type = self._variables[name]["type"]
            
            del self._variables[name]
            self._type_counts[var_type] -= 1
            
            self._history.append({
                "name": name,
                "old_value": old_value,
                "new_value": "DELETED",
                "action": "DELETE"
            })
        
        def list_variables(self):
            """List all variables with their info"""
            result = []
            for name, info in self._variables.items():
                result.append({
                    "name": name,
                    "value": info["value"],
                    "type": info["type"],
                    "size": info["memory_size"],
                    "description": info["description"]
                })
            return result
        
        def get_statistics(self):
            """Get variable statistics"""
            total_variables = len(self._variables)
            total_memory = sum(var["memory_size"] for var in self._variables.values())
            
            return {
                "total_variables": total_variables,
                "type_distribution": self._type_counts.copy(),
                "total_memory_usage": total_memory,
                "history_entries": len(self._history)
            }
        
        def _is_valid_name(self, name: str) -> bool:
            """Validate variable name according to Python rules"""
            if not name.isidentifier():
                return False
            if keyword.iskeyword(name):
                return False
            if name in dir(builtins):
                return False
            return True
        
        def search_variables(self, criteria):
            """Search variables by various criteria"""
            results = []
            for name, info in self._variables.items():
                if criteria.get("type") and info["type"] != criteria["type"]:
                    continue
                if criteria.get("name_contains") and criteria["name_contains"] not in name:
                    continue
                if criteria.get("min_size") and info["memory_size"] < criteria["min_size"]:
                    continue
                
                results.append({"name": name, **info})
            
            return results
    
    # Demonstrate the variable manager
    print("  Creating Variable Manager...")
    vm = VariableManager()
    
    # Test variable creation
    test_variables = [
        ("user_name", "Alice Johnson", "The user's full name"),
        ("user_age", 28, "User's age in years"),
        ("user_scores", [95, 87, 92, 88], "List of test scores"),
        ("user_active", True, "Whether user account is active"),
        ("user_settings", {"theme": "dark", "lang": "en"}, "User preferences")
    ]
    
    print("  Setting variables...")
    for name, value, description in test_variables:
        vm.set_variable(name, value, description)
    
    # Display variable list
    print("  \n📋 Variable List:")
    for var in vm.list_variables():
        print(f"    {var['name']}: {var['value']} ({var['type']}) - {var['description']}")
    
    # Show statistics
    stats = vm.get_statistics()
    print(f"  \n📊 Statistics:")
    print(f"    Total variables: {stats['total_variables']}")
    print(f"    Type distribution: {stats['type_distribution']}")
    print(f"    Total memory: {stats['total_memory_usage']} bytes")
    
    # Test search functionality
    print(f"  \n🔍 Search Results (strings only):")
    string_vars = vm.search_variables({"type": "str"})
    for var in string_vars:
        print(f"    {var['name']}: {var['value']}")
    
    # Test variable deletion
    print(f"  \n🗑️ Deleting user_active...")
    vm.delete_variable("user_active")
    
    final_stats = vm.get_statistics()
    print(f"  Variables after deletion: {final_stats['total_variables']}")
    
    print(f"  \n✅ Variable Management System completed successfully!")

variable_mastery_test()

print("\n" + "=" * 70)
print("🎉 CONGRATULATIONS! You've mastered Python Variables!")
print("🏆 You've completed the most comprehensive variables guide!")
print("=" * 70)

print(f"""
🎯 What You've Learned:

✅ Variable assignment syntax and patterns
✅ All data types and their variable usage
✅ Naming conventions and best practices
✅ Scope and lifetime management
✅ Memory management and performance
✅ Advanced techniques and optimization
✅ Debugging and troubleshooting
✅ Real-world practical applications

🚀 Next Steps:
1. Practice with your own projects
2. Explore functions and classes
3. Learn about modules and packages
4. Study advanced Python concepts
5. Build real applications

💡 Remember:
- Variables are the foundation of programming
- Good naming makes code readable
- Understanding scope prevents bugs
- Performance matters in large applications
- Practice makes perfect!

Happy coding! 🐍✨
""")