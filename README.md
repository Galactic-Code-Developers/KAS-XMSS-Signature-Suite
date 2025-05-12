# KAS-XMSS: Sovereign Post-Quantum Signature Suite

KAS-XMSS is a deterministic, hash-based post-quantum digital signature framework developed by the Kapodistrian Academy of Science.

Built upon the XMSS standard (RFC 8391), KAS-XMSS offers:
- Entropy-verified, reproducible key generation
- Stateless or schedulable-state operation modes
- Full independence from NIST and foreign cryptographic authorities
- Strong Grover/Shor resistance via SHAKE256 + Merkle tree constructs

## Applications

- QD-RSA hybrid deployments
- Academic PKI systems
- Scientific long-term archives
- National digital identity systems

## Components

- `/reference/` – C and Python reference implementations
- `/test_vectors/` – Reproducible test signatures and seeds
- `kas_xmss_whitepaper.pdf` – Design and threat model

## Contact

validation@kapodistrian.edu.gr
