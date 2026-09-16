import os
import sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.chdir(ROOT)

from tools.get_file_content import get_file_content


result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print(get_file_content("calculator", "main.py"))

print(get_file_content("calculator", "pkg/calculator.py"))

print(get_file_content("calculator", "/bin/cat"))

print(get_file_content("calculator", "pkg/does_not_exist.py"))