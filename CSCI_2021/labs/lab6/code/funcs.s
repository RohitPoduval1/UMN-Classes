.text
.global my_max
.global my_pow

# Computes maximum of 2 arguments
# Return x if x > y, else return y
# You can assume argument 1 (x) is in %edi
# You can assume argument 2 (y) is in %esi
# If you need to store temporary values, you may use the following registers:
#   %eax, %ecx, %edx, %esi, %edi, %r8d, %r9d, %r10d, %r11d
# DO NOT USE other registers. We will learn why soon.
my_max:
    movl $0, %eax    # move the value 0 into return register eax
	cmpl %esi, %edi  # compare arg1 (x) with arg2 (y)
	jg .GREATER      # if x > y, go to GREATER
	
	movl %esi, %eax  # else (x <= y) return y
    ret

.GREATER:
	movl %edi, %eax  # move arg1 (x) into the return register %eax (return x)
	ret
	

# Computes base^exp
# You can assume argument 1 (base) is in %edi
# You can assume argument 2 (exp) is in %esi
# If you need to store temporary values, you may use the following registers:
#   %eax, %ecx, %edx, %esi, %edi, %r8d, %r9d, %r10d, %r11d
# DO NOT USE other registers. We will learn why soon.
my_pow:
    movl $1, %eax     # eventual return value initialized with 1
	movl $0, %ecx     # counter = 0 (to keep track of number of multiplications)
	jmp .EXPONENT     # jump to .EXPONENT to perform the repeated mutliplication

    ret


.EXPONENT:
	mul %edi      	  # %eax = R[%eax] * R[%edi]
	addl $1, %ecx     # increment counter since a multiplication was performed

	cmpl %esi, %ecx   # compare counter and exponent
	jl .EXPONENT      # if counter < exponent: continue multiplying 

	ret				  # else break
