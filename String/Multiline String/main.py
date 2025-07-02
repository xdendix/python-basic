# tidak menggunakan multiline string
text_1 = "ini baris satu"
text_2 = "ini baris dua"
text_3 = "ini baris tiga"

print(text_1, text_2, text_3)

print(20 * "=")

print(f"{text_1} \n {text_2} \n {text_3}")

# menggunakan multiline string
print(20 * "=")
multiline_string = f"""
    1. {text_1}
    2. {text_2}
    3. {text_3}
"""

print(multiline_string)