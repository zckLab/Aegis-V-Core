import os
import time

class AegisCrypto:
    def __init__(self, key=None):
        self.key = key if key else os.urandom(16).hex()

    def get_signature(self):
        return f"AEGIS_SEC_INIT_{self.key[:8].upper()}"