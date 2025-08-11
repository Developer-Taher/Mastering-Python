# =====================================
# Escape Sequences and String Formatting
# Complete Tutorial Guide
# =====================================

"""
What are Escape Sequences?
Special characters that start with backslash (\) and represent characters
that are difficult or impossible to type directly in strings.
They control formatting and special actions in text output.
"""

print("=" * 60)
print("PART 1: ESCAPE SEQUENCES")
print("=" * 60)

name = 'John Doe'
answer = 42

# -------------------------------------
# \n - Newline Character
# -------------------------------------
print("1. \\n - Newline Character")
print("-" * 30)

# Basic newline usage
print("Hello,\nWorld!")
print("Line 1\nLine 2\nLine 3")

# In your example (with correction)
print('Hello,\nMy name is ' + name + ' and the answer is ' + str(answer))

# Multiple newlines
print("First line\n\nThird line (skipped one)")

print("\n" + "=" * 40)

# -------------------------------------
# \t - Tab Character
# -------------------------------------
print("2. \\t - Tab Character")
print("-" * 30)

# Basic tab usage
print("Name:\tJohn")
print("Age:\t25")
print("City:\tNew York")

# In your example
print('Hello,\tMy name is ' + name + ' and the answer is ' + str(answer))

# Creating columns with tabs
print("Product\tPrice\tQuantity")
print("Apple\t$2.50\t10")
print("Banana\t$1.20\t15")

print("\n" + "=" * 40)

# -------------------------------------
# \r - Carriage Return
# -------------------------------------
print("3. \\r - Carriage Return")
print("-" * 30)

# Carriage return moves cursor to beginning of line
print("This will be overwritten\rNew text")

# In your example
print('Hello, world\rMy name is ' + name)

# Practical use: Progress indicator
import time
for i in range(6):
    print(f"\rLoading: {'█' * i}{'░' * (5-i)} {i*20}%", end="")
    time.sleep(0.3)
print("\rLoading complete!     ")

print("\n" + "=" * 40)

# -------------------------------------
# \b - Backspace Character
# -------------------------------------
print("4. \\b - Backspace Character")
print("-" * 30)

# Backspace removes previous character
print("Hello World\b!")  # Removes 'd', result: "Hello Worl!"
print("Programming\b\b\bing")  # Removes 'mm', adds 'ing'

# In your example (corrected)
print('Hello, \bMy name is ' + name + ' and the answer is ' + str(answer))

print("\n" + "=" * 40)

# -------------------------------------
# \f - Form Feed
# -------------------------------------
print("5. \\f - Form Feed")
print("-" * 30)

# Form feed (rarely used in modern programming)
print("Before form feed\fAfter form feed")

# In your example
print('Hello,\fMy name is ' + name + ' and the answer is ' + str(answer))

print("\n" + "=" * 40)

# -------------------------------------
# \v - Vertical Tab
# -------------------------------------
print("6. \\v - Vertical Tab")
print("-" * 30)

# Vertical tab (rarely used)
print("Line 1\vLine 2")

# In your example
print('Hello,\vMy name is ' + name + ' and the answer is ' + str(answer))

print("\n" + "=" * 40)

# -------------------------------------
# \a - Bell/Alert Character
# -------------------------------------
print("7. \\a - Bell/Alert Character")
print("-" * 30)

# Bell character (may produce sound on some systems)
print("Alert!\aThis might beep")

# In your example
print('Hello,\aMy name is ' + name + ' and the answer is ' + str(answer))

print("\n" + "=" * 40)

# -------------------------------------
# Additional Escape Sequences
# -------------------------------------
print("8. Additional Escape Sequences")
print("-" * 30)

# Backslash
print("This is a backslash: \\")

# Single quote in single-quoted string
print('It\'s a beautiful day')

# Double quote in double-quoted string
print("He said, \"Hello!\"")

# Both quotes using escape
print('She said, "It\'s amazing!"')

# Unicode characters
print("Unicode heart: \u2764")
print("Unicode star: \u2605")

# Raw strings (ignore escape sequences)
print(r"Raw string: \n \t \r (not processed)")

print("\n" + "=" * 60)
print("PART 2: STRING FORMATTING")
print("=" * 60)

# -------------------------------------
# Method 1: % Formatting (Old Style)
# -------------------------------------
print("1. % Formatting (Printf-style)")
print("-" * 40)

name = "Alice"
age = 25
height = 5.6
grade = 87.5

# %s - string
print("Hello, %s!" % name)

# %d - integer
print("Age: %d years" % age)

# %f - float
print("Height: %f feet" % height)
print("Height: %.1f feet" % height)  # 1 decimal place
print("Height: %.2f feet" % height)  # 2 decimal places

# %% - literal percent sign
print("Grade: %.1f%% (%.1f percent)" % (grade, grade))

# Multiple values
print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))

# Width and alignment
print("Name: %10s|" % name)      # Right-aligned, width 10
print("Name: %-10s|" % name)     # Left-aligned, width 10
print("Number: %05d" % 42)       # Zero-padded, width 5

print("\n" + "=" * 40)

# -------------------------------------
# Method 2: .format() Method
# -------------------------------------
print("2. .format() Method")
print("-" * 40)

# Basic usage
print("Hello, {}!".format(name))
print("Age: {} years".format(age))
print("Height: {:.2f} feet".format(height))

# Multiple values
print("Name: {}, Age: {}, Height: {:.1f}".format(name, age, height))

# With positional arguments
print("Name: {0}, Age: {1}, repeated name: {0}".format(name, age))

# With keyword arguments
print("Name: {student_name}, Grade: {student_grade:.1f}%".format(
    student_name=name, student_grade=grade))

# Number formatting
print("Price: ${:.2f}".format(1234.5))
print("Large number: {:,}".format(1000000))
print("Percentage: {:.1%}".format(0.875))

# Alignment and width
print("Left: '{:<10}'".format(name))
print("Right: '{:>10}'".format(name))
print("Center: '{:^10}'".format(name))
print("Fill: '{:*^10}'".format(name))

print("\n" + "=" * 40)

# -------------------------------------
# Method 3: f-strings (Best Practice)
# -------------------------------------
print("3. f-strings (Python 3.6+)")
print("-" * 40)

# Basic usage
print(f"Hello, {name}!")
print(f"Age: {age} years")
print(f"Height: {height:.2f} feet")

# Expressions inside f-strings
print(f"Next year, {name} will be {age + 1} years old")
print(f"Area of square with side {5}: {5 ** 2}")

# Method calls
message = "hello world"
print(f"Uppercase: {message.upper()}")
print(f"Title case: {message.title()}")

# Number formatting
price = 1234.567
print(f"Price: ${price:.2f}")
print(f"Large number: {1000000:,}")
print(f"Percentage: {0.875:.1%}")
print(f"Scientific: {price:.2e}")

# Alignment and width
print(f"Left: '{name:<10}'")
print(f"Right: '{name:>10}'")
print(f"Center: '{name:^10}'")
print(f"Fill: '{name:*^10}'")

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Current time: {now:%Y-%m-%d %H:%M:%S}")

print("\n" + "=" * 40)

# -------------------------------------
# Comparison of All Methods
# -------------------------------------
print("4. Comparison of All Methods")
print("-" * 40)

name = "Bob"
age = 30
salary = 75000.50

print("% formatting:")
print("Employee: %s, Age: %d, Salary: $%.2f" % (name, age, salary))

print("\n.format() method:")
print("Employee: {}, Age: {}, Salary: ${:.2f}".format(name, age, salary))

print("\nf-string:")
print(f"Employee: {name}, Age: {age}, Salary: ${salary:.2f}")

print("\n" + "=" * 40)

# -------------------------------------
# Advanced f-string Features
# -------------------------------------
print("5. Advanced f-string Features")
print("-" * 40)

# Debugging (Python 3.8+)
x = 10
y = 20
# print(f"{x=}, {y=}, {x+y=}")  # Shows variable names and values

# Nested f-strings
width = 10
precision = 2
value = 123.456
print(f"Value: {value:{width}.{precision}f}")

# Conditional expressions
score = 85
print(f"Grade: {score} ({'Pass' if score >= 60 else 'Fail'})")

# Dictionary access
person = {'name': 'Charlie', 'age': 35}
print(f"Person: {person['name']}, Age: {person['age']}")

# List access
colors = ['red', 'green', 'blue']
print(f"Colors: {colors[0]}, {colors[1]}, {colors[2]}")

print("\n" + "=" * 40)

# -------------------------------------
# Practical Examples
# -------------------------------------
print("6. Practical Examples")
print("-" * 40)

# Example 1: Creating a receipt
def create_receipt(items):
    receipt = "RECEIPT\n" + "="*30 + "\n"
    total = 0
    for item, price in items:
        receipt += f"{item:<20} ${price:>6.2f}\n"
        total += price
    receipt += "-"*30 + "\n"
    receipt += f"{'TOTAL':<20} ${total:>6.2f}\n"
    receipt += "="*30
    return receipt

items = [("Coffee", 4.50), ("Sandwich", 8.75), ("Cookie", 2.25)]
print(create_receipt(items))

print("\n" + "-" * 40)

# Example 2: Progress report
def progress_report(tasks):
    print("PROJECT PROGRESS REPORT")
    print("="*50)
    for task, completed, total in tasks:
        percentage = (completed / total) * 100
        bar_length = 20
        filled = int(bar_length * completed / total)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"{task:<15} [{bar}] {percentage:5.1f}% ({completed}/{total})")

tasks = [
    ("Frontend", 8, 10),
    ("Backend", 6, 8),
    ("Testing", 3, 5),
    ("Documentation", 2, 4)
]
progress_report(tasks)

print("\n" + "-" * 40)

# Example 3: Data table
def create_table(headers, rows):
    # Calculate column widths
    widths = [len(header) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    
    # Create format string
    format_str = " | ".join(f"{{:<{width}}}" for width in widths)
    
    # Print table
    print(format_str.format(*headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_str.format(*[str(cell) for cell in row]))

headers = ["Name", "Age", "City", "Salary"]
data = [
    ["Alice", 28, "New York", 75000],
    ["Bob", 32, "San Francisco", 95000],
    ["Charlie", 25, "Chicago", 65000]
]
create_table(headers, data)

print("\n" + "=" * 60)
print("SUMMARY AND BEST PRACTICES")
print("=" * 60)

print("""
ESCAPE SEQUENCES SUMMARY:
\\n  - New line (most common)
\\t  - Tab character
\\r  - Carriage return
\\b  - Backspace
\\f  - Form feed
\\v  - Vertical tab
\\a  - Bell/alert
\\\\  - Literal backslash
\\'  - Single quote
\\"  - Double quote

STRING FORMATTING COMPARISON:

1. % Formatting (Old, avoid in new code):
   "Hello %s, you are %d years old" % (name, age)

2. .format() Method (Good for complex cases):
   "Hello {}, you are {} years old".format(name, age)

3. f-strings (Best practice, Python 3.6+):
   f"Hello {name}, you are {age} years old"

BEST PRACTICES:
✅ Use f-strings for most cases (readable, fast, powerful)
✅ Use .format() for complex templates or older Python versions
✅ Use raw strings r"" when you need literal backslashes
✅ Be consistent with your formatting choice in a project
❌ Avoid % formatting in new code
❌ Don't mix formatting styles unnecessarily

COMMON FORMATTING PATTERNS:
- Numbers: f"{value:.2f}" (2 decimal places)
- Percentages: f"{value:.1%}" (percentage with 1 decimal)
- Large numbers: f"{value:,}" (with commas)
- Padding: f"{text:>10}" (right-align in 10 chars)
- Dates: f"{date:%Y-%m-%d}" (custom date format)
""")

# Final comprehensive example
def create_employee_report(employees):
    """Create a comprehensive employee report"""
    report = f"""
{'='*60}
                    EMPLOYEE REPORT
{'='*60}
Generated on: {datetime.now():%Y-%m-%d at %H:%M:%S}

"""
    
    for i, emp in enumerate(employees, 1):
        name, age, department, salary, performance = emp
        
        # Performance bar
        stars = "★" * performance + "☆" * (5 - performance)
        
        report += f"""
Employee #{i}:
{'-'*30}
Name:        {name}
Age:         {age} years old
Department:  {department}
Salary:      ${salary:,.2f}
Performance: {stars} ({performance}/5)
Annual Tax:  ${salary * 0.25:,.2f}
Net Salary:  ${salary * 0.75:,.2f}

"""
    
    total_salary = sum(emp[3] for emp in employees)
    avg_age = sum(emp[1] for emp in employees) / len(employees)
    
    report += f"""
{'='*60}
SUMMARY:
Total Employees: {len(employees)}
Average Age:     {avg_age:.1f} years
Total Salaries:  ${total_salary:,.2f}
Average Salary:  ${total_salary/len(employees):,.2f}
{'='*60}
"""
    
    return report

# Sample data
employees = [
    ("John Smith", 28, "Engineering", 85000, 4),
    ("Sarah Johnson", 32, "Marketing", 72000, 5),
    ("Mike Brown", 29, "Sales", 68000, 3),
    ("Lisa Davis", 35, "Engineering", 92000, 4)
]

print(create_employee_report(employees))