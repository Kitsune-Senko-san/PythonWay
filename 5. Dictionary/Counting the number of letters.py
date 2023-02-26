"""
When the numbers one to five are written as words (one, two, three, four, five), the total number of letters used is 19
(three for "one," three for "two," five for "three," four for "four," and four for "five").

If all numbers from 1 to 1111 (inclusive) were written out as words, how many letters would be used?
Don't count spaces or hyphens, and note that British usage includes the word "and" when writing out numbers.
For instance, 342 ("three hundred and forty-two") contains 23 letters and 115 ("one hundred and fifteen") contains 20 letters.
"""


def number_to_words(num):
    words_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                  7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
                  12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                  16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                  20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                  60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    if num in words_dict:
        return words_dict[num]
    elif num < 100:
        return words_dict[num // 10 * 10] + '-' + words_dict[num % 10]
    elif num < 1000:
        if num % 100 == 0:
            return words_dict[num // 100] + ' hundred'
        else:
            return words_dict[num // 100] + ' hundred and ' + number_to_words(num % 100)
    elif num < 1200:
        if num % 1000 == 0:
            return words_dict[num // 1000] + ' thousand'
        elif num < 1100:
            return words_dict[num // 1000] + ' thousand ' + number_to_words(num % 100)
        else:
            return words_dict[num // 1000] + ' thousand ' + words_dict[num // 1000] + ' hundred and ' + number_to_words(num % 100)
    else:
        return 'number out of range'


result = 0

for i in range(1, 1112):
    number = number_to_words(i)
    space_count = number.count(' ')
    hyphens_count = number.count('-')
    result += len(number) - space_count - hyphens_count

print("from 1 to 1111 number of letters:", result)
