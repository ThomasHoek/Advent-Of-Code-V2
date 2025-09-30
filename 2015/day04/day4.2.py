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


x = 0
while True:
    txt = f"ckczppom{x}"
    if to_hash(txt)[:6] == "000000":
        print(txt)
        break
    x += 1
