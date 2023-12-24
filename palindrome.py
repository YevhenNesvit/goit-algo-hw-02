from collections import deque

def is_palindrome(input_str):
    # Перетворимо рядок у нижній регістр і видалимо пробіли
    processed_str = input_str.lower().replace(" ", "")
    
    # Створимо двосторонню чергу та додамо символи рядка до неї
    char_queue = deque(processed_str)
    
    # Порівняємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False  # Якщо символи не збігаються, рядок не є паліндромом
    
    return True  # Якщо усі символи збігаються, рядок є паліндромом

# Приклад використання:
input_true = "A man a plan a canal Panama"
result = is_palindrome(input_true)
print(f'Is "{input_true}" a palindrome? {result}')

input_false = "This is not a palindrome"
result = is_palindrome(input_false)
print(f'Is "{input_false}" a palindrome? {result}')