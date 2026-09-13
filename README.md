# Cryptography_AES_Block-Cipher-Modes

# AES — Block Cipher Modes

Implementation and testing of different **AES (Advanced Encryption Standard)** block cipher modes for a Cryptography course project at **PUCPR**.

## 📌 About the Project

This project explores how AES can be used with four different block cipher modes:

* **ECB** — Electronic Codebook
* **CBC** — Cipher Block Chaining
* **CTR** — Counter Mode
* **GCM** — Galois/Counter Mode

The objective was to perform encryption and decryption using each mode and observe the different parameters required to correctly decrypt the ciphertext.

The project was developed as part of a **Cryptography** course exercise.

## 🔐 AES Modes

Each AES mode requires different information during decryption:

| Mode | Key |  IV | Authentication Tag |
| ---- | :-: | :-: | :----------------: |
| ECB  |  ✓  |  —  |          —         |
| CBC  |  ✓  |  ✓  |          —         |
| CTR  |  ✓  |  ✓  |          —         |
| GCM  |  ✓  |  ✓  |          ✓         |

### ECB

**Electronic Codebook (ECB)** encrypts each block independently.

In this implementation, only the encryption key is required for decryption.

> ⚠️ ECB is generally not recommended for encrypting structured or repetitive data because identical plaintext blocks produce identical ciphertext blocks.

### CBC

**Cipher Block Chaining (CBC)** combines each plaintext block with the previous ciphertext block before encryption.

Decryption requires:

* Key
* Initialization Vector (IV)

### CTR

**Counter Mode (CTR)** turns the block cipher into a stream-like construction by generating a keystream that is XORed with the plaintext.

Decryption requires:

* Key
* Initialization Vector (IV)

### GCM

**Galois/Counter Mode (GCM)** combines encryption with authentication.

In addition to the ciphertext, GCM produces an **authentication tag**, which allows the receiver to verify that the ciphertext has not been modified.

Decryption requires:

* Key
* Initialization Vector (IV)
* Authentication tag

## 🧪 Implementation

The program:

1. Defines a plaintext message.
2. Converts the message to UTF-8 bytes.
3. Pads the message to a multiple of the AES block size when necessary.
4. Generates a random 128-bit AES key.
5. Encrypts the plaintext using each of the four modes.
6. Displays the key, IV, authentication tag (when applicable), and ciphertext.
7. Decrypts the ciphertext.
8. Compares the decrypted plaintext with the original plaintext using an assertion.

The test message used in the submitted execution was:

```text
GRUPO 7. DANYA B., GABRIEL B., MATEUS P.
```

The AES key is generated using Python's `os.urandom(16)`, producing a 16-byte (128-bit) key.

## 📂 Project Structure

```text
.
├── Modo de Blocos do Algoritmo AES.py
└── modulo_para_AES.py
```

`modulo_para_AES.py` provides the AES encryption and decryption functions used by the main script.

The main script calls:

```python
AES.cifra_AES(plaintext, chave, modo)
```

for encryption and:

```python
AES.decifra_AES(ciphertext, chave, modo, ...)
```

for decryption, passing only the parameters required by each mode.

## ▶️ Running the Project

### Requirements

* Python 3.x
* The `modulo_para_AES.py` module included with the project

### Run

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

Then execute:

```bash
python "Modo de Blocos do Algoritmo AES.py"
```

## ✅ Results

All four modes successfully encrypted and decrypted the test message.

```text
TESTE DO MODO ECB
Plaintext: GRUPO 7. DANYA B., GABRIEL B., MATEUS P.
OK: texto decifrado confere com o original

TESTE DO MODO CBC
Plaintext: GRUPO 7. DANYA B., GABRIEL B., MATEUS P.
OK: texto decifrado confere com o original

TESTE DO MODO CTR
Plaintext: GRUPO 7. DANYA B., GABRIEL B., MATEUS P.
OK: texto decifrado confere com o original

TESTE DO MODO GCM
Plaintext: GRUPO 7. DANYA B., GABRIEL B., MATEUS P.
OK: texto decifrado confere com o original
```

The `assert` statement verifies that the decrypted message is identical to the original plaintext.

## 🎓 Learning Objectives

This project was developed to practice:

* AES encryption and decryption
* Block cipher modes of operation
* Initialization Vectors (IVs)
* Authentication tags
* Symmetric-key cryptography
* Base64 representation of ciphertext
* Verification of encryption/decryption correctness

## 👥 Authors

**Grupo 7**

* Danya B.
* Gabriel B.
* Mateus P.

## 📚 Course

**Cryptography**
Pontifícia Universidade Católica do Paraná (PUCPR)

---

*Academic project developed for educational purposes.*
