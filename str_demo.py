quote_1 = 'single quoted'
quote_2 = "double quoted"
print(quote_1, quote_2)
why_1 = 'She said, "Hello!"'
why_2 = "It's mine!"
print(why_1, why_2)
why_not_1 = "She said, \"Hello!\""
why_not_2 = 'It\'s mine!'
print(why_not_1, why_not_2)
new_line = "line1\nline2\nline3\n"
print(new_line)
tab_char = "col1\tcol2\tcol3\t"
print(tab_char)
backslash = "the backslash: \\"
print(backslash)
raw_new_line = r"line1\nline2\nline3\n"
print(raw_new_line)
raw_tab_char = r"col1\tcol2\tcol3\t"
print(raw_tab_char)
raw_backslash = r"the backslash: \\"
print(raw_backslash)
sub_text = "double"
print("sub_text = ", sub_text)
print(sub_text+sub_text)
print("_" * 40)
print("len(sub_text) returns", len(sub_text))
print("min(sub_text) returns", min(sub_text))
print("max(sub_text) returns", max(sub_text))
print("sub_text not in quote_1 returns", sub_text not in quote_1)
print("sub_text in quote_2 returns", sub_text in quote_2)
print("why_1.count('e') returns", why_1.count("e"))
print("why_1.index('e') returns", why_1.index("e"))
print("why_1.find('X') returns", why_1.find("X"))