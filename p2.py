n = 5  # Number of rows

# 🌟 Pattern 1: Left-Aligned Increasing Triangle
print("Pattern 1: Left-Aligned Increasing Triangle")
for i in range(n):  # i goes from 0 to 4
    for j in range(i + 1):  # j goes from 0 to i, so stars increase
        print('*', end=' ')
    print()  # Move to next line
print("\n")

# 🌟 Pattern 2: Left-Aligned Decreasing Triangle
print("Pattern 2: Left-Aligned Decreasing Triangle")
for i in range(n):  # i = 0 to 4
    for j in range(i, n):  # j = i to 4 → stars decrease
        print('*', end=' ')
    print()
print("\n")

# 🌟 Pattern 3: Right-Aligned Increasing Triangle
print("Pattern 3: Right-Aligned Increasing Triangle")
for i in range(n):  # i = 0 to 4
    for j in range(i, n):  # Print spaces first
        print(' ', end=' ')
    for j in range(i + 1):  # Then print stars
        print('*', end=' ')
    print()
print("\n")

# 🌟 Pattern 4: Right-Aligned Decreasing Triangle
print("Pattern 4: Right-Aligned Decreasing Triangle")
for i in range(n):  # i = 0 to 4
    for j in range(i + 1):  # Spaces increase
        print(' ', end=' ')
    for j in range(i, n):  # Stars decrease
        print('*', end=' ')
    print()
print("\n")

# 🌟 Pattern 5: Pyramid (Middle-Aligned Increasing Triangle)
print("Pattern 5: Pyramid (Centered Increasing Triangle)")
for i in range(n):  # i = 0 to 4
    for j in range(i, n):  # Print spaces
        print(' ', end=' ')
    for j in range(i):  # Print left-side stars
        print('*', end=' ')
    for j in range(i + 1):  # Print right-side stars
        print('*', end=' ')
    print()
print("\n")

# 🌟 Pattern 6: Inverted Pyramid (Middle-Aligned Decreasing Triangle)
print("Pattern 6: Inverted Pyramid (Centered Decreasing Triangle)")
for i in range(n):  # i = 0 to 4
    for j in range(i + 1):  # Print spaces
        print(' ', end=' ')
    for j in range(i, n - 1):  # Left-side stars
        print('*', end=' ')
    for j in range(i, n):  # Right-side stars
        print('*', end=' ')
    print()
print("\n")

# 🌟 Pattern 7: Diamond (Pyramid + Inverted Pyramid)
print("Pattern 7: Diamond Shape")
# Upper part (Pyramid)
for i in range(n - 1):  # i = 0 to 3
    for j in range(i, n):  # Spaces
        print(' ', end=' ')
    for j in range(i):  # Left stars
        print('*', end=' ')
    for j in range(i + 1):  # Right stars
        print('*', end=' ')
    print()
# Lower part (Inverted Pyramid)
for i in range(n):  # i = 0 to 4
    for j in range(i + 1):  # Spaces
        print(' ', end=' ')
    for j in range(i, n - 1):  # Left stars
        print('*', end=' ')
    for j in range(i, n):  # Right stars
        print('*', end=' ')
    print()
