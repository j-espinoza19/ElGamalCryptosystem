import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def rootprimitivity(p, g):
    powers = set()
    for k in range(1, p):
        value = pow(g, k, p)
        powers.add(value)
    return len(powers) == (p - 1)

def generate_prime_and_root(entry_block_size):
    min_prime_size = 256 ** int(entry_block_size)
    while True:
        p = random.randint(min_prime_size, 1000000)
        if is_prime(p):
            possible_g = list(range(2, p))
            random.shuffle(possible_g)
            for g in possible_g:
                if rootprimitivity(p, g):
                    return p, g

def generate_exponent(p):
    return random.randint(2, p - 2)

def k_inverse(k, p):
    for i in range(1, p):
        if (k * i) % p == 1:
            return i

def encryption(int_blocks, k, p):
    encrypted_blocks = [(m * k) % p for m in int_blocks]
    return encrypted_blocks

def decryption(encrypted_blocks, k, p):
    k_inv = k_inverse(k, p)
    decrypted_blocks = [(c * k_inv) % p for c in encrypted_blocks]
    return decrypted_blocks

def message_to_blocks(message, block_size):
    blocks = [message[i:i + block_size] for i in range(0, len(message), block_size)]
    int_blocks = []
    for block in blocks:
        block_utf = block.encode('utf-8')
        int_value = 0
        for position in range(len(block_utf)):
            byte = block_utf[position]
            int_value += byte * (256 ** (len(block_utf) - position - 1))
        int_blocks.append(int_value)
    return int_blocks

def blocks_to_message(decrypted_blocks):
    decrypted_message = ""
    for int_block in decrypted_blocks:
        str_block = []
        while int_block > 0:
            str_block.insert(0, int_block % 256)
            int_block //= 256
        block_str = bytes(str_block).decode('utf-8')
        decrypted_message += block_str
    return decrypted_message
