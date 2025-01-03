import re


class Rational:
    def __init__(self, num=0, den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
    def __str__(self):
        if self.numerator == 0:
            return "0"
        else:
            return f"{self.numerator}/{self.denominator}"
    def scale(self, num):
        return f"{self.numerator * num}/{self.denominator * num}"


class Sentence:
    def __init__(self, text=""):
        self.__sentence = text

    def getSentence(self):
        return self.__sentence
    
    def getWords(self):
        return [word for word in self.__sentence.split(" ")]
    
    def getLength(self):
        return len(self.__sentence)

    def getNumWords(self):
        count = 0
        for word in self.__sentence.split(" "):
            count += 1
        return count


class SentenceV1:
    def __init__(self, text=""):
        self.__sentence_list = text.split(" ")
    
    def getSentence(self):
        return " ".join(self.__sentence_list)
    
    def getWords(self):
        return self.__sentence_list
    
    def getLength(self):
        return len(self.getSentence())

    def getNumWords(self):
        count = 0
        for word in self.__sentence_list:
            count += 1
        return count 


class Poly:
    def __init__(self, coeff=[0]):
        self.__coeff = coeff

    def degree(self):
        return len(self.__coeff) - 1
    
    def insertTerm(self, deg, coeff):
        # if you're adding a new highest degree, you need to populate the nonexistent ones with 0
        if deg > len(self.__coeff):
            for i in range(deg):
                try:
                    self.__coeff[i]            # try to access the lower elements
                except:
                    self.__coeff.insert(i, 0)  # if it doesn't work, the element doesn't exist so put 0 there
            self.__coeff.append(coeff)         # the highest degree will be the last coefficient in the list

        # if the degree already exists, just replace it with the new one and you're done
        elif deg < len(self.__coeff):
            self.__coeff[deg] = coeff
        return self.__coeff

    def __str__(self):
        ans = ""
        # Handles the first term
        if self.__coeff[-1] == 1:
            ans += f"x^{len(self.__coeff) - 1}"
        else:
            ans += f"{self.__coeff[-1]}x^{len(self.__coeff) - 1}"
        
        # Get the general format of the polynomial for every term other than the first
        # coefficient * x ^ exponent
        for i in range(len(self.__coeff) - 2, -1, -1):  # step backwards so the highest degree is first
            exp = i
            coeff = self.__coeff[i]
            if coeff >= 0:
                ans += f"+{coeff}x^{exp}"
            elif coeff < 0:
                ans += f"{coeff}x^{exp}"

        # Clean up the polynomial
        ans = ans.replace("x^0", "")
        ans = ans.replace("x^1", "x")
        matches = re.findall('\+0x\^\d', ans)
        for match in matches:
            ans = ans.replace(match, "")
        ans = ans.replace("-", " - ")
        ans = ans.replace("+", " + ")
        return ans
    
    def integrate(self):
        ans = ""
        # Handles the first term
        if self.__coeff[-1] == 1:
            if self.__coeff[-1] == 0:
                pass
            elif (len(self.__coeff)) / 1 == 1:
                ans += f"+x^{len(self.__coeff)}"
            else:
                ans += f"x^{len(self.__coeff)}/{len(self.__coeff)}"
        else:
            ans += f"{self.__coeff[-1]}x^{len(self.__coeff)}/{len(self.__coeff)}"
        
        for i in range(len(self.__coeff) - 2, -1, -1): 
            exp = i
            coeff = self.__coeff[i]
            
            if coeff == 0:
                pass
            elif (exp + 1) / coeff == 1:
                ans += f"+x^{exp + 1}"
            else:
                ans += f"{coeff}x^{exp+1}/{exp+1}"
        
        # Clean up the polynomial
        ans = ans.replace("x^0", "")
        ans = ans.replace("x^1", "x")
        matches = re.findall('\+0x\^\d', ans)  # match any pattern of 0x to any power
        for match in matches:
            ans = ans.replace(match, "")
        ans = ans.replace("-", " - ")
        ans = ans.replace("+", " + ")
        ans += " + C"
        return ans
            

def main():
    # Tests for Rational class
    x = Rational()
    y = Rational(3, 5)
    print(x)  # should print 0
    print(y)  # should print 3/5
    print(y.scale(2) == "6/10")


    # Tests for Sentence class
    hi = Sentence("hi")
    print(hi.getSentence() == "hi")
    print(hi.getLength() == 2)
    print(hi.getNumWords() == 1)
    print(hi.getWords() == ["hi"])
    s = Sentence("I am programming now")
    print(s.getSentence() == "I am programming now")
    print(s.getLength() == 20)
    print(s.getNumWords() == 4)
    print(s.getWords() == ["I", "am", "programming", "now"])

    n = SentenceV1("This is revised")
    print(n.getSentence() == "This is revised")
    print(n.getLength() == 15)
    print(n.getNumWords() == 3)
    print(n.getWords() == ["This", "is", "revised"])
    '''
    * Is one method of storing the sentence better than the other?
        -Storing the sentence as a list of words (as in SentenceV1) might be better because you only have to
        split the sentence once in the constructor. In Sentence, you have to split the sentence multiple times.
        If you are going to split the sentence that many times, you might as well do it once. 
    * Are some methods more efficient in one version than in the other?
        -getWords is more efficient in SentenceV1 because the sentence is already separated for you
    '''


    # Tests for Poly class
    p2 = Poly([1, 5, 1])                            # x^2 + 5x + 1
    print(p2.insertTerm(1, 2) == [1, 2, 1])
    print(p2.integrate())                           # x^3/3 + x^2 + x + C
    p1 = Poly([-4, -23.2, 36.7])
    print(p1)                                       # 36.7x^2 – 23.2x - 4
    p3 = Poly([1, 2, 3, 4, 0, 5])                   # 5x^5 + 4x^3 + 3x^2 + 2x + 1
    print(p3)                                       # 5x^5 + 4x^3 + 3x^2 + 2x + 1
    print(p3.integrate())                           # 5x^6/6 + x^4 + x^3 + x^2 + x + C


if __name__ == "__main__":
    main()
