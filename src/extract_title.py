
def extract_title(markdown):
    lines = markdown.split("\n")
    lines = [line for line in lines if line]
    if len(lines) <= 0:
        raise ValueError("Empty markdown!!")

    if not lines[0].startswith("# "):
        raise ValueError("Header is not provided")

    return lines[0].replace("# ", "")
