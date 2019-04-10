import hashlib

# q1
print("Sha256:")
cypher1 = hashlib.sha256()
cypher1.update(b"If you want to keep a secret, you must also hide it from yourself")
cypher1 = cypher1.hexdigest()
print("If you want to keep a secret, you must also hide it from yourself -> ", cypher1)
cypher2 = hashlib.sha256()
cypher2.update(b"f you want to keep a secret, you must also hide it from yourself")
cypher2 = cypher2.hexdigest()
print(" f you want to keep a secret, you must also hide it from yourself -> ", cypher2)

tmp = 0
for i in range(64):
    if cypher1[i] == cypher2[i]:
        tmp += 1

print((64 - tmp), " chars changed.")


print("\nmd5:")
cypher3 = hashlib.md5()
cypher3.update(b"If you want to keep a secret, you must also hide it from yourself")
cypher3 = cypher3.hexdigest()
print("If you want to keep a secret, you must also hide it from yourself -> ", cypher3)
cypher4 = hashlib.md5()
cypher4.update(b"f you want to keep a secret, you must also hide it from yourself")
cypher4 = cypher4.hexdigest()
print(" f you want to keep a secret, you must also hide it from yourself -> ", cypher4)

tmp = 0
for i in range(32):
    if cypher3[i] == cypher4[i]:
        tmp += 1

print((64 - tmp), " chars changed.")