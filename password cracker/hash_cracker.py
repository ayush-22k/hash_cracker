import hashlib

def read_dictionary(file_path):
    try:
        with open(file_path,'r')as file:
            return[line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: Dictionary file not found at {file_path}")
        return []
    
def hash_crack(target_hash, dictionary):
    for i in dictionary:
        hashed_word = hashlib.sha256(i.encode()).hexdigest()
        if hashed_word == target_hash:
            return i
    else:
        return None
    
if __name__== "__main__":
    target='e9cee71ab932fde863338d08be4de9dfe39ea049bdafb342ce659ec5450b69ae'
    dictionary=read_dictionary(r"prob_password.txt")

    if not dictionary:
        print("Error: Unable to read the dictionary.")
    else:
        cracked_password = hash_crack(target, dictionary)
        if cracked_password:
            print('Password cracked:', cracked_password)
        else:
            print("Password not found in dictionary!")