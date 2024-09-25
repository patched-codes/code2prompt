import re

def strip_body_contents(code: str, language: str) -> str:
    """
    Extract the names of functions and classes, along with their input parameters and types (if present) from the given code.
    :param code: The code string to extract information from.
    :param language: The programming language of the code.
    :return: A string containing the extracted information, one item per line.
    """
    if language in ['python', 'ruby']:
        pattern = re.compile(r'(def|class)\s+(\w+)\s*\((.*?)\)')
    elif language in ['javascript', 'typescript']:
        pattern = re.compile(r'(function|class)\s+(\w+)\s*\((.*?)\)')
    elif language in ['java', 'c', 'cpp', 'csharp']:
        pattern = re.compile(r'(?:class|interface|enum|\b(?:void|int|float|double|char|boolean|[a-zA-Z_][\w.<>[\]]*)\b)\s+(\w+)\s*(?:\((.*?)\))?')
    else:
        return "Unsupported language"

    matches = pattern.findall(code)
    
    result = []
    for match in matches:
        if language in ['python', 'ruby', 'javascript', 'typescript']:
            name = match[1]
            params = match[2]
            result.append(f"{match[0]} {name}({params})")
        else:
            name = match[0]
            params = match[1] if len(match) > 1 else ""
            result.append(f"{name}({params})")

    return "\n".join(result)