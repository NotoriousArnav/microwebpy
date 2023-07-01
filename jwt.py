import hashlib
import binascii
import json
import utils

class JWT:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def encode(self, payload):
        header = {
            "typ": "JWT",
            "alg": "HS256"
        }
        header_str = self._base64url_encode(ujson.dumps(header).encode())
        payload_str = self._base64url_encode(ujson.dumps(payload).encode())

        data = header_str + b'.' + payload_str
        signature = self._generate_signature(data)
        jwt_token = data + b'.' + signature

        return jwt_token

    def decode(self, jwt_token):
        parts = jwt_token.split(b'.')
        if len(parts) != 3:
            raise ValueError("Invalid JWT token")

        data = parts[0] + b'.' + parts[1]
        signature = parts[2]

        expected_signature = self._generate_signature(data)

        if signature != expected_signature:
            raise ValueError("Invalid JWT signature")

        payload = ujson.loads(self._base64url_decode(parts[1]))

        return payload

    def _generate_signature(self, data):
        return utils.hmac_sha256(self.secret_key, data)

    def _base64url_encode(self, data):
        encoded_data = ubinascii.b2a_base64(data).rstrip(b'\n=').replace(b'+', b'-').replace(b'/', b'_')
        return encoded_data

    def _base64url_decode(self, encoded_data):
        padding = b'=' * (4 - (len(encoded_data) % 4))
        decoded_data = ubinascii.a2b_base64(encoded_data + padding).decode()
        return decoded_data
