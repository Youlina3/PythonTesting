# Palindrome
# A palindrome is a word that reads the same backward or forward.

# Write a function that checks if a given word is a palindrome. Character case should be ignored.

# For example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.

class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word_reverse = word[::-1].lower()
        for i in range(len(word)):
            if word[i].lower() != word_reverse[i]:
                return False
        return True

print(Palindrome.is_palindrome('Deleveled'))