from functions.get_files_infos import get_files_info
import textwrap

print("Result for current directory:")
print(textwrap.indent(get_files_info("calculator", "."), "  "))
print("\nResult for 'pkg' directory:")
print(textwrap.indent(get_files_info("calculator", "pkg"), "  "))
print("\nResult for '/bin' directory:")
print(textwrap.indent(get_files_info("calculator", "/bin"), "  "))
print("\nResult for '../' directory:")
print(textwrap.indent(get_files_info("calculator", "../"), "  "))