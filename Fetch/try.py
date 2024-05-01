import re
def extract_apply_link(text):
    # Regular expression pattern to match URLs
    url_pattern = r'(https?://\S+)'
    matches = re.findall(url_pattern, text)
    if matches:
        return matches[0]  # Return the first URL found in the text
    else:
        return None  # Return None if no URL is found
    
print(extract_apply_link('kncikn https://bitbcbcsibc uvbc'))