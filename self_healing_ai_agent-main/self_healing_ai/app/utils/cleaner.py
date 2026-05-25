import re


def clean_output(text):

    # Remove markdown
    text = re.sub(r"```python", "", text)
    text = re.sub(r"```", "", text)

    # Remove common AI phrases
    bad_phrases = [
        "Sure, I can help",
        "Here's",
        "Explanation",
        "Example",
        "Output"
    ]

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:

        skip = False

        for phrase in bad_phrases:

            if phrase.lower() in line.lower():
                skip = True

        if not skip:
            cleaned_lines.append(line)

    cleaned = "\n".join(cleaned_lines)

    # Try extracting first function only
    match = re.search(
        r"(def\s+\w+\(.*?\):[\s\S]*)",
        cleaned
    )

    if match:
        return match.group(1).strip()

    return cleaned.strip()