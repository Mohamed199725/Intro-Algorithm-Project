def analyze_sentence(sentence):
    # Initialize counters
    sentence_length = 0
    word_count = 0
    vowel_count = 0

    # Define vowels
    vowels = set("aeiouAEIOU")

    # Iterate through each character in the sentence
    for char in sentence:
        # Increment the length counter for each character
        sentence_length += 1

        # Check if the character is a space, indicating the end of a word
        if char == ' ':
            word_count += 1

        # Check if the character is a vowel
        elif char in vowels:
            vowel_count += 1

    # The last word doesn't end with a space, so add 1 to the word count
    word_count += 1

    # Display the results
    print(f"Length of the sentence: {sentence_length} characters")
    print(f"Number of words in the sentence: {word_count}")
    print(f"Number of vowels in the sentence: {vowel_count}")

# Example usage:
input_sentence = "Hello, how are you doing today?"
analyze_sentence(input_sentence)
