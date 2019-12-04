import secrets
import Alpha


class CeaserCipher:
    def __init__(self, alpha):
        self.alpha = alpha

    def KeyGen(self):
        return secrets.randbelow(len(self.alpha))

    def Encrypt(self, key, plaintext):
        return ''.join(
            [self.alpha[(self.alpha.index(c) + key) % len(self.alpha)] if c in self.alpha else c for c in plaintext])

    def Decrypt(self, key, ciphertext):
        return self.Encrypt(len(self.alpha) - key, ciphertext)


cipher = CeaserCipher(Alpha.HEBREW)

key = cipher.KeyGen()
print(key)
plaintext = 'אבגד'
ciphertext = cipher.Encrypt(key, plaintext)
print(ciphertext)
plaintext = cipher.Decrypt(key, ciphertext)
print(plaintext)
