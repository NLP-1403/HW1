import re
import csv
from pathlib import Path

"""
    This class used to manage rules and regex 
    """
HALF_SPACE = '‌'
    
class Regexer:

    def __init__(self) -> None:

        file = open('HalfSpace_Data/suffix.csv', encoding="utf-8")
        self.suffix = csv.reader(file)

        file = open('HalfSpace_Data/prefix.txt', encoding="utf-8")
        self.prefix = csv.reader(file)


    """
    This method take an array of tuples (pattern, replacement) and compile them
    @param patterns array of tuples (pattern, replacement)
    @param self python class
    @return an array of compiled regex patterns
    """
    def compilePatterns(self, patterns):
        return [(re.compile(pattern), repl) for pattern, repl in patterns]

    """
    This method fetchs all suffix pattern from rule file and generate regex patterns
    @param self python class
    @return an array of regex patterns[(pattern, replacement)]
    """

    def suffixPatternGenerator(self):
        patterns = []
        for item in self.suffix:
            suffix = item[0]
            type = item[1]
            exceptions = item[2] if item[2] else ''
            specific_roots = item[3].split('|') if len(item) > 3 and item[3] else []

            # Define the replacement function inside the loop to capture the current specific_roots
            def make_replacement(specific_roots):
                def replacement(match):
                    root = match.group(1)
                    current_suffix = match.group(3)

                    # Check if the root matches any of the specific roots
                    if any(root == specific_root for specific_root in specific_roots):
                        replacement_space = ''  # No space if root matches any specific_root
                    elif exceptions and root.endswith(exceptions):
                        replacement_space = HALF_SPACE if type == 'a' else ''  # Half space or no space based on type
                    else:
                        replacement_space = HALF_SPACE if type == 'h' else ''  # Default to half space or no space based on type

                    return root + replacement_space + current_suffix

                return replacement

            # Pattern to match the root and the suffix
            pattern = r'(\S+)(\s+)(' + suffix + r')\b'

            # Compile the pattern and add it with the replacement function to the patterns list
            patterns.append((re.compile(pattern), make_replacement(specific_roots)))

        return patterns

    """
    This method fetchs all affix pattern from rule file and generate regex patterns
    @param self python class
    @return an array of regex patterns[(pattern, replacement)]
    """

    def prefixPatternGenerator(self):
        patterns = []
        for item in self.prefix:
            prefix = item[0]
            type = item[1]
            exceptions = item[2] if item[2] else ''

            # Pattern to match a word boundary or space before the prefix and the following word (root)
            pattern = r'(?:(?<=\s)|(?<=^))(' + prefix + r')\s+(\S+)'

            # Function to determine the replacement based on the type and exceptions
            def replacement(match):
                current_prefix = match.group(1)
                root = match.group(2)
                space = ''

                # Check if the root is an exception
                if root.startswith(tuple(exceptions)) or root == exceptions:
                    if type == 'h':
                        space = ''  # No space for exceptions if type is 'h'
                    elif type == 'a':
                        space = HALF_SPACE  # Half space for exceptions if type is 'a'
                else:
                    if type == 'h':
                        # Special case for 'h' type with 3-character roots not starting with specific letters
                        if len(root) == 3 and not root.startswith(('آ', 'م', 'ا')):
                            space = ''
                        else:
                            space = HALF_SPACE  # Half space for non-exceptions if type is 'h'
                    elif type == 'a':
                        space = ''  # No space for non-exceptions if type is 'a'

                return current_prefix + space + root

            # Compile the pattern and add it with the replacement function to the patterns list
            patterns.append((re.compile(pattern), replacement))

        return patterns


