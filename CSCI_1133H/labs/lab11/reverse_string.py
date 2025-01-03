# Lab 11
# Warm up 1

def reverse_string(orig_string):
    if len(orig_string) == 0:
        return ""
    else:
        return orig_string[-1] + reverse_string(orig_string[:-1])
    
def main():
    print(reverse_string("hello"))
    print(reverse_string("CSCI 1133 is cool"))


if __name__ == "__main__":
    main()
