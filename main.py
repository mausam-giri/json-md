import re
from collections import defaultdict

def decode_json_to_markdown(data):
    """Takes JSON data and return markdown"""
    def recurse(obj, level=1):
        lines = []
        prefix = "#" * level
        if isinstance(obj, dict):
            for key, value in obj.items():
                lines.append(f"{prefix} {key}")
                lines.extend(recurse(value, level + 1))
        elif isinstance(obj, list):
            for item in obj:
                lines.append(f"- {item}")
        return lines

    return "\n".join(recurse(data))



def encode_markdown_to_json(markdown_text):
    """Takes mardown and return json"""
    lines = markdown_text.strip().splitlines()
    root = {}
    stack = [(0, root)]  # stack of (level, container)

    for line in lines:
        line = line.rstrip()

        header_match = re.match(r'^(#+)\s+(.*)$', line)
        if header_match:
            level = len(header_match.group(1))
            key = header_match.group(2)

            while stack and stack[-1][0] >= level:
                stack.pop()

            parent = stack[-1][1]
            parent[key] = {}
            stack.append((level, parent[key]))

        elif line.startswith("- "):
            item = line[2:]

            if not stack:
                raise ValueError("List item found without parent context")

            parent = stack[-1][1]

            if isinstance(parent, dict) and not parent:
                stack[-1] = (stack[-1][0], [item])
                grandparent = stack[-2][1]
                for k, v in grandparent.items():
                    if v == parent:
                        grandparent[k] = stack[-1][1]
                        break
            elif isinstance(parent, list):
                parent.append(item)
            else:
                raise ValueError(f"Invalid parent type: {type(parent)} for list item")

    return root