import json
import base58

# Replace with your wallet JSON file path
with open('/Users/developer/.config/solana/id.json', 'r') as file:
    private_key = json.load(file)
    print(private_key)
private_key_base58 = base58.b58encode(bytes(private_key)).decode('utf-8')
print(f"Base58 Private Key: {private_key_base58}")
