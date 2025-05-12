"""
fill_kas_xmss_vectors.py — Generate test vector outputs for KAS-XMSS
Requires: kas_xmss.py (in same directory or importable path)
"""

import csv
from hashlib import sha256, shake_256

def generate_entropy(seed: bytes, label: bytes = b"KAS-XMSS") -> bytes:
    shake = shake_256()
    shake.update(label)
    shake.update(seed)
    return shake.digest(32)

def wots_sign(message: bytes, sk: bytes) -> bytes:
    sig = b""
    for i in range(16):
        m_block = message[i % len(message):i % len(message)+1]
        x = sk[i % len(sk):i % len(sk)+1] + m_block
        for _ in range(4):
            x = sha256(x).digest()
        sig += x
    return sig

def generate_signature(seed: str, message: str) -> str:
    sk = generate_entropy(seed.encode(), b"private_key")
    sig = wots_sign(message.encode(), sk)
    return sig.hex()

def process_csv(input_csv: str, output_csv: str):
    with open(input_csv, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        row['expected_output'] = generate_signature(row['seed'], row['message'])

    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['seed', 'message', 'expected_output'])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    process_csv("kas_xmss_test_vectors.csv", "kas_xmss_test_vectors_filled.csv")
    print("[*] Test vector CSV updated → kas_xmss_test_vectors_filled.csv")
