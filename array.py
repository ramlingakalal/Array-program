import sys

def calculate_sum(scores):
    """Calculate sum of given scores."""
    return sum(scores)

def calculate_average(scores):
    """Calculate average of given scores."""
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

if __name__ == "__main__":
    print("=== Array Scores Processor (main branch) ===")
    try:
        # Case 1: CLI arguments passed (for Jenkins)
        if len(sys.argv) > 1:
            scores = []
            for x in sys.argv[1:]:
                scores.append(int(x))   # converts to integer only
        else:
            # Case 2: Console input
            raw_input_value = input("Enter integer scores: ")
            parts = raw_input_value.split()
            scores = []
            for x in parts:
                scores.append(int(x))  # converts to integer only

        print("\n=== Program Parameters ===")
        print("Scores entered:", scores)

        total = calculate_sum(scores)
        avg = calculate_average(scores)

        print(f"\nSum of scores = {total}")
        print(f"Average of scores = {avg:.2f}")

    except ValueError:
        print("Invalid input! Please enter integer values only.")
