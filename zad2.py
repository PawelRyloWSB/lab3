import base64


def encrypt_base64(text):
    return base64.b64encode(text.encode()).decode()


def decrypt_base64(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()


encoded_text = encrypt_base64("Test")
decoded_text = decrypt_base64(encoded_text)

print(f"Encoded: {encoded_text}")
print(f"Decoded: {decoded_text}")
