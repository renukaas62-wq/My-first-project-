def detect_error(code_line):
    errors = []
    if "if" in code_line and "=" in code_line and "==" not in code_line:
        errors.append("⚠️  In if condition use == not =")
    if code_line.count("(") != code_line.count(")"):
        errors.append("⚠️  Brackets () are not balanced")
    if "print" in code_line and "(" not in code_line:
        errors.append("⚠️  print needs brackets ()")
    if not errors:
        return "✅ No basic error found!"
    return "\n".join(errors)

print("=== AI Error Detector (My First Project) ===")
user_code = input("Paste one line of code: ")
result = detect_error(user_code)
print(result)
