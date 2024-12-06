class StringUtils:
    def reverse_string(self, s):
        return ''.join(reversed(s))  # Alternativa ao slicing, funcional e simples.

    def is_palindrome(self, s):
        return s == s[::-1]
