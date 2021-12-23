p = int(input("Enter a modulus value (P): "))
g = int(input("Enter a base value (G): "))

alice_secret_integer = int(input("\nEnter Alice's secret integer: "))
bob_secret_integer = int(input("Enter Bob's secret integer: "))

print(f"The Value of Public Keys: \n1. P: {p}\n2. G: {g}")

A = (g ** alice_secret_integer) % p
print("\nKey send by Alice to Bob: ", A)

B = g ** bob_secret_integer % p
print("Key send by Bob to Alice: ", B)

alice_shared_secret_integer = (B ** alice_secret_integer) % p
print("\nAlice Shared Secret number: ", alice_shared_secret_integer)

bob_shared_secret_integer = (A ** bob_secret_integer) % p
print("Bob Shared Secret number: ", bob_shared_secret_integer)