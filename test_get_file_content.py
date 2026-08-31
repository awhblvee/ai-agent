from functions.get_file_content import get_file_content


result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print(get_file_content("calculator", "main.py"))

# 3. Subdirectory calculator file
print(get_file_content("calculator", "pkg/calculator.py"))

# 4. Out-of-bounds path check
print(get_file_content("calculator", "/bin/cat"))

# 5. Non-existent file check
print(get_file_content("calculator", "pkg/does_not_exist.py"))