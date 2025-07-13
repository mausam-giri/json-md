import decode_json_to_markdown, encode_markdown_to_json

json_data = {
    "Characters": {
        "Aide de camp": {
            "4": {
                "Personality": ["Disdainful"],
                "Mood": ["Disdainful"],
                "Relationships": [
                    "Subordinate to Authand",
                    "Interacts with Kalia"
                ]
            }
        }
    }
}

# Decode JSON to Markdown
markdown = decode_json_to_markdown(json_data)
print("Markdown:\n", markdown)

# Encode Markdown back to JSON
parsed_json = encode_markdown_to_json(markdown)
print("\nParsed JSON:\n", parsed_json)