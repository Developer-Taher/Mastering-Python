# =====================================
# Complete Guide to Python Lists
# Comprehensive Tutorial and Reference
# =====================================

"""
What are Lists?
- Lists are ordered, mutable collections used to store sequences of items.
- They can contain mixed types (e.g., integers, strings, other lists), and can be nested.
- Lists are one of Python's core data structures and are used extensively.

Examples: [1, 2, 3], ["a", "b", "c"], [1, "two", 3.0, [4, 5]]
"""

from __future__ import annotations

import sys
import timeit
import statistics as stats
import itertools as it
from collections import deque
import heapq
import copy
from typing import Any, Iterable, Callable, List, Tuple, Dict


print("=" * 70)
print("📚 Complete Guide to Python Lists")
print("=" * 70)


print("\n" + "=" * 50)
print("1️⃣ Introduction to Lists")
print("=" * 50)

print(
    """
📝 What are Lists?
✅ Ordered, mutable sequences
✅ Allow duplicates and mixed types
✅ Indexed starting at 0, support negative indices
✅ Can be nested (lists of lists)
✅ Dynamic size (grow/shrink)

🎯 Common Uses:
• Storing collections (users, tasks, numbers)
• Iteration and aggregation
• Queues, stacks, simple buffers
• Data transformation pipelines
"""
)


print("\n" + "=" * 50)
print("2️⃣ Creating Lists - Multiple Techniques")
print("=" * 50)

print("\n📋 Ways to Create Lists")
print("-" * 25)

# Literals
numbers = [1, 2, 3, 4]
mixed = [1, "two", 3.0, True]
nested = [[1, 2], [3, 4], [5, [6, 7]]]

print(f"Literal (numbers): {numbers}")
print(f"Literal (mixed):   {mixed}")
print(f"Literal (nested):  {nested}")

# From iterables
from_range = list(range(5))
from_string = list("hello")
from_tuple = list((10, 20, 30))

print(f"From range:  {from_range}")
print(f"From string: {from_string}")
print(f"From tuple:  {from_tuple}")

# Repetition and unpacking
repeated = [0] * 5
unpacked = [*range(3), *"ab", 99]
print(f"Repeated [0] * 5: {repeated}")
print(f"Unpacked: {unpacked}")

# Caution: nested repetition
print("\n⚠️ Caution with nested repetition:")
ok_grid = [[0, 0, 0] for _ in range(3)]
bad_grid = [[0, 0, 0]] * 3  # Aliased rows
ok_grid[0][0] = 1
bad_grid[0][0] = 1
print(f"List comp grid: {ok_grid} (independent rows)")
print(f"Repetition grid: {bad_grid} (same row references)")


print("\n" + "=" * 50)
print("3️⃣ Indexing, Slicing, and Assignment")
print("=" * 50)

letters = list("abcdefg")
print(f"Sample: {letters}")

# Indexing
print("\n🔢 Indexing:")
print(f"  letters[0]  → {letters[0]}")
print(f"  letters[-1] → {letters[-1]}")

# Slicing (non-inclusive end)
print("\n✂️ Slicing:")
print(f"  letters[1:4]   → {letters[1:4]}")
print(f"  letters[:3]    → {letters[:3]}")
print(f"  letters[3:]    → {letters[3:]}")
print(f"  letters[::2]   → {letters[::2]}")
print(f"  letters[::-1]  → {letters[::-1]}  # reversed copy")

# Slice assignment (mutation)
print("\n🛠️ Slice Assignment:")
mutable = list("spam")
print(f"  start: {mutable}")
mutable[1:3] = list("PL")
print(f"  after mutable[1:3] = ['P','L'] → {mutable}")
mutable[1:1] = ["X", "Y"]  # insertion
print(f"  after insertion via slice → {mutable}")
mutable[0:3] = []  # deletion
print(f"  after deletion via slice → {mutable}")


print("\n" + "=" * 50)
print("4️⃣ Core List Methods")
print("=" * 50)

sample = [1, 2, 3]
print(f"Start: {sample}")
sample.append(4)
print(f"append(4): {sample}")
sample.extend([5, 6])
print(f"extend([5,6]): {sample}")
sample.insert(1, 1.5)
print(f"insert(1, 1.5): {sample}")
removed = sample.pop()  # remove last
print(f"pop() → {removed}, now {sample}")
sample.remove(1.5)
print(f"remove(1.5): {sample}")
count_2 = sample.count(2)
print(f"count(2) → {count_2}")
idx_3 = sample.index(3)
print(f"index(3) → {idx_3}")
sample.reverse()
print(f"reverse(): {sample}")
copy1 = sample.copy()
print(f"copy(): {copy1}")

# sort vs sorted
print("\n🔽 Sorting:")
unsorted = [5, 1, 3, 7, 2]
sorted_copy = sorted(unsorted)
print(f"sorted(unsorted) → {sorted_copy}; original: {unsorted}")
unsorted.sort(reverse=True)
print(f"list.sort(reverse=True) → {unsorted}")

# sorting with key
words = ["banana", "apple", "cherry", "date"]
print(f"\nKey sort by length: {sorted(words, key=len)}")
print(f"Key sort by last letter: {sorted(words, key=lambda s: s[-1])}")


print("\n" + "=" * 50)
print("5️⃣ List Comprehensions")
print("=" * 50)

print("\n🚀 Powerful and readable transformations")
nums = list(range(10))
squares = [n * n for n in nums]
evens = [n for n in nums if n % 2 == 0]
pairs = [(a, b) for a in range(3) for b in range(2)]
flat = [x for chunk in [[1, 2], [3, 4], [5]] for x in chunk]

print(f"nums:     {nums}")
print(f"squares:  {squares}")
print(f"evens:    {evens}")
print(f"pairs:    {pairs}")
print(f"flatten:  {flat}")

# Conditional expression
labels = ["even" if n % 2 == 0 else "odd" for n in range(6)]
print(f"labels:   {labels}")


print("\n" + "=" * 50)
print("6️⃣ Iteration Patterns")
print("=" * 50)

things = ["a", "b", "c"]
print("\n🔁 Basic iteration:")
for x in things:
    print(f"  item: {x}")

print("\n🔢 enumerate():")
for i, x in enumerate(things, start=1):
    print(f"  {i}: {x}")

print("\n🔗 zip():")
xs = [1, 2, 3]
ys = [10, 20, 30]
for a, b in zip(xs, ys):
    print(f"  pair: ({a}, {b})")

print("\n🧪 for-else (runs else if loop not broken):")
for n in [2, 4, 6, 8]:
    if n % 2 == 1:
        print("  found odd → break")
        break
else:
    print("  no odd numbers found")


print("\n" + "=" * 50)
print("7️⃣ Searching and Membership")
print("=" * 50)

data = [3, 1, 4, 1, 5, 9]
print(f"data: {data}")
print(f"Contains 4? → {4 in data}")
print(f"Contains 7? → {7 in data}")
print(f"any even? → {any(n % 2 == 0 for n in data)}")
print(f"all > 0?  → {all(n > 0 for n in data)}")

print("\n📐 Binary search with bisect (sorted lists):")
import bisect
sorted_data = sorted(data)
pos = bisect.bisect_left(sorted_data, 4)
print(f"sorted: {sorted_data}; 4 should be at index {pos}")


print("\n" + "=" * 50)
print("8️⃣ Stacks, Queues, Deques, Heaps")
print("=" * 50)

print("\n🧱 Stack (LIFO) using list:")
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(f"push 1,2,3 → {stack}")
print(f"pop → {stack.pop()}, now {stack}")

print("\n📦 Queue (FIFO) – prefer deque for O(1) popleft:")
q = deque(["task1", "task2", "task3"])
q.append("task4")
print(f"queue: {list(q)}; popleft → {q.popleft()}; now {list(q)}")

print("\n⛰️ Heap (priority queue) with heapq:")
items = [5, 1, 4, 2, 3]
heapq.heapify(items)
print(f"heapified: {items}")
heapq.heappush(items, 0)
print(f"push 0 → {items}")
print(f"pop → {heapq.heappop(items)}, now {items}")


print("\n" + "=" * 50)
print("9️⃣ Transformations and Aggregations")
print("=" * 50)

nums = [1, 2, 3, 4, 5]
print(f"nums: {nums}")
print(f"sum: {sum(nums)}  min: {min(nums)}  max: {max(nums)}  mean: {stats.mean(nums):.2f}")
print(f"map(*2): {list(map(lambda x: x * 2, nums))}")
print(f"filter even: {list(filter(lambda x: x % 2 == 0, nums))}")
print(f"list comp *2: {[x * 2 for x in nums]}")

print("\n🔗 Accumulations:")
from itertools import accumulate
print(f"prefix sums: {list(accumulate(nums))}")

print("\n🧩 Grouping and chunking:")
def chunk(seq: List[Any], size: int) -> List[List[Any]]:
    return [seq[i : i + size] for i in range(0, len(seq), size)]

print(f"chunks of 2: {chunk(list(range(7)), 2)}")


print("\n" + "=" * 50)
print("🔟 Mutability, Copies, and Aliasing")
print("=" * 50)

print("\n🧬 Mutability & aliasing:")
a = [1, 2, 3]
b = a  # alias, same object
a.append(4)
print(f"a: {a}, b: {b}, a is b? {a is b}")

print("\n🧪 Shallow copy options:")
src = [[1], [2]]
sh1 = src.copy()
sh2 = list(src)
sh3 = src[:]
print(f"src: {src}")
src[0].append(9)
print(f"after src[0].append(9) → sh1:{sh1} sh2:{sh2} sh3:{sh3} (inner lists shared)")

print("\n🧪 Deep copy:")
src2 = [[1], [2]]
dp = copy.deepcopy(src2)
src2[0].append(9)
print(f"src2: {src2}; deepcopy unaffected → {dp}")


print("\n" + "=" * 50)
print("1️⃣1️⃣ Common Pitfalls and How to Avoid Them")
print("=" * 50)

print("\n❌ Modifying a list while iterating over it:")
bad = [1, 2, 3, 4]
for x in bad[:]:  # iterate over a copy to remove safely
    if x % 2 == 0:
        bad.remove(x)
print(f"remove evens safely (via copy): {bad}")

print("\n❌ Using * for nested lists:")
rows_ok = [[0 for _ in range(3)] for _ in range(2)]
rows_bad = [[0] * 3] * 2
rows_ok[0][0] = 1
rows_bad[0][0] = 1
print(f"ok rows:  {rows_ok}")
print(f"bad rows: {rows_bad}  # both rows changed")


print("\n" + "=" * 50)
print("1️⃣2️⃣ Performance and Memory")
print("=" * 50)

print("\n⚡ Appending vs concatenation in loops (1000 iterations):")
setup_code = "nums = list(range(1000))"
def_time_plus = timeit.timeit(
    "res=[]\nfor n in nums: res = res + [n]",
    setup=setup_code,
    number=300,
)
def_time_append = timeit.timeit(
    "res=[]\nfor n in nums: res.append(n)",
    setup=setup_code,
    number=300,
)
print(f"  concat with + : {def_time_plus:.4f}s")
print(f"  append        : {def_time_append:.4f}s")

print("\n💾 Memory & overhead:")
small = []
large = list(range(10000))
print(f"  empty list size: {sys.getsizeof(small)} bytes")
print(f"  large list size: {sys.getsizeof(large)} bytes, length: {len(large)}")


print("\n" + "=" * 50)
print("1️⃣3️⃣ 2D Lists (Matrices) and Transforms")
print("=" * 50)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(f"matrix: {matrix}")
print(f"transpose (zip): {list(map(list, zip(*matrix)))}")
print(f"transpose (comp): {[ [row[i] for row in matrix] for i in range(len(matrix[0])) ]}")


print("\n" + "=" * 50)
print("1️⃣4️⃣ Real-World List Patterns")
print("=" * 50)

print("\n🧹 Deduplicate while preserving order:")
def dedupe(seq: Iterable[Any]) -> List[Any]:
    seen = set()
    out: List[Any] = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

print(f"dedupe: {dedupe([1,2,2,3,1,4])}")

print("\n🧩 Flatten arbitrarily nested lists (one level shown; see itertools.chain):")
flat_once = list(it.chain.from_iterable([[1, 2], [3, 4], [5]]))
print(f"flatten once: {flat_once}")

def flatten(nested_list: Iterable[Any]) -> List[Any]:
    result: List[Any] = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(f"flatten nested: {flatten([1, [2, [3, 4]], 5])}")

print("\n🥣 Group items by a key:")
def group_by(seq: Iterable[Any], key_fn: Callable[[Any], Any]) -> Dict[Any, List[Any]]:
    grouped: Dict[Any, List[Any]] = {}
    for item in seq:
        k = key_fn(item)
        grouped.setdefault(k, []).append(item)
    return grouped

animals = ["cat", "cow", "dog", "ant", "duck"]
print(f"group by first letter: {group_by(animals, lambda s: s[0])}")


print("\n" + "=" * 50)
print("1️⃣5️⃣ Type Hints and Best Practices")
print("=" * 50)

print(
    """
💡 Best Practices:
✅ Prefer list comprehensions for clarity and performance
✅ Use append/extend over + concatenation in loops
✅ Copy carefully (distinguish shallow vs deep copies)
✅ Avoid modifying lists while iterating; iterate over a copy or build new list
✅ For FIFO queues, use collections.deque
✅ For priority queues, use heapq
✅ Use key= in sorting for complex orderings
✅ Use list[Type] or typing.List[Type] for annotations
"""
)


print("\n" + "=" * 50)
print("1️⃣6️⃣ Testing Helpers and Exercises")
print("=" * 50)

def test_function(func: Callable[[Any], Any], cases: List[Tuple[Any, Any]]) -> None:
    print(f"Testing: {func.__name__}")
    for i, (inp, expected) in enumerate(cases, 1):
        try:
            got = func(inp)
            ok = got == expected
            status = "✅ PASS" if ok else "❌ FAIL"
            print(f"  {i:02d}. {status} | in={inp} expected={expected} got={got}")
        except Exception as e:
            print(f"  {i:02d}. ❌ ERROR | in={inp} error={e}")

def reverse_list(seq: List[Any]) -> List[Any]:
    return list(reversed(seq))

def unique_preserve(seq: List[Any]) -> List[Any]:
    return dedupe(seq)

print("\n🧪 Sample Tests:")
test_function(reverse_list, [([1, 2, 3], [3, 2, 1]), ([], []), (["a"], ["a"])])
test_function(unique_preserve, [([1, 2, 2, 1], [1, 2]), ([], []), ([3, 3, 3], [3])])


print("\n" + "=" * 70)
print("🎉 Lists Guide Completed!")
print("=" * 70)

print(
    """
📋 Lists Quick Reference:

Creating:
  [], list(iterable), [value] * n, [*iter1, *iter2]

Indexing/Slicing:
  lst[i], lst[-1], lst[a:b:c], lst[::-1]

Core Methods:
  append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy

Sorting:
  sorted(lst) → new list;  lst.sort() in-place
  key=func, reverse=True

Comprehensions:
  [expr for x in seq if cond]
  [(a,b) for a in A for b in B]

Copies:
  shallow: lst.copy(), list(lst), lst[:]
  deep: copy.deepcopy(lst)

Queues/Heaps:
  deque([...]).append/popleft
  heapq.heapify(lst); heappush/heappop

Searching:
  x in lst, any(pred(x) for x in lst), all(...)
  bisect for positions in sorted lists
"""
)

# End of comprehensive lists guide


