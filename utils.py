import uhashlib
import ubinascii

def hmac_sha256(key, message):
    hmac_hash = uhashlib.sha256()
    hmac_hash.update(key)
    hmac_hash.update(message)
    digest = hmac_hash.digest()
    return digest
