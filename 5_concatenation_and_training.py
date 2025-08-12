# =====================================
# String Concatenation in Python
# Complete Tutorial and Guide
# =====================================

"""
What is String Concatenation?
It's the process of joining or combining two or more strings together to form a single string
Example: "Hello" + " " + "World" = "Hello World"
"""

print("=" * 50)
print("1. String Concatenation Basics")
print("=" * 50)

# -------------------------------------
# Method 1: Using the + operator
# -------------------------------------

first_name = "John"
last_name = "Doe"

# Concatenating strings using +
full_name = first_name + " " + last_name
print("Full name:", full_name)

# You can concatenate multiple strings
greeting = "Hello" + " " + "there" + " " + full_name
print(greeting)

# Concatenating strings with variables
age = "25"  # Note: this is a string, not int
message = "I am " + age + " years old"
print(message)

print("\n" + "=" * 50)
print("2. Common Concatenation Problems")
print("=" * 50)

# Common mistake: trying to concatenate string with number
name = "Alice"
age_number = 30  # int

# This will give TypeError:
# message = "My name is " + name + " and I am " + age_number + " years old"
# print(message)  # TypeError!

# Solution: convert number to string
message_correct = "My name is " + name + " and I am " + str(age_number) + " years old"
print("Correct way:", message_correct)

print("\n" + "=" * 50)
print("3. Advanced Concatenation Methods")
print("=" * 50)

# -------------------------------------
# Method 2: f-strings (Best Practice)
# -------------------------------------

name = "Sarah"
age = 22
salary = 5000.50

# f-string - newest and easiest method
message_f = f"My name is {name} and I am {age} years old with salary ${salary}"
print("f-string:", message_f)

# You can perform calculations inside f-strings
future_age = f"Next year I will be {age + 1} years old"
print(future_age)

# Formatting numbers in f-strings
formatted_salary = f"My salary is ${salary:.2f}"
print("Formatted salary:", formatted_salary)

# -------------------------------------
# Method 3: .format() method
# -------------------------------------

template = "My name is {} and I am {} years old"
formatted_message = template.format(name, age)
print(".format():", formatted_message)

# With position numbers
template2 = "My name is {0} and I am {1} years old, again my name is {0}"
formatted_message2 = template2.format(name, age)
print("With positions:", formatted_message2)

# With variable names
template3 = "My name is {student_name} and I am {student_age} years old"
formatted_message3 = template3.format(student_name=name, student_age=age)
print("With names:", formatted_message3)

print("\n" + "=" * 50)
print("4. Joining Lists and Elements")
print("=" * 50)

# -------------------------------------
# Joining list elements: join() method
# -------------------------------------

# List of words
words = ["Python", "is", "an", "awesome", "language"]

# Join with space
sentence = " ".join(words)
print("Joined sentence:", sentence)

# Join with comma
comma_separated = ", ".join(words)
print("Comma separated:", comma_separated)

# Join without separator
no_space = "".join(words)
print("No spaces:", no_space)

# Joining numbers (must convert to strings first)
numbers = [1, 2, 3, 4, 5]
numbers_str = [str(num) for num in numbers]
joined_numbers = "-".join(numbers_str)
print("Joined numbers:", joined_numbers)

print("\n" + "=" * 50)
print("5. Practical Examples")
print("=" * 50)

# Example 1: Building URL
domain = "www.example.com"
page = "articles"
article_id = "123"
url = "https://" + domain + "/" + page + "/" + article_id
print("Traditional URL:", url)

# Same example with f-string
url_f = f"https://{domain}/{page}/{article_id}"
print("URL with f-string:", url_f)

# Example 2: Building file path
folder = "Documents"
subfolder = "Projects"
filename = "project.py"
filepath = folder + "/" + subfolder + "/" + filename
print("File path:", filepath)

# Example 3: Building SQL query
table_name = "users"
user_id = 42
query = f"SELECT * FROM {table_name} WHERE id = {user_id}"
print("SQL query:", query)

print("\n" + "=" * 50)
print("6. Tips and Best Practices")
print("=" * 50)

# Tip 1: Use f-strings for simple cases
student = "Mike"
grade = 85
simple_msg = f"Student {student} got grade {grade}"
print("Simple:", simple_msg)

# Tip 2: Use join() for long lists
long_list = ["item" + str(i) for i in range(1, 11)]
efficient_join = " - ".join(long_list)
print("Long list:", efficient_join)

# Tip 3: Avoid + with long lists (slow)
# Instead of:
# result = ""
# for item in long_list:
#     result = result + item + " "  # Slow!

# Use:
result_fast = " ".join(long_list)
print("Fast way:", result_fast[:50] + "...")

print("\n" + "=" * 50)
print("7. Advanced Applications")
print("=" * 50)

# Application 1: Building HTML table
def create_html_table(data):
    """Create HTML table from data"""
    html = "<table>\n"
    for row in data:
        html += "  <tr>\n"
        for cell in row:
            html += f"    <td>{cell}</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html

sample_data = [
    ["Name", "Age", "Job"],
    ["John", "25", "Developer"],
    ["Sarah", "30", "Designer"]
]
html_table = create_html_table(sample_data)
print("HTML Table:")
print(html_table)

# Application 2: Generating CSS code
def generate_css_class(class_name, properties):
    """Generate CSS class"""
    css = f".{class_name} {{\n"
    for prop, value in properties.items():
        css += f"  {prop}: {value};\n"
    css += "}"
    return css

css_properties = {
    "color": "blue",
    "font-size": "16px",
    "margin": "10px"
}
css_code = generate_css_class("my-button", css_properties)
print("\nCSS Code:")
print(css_code)

print("\n" + "=" * 50)
print("8. Common Errors and Solutions")
print("=" * 50)

# Error 1: Forgetting spaces
first = "Hello"
second = "World"
wrong = first + second  # "HelloWorld"
correct = first + " " + second  # "Hello World"
print("Wrong:", wrong)
print("Correct:", correct)

# Error 2: Mixing types
name = "Sarah"
score = 95
# wrong = "Score: " + score  # TypeError
correct_conversion = "Score: " + str(score)
correct_f_string = f"Score: {score}"
print("Correct conversion:", correct_conversion)
print("Correct f-string:", correct_f_string)

# Error 3: Using + with None
value = None
# wrong = "Value: " + value  # TypeError
safe_way = f"Value: {value if value is not None else 'undefined'}"
print("Safe way:", safe_way)

print("\n" + "=" * 50)
print("9. Performance Comparison")
print("=" * 50)

import time

# Measuring performance of different methods
iterations = 10000

# + method (slow for long strings)
start_time = time.time()
result = ""
for i in range(1000):
    result += "x"
plus_time = time.time() - start_time
print(f"+ method time: {plus_time:.4f} seconds")

# join method (fast)
start_time = time.time()
result = "".join(["x" for i in range(1000)])
join_time = time.time() - start_time
print(f"join method time: {join_time:.4f} seconds")

print(f"join is {plus_time/join_time:.1f}x faster")

print("\n" + "=" * 50)
print("10. Summary and Review")
print("=" * 50)

print("""
String Concatenation Methods Summary:

1. + operator: Simple but slow with long strings
   Example: "Hello" + " " + "World"

2. f-strings: Best for general use (Python 3.6+)
   Example: f"Hello {name}"

3. .format(): Good for complex templates
   Example: "Hello {}".format(name)

4. .join(): Best for lists
   Example: " ".join(["Hello", "World"])

5. % formatting: Old style, not recommended
   Example: "Hello %s" % name

Important Tips:
✅ Use f-strings in most cases
✅ Use join() for long lists
✅ Convert numbers to strings before concatenation
❌ Avoid + with long lists
❌ Don't forget spaces between words
""")

# Final comprehensive example
def create_user_profile(name, age, email, hobbies):
    """Create complete user profile"""
    profile = f"""
{'='*40}
         USER PROFILE
{'='*40}
Name: {name}
Age: {age} years old
Email: {email}
Hobbies: {', '.join(hobbies)}
Created: {time.strftime('%Y-%m-%d %H:%M:%S')}
{'='*40}
    """
    return profile

user_profile = create_user_profile(
    "John Smith", 
    28, 
    "john@example.com", 
    ["Programming", "Reading", "Travel"]
)
print(user_profile)

# -------------------------------------
# Practice Exercises
# -------------------------------------

print("\n" + "=" * 50)
print("11. Practice Exercises")
print("=" * 50)

# Exercise 1: Create email signature
def create_email_signature(name, title, company, phone):
    signature = f"""
Best regards,
{name}
{title}
{company}
Phone: {phone}
    """
    return signature.strip()

signature = create_email_signature("Jane Doe", "Software Engineer", "Tech Corp", "+1-555-0123")
print("Email Signature:")
print(signature)

# Exercise 2: Format currency
def format_currency(amount, currency="USD"):
    if currency == "USD":
        return f"${amount:,.2f}"
    elif currency == "EUR":
        return f"€{amount:,.2f}"
    else:
        return f"{amount:,.2f} {currency}"

prices = [1234.56, 9876.54, 100.00]
for price in prices:
    print(f"Price: {format_currency(price)}")

# Exercise 3: Create command line output
def create_progress_bar(current, total, width=50):
    percentage = current / total
    filled_width = int(width * percentage)
    bar = "█" * filled_width + "░" * (width - filled_width)
    return f"[{bar}] {percentage:.1%} ({current}/{total})"

print("\nProgress Examples:")
for i in [25, 50, 75, 100]:
    print(create_progress_bar(i, 100))

# Exercise 4: Generate configuration file
def generate_config(settings):
    config_lines = ["[SETTINGS]"]
    for key, value in settings.items():
        config_lines.append(f"{key}={value}")
    return "\n".join(config_lines)

app_settings = {
    "debug": "true",
    "port": "8080",
    "host": "localhost",
    "database_url": "postgresql://localhost/myapp"
}

config_content = generate_config(app_settings)
print("\nConfiguration File:")
print(config_content)