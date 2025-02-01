import re

def generate_slugs(urls):
    """Generates slugs from a list of URLs, removing .html extension, handling empty sections after final slash, and extracting segments before subsequent slashes."""
    slugs = []
    for url in urls:
        # Remove .html extension if present
        slug = re.sub(r"\.html$", "", url)
        
        # Handle empty sections after final slash
        if not slug or re.fullmatch(r"^/$", slug):
            # Extract content before next slash or use content before the last slash if nothing after it
            match = re.search(r"(?:https?://)?[^/]+/([^/]+)/?$", slug)
            if match:
                slug = match.group(1)
        else:
            # Extract part after final slash, considering optional trailing slash
            match = re.search(r"^.*/([^/]+)/?$", slug)
            if match:
                slug = match.group(1)
        
        # Replace hyphens with spaces
        slug = slug.replace("-", " ")
        slug = slug.replace("_", " ")
        
        # Convert to lowercase and strip whitespace
        slug = slug.lower().strip()
        slugs.append(slug)
    return slugs

# Continuous loop for user input
while True:
    print("\nEnter URLs separated by newlines (or press Enter on an empty line to finish):")
    urls = []
    while True:
        url_input = input()
        if not url_input:
            break
        urls.append(url_input)

    if not urls:
        print("No URLs entered. Exiting.")
        break

    slugs = generate_slugs(urls)
    print("\nGenerated slugs:")
    for slug in slugs:
        print(slug)
