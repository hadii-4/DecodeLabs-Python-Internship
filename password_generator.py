import math
import secrets
import string
def calculate_entropy(length: int, pool_size: int) -> float:
    """Calculates password entropy in bits using E = L * log2(R)."""
    if length <= 0 or pool_size <= 0:
        return 0.0
    return length * math.log2(pool_size)

def generate_password(
    length: int = 16, use_symbols: bool = True
) -> tuple[str, float]:
    """Generates a cryptographically secure random password and calculates its entropy."""
    # Phase 1: Input Validation
    if length < 8:
        raise ValueError(
            "Password length must be at least 8 characters for basic security."
        )
    # Phase 2: Character Pool Assembly
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    # Using 'secrets' module for hardware-level security (non-deterministic entropy)
    password = "".join(secrets.choice(characters) for _ in range(length))

    # Phase 3: Entropy Calculation
    entropy = calculate_entropy(length, len(characters))

    return password, entropy

# --- Main Execution ---
if __name__ == "__main__":
    print("=== Secure Password Generator Engine ===")

    try:
        user_len = input("Enter password length (Default: 16): ").strip()
        length = int(user_len) if user_len else 16

        symbols_choice = (
            input("Include special symbols? (Y/n): ").strip().lower()
        )
        use_symbols = symbols_choice != "n"
        # Generate Password
        pwd, entropy_score = generate_password(length, use_symbols)
        # Output Display
        print("\n" + "-" * 40)
        print(f"Generated Password : {pwd}")
        print(f"Entropy Score      : {entropy_score:.2f} bits")
        # Security Feedback Evaluation
        if entropy_score >= 80:
            print("Security Assessment: Excellent (Very Strong)")
        elif entropy_score >= 60:
            print("Security Assessment: Moderate (Good)")
        else:
            print("Security Assessment: Weak (Susceptible to attack)")
        print("-" * 40)

    except ValueError as err:
        print(f"\n[Error]: {err}")