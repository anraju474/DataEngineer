"""
Python Data Structures Playground
---------------------------------
This script demonstrates how to work with:
1. String
2. List
3. Tuple
4. Set
5. Dictionary

Each function focuses on one data structure and shows
commonly used operations with clear print outputs.

Perfect for beginners and LinkedIn learning posts.
"""

# --------------------------------------------------
# Common functions that work across data structures
# --------------------------------------------------
def common_functions(text, lst, tpl, st, dct):
    """Demonstrates len, max, min, sum, and membership operations"""
    
    print("\n===== LENGTH =====")
    print(f"String Length : {len(text)}")
    print(f"List Length   : {len(lst)}")
    print(f"Tuple Length  : {len(tpl)}")
    print(f"Set Length    : {len(st)}")
    print(f"Dict Length   : {len(dct)}")

    print("\n===== MAX & MIN =====")
    print(f"Max in String : {max(text)}")
    print(f"Min in String : {min(text)}")
    print(f"Max in List   : {max(lst)}")
    print(f"Min in List   : {min(lst)}")

    print("\n===== MEMBERSHIP COUNT =====")
    search = "Johnson"
    print(f"'{search}' in List  : {lst.count(search)} time(s)")
    print(f"'{search}' in Tuple : {tpl.count(search)} time(s)")
    print(f"'{search}' in Set   : {1 if search in st else 0} time")

    print("\n===== SUM =====")
    numbers = [1, 2, 3, 55, 67]
    print(f"List Sum  : {sum(numbers)}")
    print(f"Tuple Sum : {sum(tuple(numbers))}")
    print(f"Set Sum   : {sum(set(numbers))}")


# --------------------------------------------------
# List Operations
# --------------------------------------------------
def play_with_list(lst):
    print("\n===== LIST OPERATIONS =====")
    print("Original List:", lst)

    lst.append("Raju")                 # Add element
    lst.insert(0, "Anusha")             # Insert at position
    lst.extend(["Jacob"])               # Extend list

    print("After Additions:", lst)

    lst.remove("Raju")                  # Remove by value
    popped = lst.pop(0)                 # Remove by index

    print("After Removals:", lst)
    print("Popped Element:", popped)

    upper_list = [name.upper() for name in lst]
    print("Uppercase List:", upper_list)

    print("Sorted List:", sorted(lst))
    lst.clear()
    print("Cleared List:", lst)


# --------------------------------------------------
# Tuple Operations (Immutable)
# --------------------------------------------------
def play_with_tuple(tpl):
    print("\n===== TUPLE OPERATIONS =====")
    print("Original Tuple:", tpl)

    new_tuple = tpl + ("Raju", "Anusha")  # Concatenation
    print("After Concatenation:", new_tuple)

    print("Count of 'Robert':", tpl.count("Robert"))
    print("Sorted Tuple:", sorted(tpl))


# --------------------------------------------------
# String Operations
# --------------------------------------------------
def play_with_string(text):
    print("\n===== STRING OPERATIONS =====")
    print("Original String:", text)

    print("Upper       :", text.upper())
    print("Lower       :", text.lower())
    print("Title       :", text.title())
    print("Capitalized :", text.capitalize())

    replaced = text.replace("Sarah", "Sarah,")
    parts = [p.strip() for p in replaced.split(",")]
    joined = " ".join(parts)

    print("Replaced    :", replaced)
    print("Split       :", parts)
    print("Joined      :", joined)


# --------------------------------------------------
# Set Operations
# --------------------------------------------------
def play_with_set(st):
    print("\n===== SET OPERATIONS =====")
    print("Original Set:", st)

    st.add("Raju")
    st.update(["Ravi", "Rajesh"])

    print("After Additions:", st)

    st.discard("johnny")  # Safe remove
    print("After Removal:", st)

    other_set = {"Michael", "Ravi"}
    print("Intersection:", st & other_set)
    print("Union       :", st | other_set)
    print("Difference  :", other_set - st)


# --------------------------------------------------
# Dictionary Operations
# --------------------------------------------------
def play_with_dict(dct):
    print("\n===== DICTIONARY OPERATIONS =====")
    print("Original Dictionary:", dct)

    dct["c5"] = "Raju"
    print("After Addition:", dct)

    dct.pop("c5")
    print("After Removal:", dct)

    capitalized = {k: v.capitalize() for k, v in dct.items()}
    print("Capitalized Values:", capitalized)


# --------------------------------------------------
# Main Execution
# --------------------------------------------------
if __name__ == "__main__":
    text = "SarahJohnson"
    lst = ["Sarah", "Johnson", "Robert", "johnny"]
    tpl = ("Sarah", "Johnson", "Robert", "johnny")
    st = {"Sarah", "Johnson", "Robert", "johnny"}
    dct = {"c1": "Sarah", "c2": "Johnson", "c3": "Robert", "c4": "johnny"}

    common_functions(text, lst, tpl, st, dct)
    play_with_list(lst.copy())
    play_with_tuple(tpl)
    play_with_string(text)
    play_with_set(st.copy())
    play_with_dict(dct.copy())
