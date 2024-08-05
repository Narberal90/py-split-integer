def split_integer(value: int, number_of_parts: int) -> list | int:
    if not value > number_of_parts:
        return 0
    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(value // parts_left)
        value -= next_number
    return parts
