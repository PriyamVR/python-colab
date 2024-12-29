Here are the solutions to all the tasks in Python:

### 1. Compare a number with 200
```python
num = int(input("Enter a number: "))
if num > 200:
    print("Greater if num is greater than 200.")
elif num < 200:
    print("Lesser if num is less than 200.")
else:
    print("Equal if num is exactly equal to 200.")
```

---

### 2. Simple ATM banking system
```python
# ATM System
PIN = "1234"  # Set a default PIN for simplicity
balance = 1000  # Default balance

entered_pin = input("Enter your PIN: ")

if entered_pin == PIN:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            print(f"Your balance is: ${balance}")
        elif choice == 2:
            deposit = float(input("Enter amount to deposit: "))
            balance += deposit
            print(f"Deposited successfully! New balance: ${balance}")
        elif choice == 3:
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw <= balance:
                balance -= withdraw
                print(f"Withdrawal successful! Remaining balance: ${balance}")
            else:
                print("Insufficient funds!")
        elif choice == 4:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN. Access denied.")
```

---

### 3. Assign grades based on marks
```python
marks = int(input("Enter your marks: "))

if marks > 90:
    print("Grade: A")
elif marks > 80:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")
```

---

### 4. Print the given pattern
```python
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
```

---

### 5. Find the largest among three numbers
```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest = max(num1, num2, num3)
print(f"The largest number is: {largest}")
``` 

Feel free to run these programs and let me know if you need further explanations!