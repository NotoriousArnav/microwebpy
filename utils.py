import hashlib
import binascii

def hmac_sha256(key, message):
    hmac_hash = hashlib.sha256()
    hmac_hash.update(key)
    hmac_hash.update(message)
    digest = hmac_hash.digest()
    return digest

def parse_headers(request):
    header, body = str(request + '\n').split('\n\n')
    headers = header.split('\n')
    r = {}
    
    if len(headers) > 1:
        for x in headers[1:]:
            if ':' in x:
                key, value = x.split(':', 1)
                r[key.strip()] = value.strip()
    
    return r
