def generate_password(length, uppercase_limit, lowercase_limit, special_limit,digit_limit):
    uppercase_chars = [chr(i) for i in range(65, 91)]  # ASCII uppercase characters
    lowercase_chars = [chr(i) for i in range(97, 123)]# ASCII lowercase characters
    special_chars = [chr(i) for i in range(33,95)]
    digits_chars = [chr(i) for i in range(48,57)]
    all_chars = uppercase_chars + lowercase_chars + special_chars + digits_chars
    password = ""
    excluded_chars = [33,34,39,40,41,42,43,44,46,47,58,60,61,62,63,91,92,93,94,96,123,124,125,126]  # ASCII values of characters to exclude
    start_char = 33  # ASCII printable characters start from 33
    end_char = 126   # ASCII printable characters end at 126
    seed = 7  # Initial seed for randomness
    uppercase_count = 0
    lowercase_count = 0
    special_count =0
    digit_count =0
    n=int(input("enter a number:"))
    for _ in range(length):
        seed = (n * seed + 31) % 997# Custom pseudo-random number generator
       # random_num = seed % 94 + 33  # ASCII printable characters from 33 to 126
        random_num = start_char + seed % (end_char - start_char + 1 - len(excluded_chars))
        for excluded_char in excluded_chars:
           if random_num >= excluded_char:
               random_num += 1
        
        
        if random_num in uppercase_chars and uppercase_count <= uppercase_limit:
            password += chr(random_num)
            uppercase_count += 1
        elif random_num in lowercase_chars and lowercase_count <= lowercase_limit:
            password += chr(random_num)
            lowercase_count += 1
        elif random_num in special_chars and special_count <= special_limit:
            password += chr(random_num)
            special_count += 1
        elif random_num in digits_chars and digit_count <= digit_limit:
            password += chr(random_num)
            digit_count += 1
        else:
            password += chr(random_num)
    
    return password

total_length = int(input("enter the total length of the password:"))
uppercase_limit = int(input("enter the uppercase limit of the password:"))
lowercase_limit = int(input("enter the lowercase limit of the password:"))
special_limit = int(input("enter the special char limit of the password:"))
digit_limit = int(input("enter the digit limit of the password:"))

generated_password = generate_password(total_length, uppercase_limit, lowercase_limit,special_limit,digit_limit)
print(generated_password)