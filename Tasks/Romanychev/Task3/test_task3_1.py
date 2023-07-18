import time
import random
import re
import unicodedata
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import matplotlib.pyplot as plt


def generate_random_string(length):
    all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choices(all_characters, k=length))


def count_vowels_for(input_string):
    vowels = "aeiou"
    vowel_counts = {vowel.lower(): 0 for vowel in vowels}
    for char in input_string:
        if char.lower() in vowels:
            vowel_counts[char.lower()] += 1
    return vowel_counts


def count_vowels_count(input_string):
    vowels = "aeiou"
    input_string_lower = input_string.lower()
    vowel_counts = {vowel: input_string_lower.count(vowel) for vowel in vowels}
    return vowel_counts


def count_vowels_regex(input_string):
    vowels_pattern = re.compile(r'[aeiou]', re.IGNORECASE)
    vowel_counts = Counter(vowel.group().lower()
                           for vowel in re.finditer(vowels_pattern, input_string))
    return dict(vowel_counts)


def count_vowels_sum(input_string):
    vowels = "aeiou"
    input_string_lower = input_string.lower()
    return {vowel: sum(1 for char in input_string_lower if char == vowel) for vowel in vowels}


def count_vowels_collections(input_string):
    input_string_lower = input_string.lower()
    vowel_counts = Counter(input_string_lower)
    vowels = "aeiou"
    return {vowel: vowel_counts[vowel] for vowel in vowels}


def count_vowels_unicodedata(input_string):
    vowels = "aeiou"
    return {vowel.lower(): sum(1 for char in input_string if unicodedata.category(char) == 'Ll' and char.lower() == vowel) for vowel in vowels}


def measure_time(func, input_string):
    start_time = time.time()
    result = func(input_string)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


if __name__ == "__main__":
    function_dict = {
        "count_vowels_for": count_vowels_for,
        "count_vowels_count": count_vowels_count,
        "count_vowels_regex": count_vowels_regex,
        "count_vowels_sum": count_vowels_sum,
        "count_vowels_collections": count_vowels_collections,
        "count_vowels_unicodedata": count_vowels_unicodedata,
    }

    input_lengths = [10**n for n in range(2, 9)]
    results = {func_name: [] for func_name in function_dict}

    with ProcessPoolExecutor() as executor:
        for length in input_lengths:
            input_string = generate_random_string(length)
            print(f"Длина входных данных: {length}")
            for func_name, func in function_dict.items():
                result, execution_time = measure_time(func, input_string)
                print(
                    f"Функция: {func_name}: {execution_time:.5f} Время выполнения в секундах")
                results[func_name].append(execution_time)
            print("-" * 40)

    # Построение графика
    plt.figure(figsize=(12, 8))
    colors = plt.cm.tab10.colors
    markers = ['o', 's', '^', 'D', 'p', '*', 'v', '<', '>']
    for i, (func_name, times) in enumerate(results.items()):
        plt.plot(input_lengths, times, label=func_name,
                 color=colors[i], marker=markers[i])
        plt.text(input_lengths[-1], times[-1], func_name, color=colors[i])

    plt.xlabel('Длина входных данных (количество символов)')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение производительности функций подсчета гласных')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xscale('log')
    plt.xticks(input_lengths, [f"10^{n}" for n in range(2, 9)])
    plt.tight_layout()
    plt.show()
