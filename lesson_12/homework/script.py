# # Homework:

# # Exercise 1: Threaded Prime Number Checker

# # Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.


# import threading

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def check_primes(start, end, result):
#     primes = []
#     for num in range(start, end + 1):
#         if is_prime(num):
#             primes.append(num)
#     result.extend(primes)

# def main():
#     start_range = 1
#     end_range = 100
#     thread_count = 4
#     threads = []
#     result = []

#     chunk_size = (end_range - start_range + 1) // thread_count

#     for i in range(thread_count):
#         start = start_range + i * chunk_size
#         end = start_range + (i + 1) * chunk_size - 1 if i < thread_count - 1 else end_range
#         t = threading.Thread(target=check_primes, args=(start, end, result))
#         threads.append(t)
#         t.start()

#     for t in threads:
#         t.join()

#     result.sort()
#     print("Prime numbers:", result)

# if __name__ == "__main__":
#     main()

# # Exercise 2: Threaded File Processing

# # Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.\

# import threading
# from collections import defaultdict

# def count_words(lines, result):
#     local_count = defaultdict(int)
#     for line in lines:
#         words = line.strip().split()
#         for word in words:
#             word = word.lower().strip(".,!?\"'")  # Clean punctuation
#             local_count[word] += 1
#     result.append(local_count)

# def merge_results(results):
#     final_count = defaultdict(int)
#     for res in results:
#         for word, count in res.items():
#             final_count[word] += count
#     return final_count

# def main():
#     filename = "sample.txt"  # Replace with your file

#     # Read all lines
#     with open(filename, 'r') as f:
#         lines = f.readlines()

#     thread_count = 4
#     chunk_size = len(lines) // thread_count
#     threads = []
#     results = []

#     for i in range(thread_count):
#         start = i * chunk_size
#         end = None if i == thread_count - 1 else (i + 1) * chunk_size
#         t = threading.Thread(target=count_words, args=(lines[start:end], results))
#         threads.append(t)
#         t.start()

#     for t in threads:
#         t.join()

#     final_counts = merge_results(results)
    
#     # Print top 10 most common words
#     sorted_counts = sorted(final_counts.items(), key=lambda x: x[1], reverse=True)
#     print("Top 10 words:")
#     for word, count in sorted_counts[:10]:
#         print(f"{word}: {count}")

# if __name__ == "__main__":
#     main()
