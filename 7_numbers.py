# =====================================
# Complete Guide to Python Numbers
# Comprehensive Tutorial and Reference
# =====================================

"""
What are Numbers?
Numbers are fundamental data types in Python used to represent numerical values.
Python provides several types of numbers: integers, floats, complex numbers, and more.
They are essential for mathematical calculations, data analysis, and scientific computing.

Examples: 42, 3.14, -17, 2+3j, 1_000_000, 0xFF, 0o755, 0b1010
"""

import math
import cmath
import decimal
import fractions
import random
import statistics
import sys
import timeit
from datetime import datetime

print("=" * 70)
print("🔢 Complete Guide to Python Numbers")
print("=" * 70)

print("\n" + "=" * 50)
print("1️⃣ Introduction to Numbers")
print("=" * 50)

print("""
🧮 What are Numbers?
✅ Fundamental data types for numerical values
✅ Support mathematical operations (+, -, *, /, etc.)
✅ Multiple types: int, float, complex, decimal, fraction
✅ Immutable (cannot be changed after creation)
✅ Essential for calculations and data processing

🎯 Common Uses:
• Mathematical calculations
• Data analysis and statistics
• Financial computations
• Scientific computing
• Game development (scores, coordinates)
• System programming (memory sizes, time)
""")

print("\n" + "=" * 50)
print("2️⃣ Number Types in Python")
print("=" * 50)

print("\n📊 Python Number Types")
print("-" * 24)

# Integer examples
print("🔢 Integers (int):")
integers = [42, -17, 0, 1000000, 999999999999999999999999999999]
for num in integers:
    print(f"  {num} → type: {type(num).__name__}, size: {sys.getsizeof(num)} bytes")

# Float examples
print(f"\n🌊 Floating Point Numbers (float):")
floats = [3.14, -2.5, 0.0, 1e6, 1.23e-4, float('inf'), float('-inf')]
for num in floats:
    if str(num) not in ['inf', '-inf', 'nan']:
        print(f"  {num} → type: {type(num).__name__}, size: {sys.getsizeof(num)} bytes")
    else:
        print(f"  {num} → type: {type(num).__name__} (special value)")

# Complex numbers
print(f"\n🎭 Complex Numbers (complex):")
complex_nums = [3+4j, -2-5j, 1j, complex(2, 3), complex('3+4j')]
for num in complex_nums:
    print(f"  {num} → real: {num.real}, imaginary: {num.imag}")

# Special numeric types
print(f"\n🎯 Special Numeric Types:")

# Decimal for precision
from decimal import Decimal
decimal_nums = [Decimal('3.14'), Decimal('0.1') + Decimal('0.2')]
print(f"Decimal (high precision):")
for num in decimal_nums:
    print(f"  {num} → type: {type(num).__name__}")

# Fractions for exact ratios
from fractions import Fraction
fraction_nums = [Fraction(1, 3), Fraction(22, 7), Fraction('0.25')]
print(f"Fraction (exact ratios):")
for num in fraction_nums:
    print(f"  {num} → decimal: {float(num):.6f}")

print("\n" + "=" * 50)
print("3️⃣ Number Literals and Representations")
print("=" * 50)

print("\n🎨 Different Ways to Write Numbers")
print("-" * 34)

# Integer literals
print("🔢 Integer Literals:")
int_literals = {
    "Decimal": [42, 100, -50],
    "Binary": [0b1010, 0b11111111, 0B101010],  # 10, 255, 42
    "Octal": [0o755, 0o644, 0O123],  # 493, 420, 83
    "Hexadecimal": [0xFF, 0xDEADBEEF, 0X123ABC]  # 255, 3735928559, 1194684
}

for format_type, numbers in int_literals.items():
    print(f"  {format_type}:")
    for num in numbers:
        print(f"    {num} (decimal: {int(num)})")

# Float literals
print(f"\n🌊 Float Literals:")
float_formats = [
    ("Standard", [3.14, -2.5, 0.0]),
    ("Scientific", [1e6, 2.5e-3, -1.23E+4]),
    ("With underscores", [1_000.500_123, 2_000_000.0])
]

for format_type, numbers in float_formats:
    print(f"  {format_type}:")
    for num in numbers:
        print(f"    {num}")

# Number separators (Python 3.6+)
print(f"\n📏 Number Separators (Readability):")
large_numbers = [
    1_000_000,      # One million
    3.141_592_653,  # Pi with separators
    0xFF_FF_FF,     # Hex with separators
    0b_1010_1010,   # Binary with separators
]

for num in large_numbers:
    print(f"  {num} → {int(num) if isinstance(num, (int, float)) and num.is_integer() else num}")

print("\n" + "=" * 50)
print("4️⃣ Basic Arithmetic Operations")
print("=" * 50)

print("\n➕ Mathematical Operations")
print("-" * 25)

# Basic operations
a, b = 15, 4
print(f"Given: a = {a}, b = {b}")
print(f"")

operations = [
    ("Addition", a + b, f"{a} + {b}"),
    ("Subtraction", a - b, f"{a} - {b}"),
    ("Multiplication", a * b, f"{a} * {b}"),
    ("Division (float)", a / b, f"{a} / {b}"),
    ("Floor Division", a // b, f"{a} // {b}"),
    ("Modulus", a % b, f"{a} % {b}"),
    ("Exponentiation", a ** b, f"{a} ** {b}"),
]

for name, result, expression in operations:
    print(f"  {name:20}: {expression:8} = {result}")

# Operator precedence
print(f"\n🎯 Operator Precedence Examples:")
expressions = [
    "2 + 3 * 4",      # 14 (not 20)
    "2 ** 3 ** 2",    # 512 (right-associative)
    "(2 + 3) * 4",    # 20
    "10 / 2 * 3",     # 15.0 (left-associative)
    "2 + 3 * 4 ** 2", # 50
]

for expr in expressions:
    result = eval(expr)
    print(f"  {expr:15} = {result}")

# Different division types
print(f"\n➗ Division Types:")
dividend, divisor = 17, 5
print(f"Given: {dividend} ÷ {divisor}")
print(f"  Regular division (/)    : {dividend / divisor}")
print(f"  Floor division (//)     : {dividend // divisor}")
print(f"  Modulus (remainder) (%) : {dividend % divisor}")
print(f"  Divmod function         : {divmod(dividend, divisor)}")

# Negative number divisions
print(f"\nWith negative numbers:")
print(f"  -17 / 5  = {-17 / 5}")
print(f"  -17 // 5 = {-17 // 5}")
print(f"  17 // -5 = {17 // -5}")
print(f"  -17 % 5  = {-17 % 5}")

print("\n" + "=" * 50)
print("5️⃣ Number Conversion and Casting")
print("=" * 50)

print("\n🔄 Type Conversion")
print("-" * 17)

# Basic conversions
original_values = [42, 3.14, "123", "45.67", True, False]
print("🔀 Basic Type Conversions:")
print(f"{'Original':<15} {'Type':<10} {'int()':<10} {'float()':<12} {'str()':<10}")
print("-" * 60)

for val in original_values:
    try:
        int_val = int(val)
    except (ValueError, TypeError):
        int_val = "Error"
    
    try:
        float_val = float(val)
    except (ValueError, TypeError):
        float_val = "Error"
    
    str_val = str(val)
    print(f"{str(val):<15} {type(val).__name__:<10} {str(int_val):<10} {str(float_val):<12} {str_val:<10}")

# Advanced conversions
print(f"\n🎯 Advanced Conversions:")

# String to number with different bases
print("String to int with different bases:")
string_numbers = [
    ("1010", 2),      # Binary
    ("755", 8),       # Octal
    ("FF", 16),       # Hexadecimal
    ("123", 10),      # Decimal
]

for num_str, base in string_numbers:
    converted = int(num_str, base)
    print(f"  int('{num_str}', {base:2d}) = {converted:4d} (base {base})")

# Number to string with different bases
print(f"\nNumber to string with different bases:")
number = 255
print(f"Number: {number}")
print(f"  Binary:      bin({number}) = {bin(number)}")
print(f"  Octal:       oct({number}) = {oct(number)}")
print(f"  Hexadecimal: hex({number}) = {hex(number)}")

# Complex number conversions
print(f"\n🎭 Complex Number Conversions:")
complex_num = 3 + 4j
print(f"Complex number: {complex_num}")
print(f"  Real part:      {complex_num.real}")
print(f"  Imaginary part: {complex_num.imag}")
print(f"  Absolute value: {abs(complex_num)}")
print(f"  Conjugate:      {complex_num.conjugate()}")

# Precision conversions
print(f"\n🎯 Precision Conversions:")
pi_float = 3.141592653589793
print(f"Original float: {pi_float}")
print(f"  Decimal:     {Decimal(str(pi_float))}")
print(f"  Fraction:    {Fraction(pi_float).limit_denominator(1000)}")

print("\n" + "=" * 50)
print("6️⃣ Built-in Mathematical Functions")
print("=" * 50)

print("\n🧮 Essential Math Functions")
print("-" * 26)

# Basic math functions
test_numbers = [-5.7, -2, 0, 2.3, 5.9, 10]
print("📊 Basic Math Functions:")
print(f"{'Number':<8} {'abs()':<8} {'round()':<8} {'int()':<8} {'float()':<10}")
print("-" * 45)

for num in test_numbers:
    print(f"{num:<8} {abs(num):<8} {round(num):<8} {int(num):<8} {float(num):<10}")

# Min, max, sum functions
numbers_list = [1, 5, 2, 9, 3, 7]
print(f"\n📈 Aggregate Functions:")
print(f"Numbers: {numbers_list}")
print(f"  min():  {min(numbers_list)}")
print(f"  max():  {max(numbers_list)}")
print(f"  sum():  {sum(numbers_list)}")
print(f"  len():  {len(numbers_list)}")

# Range function
print(f"\n🔢 Range Function:")
range_examples = [
    ("range(5)", list(range(5))),
    ("range(2, 8)", list(range(2, 8))),
    ("range(0, 10, 2)", list(range(0, 10, 2))),
    ("range(10, 0, -2)", list(range(10, 0, -2))),
]

for description, result in range_examples:
    print(f"  {description:20} = {result}")

# Rounding and precision
print(f"\n🎯 Rounding and Precision:")
pi = 3.141592653589793
print(f"Pi = {pi}")
print(f"  round(pi):     {round(pi)}")
print(f"  round(pi, 2):  {round(pi, 2)}")
print(f"  round(pi, 4):  {round(pi, 4)}")

# Rounding with different strategies
print(f"\nRounding strategies for 2.5:")
print(f"  round(2.5):    {round(2.5)}")    # Banker's rounding
print(f"  round(3.5):    {round(3.5)}")    # Banker's rounding
print(f"  math.ceil(2.5): {math.ceil(2.5)}")
print(f"  math.floor(2.5): {math.floor(2.5)}")

print("\n" + "=" * 50)
print("7️⃣ Math Module - Advanced Functions")
print("=" * 50)

print("\n📐 Math Module Functions")
print("-" * 23)

# Import math module functions
print("🔢 Mathematical Constants:")
constants = [
    ("math.pi", math.pi),
    ("math.e", math.e),
    ("math.tau", math.tau),
    ("math.inf", math.inf),
    ("-math.inf", -math.inf),
]

for name, value in constants:
    print(f"  {name:12} = {value}")

# Power and logarithmic functions
print(f"\n⚡ Power and Logarithmic Functions:")
x = 8
print(f"Given x = {x}:")
power_log_functions = [
    ("math.sqrt(x)", math.sqrt(x)),
    ("math.pow(x, 2)", math.pow(x, 2)),
    ("math.log(x)", math.log(x)),
    ("math.log10(x)", math.log10(x)),
    ("math.log2(x)", math.log2(x)),
    ("math.exp(2)", math.exp(2)),
]

for func_name, result in power_log_functions:
    print(f"  {func_name:15} = {result:.6f}")

# Trigonometric functions
print(f"\n📐 Trigonometric Functions:")
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print(f"Angle: {angle_degrees}° = {angle_radians:.6f} radians")

trig_functions = [
    ("math.sin(angle)", math.sin(angle_radians)),
    ("math.cos(angle)", math.cos(angle_radians)),
    ("math.tan(angle)", math.tan(angle_radians)),
    ("math.asin(0.5)", math.asin(0.5)),
    ("math.acos(0.5)", math.acos(0.5)),
    ("math.atan(1)", math.atan(1)),
]

for func_name, result in trig_functions:
    print(f"  {func_name:18} = {result:.6f}")

# Hyperbolic functions
print(f"\n🌊 Hyperbolic Functions:")
x = 1
hyperbolic_functions = [
    ("math.sinh(x)", math.sinh(x)),
    ("math.cosh(x)", math.cosh(x)),
    ("math.tanh(x)", math.tanh(x)),
]

for func_name, result in hyperbolic_functions:
    print(f"  {func_name:15} = {result:.6f}")

# Special functions
print(f"\n🎯 Special Math Functions:")
special_examples = [
    ("math.factorial(5)", math.factorial(5)),
    ("math.gcd(48, 18)", math.gcd(48, 18)),
    ("math.lcm(12, 8)", math.lcm(12, 8)),  # Python 3.9+
    ("math.isqrt(17)", math.isqrt(17)),    # Integer square root
    ("math.fabs(-5.5)", math.fabs(-5.5)),  # Absolute value (float)
]

for func_name, result in special_examples:
    try:
        print(f"  {func_name:20} = {result}")
    except AttributeError:
        print(f"  {func_name:20} = Not available in this Python version")

print("\n" + "=" * 50)
print("8️⃣ Number Formatting and Display")
print("=" * 50)

print("\n🎨 Number Formatting Techniques")
print("-" * 30)

# Basic number formatting
number = 1234567.89123
print(f"Number: {number}")

# Old style formatting
print(f"\n📜 Old Style (% formatting):")
old_formats = [
    ("%d", number),           # Integer
    ("%f", number),           # Float
    ("%.2f", number),         # 2 decimal places
    ("%e", number),           # Scientific notation
    ("%g", number),           # General format
    ("%,d", int(number)),     # Thousand separators (if supported)
]

for format_str, val in old_formats:
    try:
        result = format_str % val
        print(f"  '{format_str}' % {val} = '{result}'")
    except (ValueError, TypeError):
        print(f"  '{format_str}' % {val} = Error")

# .format() method
print(f"\n🔧 .format() Method:")
format_examples = [
    ("{:.2f}", "2 decimal places"),
    ("{:,.2f}", "Comma separator"),
    ("{:10.2f}", "Width 10, 2 decimals"),
    ("{:>10.2f}", "Right aligned"),
    ("{:^15.2f}", "Center aligned"),
    ("{:e}", "Scientific notation"),
    ("{:.2%}", "Percentage"),
]

for format_spec, description in format_examples:
    formatted = format_spec.format(number if not format_spec.endswith('%}') else number/1000000)
    print(f"  {format_spec:12} → '{formatted:>15}' ({description})")

# f-strings (modern)
print(f"\n🚀 f-strings (Modern Python 3.6+):")
print(f"Number: {number}")
print(f"  Two decimals:     {number:.2f}")
print(f"  Comma separator:  {number:,.2f}")
print(f"  Scientific:       {number:e}")
print(f"  Percentage:       {number/1000000:.2%}")
print(f"  Binary:           {int(number):b}")
print(f"  Hexadecimal:      {int(number):x}")
print(f"  Padded zeros:     {int(number):08d}")

# Currency formatting
print(f"\n💰 Currency Formatting:")
price = 1234.56
currencies = [
    f"${price:.2f}",
    f"€{price:.2f}",
    f"£{price:,.2f}",
    f"¥{price:,.0f}",
]

for currency in currencies:
    print(f"  {currency}")

# Number base formatting
print(f"\n🔢 Number Base Formatting:")
num = 255
print(f"Number: {num}")
print(f"  Binary:      {num:b}")
print(f"  Octal:       {num:o}")
print(f"  Hexadecimal: {num:x}")
print(f"  Hex (upper): {num:X}")
print(f"  With prefix: {num:#b}, {num:#o}, {num:#x}")

print("\n" + "=" * 50)
print("9️⃣ Decimal Module - High Precision")
print("=" * 50)

print("\n🎯 Decimal for Precise Calculations")
print("-" * 32)

# Floating point precision issues
print("⚠️ Floating Point Precision Issues:")
print(f"  0.1 + 0.2 = {0.1 + 0.2}")
print(f"  0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")

# Decimal solution
from decimal import Decimal, getcontext
print(f"\n✅ Decimal Solution:")
d1 = Decimal('0.1')
d2 = Decimal('0.2')
d3 = Decimal('0.3')
print(f"  Decimal('0.1') + Decimal('0.2') = {d1 + d2}")
print(f"  Decimal('0.1') + Decimal('0.2') == Decimal('0.3'): {d1 + d2 == d3}")

# Decimal context and precision
print(f"\n🎯 Decimal Precision Control:")
print(f"Current precision: {getcontext().prec}")

# Change precision
getcontext().prec = 50
pi_high_precision = Decimal(1) / Decimal(7)
print(f"1/7 with high precision: {pi_high_precision}")

# Reset precision
getcontext().prec = 28

# Decimal operations
print(f"\n🧮 Decimal Operations:")
price = Decimal('19.99')
tax_rate = Decimal('0.08')
quantity = Decimal('3')

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"  Price: ${price}")
print(f"  Quantity: {quantity}")
print(f"  Subtotal: ${subtotal}")
print(f"  Tax (8%): ${tax:.2f}")
print(f"  Total: ${total:.2f}")

# Decimal rounding
print(f"\n🎯 Decimal Rounding:")
from decimal import ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_UP, ROUND_DOWN

value = Decimal('2.675')
print(f"Value: {value}")
print(f"  ROUND_HALF_UP:   {value.quantize(Decimal('0.01'), ROUND_HALF_UP)}")
print(f"  ROUND_HALF_DOWN: {value.quantize(Decimal('0.01'), ROUND_HALF_DOWN)}")
print(f"  ROUND_UP:        {value.quantize(Decimal('0.01'), ROUND_UP)}")
print(f"  ROUND_DOWN:      {value.quantize(Decimal('0.01'), ROUND_DOWN)}")

print("\n" + "=" * 50)
print("🔟 Fractions Module - Exact Ratios")
print("=" * 50)

print("\n🔢 Fractions for Exact Arithmetic")
print("-" * 30)

# Creating fractions
print("📊 Creating Fractions:")
fractions_examples = [
    Fraction(1, 3),
    Fraction(22, 7),
    Fraction('3.14'),
    Fraction(0.25),
    Fraction('22/7'),
]

for frac in fractions_examples:
    print(f"  {frac} = {float(frac):.6f}")

# Fraction arithmetic
print(f"\n➕ Fraction Arithmetic:")
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
print(f"f1 = {f1}, f2 = {f2}")
print(f"  f1 + f2 = {f1 + f2}")
print(f"  f1 - f2 = {f1 - f2}")
print(f"  f1 * f2 = {f1 * f2}")
print(f"  f1 / f2 = {f1 / f2}")

# Mixed operations
print(f"\n🔄 Mixed Operations:")
result = Fraction(1, 3) + Fraction(1, 6) - Fraction(1, 12)
print(f"1/3 + 1/6 - 1/12 = {result}")
print(f"As decimal: {float(result)}")

# Converting decimals to fractions
print(f"\n🔄 Converting Decimals to Fractions:")
decimals = [0.25, 0.125, 0.333333, 3.14159]
for decimal_val in decimals:
    frac = Fraction(decimal_val).limit_denominator(1000)
    print(f"  {decimal_val} ≈ {frac} = {float(frac):.6f}")

print("\n" + "=" * 50)
print("1️⃣1️⃣ Random Numbers and Statistics")
print("=" * 50)

print("\n🎲 Random Number Generation")
print("-" * 26)

# Basic random functions
import random
print("🎯 Basic Random Functions:")
random.seed(42)  # For reproducible results
print(f"  random.random():           {random.random():.6f}")
print(f"  random.randint(1, 10):     {random.randint(1, 10)}")
print(f"  random.randrange(0, 100, 5): {random.randrange(0, 100, 5)}")
print(f"  random.uniform(1.5, 10.5): {random.uniform(1.5, 10.5):.6f}")

# Random choices
print(f"\n🎪 Random Choices:")
colors = ['red', 'green', 'blue', 'yellow']
numbers = list(range(1, 11))
print(f"  random.choice({colors}): {random.choice(colors)}")
print(f"  random.choices({numbers[:5]}, k=3): {random.choices(numbers[:5], k=3)}")
print(f"  random.sample({numbers[:5]}, 3): {random.sample(numbers[:5], 3)}")

# Random shuffle
print(f"\n🔀 Random Shuffle:")
deck = list(range(1, 11))
print(f"Original: {deck}")
random.shuffle(deck)
print(f"Shuffled: {deck}")

# Statistical distributions
print(f"\n📊 Statistical Distributions:")
distributions = [
    ("Normal (Gaussian)", lambda: random.gauss(0, 1)),
    ("Exponential", lambda: random.expovariate(1)),
    ("Beta", lambda: random.betavariate(2, 5)),
]

for name, func in distributions:
    samples = [round(func(), 3) for _ in range(5)]
    print(f"  {name:20}: {samples}")

# Statistics module
print(f"\n📈 Statistics Module:")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Data: {data}")
print(f"  Mean:        {statistics.mean(data):.2f}")
print(f"  Median:      {statistics.median(data):.2f}")
print(f"  Mode:        {statistics.mode([1, 1, 2, 3, 3, 3, 4])}")
print(f"  Std Dev:     {statistics.stdev(data):.2f}")
print(f"  Variance:    {statistics.variance(data):.2f}")

# Harmonic and geometric means
print(f"  Harmonic:    {statistics.harmonic_mean(data):.2f}")
try:
    print(f"  Geometric:   {statistics.geometric_mean(data):.2f}")
except AttributeError:
    print(f"  Geometric:   Not available in this Python version")

print("\n" + "=" * 50)
print("1️⃣2️⃣ Complex Numbers in Detail")
print("=" * 50)

print("\n🎭 Complex Number Operations")
print("-" * 27)

# Creating complex numbers
print("🔢 Creating Complex Numbers:")
complex_examples = [
    3 + 4j,
    complex(2, -3),
    complex('5+2j'),
    1j,
    5 + 0j,
]

for comp in complex_examples:
    print(f"  {comp} → Real: {comp.real}, Imaginary: {comp.imag}")

# Complex arithmetic
print(f"\n➕ Complex Arithmetic:")
z1 = 3 + 4j
z2 = 1 - 2j
print(f"z1 = {z1}, z2 = {z2}")
print(f"  z1 + z2 = {z1 + z2}")
print(f"  z1 - z2 = {z1 - z2}")
print(f"  z1 * z2 = {z1 * z2}")
print(f"  z1 / z2 = {z1 / z2}")

# Complex functions
print(f"\n🎯 Complex Functions:")
z = 3 + 4j
print(f"z = {z}")
print(f"  abs(z):           {abs(z):.6f}")
print(f"  z.conjugate():    {z.conjugate()}")
print(f"  cmath.phase(z):   {cmath.phase(z):.6f} radians")
print(f"  cmath.polar(z):   {cmath.polar(z)}")
print(f"  cmath.rect(5, 0.927): {cmath.rect(5, 0.927)}")

# Complex mathematical functions
print(f"\n📐 Complex Math Functions:")
z = 1 + 1j
complex_functions = [
    ("cmath.sqrt(z)", cmath.sqrt(z)),
    ("cmath.exp(z)", cmath.exp(z)),
    ("cmath.log(z)", cmath.log(z)),
    ("cmath.sin(z)", cmath.sin(z)),
    ("cmath.cos(z)", cmath.cos(z)),
]

for func_name, result in complex_functions:
    print(f"  {func_name:15} = {result}")

print("\n" + "=" * 50)
print("1️⃣3️⃣ Number Performance and Memory")
print("=" * 50)

print("\n⚡ Number Performance Analysis")
print("-" * 28)

# Integer size comparison
print("💾 Integer Memory Usage:")
integers = [1, 100, 10000, 1000000, 10**100]
for num in integers:
    size = sys.getsizeof(num)
    print(f"  {str(num):20} → {size:4d} bytes")

# Float vs Decimal performance
print(f"\n⏱️ Performance Comparison:")

def test_float_operations(n=100000):
    total = 0.0
    for i in range(n):
        total += 0.1
    return total

def test_decimal_operations(n=100000):
    total = Decimal('0.0')
    increment = Decimal('0.1')
    for i in range(n):
        total += increment
    return total

# Time the operations
n = 10000
float_time = timeit.timeit(lambda: test_float_operations(n), number=1)
decimal_time = timeit.timeit(lambda: test_decimal_operations(n), number=1)

print(f"Operations: {n:,}")
print(f"  Float operations:   {float_time:.6f} seconds")
print(f"  Decimal operations: {decimal_time:.6f} seconds")
print(f"  Speed ratio:        {decimal_time/float_time:.1f}x slower for Decimal")

# Integer operations performance
print(f"\n🔢 Integer Operation Performance:")
large_int = 10**1000
operations = [
    ("Addition", lambda: large_int + large_int),
    ("Multiplication", lambda: large_int * 2),
    ("Power", lambda: 123 ** 456),
    ("String conversion", lambda: str(large_int)),
]

for op_name, op_func in operations:
    time_taken = timeit.timeit(op_func, number=100)
    print(f"  {op_name:20}: {time_taken:.6f} seconds (100 iterations)")

print("\n" + "=" * 50)
print("1️⃣4️⃣ Number Validation and Parsing")
print("=" * 50)

print("\n🔍 Number Validation Techniques")
print("-" * 30)

def validate_number(value, number_type='float'):
    """Comprehensive number validation"""
    if isinstance(value, (int, float, complex)):
        return True, value, "Already a number"
    
    if not isinstance(value, str):
        return False, None, "Not a string or number"
    
    # Clean the string
    cleaned = value.strip()
    
    if not cleaned:
        return False, None, "Empty string"
    
    try:
        if number_type == 'int':
            # Check for integer
            if '.' in cleaned or 'e' in cleaned.lower():
                return False, None, "Contains decimal point or scientific notation"
            result = int(cleaned)
            return True, result, "Valid integer"
        
        elif number_type == 'float':
            result = float(cleaned)
            if math.isnan(result):
                return False, None, "NaN value"
            if math.isinf(result):
                return False, None, "Infinite value"
            return True, result, "Valid float"
        
        elif number_type == 'complex':
            result = complex(cleaned)
            return True, result, "Valid complex number"
    
    except ValueError as e:
        return False, None, f"Conversion error: {e}"

print("🔍 Number Validation Examples:")
test_inputs = [
    ("123", "int"),
    ("123.45", "float"),
    ("3+4j", "complex"),
    ("not_a_number", "float"),
    ("", "float"),
    ("inf", "float"),
    ("nan", "float"),
    ("1.23e-4", "float"),
    ("0xFF", "int"),  # This will fail in int() without base
]

for test_input, num_type in test_inputs:
    is_valid, result, message = validate_number(test_input, num_type)
    status = "✅" if is_valid else "❌"
    print(f"  {status} '{test_input}' as {num_type}: {message}")
    if is_valid:
        print(f"      Result: {result} (type: {type(result).__name__})")

# Safe number parsing
def safe_parse_number(value, default=0):
    """Safely parse a number with fallback"""
    try:
        # Try integer first
        if isinstance(value, str) and '.' not in value and 'e' not in value.lower():
            return int(value)
        else:
            return float(value)
    except (ValueError, TypeError):
        return default

print(f"\n🛡️ Safe Number Parsing:")
unsafe_inputs = ["123", "45.67", "invalid", None, [], "1e6"]
for inp in unsafe_inputs:
    result = safe_parse_number(inp, -1)
    print(f"  safe_parse_number({inp!r}) = {result}")

print("\n" + "=" * 50)
print("1️⃣5️⃣ Financial and Scientific Computing")
print("=" * 50)

print("\n💰 Financial Calculations")
print("-" * 23)

# Compound interest calculation
def compound_interest(principal, rate, time, n=1):
    """Calculate compound interest"""
    # Using Decimal for precision
    P = Decimal(str(principal))
    r = Decimal(str(rate))
    t = Decimal(str(time))
    n = Decimal(str(n))
    
    amount = P * (1 + r/n) ** (n * t)
    interest = amount - P
    return float(amount), float(interest)

print("📈 Compound Interest Examples:")
investments = [
    (1000, 0.05, 10, 1),    # $1000, 5% annually, 10 years
    (5000, 0.03, 5, 12),    # $5000, 3% monthly, 5 years
    (10000, 0.07, 20, 4),   # $10000, 7% quarterly, 20 years
]

for principal, rate, time, compounding in investments:
    amount, interest = compound_interest(principal, rate, time, compounding)
    print(f"  ${principal:,} at {rate:.1%} for {time} years:")
    print(f"    Final amount: ${amount:,.2f}")
    print(f"    Interest earned: ${interest:,.2f}")
    print()

# Loan payment calculation
def loan_payment(principal, rate, years):
    """Calculate monthly loan payment"""
    P = Decimal(str(principal))
    r = Decimal(str(rate/12))  # Monthly rate
    n = Decimal(str(years * 12))  # Total payments
    
    if rate == 0:
        return float(P / n)
    
    payment = P * (r * (1 + r)**n) / ((1 + r)**n - 1)
    return float(payment)

print("🏠 Loan Payment Calculator:")
loans = [
    (200000, 0.045, 30),  # $200k house, 4.5%, 30 years
    (25000, 0.06, 5),     # $25k car, 6%, 5 years
    (10000, 0.0, 2),      # $10k no interest, 2 years
]

for principal, rate, years in loans:
    payment = loan_payment(principal, rate, years)
    total_paid = payment * years * 12
    total_interest = total_paid - principal
    
    print(f"  Loan: ${principal:,} at {rate:.1%} for {years} years")
    print(f"    Monthly payment: ${payment:,.2f}")
    print(f"    Total paid: ${total_paid:,.2f}")
    print(f"    Total interest: ${total_interest:,.2f}")
    print()

# Scientific calculations
print("🔬 Scientific Computing Examples:")

# Quadratic formula
def quadratic_formula(a, b, c):
    """Solve quadratic equation ax² + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        # Complex roots
        real_part = -b / (2*a)
        imag_part = cmath.sqrt(discriminant) / (2*a)
        root1 = complex(real_part, imag_part.imag)
        root2 = complex(real_part, -imag_part.imag)
    else:
        # Real roots
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
    
    return root1, root2

print("📐 Quadratic Formula Examples:")
equations = [
    (1, -5, 6),    # x² - 5x + 6 = 0
    (1, 0, -4),    # x² - 4 = 0
    (1, 2, 5),     # x² + 2x + 5 = 0 (complex roots)
]

for a, b, c in equations:
    root1, root2 = quadratic_formula(a, b, c)
    print(f"  {a}x² + {b}x + {c} = 0")
    print(f"    Roots: {root1}, {root2}")

# Statistical calculations
print(f"\n📊 Statistical Calculations:")
data_sets = [
    [85, 90, 78, 92, 88, 76, 95, 89],  # Test scores
    [12.5, 13.1, 11.8, 12.9, 13.5, 12.2, 13.8],  # Measurements
]

for i, data in enumerate(data_sets, 1):
    print(f"  Dataset {i}: {data}")
    print(f"    Mean: {statistics.mean(data):.2f}")
    print(f"    Median: {statistics.median(data):.2f}")
    print(f"    Std Dev: {statistics.stdev(data):.2f}")
    print(f"    Range: {max(data) - min(data):.2f}")
    print()

print("\n" + "=" * 50)
print("1️⃣6️⃣ Number Algorithms and Patterns")
print("=" * 50)

print("\n🧮 Mathematical Algorithms")
print("-" * 25)

# Prime number checker
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

print("🔢 Prime Number Checker:")
test_numbers = [2, 3, 4, 17, 25, 29, 97, 100, 101]
for num in test_numbers:
    result = is_prime(num)
    status = "✅ Prime" if result else "❌ Not Prime"
    print(f"  {num:3d}: {status}")

# Fibonacci sequence
def fibonacci_sequence(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(f"\n🌀 Fibonacci Sequence:")
fib_numbers = fibonacci_sequence(15)
print(f"First 15 Fibonacci numbers: {fib_numbers}")

# Golden ratio approximation
print(f"Golden ratio approximations:")
for i in range(10, 15):
    ratio = fib_numbers[i] / fib_numbers[i-1]
    print(f"  F({i})/F({i-1}) = {ratio:.10f}")

golden_ratio = (1 + math.sqrt(5)) / 2
print(f"Actual golden ratio: {golden_ratio:.10f}")

# Greatest Common Divisor (Euclidean algorithm)
def gcd_euclidean(a, b):
    """Calculate GCD using Euclidean algorithm"""
    steps = []
    while b:
        steps.append(f"{a} = {a//b} × {b} + {a%b}")
        a, b = b, a % b
    return a, steps

print(f"\n🔄 Euclidean Algorithm for GCD:")
pairs = [(48, 18), (100, 25), (17, 13)]
for a, b in pairs:
    gcd_result, steps = gcd_euclidean(a, b)
    print(f"GCD({a}, {b}) = {gcd_result}")
    for step in steps:
        print(f"  {step}")
    print()

# Number patterns
print(f"🎯 Number Patterns:")

# Perfect squares
squares = [i**2 for i in range(1, 11)]
print(f"Perfect squares: {squares}")

# Triangular numbers
triangular = [i*(i+1)//2 for i in range(1, 11)]
print(f"Triangular numbers: {triangular}")

# Factorials
factorials = [math.factorial(i) for i in range(10)]
print(f"Factorials: {factorials}")

print("\n" + "=" * 50)
print("1️⃣7️⃣ Number Security and Cryptography")
print("=" * 50)

print("\n🔒 Cryptographic Number Operations")
print("-" * 33)

# Modular arithmetic
def mod_pow(base, exp, mod):
    """Efficient modular exponentiation"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

print("🔐 Modular Exponentiation:")
examples = [
    (3, 7, 11),   # 3^7 mod 11
    (5, 13, 17),  # 5^13 mod 17
    (2, 100, 13), # 2^100 mod 13
]

for base, exp, mod in examples:
    result = mod_pow(base, exp, mod)
    builtin_result = pow(base, exp, mod)  # Python's built-in
    print(f"  {base}^{exp} mod {mod} = {result} (builtin: {builtin_result})")

# Simple RSA example (educational only)
def simple_rsa_demo():
    """Simple RSA demonstration (educational only)"""
    # Choose small primes (in real RSA, these would be much larger)
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e (commonly 65537 in practice)
    e = 17
    
    # Calculate d (private key)
    d = pow(e, -1, phi)  # Modular inverse
    
    return (e, n), (d, n), p, q

print(f"\n🔑 Simple RSA Demo (Educational):")
public_key, private_key, p, q = simple_rsa_demo()
e, n = public_key
d, n_private = private_key

print(f"Primes: p = {p}, q = {q}")
print(f"n = p × q = {n}")
print(f"φ(n) = (p-1)(q-1) = {(p-1)*(q-1)}")
print(f"Public key: (e={e}, n={n})")
print(f"Private key: (d={d}, n={n_private})")

# Encrypt/decrypt a small message
message = 42
encrypted = pow(message, e, n)
decrypted = pow(encrypted, d, n)

print(f"\nMessage: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

# Hash function simulation
def simple_hash(data, mod=1000000007):
    """Simple hash function for demonstration"""
    hash_value = 0
    for char in str(data):
        hash_value = (hash_value * 31 + ord(char)) % mod
    return hash_value

print(f"\n🔍 Simple Hash Function:")
data_samples = ["hello", "world", "Python", "12345", "hello "]
for data in data_samples:
    hash_val = simple_hash(data)
    print(f"  hash('{data}') = {hash_val}")

print("\n" + "=" * 50)
print("1️⃣8️⃣ Number Best Practices")
print("=" * 50)

print("\n💡 Number Best Practices Guide")
print("-" * 29)

print("""
🎯 Performance Best Practices:
✅ Use int for whole numbers (no size limit in Python 3)
✅ Use float for general decimal numbers
✅ Use Decimal for financial calculations requiring precision
✅ Use complex for mathematical/scientific applications
✅ Cache expensive calculations when possible
✅ Use built-in functions (sum, max, min) over loops

🔒 Precision Best Practices:
✅ Use Decimal for financial calculations
✅ Be aware of floating-point precision limitations
✅ Use math.isclose() for float comparisons
✅ Consider rounding strategies carefully
✅ Use fractions for exact rational arithmetic
✅ Validate number inputs in user-facing applications

💰 Financial Best Practices:
✅ Always use Decimal for monetary calculations
✅ Store money as integers (cents) when possible
✅ Round currency consistently
✅ Handle currency conversion carefully
✅ Validate financial inputs strictly
✅ Use appropriate rounding modes

🧪 Scientific Best Practices:
✅ Understand your precision requirements
✅ Use appropriate data types (float64, complex, etc.)
✅ Handle special values (inf, nan) appropriately
✅ Consider numerical stability in algorithms
✅ Use vectorized operations when possible
✅ Document units and ranges clearly
""")

# Example of good number practices
print("\n📋 Example: Number Utilities Class")

class NumberUtils:
    """Example of good number handling practices"""
    
    @staticmethod
    def safe_divide(a, b, default=None):
        """Safe division with error handling"""
        try:
            if b == 0:
                return default
            return a / b
        except (TypeError, ValueError):
            return default
    
    @staticmethod
    def is_close(a, b, rel_tol=1e-9, abs_tol=0.0):
        """Check if two floats are approximately equal"""
        return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    
    @staticmethod
    def clamp(value, min_val, max_val):
        """Clamp a value between min and max"""
        return max(min_val, min(value, max_val))
    
    @staticmethod
    def percentage_change(old_value, new_value):
        """Calculate percentage change"""
        if old_value == 0:
            return float('inf') if new_value > 0 else float('-inf') if new_value < 0 else 0
        return ((new_value - old_value) / old_value) * 100

print("Testing NumberUtils:")

# Test safe division
print("Safe Division:")
test_cases = [(10, 2), (10, 0), ("10", 2)]
for a, b in test_cases:
    result = NumberUtils.safe_divide(a, b, "undefined")
    print(f"  safe_divide({a}, {b}) = {result}")

# Test float comparison
print(f"\nFloat Comparison:")
comparisons = [(0.1 + 0.2, 0.3), (1.0, 1.0000000001)]
for a, b in comparisons:
    close = NumberUtils.is_close(a, b)
    equal = (a == b)
    print(f"  {a} ≈ {b}: is_close={close}, equal={equal}")

# Test clamping
print(f"\nClamping:")
clamp_tests = [(5, 0, 10), (-5, 0, 10), (15, 0, 10)]
for value, min_val, max_val in clamp_tests:
    result = NumberUtils.clamp(value, min_val, max_val)
    print(f"  clamp({value}, {min_val}, {max_val}) = {result}")

# Test percentage change
print(f"\nPercentage Change:")
change_tests = [(100, 120), (50, 25), (0, 10)]
for old, new in change_tests:
    change = NumberUtils.percentage_change(old, new)
    print(f"  {old} → {new}: {change:.1f}% change")

print("\n" + "=" * 50)
print("1️⃣9️⃣ Number Testing and Debugging")
print("=" * 50)

print("\n🧪 Number Testing Strategies")
print("-" * 26)

def comprehensive_number_test(func, test_cases, tolerance=1e-9):
    """Test a numerical function with various cases"""
    print(f"Testing function: {func.__name__}")
    
    for i, (inputs, expected) in enumerate(test_cases, 1):
        try:
            if isinstance(inputs, tuple):
                result = func(*inputs)
            else:
                result = func(inputs)
            
            # Handle different comparison types
            if isinstance(expected, float) and isinstance(result, float):
                passed = abs(result - expected) <= tolerance
                status = "✅ PASS" if passed else "❌ FAIL"
            else:
                passed = result == expected
                status = "✅ PASS" if passed else "❌ FAIL"
            
            print(f"  Test {i}: {status}")
            print(f"    Input: {inputs}")
            print(f"    Expected: {expected}")
            print(f"    Got: {result}")
            
            if not passed and isinstance(expected, float):
                print(f"    Difference: {abs(result - expected)}")
                
        except Exception as e:
            print(f"  Test {i}: ❌ ERROR - {e}")
        print()

# Test the quadratic formula function
print("🔍 Testing Quadratic Formula:")
quadratic_test_cases = [
    ((1, -5, 6), (3.0, 2.0)),       # Real roots
    ((1, 0, -4), (2.0, -2.0)),      # Real roots
    ((1, -2, 1), (1.0, 1.0)),       # Repeated root
]

comprehensive_number_test(lambda a, b, c: quadratic_formula(a, b, c), quadratic_test_cases)

# Number debugging helper
def debug_number(num, label="Number"):
    """Debug helper for number analysis"""
    print(f"🔍 {label} Debug Info:")
    print(f"  Value: {num}")
    print(f"  Type: {type(num)}")
    print(f"  Memory: {sys.getsizeof(num)} bytes")
    
    if isinstance(num, int):
        print(f"  Bit length: {num.bit_length()}")
        print(f"  Binary: {bin(num)}")
        print(f"  Hex: {hex(num)}")
    
    elif isinstance(num, float):
        print(f"  Is finite: {math.isfinite(num)}")
        print(f"  Is integer: {num.is_integer()}")
        if math.isfinite(num):
            print(f"  Hex representation: {num.hex()}")
            print(f"  As fraction: {Fraction(num).limit_denominator(1000)}")
    
    elif isinstance(num, complex):
        print(f"  Real part: {num.real}")
        print(f"  Imaginary part: {num.imag}")
        print(f"  Magnitude: {abs(num)}")
        print(f"  Phase: {cmath.phase(num)} radians")

print("🔍 Number Debugging Examples:")
debug_number(42, "Integer")
print()
debug_number(3.14159, "Float")
print()
debug_number(3+4j, "Complex")

print("\n" + "=" * 50)
print("2️⃣0️⃣ Practice Exercises")
print("=" * 50)

print("\n🏋️ Number Practice Challenges")
print("-" * 29)

print("""
Challenge 1: Create a number base converter
Challenge 2: Build a simple calculator class
Challenge 3: Implement numerical integration
Challenge 4: Create a statistics calculator
Challenge 5: Build a financial calculator
""")

# Challenge 1: Number base converter
class BaseConverter:
    """Convert numbers between different bases"""
    
    @staticmethod
    def to_base(number, base):
        """Convert decimal number to given base"""
        if number == 0:
            return "0"
        
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        
        while number:
            result = digits[number % base] + result
            number //= base
        
        return result
    
    @staticmethod
    def from_base(number_str, base):
        """Convert number from given base to decimal"""
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number_str = number_str.upper()
        result = 0
        
        for digit in number_str:
            result = result * base + digits.index(digit)
        
        return result

print("Challenge 1 - Base Converter:")
converter = BaseConverter()
test_number = 255

for base in [2, 8, 16, 36]:
    converted = converter.to_base(test_number, base)
    back_converted = converter.from_base(converted, base)
    print(f"  {test_number} in base {base:2d}: {converted:>8} (back: {back_converted})")

# Challenge 2: Simple Calculator
class Calculator:
    """Simple calculator with memory and history"""
    
    def __init__(self):
        self.memory = 0
        self.history = []
    
    def add(self, a, b=None):
        if b is None:
            b = self.memory
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b=None):
        if b is None:
            b = self.memory
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b=None):
        if b is None:
            b = self.memory
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b=None):
        if b is None:
            b = self.memory
        if b == 0:
            raise ValueError("Division by zero")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def store(self, value):
        self.memory = value
        self.history.append(f"Stored {value} in memory")
    
    def recall(self):
        return self.memory
    
    def clear_history(self):
        self.history = []

print(f"\nChallenge 2 - Calculator:")
calc = Calculator()
calc.store(10)
result1 = calc.add(5, 3)
result2 = calc.multiply(result1, 2)
result3 = calc.divide(result2)

print(f"Calculator history:")
for entry in calc.history:
    print(f"  {entry}")

# Challenge 3: Numerical Integration
def numerical_integration(func, a, b, n=1000):
    """Numerical integration using trapezoidal rule"""
    h = (b - a) / n
    result = (func(a) + func(b)) / 2
    
    for i in range(1, n):
        x = a + i * h
        result += func(x)
    
    return result * h

print(f"\nChallenge 3 - Numerical Integration:")
# Integrate x^2 from 0 to 2 (analytical result: 8/3 ≈ 2.667)
def square_function(x):
    return x ** 2

integral_result = numerical_integration(square_function, 0, 2, 10000)
analytical_result = 8/3
error = abs(integral_result - analytical_result)

print(f"  ∫₀² x² dx")
print(f"  Numerical result: {integral_result:.6f}")
print(f"  Analytical result: {analytical_result:.6f}")
print(f"  Error: {error:.6f}")

print("\n" + "=" * 70)
print("🎉 Congratulations! You've completed the Python Numbers Guide!")
print("🏆 You now have comprehensive knowledge of numerical computing!")
print("=" * 70)

print(f"""
🎯 What You've Mastered:

✅ All Python number types (int, float, complex, decimal, fraction)
✅ Number literals and representations
✅ Arithmetic operations and precedence
✅ Type conversion and casting
✅ Built-in mathematical functions
✅ Math module and advanced functions
✅ Number formatting and display
✅ High-precision arithmetic with Decimal
✅ Exact arithmetic with Fractions
✅ Random numbers and statistics
✅ Complex number operations
✅ Performance and memory considerations
✅ Number validation and parsing
✅ Financial and scientific computing
✅ Mathematical algorithms
✅ Cryptographic number operations
✅ Best practices and debugging

🚀 Next Steps:
1. Practice with real numerical data
2. Build mathematical applications
3. Learn NumPy for scientific computing
4. Explore data analysis with pandas
5. Study machine learning mathematics
6. Work with financial modeling
7. Dive into cryptography

💡 Remember:
- Choose the right number type for your use case
- Use Decimal for financial calculations
- Be aware of floating-point limitations
- Validate inputs in production code
- Consider performance implications
- Handle edge cases (inf, nan, zero division)
- Test numerical algorithms thoroughly

Keep calculating and building! 🔢✨
""")

# Quick reference card
print(f"""
📋 Numbers Quick Reference:

Types:
int               # Integers: 42, -17, 0
float             # Decimals: 3.14, 1e6
complex           # Complex: 3+4j, complex(2,3)
Decimal           # High precision: Decimal('0.1')
Fraction          # Exact ratios: Fraction(1,3)

Operations:
+, -, *, /        # Basic arithmetic
//, %             # Floor division, modulus
**                # Exponentiation
divmod(a, b)      # Returns (a//b, a%b)

Built-in Functions:
abs(x)            # Absolute value
round(x, n)       # Round to n decimal places
min(), max()      # Minimum, maximum
sum()             # Sum of sequence
pow(x, y, z)      # x^y mod z (optional)

Math Module:
import math
math.sqrt(x)      # Square root
math.log(x)       # Natural logarithm
math.sin(x)       # Trigonometric functions
math.pi, math.e   # Mathematical constants

Formatting:
f"{x:.2f}"        # 2 decimal places
f"{x:,.0f}"       # Comma separator
f"{x:e}"          # Scientific notation
f"{x:.2%}"        # Percentage

Validation:
isinstance(x, int)     # Check type
math.isfinite(x)       # Check if finite
math.isnan(x)          # Check if NaN
str.isdigit()          # Check if string is digits

Best Practices:
- Use Decimal for money
- Use math.isclose() for float comparison
- Handle division by zero
- Validate user input
- Choose appropriate precision
""")

# End of comprehensive numbers guide