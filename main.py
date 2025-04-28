def main():
    ans = input("Please enter a Word: ").lower()
    l = 0
    r = len(ans)-1
    
    while l < r:
        if word[l] != word[r]:
            return f'{ans} is Not a Palindrome'
        l+=1
        r-=1
    return f'{ans} is a Palindrome'

    


if __name__ == "__main__":
    print(main())