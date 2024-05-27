from cryptography.fernet import Fernet
import pandas as pd


key = Fernet.generate_key()
cipher_suite = Fernet(key)
df = pd.DataFrame(columns=["password", "encrypted_password", "decrypted_password", "key"])
getpass = str()



def encrypt_password(password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password):
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password


def main():
    password = input("Enter a password to encrypt: ")
    encrypted_password = encrypt_password(password)
    print(f"Encrypted password: {encrypted_password.decode()}")

    decrypted_password = decrypt_password(encrypted_password)
    print(f"Decrypted password: {decrypted_password}")

    new_row = {
        "password": password,
        "encrypted_password": encrypted_password.decode(),
        "decrypted_password": decrypted_password,
        "key": key.decode()
    }

    global df
    df = df._append(new_row, ignore_index=True)



print("welecome to password encryption and decryption")
print ("1. Add password")
print ("2. Get password")
print ("3. Exit")
choice = input("Enter your choice: ")
if choice == "1":
    main()

elif choice == "2":
    getpass = input("enter your encrypted password: ")
    position = df.set_index('encrypted_password', inplace=True)
    position = df.index.get_loc(getpass)
    print(df.iloc[position])
elif choice == "3":
    exit()
else:
    print("Invalid choice")

choice = input("Do you want to continue? (yes/no): ")

while choice == "yes":
    print("1. Add password")
    print("2. Get password")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        main()
    elif choice == "2":
        getpass = input("enter your encrypted password: ")
        position = df.set_index('encrypted_password', inplace=True)
        position = df.index.get_loc(getpass)
        print(df.iloc[position])
    elif choice == "3":
        break
    else:
        print("Invalid choice")

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        break
