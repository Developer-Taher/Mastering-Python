# =====================================
# Complete Guide to Python Sets
# Comprehensive Tutorial and Reference
# =====================================

"""
What are Sets?
Sets are unordered collections of unique items in Python.
They are one of the most powerful data structures for mathematical operations.
Sets automatically eliminate duplicate elements and provide fast membership testing.

Examples: {1, 2, 3}, {'apple', 'banana'}, {1, 'hello', 3.14}, set()
"""

import sys
import timeit
import random
import itertools
import operator
from collections import Counter, defaultdict
from functools import reduce
import copy

print("=" * 70)
print("🎯 Complete Guide to Python Sets")
print("=" * 70)

print("\n" + "=" * 50)
print("1️⃣ Introduction to Sets")
print("=" * 50)

print("""
📝 What are Sets?
✅ Unordered collections of unique items
✅ Mutable (can be changed after creation)
✅ No duplicate elements allowed
✅ Can contain mixed hashable data types
✅ No indexing (elements are not ordered)
✅ Optimized for membership testing

🎯 Common Uses:
• Remove duplicates from sequences
• Mathematical set operations (union, intersection)
• Fast membership testing
• Find unique elements in data
• Track seen/visited items in algorithms
• Implement mathematical concepts

🆚 Sets vs Other Data Structures:
Sets:   Unordered, Unique, Mutable, Fast lookup
Lists:  Ordered,   Duplicates, Mutable, Sequential access
Tuples: Ordered,   Duplicates, Immutable, Sequential access
Dicts:  Ordered,   Unique keys, Mutable, Key-value pairs
""")

print("\n" + "=" * 50)
print("2️⃣ Creating Sets - Different Methods")
print("=" * 50)

print("\n🎯 Ways to Create Sets")
print("-" * 21)

# Empty set
empty_set = set()  # Note: {} creates an empty dict, not set!
print(f"Empty set:")
print(f"  set() → {empty_set}")
#print(f"  {} → {type({}).__name__} (This creates a dict, not a set!)")

# Set with initial values
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}  # Note: True == 1, so only one will remain
print(f"\nSets with initial values:")
print(f"  Numbers: {numbers}")
print(f"  Mixed types: {mixed_set}")

# Set from string (removes duplicates)
string_set = set("Python")
print(f"From string: set('Python') → {string_set}")

# Set from list (removes duplicates)
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4]
unique_set = set(list_with_duplicates)
print(f"From list with duplicates: set({list_with_duplicates}) → {unique_set}")

# Set from range
range_set = set(range(5))
range_set2 = set(range(2, 10, 2))
print(f"From range:")
print(f"  set(range(5)) → {range_set}")
print(f"  set(range(2, 10, 2)) → {range_set2}")

# Set comprehension
squares = {x**2 for x in range(5)}
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Set comprehension:")
print(f"  {{x**2 for x in range(5)}} → {squares}")
print(f"  {{x**2 for x in range(10) if x % 2 == 0}} → {even_squares}")

# Converting other iterables
tuple_to_set = set((1, 2, 3, 2, 1))
string_to_set = set("aabbcc")
print(f"\nConverting iterables:")
print(f"  set((1, 2, 3, 2, 1)) → {tuple_to_set}")
print(f"  set('aabbcc') → {string_to_set}")

# Important note about hashable elements
print(f"\n⚠️ Important: Sets can only contain hashable elements")
try:
    # This will work
    valid_set = {1, "hello", (1, 2), True}
    print(f"Valid set: {valid_set}")
except Exception as e:
    print(f"Error: {e}")

try:
    # This will raise TypeError
    invalid_set = {1, 2, [3, 4]}  # Lists are not hashable
except TypeError as e:
    print(f"Invalid set with list: {e}")

try:
    # This will also raise TypeError
    invalid_set2 = {1, 2, {3, 4}}  # Sets are not hashable
except TypeError as e:
    print(f"Invalid set with nested set: {e}")

print("\n" + "=" * 50)
print("3️⃣ Basic Set Operations")
print("=" * 50)

print("\n🔧 Essential Set Operations")
print("-" * 25)

# Creating sample sets for demonstrations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Sample sets:")
print(f"  set_a = {set_a}")
print(f"  set_b = {set_b}")

# Length and membership
print(f"\n📏 Length and Membership:")
print(f"len(set_a): {len(set_a)}")
print(f"3 in set_a: {3 in set_a}")
print(f"9 in set_a: {9 in set_a}")
print(f"3 not in set_a: {3 not in set_a}")

# Set comparison operations
print(f"\n⚖️ Set Comparisons:")
subset = {1, 2, 3}
superset = {1, 2, 3, 4, 5, 6}
print(f"subset = {subset}")
print(f"superset = {superset}")
print(f"subset <= superset (is subset): {subset <= superset}")
print(f"superset >= subset (is superset): {superset >= subset}")
print(f"subset < superset (is proper subset): {subset < superset}")
print(f"set_a == set_b: {set_a == set_b}")
print(f"set_a != set_b: {set_a != set_b}")

# Disjoint sets
disjoint_set = {10, 11, 12}
print(f"\ndisjoint_set = {disjoint_set}")
print(f"set_a.isdisjoint(disjoint_set): {set_a.isdisjoint(disjoint_set)}")
print(f"set_a.isdisjoint(set_b): {set_a.isdisjoint(set_b)}")

print("\n" + "=" * 50)
print("4️⃣ Set Mathematical Operations")
print("=" * 50)

print("\n🧮 Mathematical Set Operations")
print("-" * 30)

# Using the same sample sets
print(f"Working with:")
print(f"  set_a = {set_a}")
print(f"  set_b = {set_b}")

# Union (all elements from both sets)
print(f"\n🔗 Union (|, union()):")
union_operator = set_a | set_b
union_method = set_a.union(set_b)
print(f"  set_a | set_b = {union_operator}")
print(f"  set_a.union(set_b) = {union_method}")

# Intersection (common elements)
print(f"\n🎯 Intersection (&, intersection()):")
intersection_operator = set_a & set_b
intersection_method = set_a.intersection(set_b)
print(f"  set_a & set_b = {intersection_operator}")
print(f"  set_a.intersection(set_b) = {intersection_method}")

# Difference (elements in first set but not in second)
print(f"\n➖ Difference (-, difference()):")
difference_a_b = set_a - set_b
difference_b_a = set_b - set_a
print(f"  set_a - set_b = {difference_a_b}")
print(f"  set_b - set_a = {difference_b_a}")
print(f"  set_a.difference(set_b) = {set_a.difference(set_b)}")

# Symmetric difference (elements in either set but not in both)
print(f"\n🔄 Symmetric Difference (^, symmetric_difference()):")
sym_diff_operator = set_a ^ set_b
sym_diff_method = set_a.symmetric_difference(set_b)
print(f"  set_a ^ set_b = {sym_diff_operator}")
print(f"  set_a.symmetric_difference(set_b) = {sym_diff_method}")

# Multiple set operations
print(f"\n🔢 Multiple Set Operations:")
set_c = {3, 4, 5, 9, 10}
set_d = {5, 6, 7, 11, 12}
print(f"  set_c = {set_c}")
print(f"  set_d = {set_d}")

# Union of multiple sets
union_multiple = set_a | set_b | set_c
union_method_multiple = set_a.union(set_b, set_c)
print(f"  set_a | set_b | set_c = {union_multiple}")
print(f"  set_a.union(set_b, set_c) = {union_method_multiple}")

# Intersection of multiple sets
intersection_multiple = set_a & set_b & set_c
print(f"  set_a & set_b & set_c = {intersection_multiple}")

print("\n" + "=" * 50)
print("5️⃣ Set Methods - Modification")
print("=" * 50)

print("\n🔄 Set Modification Methods")
print("-" * 27)

# Adding elements
demo_set = {1, 2, 3}
print(f"Starting set: {demo_set}")

# add() - adds single element
demo_set.add(4)
print(f"After add(4): {demo_set}")

demo_set.add(3)  # Adding existing element has no effect
print(f"After add(3) again: {demo_set}")

# update() - adds multiple elements from iterable
demo_set.update([5, 6, 7])
print(f"After update([5, 6, 7]): {demo_set}")

demo_set.update({8, 9}, [10, 11])  # Multiple iterables
print(f"After update({{8, 9}}, [10, 11]): {demo_set}")

# Removing elements
print(f"\n🗑️ Removing Elements:")
demo_set = {1, 2, 3, 4, 5, 6, 7}
print(f"Starting set: {demo_set}")

# remove() - removes element (raises KeyError if not found)
demo_set.remove(5)
print(f"After remove(5): {demo_set}")

try:
    demo_set.remove(10)  # This will raise KeyError
except KeyError as e:
    print(f"remove(10) raised KeyError: {e}")

# discard() - removes element (no error if not found)
demo_set.discard(6)
print(f"After discard(6): {demo_set}")

demo_set.discard(10)  # This won't raise error
print(f"After discard(10) (not in set): {demo_set}")

# pop() - removes and returns arbitrary element
popped = demo_set.pop()
print(f"After pop(): {demo_set}, popped: {popped}")

# clear() - removes all elements
demo_set_copy = demo_set.copy()
demo_set_copy.clear()
print(f"After clear(): {demo_set_copy}")

# In-place update operations
print(f"\n🔧 In-place Update Operations:")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"set1 = {set1}, set2 = {set2}")

# |= (union update)
set1_copy = set1.copy()
set1_copy |= set2
print(f"set1 |= set2: {set1_copy}")

# &= (intersection update)
set1_copy = set1.copy()
set1_copy &= set2
print(f"set1 &= set2: {set1_copy}")

# -= (difference update)
set1_copy = set1.copy()
set1_copy -= set2
print(f"set1 -= set2: {set1_copy}")

# ^= (symmetric difference update)
set1_copy = set1.copy()
set1_copy ^= set2
print(f"set1 ^= set2: {set1_copy}")

print("\n" + "=" * 50)
print("6️⃣ Set Comprehensions")
print("=" * 50)

print("\n🚀 Set Comprehensions - Powerful Creation")
print("-" * 38)

# Basic set comprehensions
print("📋 Basic Set Comprehensions:")
numbers = range(10)
print(f"Numbers: {list(numbers)}")

# Square each number
squares = {x**2 for x in numbers}
print(f"Squares: {{x**2 for x in numbers}} → {squares}")

# Even numbers only
evens = {x for x in numbers if x % 2 == 0}
print(f"Evens: {{x for x in numbers if x % 2 == 0}} → {evens}")

# String operations
print(f"\n📝 String Operations with Set Comprehensions:")
text = "hello world python programming"
words = text.split()
print(f"Words: {words}")

# First letter of each word
first_letters = {word[0] for word in words}
print(f"First letters: {{word[0] for word in words}} → {first_letters}")

# Words with more than 5 characters
long_words = {word for word in words if len(word) > 5}
print(f"Long words: {{word for word in words if len(word) > 5}} → {long_words}")

# Uppercase versions
upper_words = {word.upper() for word in words}
print(f"Uppercase: {{word.upper() for word in words}} → {upper_words}")

# Working with nested data
print(f"\n🔄 Nested Data Processing:")
nested_lists = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [1, 8, 9]]
print(f"Nested lists: {nested_lists}")

# All unique numbers from nested lists
all_numbers = {num for sublist in nested_lists for num in sublist}
print(f"All unique numbers: {all_numbers}")

# Numbers that appear in multiple sublists
from collections import Counter
all_nums_list = [num for sublist in nested_lists for num in sublist]
duplicates = {num for num, count in Counter(all_nums_list).items() if count > 1}
print(f"Numbers appearing multiple times: {duplicates}")

# Conditional set comprehensions
print(f"\n🎯 Conditional Set Comprehensions:")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Data: {data}")

# Even squares, odd cubes
processed = {x**2 if x % 2 == 0 else x**3 for x in data}
print(f"Even squares, odd cubes: {processed}")

# Performance comparison
print(f"\n⚡ Performance Comparison:")
def traditional_unique(data):
    result = set()
    for item in data:
        if item % 2 == 0:
            result.add(item)
    return result

def comprehension_unique(data):
    return {item for item in data if item % 2 == 0}

test_data = list(range(1000))
traditional_time = timeit.timeit(lambda: traditional_unique(test_data), number=1000)
comprehension_time = timeit.timeit(lambda: comprehension_unique(test_data), number=1000)

print(f"Traditional loop: {traditional_time:.6f} seconds")
print(f"Set comprehension: {comprehension_time:.6f} seconds")
print(f"Speedup: {traditional_time/comprehension_time:.2f}x faster")

print("\n" + "=" * 50)
print("7️⃣ Advanced Set Operations")
print("=" * 50)

print("\n🎯 Advanced Set Techniques")
print("-" * 26)

# Copying sets
print("📋 Copying Sets:")
original = {1, 2, 3, 4, 5}
print(f"Original: {original}")

# Shallow copy methods
shallow1 = original.copy()
shallow2 = set(original)
print(f"Shallow copies:")
print(f"  original.copy(): {shallow1}")
print(f"  set(original): {shallow2}")

# Working with frozen sets
print(f"\n🧊 Frozen Sets (Immutable Sets):")
frozen_set = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen_set}")
print(f"Type: {type(frozen_set)}")

# Frozen sets can be elements of other sets
set_of_sets = {frozenset([1, 2]), frozenset([3, 4]), frozenset([5, 6])}
print(f"Set of frozen sets: {set_of_sets}")

# Frozen sets can be dictionary keys
frozen_dict = {frozenset([1, 2]): "first", frozenset([3, 4]): "second"}
print(f"Dict with frozen set keys: {frozen_dict}")

# Set operations with different types
print(f"\n🔄 Set Operations with Different Iterables:")
set_example = {1, 2, 3, 4}
list_example = [3, 4, 5, 6]
tuple_example = (5, 6, 7, 8)

print(f"Set: {set_example}")
print(f"List: {list_example}")
print(f"Tuple: {tuple_example}")

# Union with different iterables
union_with_list = set_example.union(list_example)
union_with_tuple = set_example.union(tuple_example)
print(f"Union with list: {union_with_list}")
print(f"Union with tuple: {union_with_tuple}")

# Intersection with different iterables
intersection_with_list = set_example.intersection(list_example)
print(f"Intersection with list: {intersection_with_list}")

# Filter and map operations
print(f"\n🔍 Filter and Map Operations:")
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"Numbers: {numbers}")

# Using filter()
evens = set(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens with filter(): {evens}")

# Using map()
squares = set(map(lambda x: x**2, numbers))
print(f"Squares with map(): {squares}")

# Chaining operations
print(f"\n🔗 Chaining Set Operations:")
data = [1, 2, 3, 4, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
print(f"Original data: {data}")

# Remove duplicates, filter evens, square them
result = {x**2 for x in set(data) if x % 2 == 0}
print(f"Unique evens squared: {result}")

# Step by step
step1 = set(data)  # Remove duplicates
step2 = {x for x in step1 if x % 2 == 0}  # Filter evens
step3 = {x**2 for x in step2}  # Square them
print(f"Step by step:")
print(f"  Remove duplicates: {step1}")
print(f"  Filter evens: {step2}")
print(f"  Square them: {step3}")

print("\n" + "=" * 50)
print("8️⃣ Set Performance and Memory")
print("=" * 50)

print("\n⚡ Performance Analysis")
print("-" * 21)

# Memory usage
print("💾 Memory Usage Analysis:")
set_data = set(range(1000))
list_data = list(range(1000))
tuple_data = tuple(range(1000))

containers_to_analyze = [
    ("Set", set_data),
    ("List", list_data),
    ("Tuple", tuple_data),
]

for name, container in containers_to_analyze:
    memory_size = sys.getsizeof(container)
    element_count = len(container)
    print(f"  {name:8}: {element_count:4d} elements, {memory_size:8d} bytes")

# Membership testing performance
print(f"\n🔍 Membership Testing Performance:")
test_set = set(range(10000))
test_list = list(range(10000))
search_value = 9999

def test_set_membership():
    return search_value in test_set

def test_list_membership():
    return search_value in test_list

set_time = timeit.timeit(test_set_membership, number=10000)
list_time = timeit.timeit(test_list_membership, number=10000)

print(f"Searching for {search_value} in 10,000 elements (10k iterations):")
print(f"  Set membership:  {set_time:.6f} seconds")
print(f"  List membership: {list_time:.6f} seconds")
print(f"  Speedup: {list_time/set_time:.0f}x faster for sets")

# Set operations performance
print(f"\n⚡ Set Operations Performance:")
set1 = set(range(5000))
set2 = set(range(2500, 7500))

def test_set_union():
    return set1 | set2

def test_set_intersection():
    return set1 & set2

def test_set_difference():
    return set1 - set2

operations = [
    ("Union", test_set_union),
    ("Intersection", test_set_intersection),
    ("Difference", test_set_difference),
]

for op_name, op_func in operations:
    time_taken = timeit.timeit(op_func, number=1000)
    result_size = len(op_func())
    print(f"  {op_name:12}: {time_taken:.6f} seconds, result size: {result_size}")

# Duplicate removal performance
print(f"\n🗂️ Duplicate Removal Performance:")
data_with_duplicates = [random.randint(1, 1000) for _ in range(10000)]

def remove_duplicates_set():
    return list(set(data_with_duplicates))

def remove_duplicates_loop():
    seen = []
    for item in data_with_duplicates:
        if item not in seen:
            seen.append(item)
    return seen

def remove_duplicates_dict():
    return list(dict.fromkeys(data_with_duplicates))

methods = [
    ("Set method", remove_duplicates_set),
    ("Loop method", remove_duplicates_loop),
    ("Dict method", remove_duplicates_dict),
]

print(f"Removing duplicates from {len(data_with_duplicates):,} elements:")
for method_name, method_func in methods:
    time_taken = timeit.timeit(method_func, number=100)
    result_size = len(method_func())
    print(f"  {method_name:12}: {time_taken:.6f} seconds, unique: {result_size}")

print("\n" + "=" * 50)
print("9️⃣ Set Algorithms")
print("=" * 50)

print("\n🧮 Common Set Algorithms")
print("-" * 23)

# Finding common elements across multiple lists
def find_common_elements(*lists):
    """Find elements common to all lists"""
    if not lists:
        return set()
    
    result = set(lists[0])
    for lst in lists[1:]:
        result &= set(lst)
    
    return result

print("🔍 Finding Common Elements:")
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [3, 4, 5, 6, 10, 11]
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"List 3: {list3}")
common = find_common_elements(list1, list2, list3)
print(f"Common elements: {common}")

# Finding unique elements across multiple lists
def find_unique_elements(*lists):
    """Find elements that appear in exactly one list"""
    all_elements = set()
    element_counts = Counter()
    
    for lst in lists:
        unique_in_list = set(lst)
        all_elements |= unique_in_list
        for element in unique_in_list:
            element_counts[element] += 1
    
    return {element for element, count in element_counts.items() if count == 1}

print(f"\n🎯 Finding Unique Elements (appearing in exactly one list):")
unique = find_unique_elements(list1, list2, list3)
print(f"Unique elements: {unique}")

# Jaccard similarity
def jaccard_similarity(set1, set2):
    """Calculate Jaccard similarity between two sets"""
    intersection = set1 & set2
    union = set1 | set2
    
    if len(union) == 0:
        return 0.0
    
    return len(intersection) / len(union)

print(f"\n📊 Jaccard Similarity:")
set_x = {1, 2, 3, 4, 5}
set_y = {4, 5, 6, 7, 8}
set_z = {1, 2, 3}
print(f"Set X: {set_x}")
print(f"Set Y: {set_y}")
print(f"Set Z: {set_z}")
print(f"Jaccard(X, Y): {jaccard_similarity(set_x, set_y):.3f}")
print(f"Jaccard(X, Z): {jaccard_similarity(set_x, set_z):.3f}")
print(f"Jaccard(Y, Z): {jaccard_similarity(set_y, set_z):.3f}")

# Power set generation
def power_set(s):
    """Generate power set (all possible subsets)"""
    s = list(s)
    power_sets = []
    
    for i in range(2**len(s)):
        subset = []
        for j in range(len(s)):
            if i & (1 << j):
                subset.append(s[j])
        power_sets.append(set(subset))
    
    return power_sets

print(f"\n🔋 Power Set Generation:")
small_set = {1, 2, 3}
print(f"Original set: {small_set}")
power = power_set(small_set)
print(f"Power set ({len(power)} subsets):")
for i, subset in enumerate(sorted(power, key=len)):
    print(f"  {i+1:2}: {subset}")

# Finding symmetric difference across multiple sets
def multi_symmetric_difference(*sets):
    """Find symmetric difference across multiple sets"""
    result = set()
    for s in sets:
        result ^= set(s)
    return result

print(f"\n🔄 Multiple Set Symmetric Difference:")
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Set 3: {set3}")
multi_sym_diff = multi_symmetric_difference(set1, set2, set3)
print(f"Multi-symmetric difference: {multi_sym_diff}")

print("\n" + "=" * 50)
print("🔟 Real-World Applications")
print("=" * 50)

print("\n🛠️ Practical Set Applications")
print("-" * 27)

# Tag system for blog posts
class BlogPost:
    """Blog post with tag system using sets"""
    
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = set(tags) if tags else set()
    
    def add_tag(self, tag):
        """Add a tag to the post"""
        self.tags.add(tag.lower())
    
    def remove_tag(self, tag):
        """Remove a tag from the post"""
        self.tags.discard(tag.lower())
    
    def has_tag(self, tag):
        """Check if post has a specific tag"""
        return tag.lower() in self.tags
    
    def has_any_tags(self, tags):
        """Check if post has any of the given tags"""
        return bool(self.tags & set(tag.lower() for tag in tags))
    
    def has_all_tags(self, tags):
        """Check if post has all of the given tags"""
        return set(tag.lower() for tag in tags) <= self.tags
    
    def __str__(self):
        return f"'{self.title}' - Tags: {self.tags}"

class BlogSystem:
    """Blog system with tag-based filtering"""
    
    def __init__(self):
        self.posts = []
    
    def add_post(self, post):
        """Add a post to the system"""
        self.posts.append(post)
    
    def get_all_tags(self):
        """Get all unique tags across all posts"""
        all_tags = set()
        for post in self.posts:
            all_tags |= post.tags
        return all_tags
    
    def find_by_tag(self, tag):
        """Find posts with specific tag"""
        return [post for post in self.posts if post.has_tag(tag)]
    
    def find_by_any_tags(self, tags):
        """Find posts with any of the given tags"""
        return [post for post in self.posts if post.has_any_tags(tags)]
    
    def find_by_all_tags(self, tags):
        """Find posts with all of the given tags"""
        return [post for post in self.posts if post.has_all_tags(tags)]
    
    def get_related_posts(self, post, min_common_tags=1):
        """Find posts related to given post based on common tags"""
        related = []
        for other_post in self.posts:
            if other_post != post:
                common_tags = post.tags & other_post.tags
                if len(common_tags) >= min_common_tags:
                    related.append((other_post, common_tags))
        return related

print("📝 Blog Tag System:")
blog = BlogSystem()

# Create blog posts
post1 = BlogPost("Introduction to Python", "Python basics...", 
                ["python", "programming", "beginner"])
post2 = BlogPost("Advanced Python Sets", "Deep dive into sets...", 
                ["python", "advanced", "data-structures"])
post3 = BlogPost("Web Development with Flask", "Building web apps...", 
                ["python", "web", "flask", "programming"])
post4 = BlogPost("Data Analysis Tutorial", "Using pandas...", 
                ["python", "data-analysis", "pandas"])

# Add posts to blog
for post in [post1, post2, post3, post4]:
    blog.add_post(post)
    print(f"  Added: {post}")

print(f"\nAll unique tags: {blog.get_all_tags()}")

# Find posts by tag
python_posts = blog.find_by_tag("python")
print(f"\nPosts with 'python' tag:")
for post in python_posts:
    print(f"  {post}")

# Find posts with multiple tags
advanced_posts = blog.find_by_any_tags(["advanced", "web"])
print(f"\nPosts with 'advanced' OR 'web' tags:")
for post in advanced_posts:
    print(f"  {post}")

# Find related posts
related = blog.get_related_posts(post1)
print(f"\nPosts related to '{post1.title}':")
for related_post, common_tags in related:
    print(f"  {related_post.title} (common: {common_tags})")

# User access control system
print(f"\n🔐 User Access Control System:")
class UserAccessControl:
    """User access control using sets for permissions"""
    
    def __init__(self):
        self.users = {}
        self.roles = {}
        self.user_roles = {}
    
    def create_role(self, role_name, permissions):
        """Create a role with specific permissions"""
        self.roles[role_name] = set(permissions)
    
    def create_user(self, username):
        """Create a new user"""
        self.users[username] = True
        self.user_roles[username] = set()
    
    def assign_role(self, username, role_name):
        """Assign a role to a user"""
        if username in self.users and role_name in self.roles:
            self.user_roles[username].add(role_name)
    
    def revoke_role(self, username, role_name):
        """Revoke a role from a user"""
        if username in self.user_roles:
            self.user_roles[username].discard(role_name)
    
    def get_user_permissions(self, username):
        """Get all permissions for a user"""
        if username not in self.user_roles:
            return set()
        
        permissions = set()
        for role in self.user_roles[username]:
            if role in self.roles:
                permissions |= self.roles[role]
        return permissions
    
    def user_can(self, username, permission):
        """Check if user has a specific permission"""
        user_permissions = self.get_user_permissions(username)
        return permission in user_permissions
    
    def users_with_permission(self, permission):
        """Find all users with a specific permission"""
        users = []
        for username in self.users:
            if self.user_can(username, permission):
                users.append(username)
        return users

# Set up access control system
access_control = UserAccessControl()

# Create roles
access_control.create_role("admin", ["read", "write", "delete", "manage_users"])
access_control.create_role("editor", ["read", "write", "edit"])
access_control.create_role("viewer", ["read"])
access_control.create_role("moderator", ["read", "write", "moderate"])

# Create users
users = ["alice", "bob", "charlie", "diana"]
for user in users:
    access_control.create_user(user)

# Assign roles
access_control.assign_role("alice", "admin")
access_control.assign_role("bob", "editor")
access_control.assign_role("charlie", "viewer")
access_control.assign_role("diana", "moderator")
access_control.assign_role("bob", "viewer")  # Bob has multiple roles

print("User permissions:")
for user in users:
    permissions = access_control.get_user_permissions(user)
    print(f"  {user}: {permissions}")

print(f"\nUsers who can 'write': {access_control.users_with_permission('write')}")
print(f"Users who can 'delete': {access_control.users_with_permission('delete')}")

# Inventory tracking system
print(f"\n📦 Inventory Tracking System:")
class InventoryTracker:
    """Track inventory using sets for categories and tags"""
    
    def __init__(self):
        self.items = {}
        self.categories = {}
        self.suppliers = {}
    
    def add_item(self, item_id, name, categories=None, suppliers=None):
        """Add an item to inventory"""
        self.items[item_id] = {
            'name': name,
            'categories': set(categories) if categories else set(),
            'suppliers': set(suppliers) if suppliers else set()
        }
    
    def add_category(self, item_id, category):
        """Add category to an item"""
        if item_id in self.items:
            self.items[item_id]['categories'].add(category)
    
    def add_supplier(self, item_id, supplier):
        """Add supplier to an item"""
        if item_id in self.items:
            self.items[item_id]['suppliers'].add(supplier)
    
    def find_items_by_category(self, category):
        """Find all items in a specific category"""
        return [item_id for item_id, item in self.items.items() 
                if category in item['categories']]
    
    def find_items_by_supplier(self, supplier):
        """Find all items from a specific supplier"""
        return [item_id for item_id, item in self.items.items() 
                if supplier in item['suppliers']]
    
    def find_items_multiple_categories(self, categories, match_all=True):
        """Find items matching multiple categories"""
        category_set = set(categories)
        results = []
        
        for item_id, item in self.items.items():
            item_categories = item['categories']
            if match_all:
                if category_set <= item_categories:  # All categories must match
                    results.append(item_id)
            else:
                if category_set & item_categories:  # Any category matches
                    results.append(item_id)
        
        return results
    
    def get_all_categories(self):
        """Get all unique categories"""
        all_categories = set()
        for item in self.items.values():
            all_categories |= item['categories']
        return all_categories
    
    def get_all_suppliers(self):
        """Get all unique suppliers"""
        all_suppliers = set()
        for item in self.items.values():
            all_suppliers |= item['suppliers']
        return all_suppliers

# Set up inventory system
inventory = InventoryTracker()

# Add items
inventory.add_item("001", "Laptop", ["electronics", "computers"], ["TechCorp", "CompuSupply"])
inventory.add_item("002", "Mouse", ["electronics", "accessories"], ["TechCorp", "OfficeMax"])
inventory.add_item("003", "Desk", ["furniture", "office"], ["FurniCorp", "OfficeMax"])
inventory.add_item("004", "Chair", ["furniture", "office", "ergonomic"], ["FurniCorp"])
inventory.add_item("005", "Monitor", ["electronics", "computers"], ["TechCorp", "DisplayPlus"])

print("Inventory items:")
for item_id, item in inventory.items.items():
    print(f"  {item_id}: {item['name']}")
    print(f"    Categories: {item['categories']}")
    print(f"    Suppliers: {item['suppliers']}")

print(f"\nAll categories: {inventory.get_all_categories()}")
print(f"All suppliers: {inventory.get_all_suppliers()}")

electronics = inventory.find_items_by_category("electronics")
print(f"\nElectronics items: {electronics}")

techcorp_items = inventory.find_items_by_supplier("TechCorp")
print(f"TechCorp items: {techcorp_items}")

office_electronics = inventory.find_items_multiple_categories(["office", "electronics"], match_all=True)
print(f"Items in both 'office' AND 'electronics': {office_electronics}")

office_or_electronics = inventory.find_items_multiple_categories(["office", "electronics"], match_all=False)
print(f"Items in 'office' OR 'electronics': {office_or_electronics}")

print("\n" + "=" * 50)
print("1️⃣1️⃣ Best Practices")
print("=" * 50)

print("\n💡 Set Best Practices Guide")
print("-" * 25)

print("""
🎯 When to Use Sets:
✅ Remove duplicates from collections
✅ Fast membership testing (x in set)
✅ Mathematical set operations (union, intersection)
✅ Track unique items (visited nodes, processed files)
✅ Find common/different elements between collections
✅ Implement algorithms requiring unique elements

🎯 When NOT to Use Sets:
❌ When you need ordered/indexed access
❌ When you need to store duplicate elements
❌ When elements are not hashable (lists, dicts)
❌ When you need to count occurrences

🔒 Hashability Best Practices:
✅ Use immutable elements (int, str, tuple, frozenset)
✅ Be careful with nested mutable structures
✅ Use frozenset for sets as dictionary keys
✅ Convert mutable elements to immutable when adding to sets

📝 Code Quality Best Practices:
✅ Use meaningful variable names for sets
✅ Document expected set contents and constraints
✅ Use set comprehensions for clarity and performance
✅ Choose appropriate set operations (& vs intersection())
✅ Handle empty sets gracefully in functions

⚡ Performance Best Practices:
✅ Use sets for O(1) membership testing
✅ Prefer set operations over loops for bulk operations
✅ Use set comprehensions over traditional loops
✅ Consider frozensets for immutable collections
✅ Use sets to eliminate duplicates before processing
""")

print("\n" + "=" * 50)
print("1️⃣2️⃣ Common Pitfalls and Solutions")
print("=" * 50)

print("\n⚠️ Common Set Pitfalls")
print("-" * 21)

# Pitfall 1: Empty set creation
print("🚨 Pitfall 1: Empty Set Creation")
print("❌ Wrong:")
empty_dict = {}  # This creates a dict, not a set!
print(f"  {{}} → {empty_dict}, type: {type(empty_dict).__name__}")

print("✅ Correct:")
empty_set = set()
print(f"  set() → {empty_set}, type: {type(empty_set).__name__}")

# Pitfall 2: Unhashable elements
print(f"\n🚨 Pitfall 2: Unhashable Elements")
print("❌ Problem:")
try:
    bad_set = {1, 2, [3, 4]}  # Lists are not hashable
    print(f"This won't work: {bad_set}")
except TypeError as e:
    print(f"  Error: {e}")

print("✅ Solution:")
good_set = {1, 2, (3, 4)}  # Use tuples instead
print(f"  Use tuples: {good_set}")

# Pitfall 3: Expecting order
print(f"\n🚨 Pitfall 3: Expecting Order")
print("❌ Problem: Sets are unordered (though they maintain insertion order in Python 3.7+)")
sample_set = {3, 1, 4, 1, 5, 9, 2, 6}
print(f"  Set: {sample_set}")
print("  Don't rely on element order!")

print("✅ Solution:")
ordered_list = sorted(sample_set)
print(f"  Convert to sorted list: {ordered_list}")

# Pitfall 4: Modifying set during iteration
print(f"\n🚨 Pitfall 4: Modifying Set During Iteration")
print("❌ Dangerous:")
dangerous_set = {1, 2, 3, 4, 5}
print(f"Original: {dangerous_set}")

print("  # This can cause RuntimeError:")
print("  # for item in dangerous_set:")
print("  #     if item % 2 == 0:")
print("  #         dangerous_set.remove(item)")

print("✅ Safe approach:")
safe_set = {1, 2, 3, 4, 5}
items_to_remove = {item for item in safe_set if item % 2 == 0}
safe_set -= items_to_remove
print(f"  Remove evens: {safe_set}")

# Pitfall 5: Set vs frozenset confusion
print(f"\n🚨 Pitfall 5: Set vs Frozenset Confusion")
regular_set = {1, 2, 3}
frozen_set = frozenset([1, 2, 3])

print(f"Regular set: {regular_set} (mutable)")
print(f"Frozen set: {frozen_set} (immutable)")

try:
    nested_sets = {regular_set, frozen_set}
    print(f"Nested sets: {nested_sets}")
except TypeError as e:
    print(f"❌ Error with regular set: {e}")

print("✅ Only frozensets can be nested:")
nested_frozen = {frozen_set, frozenset([4, 5, 6])}
print(f"  Nested frozensets: {nested_frozen}")

print("\n" + "=" * 50)
print("1️⃣3️⃣ Practice Exercises")
print("=" * 50)

print("\n🏋️ Set Practice Challenges")
print("-" * 25)

print("""
Challenge 1: Word frequency analyzer using sets
Challenge 2: Find duplicate characters in strings
Challenge 3: Implement set-based caching system
Challenge 4: Social network friend recommendations
Challenge 5: Data validation using sets
""")

# Challenge 1: Word frequency analyzer
def analyze_text_uniqueness(text):
    """Analyze unique words and characters in text"""
    words = text.lower().split()
    
    # Unique words
    unique_words = set(words)
    
    # Unique characters (excluding spaces)
    unique_chars = set(char for char in text.lower() if char != ' ')
    
    # Words that appear only once
    word_counts = Counter(words)
    singleton_words = {word for word, count in word_counts.items() if count == 1}
    
    # Most common starting letters
    starting_letters = set(word[0] for word in words if word)
    
    return {
        'unique_words': unique_words,
        'unique_chars': unique_chars,
        'singleton_words': singleton_words,
        'starting_letters': starting_letters,
        'total_words': len(words),
        'unique_word_count': len(unique_words)
    }

print("Challenge 1 - Text Uniqueness Analyzer:")
sample_text = "the quick brown fox jumps over the lazy dog the fox is quick"
analysis = analyze_text_uniqueness(sample_text)
print(f"Text: '{sample_text}'")
print(f"Total words: {analysis['total_words']}")
print(f"Unique words ({len(analysis['unique_words'])}): {analysis['unique_words']}")
print(f"Singleton words: {analysis['singleton_words']}")
print(f"Starting letters: {analysis['starting_letters']}")
print(f"Unique characters: {analysis['unique_chars']}")

# Challenge 2: String duplicate finder
def find_string_duplicates(strings):
    """Find duplicate characters and substrings in a list of strings"""
    all_chars = set()
    duplicate_chars = set()
    
    # Find duplicate characters across all strings
    for string in strings:
        string_chars = set(string.lower())
        duplicate_chars |= (all_chars & string_chars)
        all_chars |= string_chars
    
    # Find strings with internal duplicates
    strings_with_duplicates = []
    for string in strings:
        if len(string) != len(set(string.lower())):
            strings_with_duplicates.append(string)
    
    return {
        'duplicate_chars': duplicate_chars,
        'strings_with_internal_duplicates': strings_with_duplicates,
        'all_unique_chars': all_chars
    }

print(f"\nChallenge 2 - String Duplicate Finder:")
test_strings = ["hello", "world", "python", "programming", "challenge"]
duplicates = find_string_duplicates(test_strings)
print(f"Strings: {test_strings}")
print(f"Characters appearing in multiple strings: {duplicates['duplicate_chars']}")
print(f"Strings with internal duplicates: {duplicates['strings_with_internal_duplicates']}")
print(f"All unique characters: {duplicates['all_unique_chars']}")

# Challenge 3: Set-based cache
class SetCache:
    """Simple cache using sets for fast lookups"""
    
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.cache_keys = set()
        self.cache_data = {}
        self.access_order = []  # For LRU implementation
    
    def get(self, key):
        """Get value from cache"""
        if key in self.cache_keys:
            # Move to end for LRU
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
    
    def put(self, key, value):
        """Put value in cache"""
        if key in self.cache_keys:
            # Update existing
            self.cache_data[key] = value
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            # Add new
            if len(self.cache_keys) >= self.max_size:
                # Remove least recently used
                lru_key = self.access_order.pop(0)
                self.cache_keys.discard(lru_key)
                del self.cache_data[lru_key]
            
            self.cache_keys.add(key)
            self.cache_data[key] = value
            self.access_order.append(key)
    
    def contains(self, key):
        """Fast membership test"""
        return key in self.cache_keys
    
    def clear(self):
        """Clear the cache"""
        self.cache_keys.clear()
        self.cache_data.clear()
        self.access_order.clear()
    
    def size(self):
        """Get cache size"""
        return len(self.cache_keys)

print(f"\nChallenge 3 - Set-based Cache:")
cache = SetCache(max_size=3)

# Add some items
cache.put("user1", {"name": "Alice", "age": 30})
cache.put("user2", {"name": "Bob", "age": 25})
cache.put("user3", {"name": "Charlie", "age": 35})

print(f"Cache size: {cache.size()}")
print(f"Contains 'user2': {cache.contains('user2')}")
print(f"Get user2: {cache.get('user2')}")

# Add one more (should evict LRU)
cache.put("user4", {"name": "Diana", "age": 28})
print(f"After adding user4:")
print(f"  Contains 'user1': {cache.contains('user1')}")  # Should be False (evicted)
print(f"  Contains 'user4': {cache.contains('user4')}")  # Should be True

# Challenge 4: Friend recommendations
class SocialNetwork:
    """Social network with friend recommendations using sets"""
    
    def __init__(self):
        self.users = set()
        self.friendships = {}  # user -> set of friends
    
    def add_user(self, user):
        """Add a user to the network"""
        self.users.add(user)
        if user not in self.friendships:
            self.friendships[user] = set()
    
    def add_friendship(self, user1, user2):
        """Add mutual friendship"""
        if user1 in self.users and user2 in self.users:
            self.friendships[user1].add(user2)
            self.friendships[user2].add(user1)
    
    def get_friends(self, user):
        """Get user's friends"""
        return self.friendships.get(user, set())
    
    def get_mutual_friends(self, user1, user2):
        """Get mutual friends between two users"""
        friends1 = self.get_friends(user1)
        friends2 = self.get_friends(user2)
        return friends1 & friends2
    
    def suggest_friends(self, user, max_suggestions=5):
        """Suggest friends based on mutual connections"""
        if user not in self.users:
            return set()
        
        user_friends = self.get_friends(user)
        suggestions = set()
        
        # Find friends of friends
        for friend in user_friends:
            friend_friends = self.get_friends(friend)
            # Suggest people who are friends of friends but not already friends
            potential = friend_friends - user_friends - {user}
            suggestions |= potential
        
        # Limit suggestions
        return set(list(suggestions)[:max_suggestions])
    
    def get_network_stats(self):
        """Get network statistics"""
        total_friendships = sum(len(friends) for friends in self.friendships.values()) // 2
        return {
            'total_users': len(self.users),
            'total_friendships': total_friendships,
            'average_friends': total_friendships * 2 / len(self.users) if self.users else 0
        }

print(f"\nChallenge 4 - Social Network Friend Recommendations:")
network = SocialNetwork()

# Add users
users = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
for user in users:
    network.add_user(user)

# Add friendships
friendships = [
    ("Alice", "Bob"), ("Alice", "Charlie"),
    ("Bob", "Diana"), ("Charlie", "Diana"),
    ("Diana", "Eve"), ("Eve", "Frank"),
    ("Bob", "Frank")
]

for user1, user2 in friendships:
    network.add_friendship(user1, user2)

print("Network friendships:")
for user in users:
    friends = network.get_friends(user)
    print(f"  {user}: {friends}")

print(f"\nMutual friends between Alice and Diana: {network.get_mutual_friends('Alice', 'Diana')}")
print(f"Friend suggestions for Alice: {network.suggest_friends('Alice')}")
print(f"Friend suggestions for Eve: {network.suggest_friends('Eve')}")

stats = network.get_network_stats()
print(f"Network stats: {stats}")

# Challenge 5: Data validation
class DataValidator:
    """Data validator using sets for allowed values"""
    
    def __init__(self):
        self.valid_emails = set()
        self.blocked_domains = set()
        self.required_fields = set()
        self.valid_statuses = set()
    
    def add_valid_email(self, email):
        """Add email to whitelist"""
        self.valid_emails.add(email.lower())
    
    def add_blocked_domain(self, domain):
        """Add domain to blacklist"""
        self.blocked_domains.add(domain.lower())
    
    def set_required_fields(self, fields):
        """Set required fields"""
        self.required_fields = set(fields)
    
    def set_valid_statuses(self, statuses):
        """Set valid status values"""
        self.valid_statuses = set(statuses)
    
    def validate_email(self, email):
        """Validate email address"""
        email = email.lower()
        
        # Check if in whitelist
        if self.valid_emails and email not in self.valid_emails:
            return False, "Email not in whitelist"
        
        # Check domain blacklist
        if '@' in email:
            domain = email.split('@')[1]
            if domain in self.blocked_domains:
                return False, f"Domain {domain} is blocked"
        
        return True, "Valid"
    
    def validate_record(self, record):
        """Validate a data record"""
        errors = []
        
        # Check required fields
        record_fields = set(record.keys())
        missing_fields = self.required_fields - record_fields
        if missing_fields:
            errors.append(f"Missing required fields: {missing_fields}")
        
        # Check status if present
        if 'status' in record and self.valid_statuses:
            if record['status'] not in self.valid_statuses:
                errors.append(f"Invalid status: {record['status']}")
        
        # Check email if present
        if 'email' in record:
            is_valid, message = self.validate_email(record['email'])
            if not is_valid:
                errors.append(f"Email error: {message}")
        
        return len(errors) == 0, errors

print(f"\nChallenge 5 - Data Validation:")
validator = DataValidator()

# Set up validation rules
validator.set_required_fields(['name', 'email', 'status'])
validator.set_valid_statuses(['active', 'inactive', 'pending'])
validator.add_blocked_domain('spam.com')
validator.add_blocked_domain('fake.net')

# Test records
test_records = [
    {'name': 'Alice', 'email': 'alice@gmail.com', 'status': 'active'},
    {'name': 'Bob', 'email': 'bob@spam.com', 'status': 'active'},  # Blocked domain
    {'name': 'Charlie', 'status': 'invalid'},  # Missing email, invalid status
    {'email': 'diana@yahoo.com', 'status': 'pending'},  # Missing name
]

print("Validation results:")
for i, record in enumerate(test_records, 1):
    is_valid, errors = validator.validate_record(record)
    print(f"  Record {i}: {record}")
    print(f"    Valid: {is_valid}")
    if errors:
        print(f"    Errors: {errors}")

print("\n" + "=" * 50)
print("1️⃣4️⃣ Performance Optimization Tips")
print("=" * 50)

print("\n⚡ Set Performance Optimization")
print("-" * 30)

# Tip 1: Use sets for membership testing
print("💡 Tip 1: Use Sets for Fast Membership Testing")

def slow_membership_test(items, search_items):
    """Slow membership test using list"""
    found = []
    for search_item in search_items:
        if search_item in items:  # O(n) for lists
            found.append(search_item)
    return found

def fast_membership_test(items, search_items):
    """Fast membership test using set"""
    items_set = set(items)
    found = []
    for search_item in search_items:
        if search_item in items_set:  # O(1) for sets
            found.append(search_item)
    return found

# Performance comparison
large_list = list(range(10000))
search_list = [100, 5000, 9999, 15000]  # Some in, some out

slow_time = timeit.timeit(
    lambda: slow_membership_test(large_list, search_list), 
    number=1000
)
fast_time = timeit.timeit(
    lambda: fast_membership_test(large_list, search_list), 
    number=1000
)

print(f"  List membership (1000 iterations): {slow_time:.6f} seconds")
print(f"  Set membership (1000 iterations): {fast_time:.6f} seconds")
print(f"  Speedup: {slow_time/fast_time:.1f}x faster")

# Tip 2: Use set operations instead of loops
print(f"\n💡 Tip 2: Use Set Operations Instead of Loops")

def manual_intersection(list1, list2):
    """Manual intersection using loops"""
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

def set_intersection(list1, list2):
    """Fast intersection using sets"""
    return list(set(list1) & set(list2))

# Performance comparison
list_a = list(range(0, 1000, 2))  # Even numbers
list_b = list(range(500, 1500, 3))  # Every 3rd number starting from 500

manual_time = timeit.timeit(
    lambda: manual_intersection(list_a, list_b), 
    number=1000
)
set_time = timeit.timeit(
    lambda: set_intersection(list_a, list_b), 
    number=1000
)

print(f"  Manual intersection (1000 iterations): {manual_time:.6f} seconds")
print(f"  Set intersection (1000 iterations): {set_time:.6f} seconds")
print(f"  Speedup: {manual_time/set_time:.1f}x faster")

# Tip 3: Use frozenset for immutable sets
print(f"\n💡 Tip 3: Use Frozenset for Immutable Sets")

def compare_frozenset_performance():
    """Compare regular set vs frozenset creation"""
    data = range(1000)
    
    def create_set():
        return set(data)
    
    def create_frozenset():
        return frozenset(data)
    
    set_time = timeit.timeit(create_set, number=1000)
    frozenset_time = timeit.timeit(create_frozenset, number=1000)
    
    return set_time, frozenset_time

set_time, frozenset_time = compare_frozenset_performance()
print(f"  Regular set creation: {set_time:.6f} seconds")
print(f"  Frozenset creation: {frozenset_time:.6f} seconds")
print(f"  Memory: frozensets are more memory efficient for large collections")
print(f"  Use case: When you need immutable sets or sets as dict keys")

print("\n" + "=" * 70)
print("🎉 Congratulations! You've complete")