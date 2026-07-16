import random

print("Welcome to Number Guessing Game")

print("Choose difficulty: Easy (1-50), Medium (1-100), Hard (1-500)")

choice = input("Enter difficulty level (e/m/h): ").lower()

if choice == 'e':
    upper_limit = 50
elif choice == 'm':
    upper_limit = 100
elif choice == 'h':
    upper_limit = 500
else:
    print("Invalid choice, defaulting to Medium (1-100).")
    upper_limit = 100

number = random.randint(1, upper_limit)
attempts = 0
max_attempts = 10  # limit

while attempts < max_attempts:
    try:
        guess = int(input(f"Enter a number from 1 to {upper_limit}: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congrats! You guessed it in {attempts} attempts.")
            break

        # Hint system
        if abs(guess - number) <= 10:
            print("🔥 You're very close!")
        elif abs(guess - number) <= 20:
            print("😉 You're getting warmer.")
    except ValueError:
        print("Please enter a valid number.")

if attempts == max_attempts and guess != number:
    print(f"😢 Game over! The correct number was {number}.")
