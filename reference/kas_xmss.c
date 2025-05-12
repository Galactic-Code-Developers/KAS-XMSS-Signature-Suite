/* kas_xmss.c — Reference C implementation seed for KAS-XMSS
 * Author: Kapodistrian Academy of Science
 * License: Academic, non-commercial use only
 */

#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <openssl/sha.h>

#define HASH_SIZE 32
#define WOTS_LEN 16
#define CHAIN_DEPTH 4

void generate_entropy(const uint8_t *seed, size_t seed_len, const char *label, uint8_t *out) {
    SHA256_CTX ctx;
    SHA256_Init(&ctx);
    SHA256_Update(&ctx, label, strlen(label));
    SHA256_Update(&ctx, seed, seed_len);
    SHA256_Final(out, &ctx);
}

void hash_chain(uint8_t *buf, size_t len, int depth) {
    for (int i = 0; i < depth; i++) {
        uint8_t tmp[HASH_SIZE];
        SHA256(buf, len, tmp);
        memcpy(buf, tmp, HASH_SIZE);
    }
}

void wots_sign(const uint8_t *msg, size_t msg_len, const uint8_t *sk, uint8_t *sig) {
    for (int i = 0; i < WOTS_LEN; i++) {
        uint8_t block[HASH_SIZE];
        memcpy(block, sk + (i % HASH_SIZE), 1);
        memcpy(block + 1, msg + (i % msg_len), 1);
        hash_chain(block, 2, CHAIN_DEPTH);
        memcpy(sig + i * HASH_SIZE, block, HASH_SIZE);
    }
}

void wots_verify(const uint8_t *msg, size_t msg_len, const uint8_t *sig, uint8_t *out) {
    for (int i = 0; i < WOTS_LEN; i++) {
        uint8_t block[HASH_SIZE];
        memcpy(block, sig + i * HASH_SIZE, HASH_SIZE);
        hash_chain(block, HASH_SIZE, CHAIN_DEPTH);
        memcpy(out + i * HASH_SIZE, block, HASH_SIZE);
    }
}

int main() {
    uint8_t seed[] = "demo-seed";
    uint8_t msg[] = "Test message for KAS-XMSS";
    uint8_t sk[HASH_SIZE], sig[HASH_SIZE * WOTS_LEN], verified[HASH_SIZE * WOTS_LEN];

    generate_entropy(seed, strlen((char *)seed), "private_key", sk);

    printf("[*] Signing message...\n");
    wots_sign(msg, sizeof(msg), sk, sig);

    printf("[*] Verifying signature...\n");
    wots_verify(msg, sizeof(msg), sig, verified);

    int valid = memcmp(sig, verified, HASH_SIZE) == 0;
    printf("[*] Signature valid: %s\n", valid ? "YES" : "NO");

    return 0;
}
