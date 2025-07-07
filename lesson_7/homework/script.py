# # Homework

# ## Task
# Learn about `map` and `filter` functions, and be prepared to explain them in class. Provide examples using these functions with `lambda` expressions.

# ---

# # Problems

# ## 1. is_prime(n) funksiyasi
# `is_prime(n)` funksiyasini hosil qiling (`n > 0`). Agar `n` soni tub bo'lsa `True`, aks holda `False` qiymat qaytarsin.

# ### Misollar:
# - **Kiritish:**  
#   4  
#   **Natija:**  
#   False  
#   _(Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)_

# - **Kiritish:**  
#   7  
#   **Natija:**  
#   True  
#   _(Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)_

# ---

# def isprime(n):
#     if n > 1:
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 print('Not prime')
#                 break
#         else:
#             print('Prime')
#     else:
#         print('Not prime')


# isprime(10)




# ## 2. digit_sum(k) funksiyasi
# `digit_sum(k)` funksiyasini yozing, u `k` sonining raqamlari yig'indisini hisoblaydi.

# ### Misollar:
# - **Kiritish:**  
#   24  
#   **Natija:**  
#   6  
#   _(Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)_

# - **Kiritish:**  
#   502  
#   **Natija:**  
#   7  
#   _(Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)_

# ---

# def sums(n):
#     string = str(n)
#     k = 0
#     for i in string:
#         k += int(i)
#     return k

# print(sums(1342))

# ## 3. Ikki sonning darajalari
# Berilgan `N` sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, `2**k` shaklidagi sonlarni) chop etuvchi funksiyani yozing.

# ### Misol:
# - **Kiritish:**  
#   10  
#   **Natija:**  
#   2 4 8  
#   _(Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)_

# def deg(n):
#     i = 1
#     while 2**i < n:
#         print(2**i, end=' ')
#         i += 1

# deg(20)


