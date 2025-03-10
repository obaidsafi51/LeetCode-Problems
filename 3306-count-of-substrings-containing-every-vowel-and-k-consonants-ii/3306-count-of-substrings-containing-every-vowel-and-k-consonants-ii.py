class Solution:
    def _isVowel(self, c: str) -> bool:
        # Helper function to check if a character is a vowel
        return c in {"a", "e", "i", "o", "u"}

    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        n = len(word)
        count = 0  # To store the number of valid substrings

        # Sliding window pointers
        left = 0
        consonant_count = 0  # To track the number of consonants in the current window
        vowel_counts = [0] * 5  # To track the count of each vowel in the current window
        # Mapping of vowels to indices: a -> 0, e -> 1, i -> 2, o -> 3, u -> 4
        vowel_to_index = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}

        for right in range(n):
            char = word[right].lower()  # Convert to lowercase to handle uppercase vowels

            # Update consonant count or vowel counts
            if self._isVowel(char):
                vowel_counts[vowel_to_index[char]] += 1  # Increment the count of the current vowel
            else:
                consonant_count += 1  # Increment consonant count

            # If consonant count exceeds k, move the left pointer
            while consonant_count > k:
                left_char = word[left].lower()
                if self._isVowel(left_char):
                    # Decrement the count of the leftmost vowel
                    vowel_counts[vowel_to_index[left_char]] -= 1
                else:
                    # Decrement consonant count
                    consonant_count -= 1
                left += 1  # Move the left pointer

            # Check if the current window has all vowels and exactly k consonants
            if all(vowel_counts) and consonant_count == k:
                count += 1

        return count

