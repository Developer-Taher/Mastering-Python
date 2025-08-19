# =====================================
# Complete Guide to Python Lists
# Comprehensive Tutorial and Reference
# =====================================

"""
What are Lists?
Lists are ordered, mutable collections of items in Python.
They are one of the most versatile and commonly used data structures.
Lists can contain elements of different types and can be modified after creation.

Examples: [1, 2, 3], ['apple', 'banana'], [1, 'hello', 3.14, True], []
"""

import sys
import timeit
import random
import itertools
import operator
from collections import Counter, defaultdict
from functools import reduce
import copy
import bisect

print("=" * 70)
print("📋 Complete Guide to Python Lists")
print("=" * 70)

print("\n" + "=" * 50)
print("1️⃣ Introduction to Lists")
print("=" * 50)

print("""
📝 What are Lists?
✅ Ordered collections of items
✅ Mutable (can be changed after creation)
✅ Allow duplicate elements
✅ Can contain mixed data types
✅ Indexed by integers starting from 0
✅ One of the most flexible data structures

🎯 Common Uses:
• Store collections of related data
• Implement queues and stacks
• Build dynamic arrays
• Process sequences of items
• Manage ordered data that changes
• Implement algorithms and data structures
""")

print("\n" + "=" * 50)
print("2️⃣ Creating Lists - Different Methods")
print("=" * 50)

print("\n📋 Ways to Create Lists")
print("-" * 23)

# Empty list
empty_list1 = []
empty_list2 = list()
print(f"Empty lists:")
print(f"  [] → {empty_list1}")
print(f"  list() → {empty_list2}")

# List with initial values
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, None]
nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"\nLists with initial values:")
print(f"  Numbers: {numbers}")
print(f"  Mixed types: {mixed_list}")
print(f"  Nested: {nested_list}")

# List from string
string_list = list("Python")
print(f"\nFrom string: list('Python') → {string_list}")

# List from range
range_list = list(range(5))
range_list2 = list(range(2, 10, 2))
print(f"From range:")
print(f"  list(range(5)) → {range_list}")
print(f"  list(range(2, 10, 2)) → {range_list2}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"List comprehension: [x**2 for x in range(5)] → {squares}")

# Multiplication to create repeated elements
repeated = [0] * 5
repeated_list = ["hello"] * 3
print(f"\nRepeated elements:")
print(f"  [0] * 5 → {repeated}")
print(f"  ['hello'] * 3 → {repeated_list}")

# Be careful with mutable objects
print(f"\n⚠️ Warning with mutable objects:")
wrong_way = [[0] * 3] * 2  # Creates references to same list
right_way = [[0] * 3 for _ in range(2)]  # Creates separate lists
print(f"  Wrong: [[0] * 3] * 2 → {wrong_way}")
print(f"  Right: [[0] * 3 for _ in range(2)] → {right_way}")

# Modify to show the difference
wrong_way[0][0] = 1
right_way[0][0] = 1
print(f"  After modifying [0][0] = 1:")
print(f"    Wrong way: {wrong_way}")
print(f"    Right way: {right_way}")

print("\n" + "=" * 50)
print("3️⃣ List Indexing and Slicing")
print("=" * 50)

print("\n📍 Accessing List Elements")
print("-" * 26)

# Sample list for indexing
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"Sample list: {fruits}")
print(f"Length: {len(fruits)} elements")

# Positive indexing
print(f"\n🔢 Positive Indexing (left to right):")
for i in range(len(fruits)):
    print(f"  Index {i}: fruits[{i}] = '{fruits[i]}'")

# Negative indexing
print(f"\n🔄 Negative Indexing (right to left):")
for i in range(1, len(fruits) + 1):
    print(f"  Index -{i}: fruits[-{i}] = '{fruits[-i]}'")

# Slicing examples
print(f"\n✂️ List Slicing Examples:")
numbers = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Numbers: {numbers}")
print(f"numbers[2:7]:     {numbers[2:7]}     # Elements from index 2 to 6")
print(f"numbers[:5]:      {numbers[:5]}      # First 5 elements")
print(f"numbers[5:]:      {numbers[5:]}      # From index 5 to end")
print(f"numbers[:]:       {numbers[:]}       # Entire list (copy)")
print(f"numbers[-3:]:     {numbers[-3:]}     # Last 3 elements")
print(f"numbers[:-3]:     {numbers[:-3]}     # All except last 3")

# Advanced slicing with step
print(f"\n⚡ Advanced Slicing with Step:")
alphabet = list("abcdefghijklmnopqrstuvwxyz")
print(f"Alphabet: {alphabet}")
print(f"alphabet[::2]:     {alphabet[::2]}     # Every 2nd element")
print(f"alphabet[1::2]:    {alphabet[1::2]}    # Every 2nd starting from index 1")
print(f"alphabet[::-1]:    {alphabet[::-1]}    # Reverse list")
print(f"alphabet[::3]:     {alphabet[::3]}     # Every 3rd element")
print(f"alphabet[2:10:2]:  {alphabet[2:10:2]}  # From 2 to 10, step 2")

print("\n" + "=" * 50)
print("4️⃣ Basic List Operations")
print("=" * 50)

print("\n🔧 Essential List Operations")
print("-" * 27)

# Length and membership
sample_list = [1, 2, 3, 2, 4, 2, 5]
print(f"Sample list: {sample_list}")
print(f"len(sample_list): {len(sample_list)}")
print(f"2 in sample_list: {2 in sample_list}")
print(f"6 in sample_list: {6 in sample_list}")
print(f"2 not in sample_list: {2 not in sample_list}")

# Counting and finding
print(f"\n🔍 Counting and Finding:")
print(f"sample_list.count(2): {sample_list.count(2)}")
print(f"sample_list.index(2): {sample_list.index(2)}")  # First occurrence

# List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"\n🔗 List Concatenation:")
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list1 + list2: {list1 + list2}")
print(f"list1 * 3: {list1 * 3}")

# Min, max, sum (for numeric lists)
numeric_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n📊 Numeric Operations:")
print(f"List: {numeric_list}")
print(f"min(numeric_list): {min(numeric_list)}")
print(f"max(numeric_list): {max(numeric_list)}")
print(f"sum(numeric_list): {sum(numeric_list)}")

print("\n" + "=" * 50)
print("5️⃣ List Methods - Modification")
print("=" * 50)

print("\n🔄 List Modification Methods")
print("-" * 27)

# Adding elements
demo_list = [1, 2, 3]
print(f"Starting list: {demo_list}")

# append() - adds single element to end
demo_list.append(4)
print(f"After append(4): {demo_list}")

demo_list.append([5, 6])  # Adds list as single element
print(f"After append([5, 6]): {demo_list}")

# extend() - adds all elements from iterable
demo_list = [1, 2, 3]  # Reset
demo_list.extend([4, 5, 6])
print(f"After extend([4, 5, 6]): {demo_list}")

# insert() - adds element at specific position
demo_list = [1, 2, 3]  # Reset
demo_list.insert(1, 'inserted')
print(f"After insert(1, 'inserted'): {demo_list}")

# Removing elements
print(f"\n🗑️ Removing Elements:")
demo_list = [1, 2, 3, 2, 4, 2, 5]
print(f"Starting list: {demo_list}")

# remove() - removes first occurrence
demo_list.remove(2)
print(f"After remove(2): {demo_list}")

# pop() - removes and returns element
popped = demo_list.pop()  # Remove last element
print(f"After pop(): {demo_list}, popped: {popped}")

# Sorting and reversing
print(f"\n📏 Sorting and Reversing:")
unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {unsorted_list}")

# sort() - modifies original list
sorted_list = unsorted_list.copy()
sorted_list.sort()
print(f"After sort(): {sorted_list}")

# reverse() - reverses in place
reversed_list = unsorted_list.copy()
reversed_list.reverse()
print(f"After reverse(): {reversed_list}")

print("\n" + "=" * 50)
print("6️⃣ List Comprehensions")
print("=" * 50)

print("\n🚀 List Comprehensions - Powerful Creation")
print("-" * 38)

# Basic list comprehensions
print("📋 Basic List Comprehensions:")
numbers = list(range(10))
print(f"Numbers: {numbers}")

# Square each number
squares = [x**2 for x in numbers]
print(f"Squares: [x**2 for x in numbers] → {squares}")

# Even numbers only
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: [x for x in numbers if x % 2 == 0] → {evens}")

# String operations
print(f"\n📝 String Operations with List Comprehensions:")
words = ["hello", "world", "python", "programming"]
print(f"Words: {words}")

# Uppercase all words
upper_words = [word.upper() for word in words]
print(f"Uppercase: [word.upper() for word in words] → {upper_words}")

# Words with more than 5 characters
long_words = [word for word in words if len(word) > 5]
print(f"Long words: [word for word in words if len(word) > 5] → {long_words}")

# Nested list comprehensions
print(f"\n🔄 Nested List Comprehensions:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")

# Flatten matrix
flattened = [item for row in matrix for item in row]
print(f"Flattened: [item for row in matrix for item in row] → {flattened}")

# Performance comparison
print(f"\n⚡ Performance Comparison:")
def traditional_squares(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

def comprehension_squares(n):
    return [i**2 for i in range(n)]

n = 1000
traditional_time = timeit.timeit(lambda: traditional_squares(n), number=1000)
comprehension_time = timeit.timeit(lambda: comprehension_squares(n), number=1000)

print(f"Traditional loop: {traditional_time:.6f} seconds")
print(f"List comprehension: {comprehension_time:.6f} seconds")
print(f"Speedup: {traditional_time/comprehension_time:.2f}x faster")

print("\n" + "=" * 50)
print("7️⃣ Advanced List Operations")
print("=" * 50)

print("\n🎯 Advanced List Techniques")
print("-" * 26)

# Copying lists
print("📋 Copying Lists:")
original = [1, [2, 3], 4]
print(f"Original: {original}")

# Shallow copy methods
shallow1 = original.copy()
shallow2 = original[:]
shallow3 = list(original)
print(f"Shallow copies:")
print(f"  original.copy(): {shallow1}")
print(f"  original[:]: {shallow2}")
print(f"  list(original): {shallow3}")

# Deep copy
deep = copy.deepcopy(original)
print(f"Deep copy: {deep}")

# Filtering and mapping
print(f"\n🔍 Filtering and Mapping:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")

# Using filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens with filter(): {evens}")

# Using map()
squares = list(map(lambda x: x**2, numbers))
print(f"Squares with map(): {squares}")

# Enumerate for index-value pairs
print(f"\n🔢 Enumerate for Index-Value Pairs:")
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")
for i, fruit in enumerate(fruits):
    print(f"  Index {i}: {fruit}")

# Zip for combining lists
print(f"\n🤝 Zip for Combining Lists:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

print(f"Names: {names}")
print(f"Ages: {ages}")
print(f"Cities: {cities}")

# Zip into tuples
combined = list(zip(names, ages, cities))
print(f"Combined: {combined}")

print("\n" + "=" * 50)
print("8️⃣ List Performance and Memory")
print("=" * 50)

print("\n⚡ Performance Analysis")
print("-" * 21)

# Memory usage
print("💾 Memory Usage Analysis:")
small_list = [1, 2, 3, 4, 5]
large_list = list(range(10000))

lists_to_analyze = [
    ("Small list", small_list),
    ("Large list", large_list),
]

for name, lst in lists_to_analyze:
    memory_size = sys.getsizeof(lst)
    element_count = len(lst)
    print(f"  {name:12}: {element_count:6d} elements, {memory_size:8d} bytes")

# Operation performance
print(f"\n⏱️ Operation Performance:")

def test_append(n=10000):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

def test_list_comprehension(n=10000):
    return [i for i in range(n)]

def test_extend(n=10000):
    lst = []
    lst.extend(range(n))
    return lst

n = 10000
operations = [
    ("Append", lambda: test_append(n)),
    ("List comprehension", lambda: test_list_comprehension(n)),
    ("Extend", lambda: test_extend(n)),
]

print(f"Building list of {n:,} elements:")
for op_name, op_func in operations:
    time_taken = timeit.timeit(op_func, number=10)
    print(f"  {op_name:20}: {time_taken:.6f} seconds")

print("\n" + "=" * 50)
print("9️⃣ List Algorithms")
print("=" * 50)

print("\n🧮 Common List Algorithms")
print("-" * 25)

# Binary search implementation
def binary_search(arr, target):
    """Binary search in sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print("🔍 Binary Search:")
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
print(f"Sorted list: {sorted_list}")
print(f"Searching for: {target}")
index = binary_search(sorted_list, target)
print(f"Found at index: {index}")

# Quick sort implementation
def quicksort(arr):
    """Quick sort algorithm"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

print(f"\n⚡ Quick Sort:")
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {unsorted}")
sorted_quick = quicksort(unsorted)
print(f"Sorted: {sorted_quick}")

# Find duplicates
def find_duplicates(arr):
    """Find all duplicates in a list"""
    seen = set()
    duplicates = set()
    
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

print(f"\n🔍 Find Duplicates:")
test_array = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3]
print(f"Array: {test_array}")
duplicates = find_duplicates(test_array)
print(f"Duplicates: {duplicates}")

print("\n" + "=" * 50)
print("🔟 Data Structures with Lists")
print("=" * 50)

print("\n🏗️ Implementing Data Structures")
print("-" * 31)

# Stack implementation
class Stack:
    """Stack implementation using list"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return stack size"""
        return len(self.items)
    
    def __str__(self):
        return f"Stack({self.items})"

print("📚 Stack Implementation:")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"After pushing 1, 2, 3: {stack}")
print(f"Peek: {stack.peek()}")
print(f"Pop: {stack.pop()}")
print(f"Final stack: {stack}")

# Queue implementation
class Queue:
    """Queue implementation using list"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        """Return front item without removing"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return queue size"""
        return len(self.items)
    
    def __str__(self):
        return f"Queue({self.items})"

print(f"\n🚶 Queue Implementation:")
queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print(f"After enqueuing A, B, C: {queue}")
print(f"Front: {queue.front()}")
print(f"Dequeue: {queue.dequeue()}")
print(f"Final queue: {queue}")

print("\n" + "=" * 50)
print("1️⃣1️⃣ Real-World Applications")
print("=" * 50)

print("\n🛠️ Practical List Applications")
print("-" * 29)

# Shopping cart implementation
class ShoppingCart:
    """Shopping cart using lists"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        """Add item to cart"""
        # Check if item already exists
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                return
        
        # Add new item
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def remove_item(self, name):
        """Remove item from cart"""
        self.items = [item for item in self.items if item['name'] != name]
    
    def get_total(self):
        """Calculate total price"""
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def get_item_count(self):
        """Get total number of items"""
        return sum(item['quantity'] for item in self.items)
    
    def __str__(self):
        if not self.items:
            return "Empty cart"
        
        result = "Shopping Cart:\n"
        for item in self.items:
            total_price = item['price'] * item['quantity']
            result += f"  {item['name']}: ${item['price']:.2f} x {item['quantity']} = ${total_price:.2f}\n"
        result += f"Total: ${self.get_total():.2f}"
        return result

print("🛒 Shopping Cart Example:")
cart = ShoppingCart()
cart.add_item("Apple", 1.50, 3)
cart.add_item("Banana", 0.75, 6)
cart.add_item("Orange", 2.00, 2)
cart.add_item("Apple", 1.50, 2)  # Add more apples
print(cart)

print(f"\nAfter removing oranges:")
cart.remove_item("Orange")
print(cart)

print("\n" + "=" * 50)
print("1️⃣2️⃣ Best Practices")
print("=" * 50)

print("\n💡 List Best Practices Guide")
print("-" * 26)

print("""
🎯 Performance Best Practices:
✅ Use list comprehensions over loops when possible
✅ Prefer append() over insert(0) for adding elements
✅ Use extend() instead of += for adding multiple elements
✅ Use enumerate() instead of range(len()) for index access
✅ Slice instead of loops for copying: new_list = old_list[:]

🔒 Memory Best Practices:
✅ Del unused list references explicitly
✅ Be careful with nested list multiplication: [[0]*3 for _ in range(3)]
✅ Consider array.array for homogeneous numeric data

📝 Code Quality Best Practices:
✅ Use meaningful variable names for lists
✅ Document expected list contents and constraints
✅ Validate input lists when accepting from external sources
✅ Handle empty lists gracefully in functions
✅ Use constants for fixed lists: COLORS = ['red', 'green', 'blue']
""")

print("\n" + "=" * 50)
print("1️⃣3️⃣ Practice Exercises")
print("=" * 50)

print("\n🏋️ List Practice Challenges")
print("-" * 26)

print("""
Challenge 1: Find the second largest element
Challenge 2: Rotate a list by k positions
Challenge 3: Find pairs that sum to a target
Challenge 4: Implement list intersection
Challenge 5: Find longest increasing subsequence
""")

# Challenge 1: Second largest element
def find_second_largest(numbers):
    """Find the second largest element in a list"""
    if len(numbers) < 2:
        return None
    
    # Remove duplicates and sort
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

print("Challenge 1 - Second Largest Element:")
test_lists = [
    [1, 3, 4, 5, 2],
    [5, 5, 5],
    [1],
    [10, 10, 9, 8, 7],
]

for test_list in test_lists:
    result = find_second_largest(test_list)
    print(f"  {test_list} → Second largest: {result}")

# Challenge 2: Rotate list
def rotate_list_k(arr, k):
    """Rotate list by k positions to the right"""
    if not arr or k == 0:
        return arr.copy()
    
    k = k % len(arr)  # Handle k > len(arr)
    return arr[-k:] + arr[:-k]

print(f"\nChallenge 2 - List Rotation:")
test_array = [1, 2, 3, 4, 5, 6, 7]
for k in [0, 1, 3, 7]:
    rotated = rotate_list_k(test_array, k)
    print(f"  Rotate {test_array} by {k}: {rotated}")

# Challenge 3: Find pairs that sum to target
def find_pairs_sum(numbers, target):
    """Find all pairs that sum to target"""
    pairs = []
    seen = {}
    
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            pairs.append((seen[complement], i))
        seen[num] = i
    
    return pairs

print(f"\nChallenge 3 - Find Pairs Sum:")
test_numbers = [2, 7, 11, 15, 3, 6]
target = 9
print(f"Numbers: {test_numbers}")
print(f"Target: {target}")
pairs = find_pairs_sum(test_numbers, target)
print(f"Pairs: {pairs}")
for i, j in pairs:
    print(f"  numbers[{i}] + numbers[{j}] = {test_numbers[i]} + {test_numbers[j]} = {target}")

# Challenge 4: List intersection
def list_intersection(list1, list2):
    """Find intersection of two lists without using sets"""
    intersection = []
    
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    
    return intersection

print(f"\nChallenge 4 - List Intersection:")
list_a = [1, 2, 3, 4, 5, 2]
list_b = [4, 5, 6, 7, 8, 2]
print(f"List A: {list_a}")
print(f"List B: {list_b}")
intersection = list_intersection(list_a, list_b)
print(f"Intersection: {intersection}")

# Challenge 5: Flatten nested list
def flatten_list(nested_list):
    """Flatten a nested list structure"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(f"\nChallenge 5 - Flatten Nested List:")
nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"Nested: {nested}")
flat = flatten_list(nested)
print(f"Flattened: {flat}")

print("\n" + "=" * 70)
print("🎉 Congratulations! You've completed the Python Lists Guide!")
print("🏆 You now have comprehensive knowledge of list manipulation!")
print("=" * 70)

print(f"""
🎯 What You've Mastered:

✅ List creation and initialization methods
✅ Indexing, slicing, and element access
✅ All essential list operations and methods
✅ List comprehensions and performance
✅ Advanced list operations and techniques
✅ Memory management and copying strategies
✅ Common algorithms and sorting
✅ Data structure implementations
✅ Real-world applications
✅ Best practices for clean code
✅ Problem-solving with lists

🚀 Next Steps:
1. Practice algorithmic problems
2. Learn other data structures (sets, dictionaries)
3. Explore NumPy for numerical computing
4. Study time complexity analysis
5. Build projects using lists

💡 Key Takeaways:
- Lists are mutable and versatile
- List comprehensions are powerful and Pythonic
- Performance matters: choose the right operation
- Always consider edge cases
- Memory efficiency is important for large datasets
- Understanding algorithms helps solve complex problems

Keep practicing and building! 🐍✨
""")

# Quick reference card
print(f"""
📋 Lists Quick Reference:

Creating:
[]                        # Empty list
[1, 2, 3]                # List with elements
list """
)