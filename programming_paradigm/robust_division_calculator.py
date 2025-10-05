def safe_divide(numerator, denominator):
    try:
        # Convert to float
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Non-numeric input provided."
