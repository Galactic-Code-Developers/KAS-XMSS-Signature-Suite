# Security Policy

## 📢 Reporting Vulnerabilities

If you discover a potential cryptographic flaw or implementation vulnerability in the KAS-XMSS reference code, we request responsible disclosure:

- 📧 Email: validation@kapodistrian.edu.gr
- Please include:
  - Description of the issue
  - A minimal reproducible example (if applicable)
  - Your contact details for potential follow-up

We aim to acknowledge receipt within 3 working days and will coordinate with you to assess, reproduce, and (if confirmed) publicly disclose with proper credit.

## 🔐 Scope

This security policy applies to:
- `reference/kas_xmss.py` and `kas_xmss.c`
- All cryptographic logic, entropy generation, and signature validation
- Test vector correctness and reproducibility

## ❌ Out of Scope

- General performance issues
- Compilation bugs unrelated to crypto output
- Vulnerabilities introduced by misuse outside this repository

Thank you for supporting responsible research in post-quantum cryptography.
