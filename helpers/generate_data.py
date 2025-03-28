import random

def generate_post_code() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(10))

def generate_first_name(post_code: str) -> str:
    groups = [post_code[i:i+2] for i in range(0, 10, 2)]
    name = ""
    for group in groups:
        num = int(group)
        letter = chr((num % 26) + ord('a'))
        name += letter
    return name
