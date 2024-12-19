program = [2, 4, 1, 1, 7, 5, 4, 7, 1, 4, 0, 3, 5, 5, 3, 0]

def step(A):
    """Run a single loop for the given program."""
    B = A % 8           # Opcode 2: B = A % 8
    B = B ^ 1           # Opcode 1: B = B ^ 1
    C = A // (2**B)     # Opcode 7: C = A // (2 ** B)
    B = B ^ 7           # Opcode 5: B = B ^ 7
    B = B ^ C           # Opcode 4: B = B ^ C
    A = A // (2**3)     # Opcode 0: A = A // (2 ** 3)
    return B % 8        # Return the result modulo 8

def find(A, col=0):
    """Recursive search for valid initial values of A."""
    print(f"Testing A={A}, col={col}")  # Debugging print

    if step(A) != program[-(col + 1)]:
        print(f"Failed at col={col}, step(A)={step(A)}, expected={program[-(col + 1)]}")
        return

    if col == len(program) - 1:
        print(f"Found valid A: {A}")
        As.append(A)  # Save A if all conditions match
    else:
        for B in range(8):  # Explore all possible values of the next B
            find(A * 8 + B, col + 1)

As = []
for a in range(256):  # Extended search range
    find(a)

if As:
    print("The smallest valid value of A is:", As[0])
else:
    print("No valid value of A found.")

