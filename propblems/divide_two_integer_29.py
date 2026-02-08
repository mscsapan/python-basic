def divide(self, dividend: int, divisor: int) -> int:
    # Handle overflow
    INT_MAX = 2 ** 31 - 1  # 2147483647
    INT_MIN = -(2 ** 31)  # -2147483648

    # Determine the sign
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    # Work with absolute values
    dividend = abs(dividend)
    divisor = abs(divisor)

    # Subtract divisor using bit shifting (without using *)
    result = 0
    while dividend >= divisor:
        temp = divisor
        power = 1
        while dividend >= (temp << 1):
            temp <<= 1
            power <<= 1
        dividend -= temp
        result += power

    # Apply sign
    result = sign * result

    # Clamp result within 32-bit integer range
    return min(max(result, INT_MIN), INT_MAX)
