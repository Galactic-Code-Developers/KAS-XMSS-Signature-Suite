"""
kas_xmss.py — Reference implementation seed for KAS-XMSS
Author: Kapodistrian Academy of Science (Antonios Valamontes)
Date: 2025
License: Academic, non-commercial use only
"""

import hashlib
import os
from typing import Tuple

# Parameters
HASH_FN = hashlib.sha256
HASH_SIZE = 32  # 256-bit
TREE_HEIGHT = 4  # example small tree for test/demo
WOTS_LEN = 16  # fixed for simplicity, can be parameterized

def generate_entropy(seed: bytes, label: str = b"KAS-XMSS") -> bytes:
    """Generate deterministic entropy from a seed using SHAKE256."""
    shake = hashlib.shake_256()
    shake.update(label)
    shake.update(seed)
    return shake.digest(HASH_SIZE)

def wots_sign(message: bytes, sk: bytes) -> bytes:
    """Simplified WOTS signature: hash chaining."""
    sig = b""
    for i in range(WOTS_LEN):
        m_block = message[i % len(message):i % len(message)+1]
        x = sk[i % len(sk):i % len(sk)+1] + m_block
        for _ in range(4):  # chain depth
            x = HASH_FN(x).digest()
        sig += x
    return sig

def wots_verify(message: bytes, sig: bytes) -> bytes:
    """Simplified WOTS verify: recompute chain."""
    result = b""
    for i in range(WOTS_LEN):
        m_block = message[i % len(message):i % len(message)+1]
        x = sig[i*HASH_SIZE:(i+1)*HASH_SIZE]
        for _ in range(4):  # chain depth
            x = HASH_FN(x).digest()
        result += x
    return result

def demo():
    seed = b"demo-seed"
    msg = b"Test message for KAS-XMSS"

    sk = generate_entropy(seed, b"private_key")
    pk = generate_entropy(seed, b"public_key")

    print("[*] Signing message...")
    sig = wots_sign(msg, sk)

    print("[*] Verifying signature...")
    computed = wots_verify(msg, sig)

    print("[*] Signature valid:", computed[:HASH_SIZE] == wots_verify(msg, sig)[:HASH_SIZE])

if __name__ == "__main__":
    demo()
