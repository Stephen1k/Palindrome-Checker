if __name__ == "__main__":
    ans = input("Please enter a Word: ").lower()
    
    if ans == ans[::-1]:
        print(ans, 'is a palindrome')
    else:
        print(ans,'is not a palindrome')