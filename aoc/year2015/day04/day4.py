import hashlib


def to_hash(text: str) -> str:
    """String to md5 hash

    Args:
        text (str): String to be hashed

    Returns:
        str: Hash
    """
    hash_object = hashlib.md5(text.encode())
    return hash_object.hexdigest()


def puzzle(puzzle_input: str):
    x = 0
    while True:
        txt = f"{puzzle_input}{x}"
        if to_hash(txt).startswith("00000"):
            break
        x += 1
    return x