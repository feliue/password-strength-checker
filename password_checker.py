"""
==============================================
  Password Strength Checker
  Author: [Abdulhakeem Umar]
  GitHub: [toyin]
  Description: A cybersecurity tool that analyzes
               password strength and gives feedback
==============================================
"""

import re
import string


def check_length(password):
    """Check if password meets length requirements."""
    if len(password) >= 16:
        return 2, "Excellent length (16+ characters)"
    elif len(password) >= 12:
        return 1, "Good length (12+ characters)"
    elif len(password) >= 8:
        return 0, "Minimum length met (8 characters) — try longer"
    else:
        return -1, "Too short (minimum 8 characters required)"


def check_uppercase(password):
    """Check for uppercase letters."""
    if any(c.isupper() for c in password):
        return 1, "Contains uppercase letters ✓"
    return 0, "Missing uppercase letters (A-Z)"


def check_lowercase(password):
    """Check for lowercase letters."""
    if any(c.islower() for c in password):
        return 1, "Contains lowercase letters ✓"
    return 0, "Missing lowercase letters (a-z)"


def check_digits(password):
    """Check for numeric digits."""
    digit_count = sum(c.isdigit() for c in password)
    if digit_count >= 2:
        return 2, f"Contains {digit_count} digits ✓"
    elif digit_count == 1:
        return 1, "Contains 1 digit (add more for strength)"
    return 0, "Missing digits (0-9)"


def check_special_characters(password):
    """Check for special characters."""
    special_chars = set(string.punctuation)
    found = [c for c in password if c in special_chars]
    if len(found) >= 2:
        return 2, f"Contains {len(found)} special characters ✓"
    elif len(found) == 1:
        return 1, "Contains 1 special character (add more)"
    return 0, "Missing special characters (!@#$%^&*...)"


def check_common_passwords(password):
    """Check against a list of common passwords."""
    common_passwords = [
        "password", "123456", "password123", "admin", "letmein",
        "qwerty", "abc123", "monkey", "1234567890", "password1",
        "iloveyou", "sunshine", "princess", "welcome", "shadow",
        "superman", "dragon", "master", "hello", "freedom"
    ]
    if password.lower() in common_passwords:
        return -2, "⚠ This is a commonly used password — change it immediately!"
    return 0, "Not a commonly known password ✓"


def check_repeated_chars(password):
    """Check for repeated characters."""
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return -1, f"⚠ Repeated characters detected (e.g. '{password[i]*3}')"
    return 0, "No excessive repeated characters ✓"


def check_sequential_patterns(password):
    """Check for sequential patterns like 123 or abc."""
    sequences = ["0123456789", "abcdefghijklmnopqrstuvwxyz", "qwertyuiop", "asdfghjkl"]
    lower_pass = password.lower()
    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in lower_pass:
                return -1, f"⚠ Sequential pattern detected (e.g. '{seq[i:i+3]}')"
    return 0, "No sequential patterns detected ✓"


def get_strength_label(score, max_score):
    """Return strength label based on score percentage."""
    percentage = (score / max_score) * 100

    if percentage >= 85:
        return "🟢 VERY STRONG", percentage
    elif percentage >= 65:
        return "🟡 STRONG", percentage
    elif percentage >= 45:
        return "🟠 MODERATE", percentage
    elif percentage >= 25:
        return "🔴 WEAK", percentage
    else:
        return "⛔ VERY WEAK", percentage


def generate_suggestions(results):
    """Generate improvement suggestions based on failed checks."""
    suggestions = []
    for check_name, (score, message) in results.items():
        if score <= 0 and "✓" not in message and "Not a commonly" not in message:
            suggestions.append(f"  → {message}")
    return suggestions


def analyze_password(password):
    """Main function to analyze password strength."""
    print("\n" + "=" * 55)
    print("         PASSWORD STRENGTH ANALYZER")
    print("=" * 55)
    print(f"  Analyzing: {'*' * len(password)}  ({len(password)} characters)")
    print("=" * 55)

    # Run all checks
    checks = {
        "Length":               check_length(password),
        "Uppercase":            check_uppercase(password),
        "Lowercase":            check_lowercase(password),
        "Digits":               check_digits(password),
        "Special Characters":   check_special_characters(password),
        "Common Passwords":     check_common_passwords(password),
        "Repeated Characters":  check_repeated_chars(password),
        "Sequential Patterns":  check_sequential_patterns(password),
    }

    # Display individual results
    print("\n  📋 DETAILED ANALYSIS:")
    print("  " + "-" * 50)
    total_score = 0
    for check_name, (score, message) in checks.items():
        status = "✅" if score > 0 else ("⚠️ " if score == 0 else "❌")
        print(f"  {status} {check_name}: {message}")
        total_score += score

    # Calculate max possible score
    max_score = 10  # Sum of all maximum possible scores

    # Normalize score (avoid negative display)
    display_score = max(0, total_score)

    # Get strength label
    strength_label, percentage = get_strength_label(display_score, max_score)

    # Display overall result
    print("\n  " + "-" * 50)
    print(f"\n  🔐 OVERALL STRENGTH: {strength_label}")
    print(f"  📊 Score: {display_score}/{max_score} ({percentage:.0f}%)")

    # Display suggestions
    suggestions = generate_suggestions(checks)
    if suggestions:
        print("\n  💡 SUGGESTIONS TO IMPROVE:")
        for suggestion in suggestions:
            print(suggestion)
    else:
        print("\n  🎉 Great password! Keep it safe and don't reuse it.")

    print("\n" + "=" * 55 + "\n")


def main():
    """Main entry point."""
    print("\n  🔒 Welcome to the Password Strength Checker")
    print("  A cybersecurity tool for analyzing password security\n")

    while True:
        password = input("  Enter a password to analyze (or 'quit' to exit): ")

        if password.lower() == 'quit':
            print("\n  Thanks for using Password Strength Checker. Stay secure! 🔐\n")
            break

        if not password:
            print("  ⚠ Please enter a password.\n")
            continue

        analyze_password(password)

        again = input("  Analyze another password? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\n  Thanks for using Password Strength Checker. Stay secure! 🔐\n")
            break


if __name__ == "__main__":
    main()
