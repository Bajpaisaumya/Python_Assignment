import re

def scrape_directory_phones(directory_text):

    list = []

    dict1 = {
        "area_code": 0,
        "prefix": 0,
        "line_number": 0,
        "formatted": 0
    }

    dict2 = {
        "area_code": 0,
        "prefix": 0,
        "line_number": 0,
        "formatted": 0
    }

    dict3 = {
        "area_code": 0,
        "prefix": 0,
        "line_number": 0,
        "formatted": 0
    }

    pattern = re.search(
        r"(\d{3})-(\d{3})-(\d{4})",
        directory_text
    )

    if pattern:
        dict1["area_code"] = pattern.group(1)
        dict1["prefix"] = pattern.group(2)
        dict1["line_number"] = pattern.group(3)
        dict1["formatted"] = f"({dict1['area_code']}) {dict1['prefix']}-{dict1['line_number']}"
        list.append(dict1)

    pattern1 = re.search(
        r"\((\d{3})\)\s(\d{3})-(\d{4})",
        directory_text
    )

    if pattern1:
        dict2["area_code"] = pattern1.group(1)
        dict2["prefix"] = pattern1.group(2)
        dict2["line_number"] = pattern1.group(3)
        dict2["formatted"] = f"({dict2['area_code']}) {dict2['prefix']}-{dict2['line_number']}"
        list.append(dict2)

    pattern2 = re.search(
        r"(?<!\d)(\d{3})(\d{3})(\d{4})(?!\d)",
        directory_text
    )

    if pattern2:
        dict3["area_code"] = pattern2.group(1)
        dict3["prefix"] = pattern2.group(2)
        dict3["line_number"] = pattern2.group(3)
        dict3["formatted"] = f"({dict3['area_code']}) {dict3['prefix']}-{dict3['line_number']}"
        list.append(dict3)

    print(list)
def main():
    directory = directory = "Contact HR at 321-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."

    scrape_directory_phones(directory)

main()