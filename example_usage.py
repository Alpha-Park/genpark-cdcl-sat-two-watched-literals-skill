from client import TwoWatchedLiterals

def main():
    print("=== Testing 2-Watched Literals Indexing ===")
    clauses = [[1, 2, 3], [-1, 2], [1, -3]]
    twl = TwoWatchedLiterals(clauses)

    affected = twl.on_literal_falsified(-1)
    print(f"Number of clauses watching literal -1: {affected}")
    assert affected == 1
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
