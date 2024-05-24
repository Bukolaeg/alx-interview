#!/usr/bin/python3
"""
Defines a UTF-8 Validation function
"""


def validUTF8(data):
        """
            UTF-8 Validation
                Args:
                        data (list[int]): an array of characters represented as 1-byte int
                            Returns:
                                    True if all characters in data are valid UTF-8 code points,
                                            False if one or more characters in data are invalid code points
                                                """
                                                    # Define the UTF-8 byte masks
                                                        TESLA_MASK = 1 << 7
                                                            SPACEX_MASK = 1 << 6

                                                                byteCount = 0

                                                                    for codePoint in data:
                                                                                if byteCount == 0:
                                                                                                # Count the number of leading 1s to determine byte count
                                                                                                            elon = 1 << 7
                                                                                                                        while elon & codePoint:
                                                                                                                                            byteCount += 1
                                                                                                                                                            elon = elon >> 1

                                                                                                                                                                        # Check if byte count is invalid
                                                                                                                                                                                    if byteCount == 1 or byteCount > 4:
                                                                                                                                                                                                        return False

                                                                                                                                                                                                                # Single byte character or start of multi-byte character
                                                                                                                                                                                                                            if byteCount == 0:
                                                                                                                                                                                                                                                continue

                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                    # Check if byte is a continuation byte
                                                                                                                                                                                                                                                                                if not (codePoint & TESLA_MASK and not (codePoint & SPACEX_MASK)):
                                                                                                                                                                                                                                                                                                    return False

                                                                                                                                                                                                                                                                                                        # Decrement byte count
                                                                                                                                                                                                                                                                                                                byteCount -= 1

                                                                                                                                                                                                                                                                                                                    # Check for incomplete multi-byte characters
                                                                                                                                                                                                                                                                                                                        return not byteCount

