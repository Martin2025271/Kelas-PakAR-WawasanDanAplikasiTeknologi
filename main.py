import hashlib

# Teks asli yang ingin diverifikasi
text = "andoyo"

# Hash yang ingin dicocokkan
original_hash = "02bd2110cf6d75229745092321c819c1c72b91ad"

# Hash teks menggunakan SHA-1
hashed_text = hashlib.sha1(text.encode()).hexdigest()

# Cocokkan hasil hash dengan hash asli
if hashed_text == original_hash:
    print("Password match:", text)
else:
    print("Password does not match.")
