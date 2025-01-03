/* 
 * CS:APP Data Lab 
 * 
 * <Please put your name and userid here>
 * 
 * bits.c - Source file with your solutions to the Lab.
 *          This is the file you will hand in to your instructor.
 *
 * WARNING: Do not include the <stdio.h> header; it confuses the dlc
 * compiler. You can still use printf for debugging without including
 * <stdio.h>, although you might get a compiler warning. In general,
 * it's not good practice to ignore compiler warnings, but in this
 * case it's OK.  
 */

#if 0
/*
 * Instructions to Students:
 *
 * STEP 1: Read the following instructions carefully.
 */

You will provide your solution to the Data Lab by
editing the collection of functions in this source file.

INTEGER CODING RULES:
 
  Replace the "return" statement in each function with one
  or more lines of C code that implements the function. Your code 
  must conform to the following style:
 
  int Funct(arg1, arg2, ...) {
      /* brief description of how your implementation works */
      int var1 = Expr1;
      ...
      int varM = ExprM;

      varJ = ExprJ;
      ...
      varN = ExprN;
      return ExprR;
  }

  Each "Expr" is an expression using ONLY the following:
  1. Integer constants 0 through 255 (0xFF), inclusive. You are
      not allowed to use big constants such as 0xffffffff.
  2. Function arguments and local variables (no global variables).
  3. Unary integer operations ! ~
  4. Binary integer operations & ^ | + << >>
    
  Some of the problems restrict the set of allowed operators even further.
  Each "Expr" may consist of multiple operators. You are not restricted to
  one operator per line.

  You are expressly forbidden to:
  1. Use any control constructs such as if, do, while, for, switch, etc.
  2. Define or use any macros.
  3. Define any additional functions in this file.
  4. Call any functions.
  5. Use any other operations, such as &&, ||, -, or ?:
  6. Use any form of casting.
  7. Use any data type other than int.  This implies that you
     cannot use arrays, structs, or unions.

 
  You may assume that your machine:
  1. Uses 2s complement, 32-bit representations of integers.
  2. Performs right shifts arithmetically.
  3. Has unpredictable behavior when shifting if the shift amount
     is less than 0 or greater than 31.


EXAMPLES OF ACCEPTABLE CODING STYLE:
  /*
   * pow2plus1 - returns 2^x + 1, where 0 <= x <= 31
   */
  int pow2plus1(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     return (1 << x) + 1;
  }

  /*
   * pow2plus4 - returns 2^x + 4, where 0 <= x <= 31
   */
  int pow2plus4(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     int result = (1 << x);
     result += 4;
     return result;
  }

FLOATING POINT CODING RULES

For the problems that require you to implement floating-point operations,
the coding rules are less strict.  You are allowed to use looping and
conditional control.  You are allowed to use both ints and unsigneds.
You can use arbitrary integer and unsigned constants. You can use any arithmetic,
logical, or comparison operations on int or unsigned data.

You are expressly forbidden to:
  1. Define or use any macros.
  2. Define any additional functions in this file.
  3. Call any functions.
  4. Use any form of casting.
  5. Use any data type other than int or unsigned.  This means that you
     cannot use arrays, structs, or unions.
  6. Use any floating point data types, operations, or constants.


NOTES:
  1. Use the dlc (data lab checker) compiler (described in the handout) to 
     check the legality of your solutions.
  2. Each function has a maximum number of operations (integer, logical,
     or comparison) that you are allowed to use for your implementation
     of the function.  The max operator count is checked by dlc.
     Note that assignment ('=') is not counted; you may use as many of
     these as you want without penalty.
  3. Use the btest test harness to check your functions for correctness.
  4. Use the BDD checker to formally verify your functions
  5. The maximum number of ops for each function is given in the
     header comment for each function. If there are any inconsistencies 
     between the maximum ops in the writeup and in this file, consider
     this file the authoritative source.

/*
 * STEP 2: Modify the following functions according the coding rules.
 * 
 *   IMPORTANT. TO AVOID GRADING SURPRISES:
 *   1. Use the dlc compiler to check that your solutions conform
 *      to the coding rules.
 *   2. Use the BDD checker to formally verify that your solutions produce 
 *      the correct answers.
 */


#endif
/* Copyright (C) 1991-2024 Free Software Foundation, Inc.
   This file is part of the GNU C Library.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <https://www.gnu.org/licenses/>.  */
/* This header is separate from features.h so that the compiler can
   include it implicitly at the start of every compilation.  It must
   not itself include <features.h> or any other header that includes
   <features.h> because the implicit include comes before any feature
   test macros that may be defined in a source file before it first
   explicitly includes a system header.  GCC knows the name of this
   header in order to preinclude it.  */
/* glibc's intent is to support the IEC 559 math functionality, real
   and complex.  If the GCC (4.9 and later) predefined macros
   specifying compiler intent are available, use them to determine
   whether the overall intent is to support these features; otherwise,
   presume an older compiler has intent to support these features and
   define these macros by default.  */
/* wchar_t uses Unicode 10.0.0.  Version 10.0 of the Unicode Standard is
   synchronized with ISO/IEC 10646:2017, fifth edition, plus
   the following additions from Amendment 1 to the fifth edition:
   - 56 emoji characters
   - 285 hentaigana
   - 3 additional Zanabazar Square characters */
//1
/* 
 * bitOr - x|y using only ~ and & 
 *   Example: bitOr(6, 5) = 7
 *   Legal ops: ~ &
 *   Max ops: 8
 *   Rating: 1
 */
int bitOr(int x, int y) {
	// DeMorgan's Law: distributing the negation gives
	// ~(~x) OR ~(~y) same as (x OR y)
    return ~(~x & ~y);
}
/* 
 * TMax - return maximum two's complement integer 
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 4
 *   Rating: 1
 */
int tmax(void) {
    // Max two's complement integer is
	//   0111 1111 ... 1111 same as
    // ~(1000 0000 ... 0000)
	int smallestInt;
    smallestInt = 1 << 31;
    return ~smallestInt;
}
//2
/* 
 * implication - return x -> y in propositional logic - 0 for false, 1
 * for true
 *   Example: implication(1,1) = 1
 *            implication(1,0) = 0
 *   Legal ops: ! ~ ^ |
 *   Max ops: 5
 *   Rating: 2
 */
int implication(int x, int y) {
    // Conditional Disjunctional Equivalence
    return (!x) | y;  // use bang for logical negation (0 or 1 only)
}
/* 
 * copyLSB - set all bits of result to least significant bit of x
 *   Example: copyLSB(5) = 0xFFFFFFFF, copyLSB(6) = 0x00000000
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 5
 *   Rating: 2
 */
int copyLSB(int x) {
    // Least significant bit is the rightmost bit
    // This is basically saying if x is even, return 0000 0000 ... 0000
    // if x is odd, return 1111 1111 ... 1111

	int leastSignificantBit;
	// Will be either 0000 0000 ... 0000 or
	// 0000 0000 ... 0001
    leastSignificantBit= x & 1;  // 1 acts as a mask to get only the least significant bit

    // Utilize logical vs arithmetic right shift to extended LSB
    return (leastSignificantBit << 31) >> 31;
}
/* 
 * addOK - Determine if can compute x+y without overflow
 *   Example: addOK(0x80000000,0x80000000) = 0,
 *            addOK(0x80000000,0x70000000) = 1, 
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 20
 *   Rating: 3
 */
int addOK(int x, int y) {
	// Notice that overflow only occurs when x and y have the same sign (xSign ^ ySign == 0)
	// In cases where overflow can occur (Pos + Pos or Neg + Neg), the sum should have the same
	// sign as x and y. 
	int xSignBit;
	int ySignBit;
	int sum;
	int sumSignBit;
	int overflowCanOccur;
	int differentSignSum;
	
	// Either 0000 0000 ... 0000 or 0000 0000 ... 0001
	xSignBit = (x >> 31) & 1;
	ySignBit = (y >> 31) & 1;

	sum = x + y;
	sumSignBit = (sum >> 31) & 1;

	// 1 means it can, 0 means it cannot
	overflowCanOccur = !(xSignBit ^ ySignBit);

	differentSignSum = xSignBit ^ sumSignBit;  // use of xSignBit or ySignBit does not matter

	return !(overflowCanOccur & differentSignSum);
}
/* 
 * rotateRight - Rotate x to the right by n
 *   Can assume that 0 <= n <= 31
 *   Examples: rotateRight(0x87654321,4) = 0x187654321
 *   Legal ops: ~ & ^ | + << >> !
 *   Max ops: 25
 *   Rating: 3 
 */
int rotateRight(int x, int n) {
	// For negatives, it makes the left n bits from all ones to all 0s 
	// Does not do anything for positive numbers since they are already all 0s on the left
	int leftCleanUpMask;
	int smallestNAtLeft;
	int xWithoutLeftmostN;

	leftCleanUpMask = ~((1 << 31) >> (n + (~1 + 1)));

	// Get the rightmost n digits and shift them over so they occupy the leftmost n digits
	smallestNAtLeft = x << (32 + (~n + 1));

	xWithoutLeftmostN = (x >> n) & leftCleanUpMask;
	return smallestNAtLeft | xWithoutLeftmostN;
}
//4
/* 
 * bang - Compute !x without using !
 *   Examples: bang(3) = 0, bang(0) = 1
 *   Legal ops: ~ & ^ | + << >>
 *   Max ops: 12
 *   Rating: 4 
 */
int bang(int x) {
	// if 0 return 1
	// else return 0
	int twosComp;
	int isZero;
	int isSignBitZero;

	twosComp = ~x + 1;	

	// Return whether x is 0
	// 1 for yes, 0 for no
	isZero = ((x | twosComp) >> 31) ^ 1;

	// 1 for yes, 0 for no
	isSignBitZero = ((x >> 31) & 1) ^ 1;

	return isSignBitZero & isZero;
}
/*
 * bitCount - returns count of number of 1's in word
 *   Examples: bitCount(5) = 2, bitCount(7) = 3
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 40
 *   Rating: 4
 */
int bitCount(int x) {
	// 0x55 is 0101 0101
	// left shift to continue the pattern for 16 total bits
	// 0101 0101 0101 0101
	int alternatesMask;
	int pairsMask;
	int every4Mask;
	int every8Mask;
	int every16Mask;
	int total;
	int totalShifted;

    alternatesMask = 0x55 | (0x55 << 8);
    alternatesMask = alternatesMask | (alternatesMask << 16);
    
	// 0x33 is 0011 0011
	// similar logic above to left shift to extend the pattern
    pairsMask = 0x33 | (0x33 << 8);
	pairsMask = pairsMask | (pairsMask << 16);
    
	// 0x0F is 0000 1111
    every4Mask = 0x0F | (0x0F << 8);
    every4Mask = every4Mask | (every4Mask << 16);
    
	// 0xFF is 1111 1111
    every8Mask = 0xFF | (0xFF << 16);
    
	// 1111 1111 1111 1111 0000 0000 0000 0000
    every16Mask = 0xFF | (0xFF << 8);

    // Apply masks and shifts to progressively count bits
	total = x;
	totalShifted = total >> 1;
    total = (total & alternatesMask) + (totalShifted & alternatesMask);
   
	totalShifted = total >> 2;
    total = (total & pairsMask) + (totalShifted & pairsMask);
    
	totalShifted = total >> 4;
    total = (total & every4Mask) + (totalShifted & every4Mask);
    
	totalShifted = total >> 8;
    total = (total & every8Mask) + (totalShifted & every8Mask);
    
	totalShifted = total >> 16;
	total = (total & every16Mask) + (totalShifted & every16Mask);
    
    return total;
}
//float
/* 
 * floatScale64 - Return bit-level equivalent of expression 64*f for
 *   floating point argument f.
 *   Both the argument and result are passed as unsigned int's, but
 *   they are to be interpreted as the bit-level representation of
 *   single-precision floating point values.
 *   When argument is NaN, return argument
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 35
 *   Rating: 4
 */
unsigned floatScale64(unsigned uf) {
	unsigned signBit;
	int exponentMask;
	unsigned exponent;
	int power;   // 2^6 = 64 
	unsigned result;
	unsigned infinity;

    infinity = 0x7F800000;
	result = uf;

	// The leftmost bit
    signBit = (uf >> 31) & 1;
	signBit = signBit << 31;

	// Masks to extract only the respective parts of the floating point number
    exponentMask = 0x7F800000;
	exponent = result & exponentMask;

	power = 6;
	while (power > 0) {
		exponent = result & exponentMask;
		if (exponent == 0) {
			result = signBit | (result << 1);  // move from fraction to exponent
		}
		else if (exponent != infinity) {
			result = result + (1 << 23);  // multiply result by 2 (to contribute to exponent)
			exponent = result & exponentMask;

			// exponent overflows
			if (exponent == infinity) {
				result = result & 0xFF800000;
			}
		}
		power--;
	}
	return result;
}

/* 
 * floatInt2Float - Return bit-level equivalent of expression (float) x
 *   Result is returned as unsigned int, but
 *   it is to be interpreted as the bit-level representation of a
 *   single-precision floating point values.
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 30
 *   Rating: 4
 */

int floatInt2Float(int x) {
    unsigned absX;      // absolute value of x
    int leftmost1Position;  // the position of the most significant 1
    int fractionMask;		// isolate the fraction part of the float
    unsigned fraction;		// the actual fraction part of the float
    unsigned exponent;
    unsigned signBit; 	    // the sign of the number, 1 for neg, 0 for pos
    int isNeedToRound;
	int shouldRoundUp;
	int hasExtraBits;
    int currentPos;
	unsigned tempX;

	// Edge Case since negating 0 gives all ones
	if (x == 0) {
		return x;
	}

    // Determine the sign bit
    signBit = x & 0x80000000;

    // Make x positive if it's negative
    if (signBit) {
        absX = -x;
    }
	else {
        absX = x;
    }

    // Find the position of the leftmost 1 bit
    leftmost1Position = -1;
    tempX = absX;
    currentPos = 0;
	// while digits of tempX are still there
    while (tempX != 0) {
		// 1 has been found
        if (tempX & 1) {
            leftmost1Position = currentPos;
        }
		// keep searching
        tempX = tempX >> 1;  // right shift to continue search for 1s
        currentPos++;
    }

    fraction = absX << (31 - leftmost1Position);
	// fraction is now on the extreme left (populating the most significant bits)

	// 0000 0000 0111 1111 1111... (23 ones for fraction isolation)
    fractionMask = 0x007FFFFF;

    isNeedToRound = (fraction >> 7) & 1;  
    shouldRoundUp = (fraction >> 6) & 1;     
    hasExtraBits = fraction & 0x3F;       

    // Move fraction from leftside to proper location
	// And isolate the fraction with the mask
    fraction = (fraction >> 8) & fractionMask;

    if (isNeedToRound && (shouldRoundUp || hasExtraBits || (fraction & 1))) {
        fraction += 1;  // round fraction
    }

    if (fraction == (fractionMask + 1)) {  // if fraction overflows into the exponent
        fraction = 0;
        leftmost1Position += 1;
    }

    exponent = 127 + leftmost1Position;
    exponent = exponent << 23;  // shift exponent to proper location

    // Assemble the final float representation
    return signBit | exponent | fraction;
}
