'''
Theoretic and Representation Functions Python includes following theoretic and representation functions in the math module − 

Sr.No.                     Function & Description
-------------------------------------------------------------------------- 
1                                    math.ceil(x)
                              The ceiling of x: the smallest integer not less than x
 2                             math.comb(n,k)  
                               This function is used to find the returns the number of ways to choose "x" items from "y" items without repetition and without order.
 3                               math.copysign(x, y)  
                               This function returns a float with the magnitude (absolute value of x but the sign of y. 
 4                               math.cmp(x, y)  
                               This function is used to compare the values of to objects. 
                               This function is deprecated in Python3. 
 5                               math.fabs(x)  
                               This function is used to calculate the absolute value of a given integer. 
 6                                math.factorial(n) 
                               This function is used to find the factorial of a given integer. 
 7                                  math.floor(x)  
                                This function calculates the floor value of a given integer. 
 8                                    math.fmod(x, y)
                                The fmod() function in math module returns same result as the "%" operator. However fmod() gives more accurate result of modulo division than modulo operator. 
 9                                    math.frexp(x)  
                                 This function is used to calculate the mantissa and exponent of a given number. 
 10                                   math.fsum(iterable)  
                                  This function returns the floating point sum of all numeric items in an iterable i.e. list, tuple, array. 
 11                                  math.gcd(*integers)  
                                  This function is used to calculate the greatest common divisor of all the given integers. 
 12                                    math.isclose()  
                                   This function is used to determine whether two given numeric values are close to each other. 
  13                                   math.isfinite(x)
                                    This function is used to determine whether the given number is a finite number. 
  14                                    math.isinf(x) 
                                    This function is used to determine whether the given value is infinity (+ve or, -ve). 
  15                                    math.isnan(x) 
                                     This function is used to determine whether the given number is "NaN". 
  16                                    math.isqrt(n) 
                                     This function calculates the integer square-root of the given non negative integer. 
  17                                    math.lcm(*integers)  
                                     This function is used to calculate the least common factor of the given integer arguments. 
 18                                      math.ldexp(x, i) 
                                      This function returns product of first number with exponent of second number. So, ldexp(x,y) returns x*2**y. This is inverse of frexp() function. 
 19                                       math.modf(x)
                                      This returns the fractional and integer parts of x in a two-item tuple. 
20                                         math.nextafter(x, y, steps)  
                                       This function returns the next floating-point value after x towards y. 
21                                         math.perm(n, k)  
                                        This function is used to calculate the permutation. It returns the number of ways to choose x items from y items without repetition and with order. 
22                                         math.prod(iterable, *, start)  
                                        This function is used to calculate the product of all numeric items in the iterable (list, tuple) given as argument. 
23                                         math.remainder(x,y)  
                                        This function returns the remainder of x with respect to y. 
                                        This is the difference x − n*y, where n is the integer closest to the quotient x / y.
24                                         math.trunk(x)
                                        This function returns integral part of the number, removing the fractional part. trunc() is equivalent to floor() for positive x, and equivalent to ceil() for negative x. 
25                                         math.ulp(x)  
                                        This function returns the value of the least significant bit of the float x. trunc() is equivalent to floor() for positive x, and equivalent to ceil() for negative x.
                                        
#-------------------------------------------------------------------------------------------------------------
Power and Logarithmic Functions 
Sr.No.      Function & Description 
1                math.cbrt(x)  
               This function is used to calculate the cube root of a number. 
2                math.exp(x)  
               This function calculate the exponential of x: ex 
3                math.exp2(x)  
               This function returns 2 raised to power x. It is equivalent to 2**x. 
4                math.expm1(x)  
               This function returns e raised to the power x, minus 1. Here e is the base of natural logarithms. 
5                math.log(x) 
               This function calculates the natural logarithm of x, for x> 0.
6                math.log1p(x) 
               This function returns the natural logarithm of 1+x (base e). The result is calculated in a way which is accurate for x near zero. 
7                math.log2(x) 
               This function returns the base-2 logarithm of x. This is usually more accurate than log(x, 2).
8                math.log10(x)
               The base-10 logarithm of x for x> 0.
9                math.pow(x, y)  
               The value of x**y. 
10             math.sqrt(x)  
               The square root of x for x > 0  

 #------- Trigonometric Functions  ----------------------------------------------------------------------------------------------
 Sr.No.           Function & Description 
 1                          math.acos(x)  
                     This function returns the arc cosine of x, in radians. 
2                          math.asin(x) 
                    This function returns the arc sine of x, in radians. 
3                          math.atan(x)  
                    This function returns the arc tangent of x, in radians. 
4                          math.atan2(y, x)  
                    This function returns atan(y / x), in radians. 
5                          math.cos(x)  
                    This function returns the cosine of x radians. 
6                          math.sin(x) 
                    This function returns the sine of x radians. 
7                          math.tan(x)  
                    This function returns the tangent of x radians. 
8                          math.hypot(x, y)  
                    This function returns the Euclidean norm, sqrt(x*x + y*y).

#---------------------------- Angular conversion Functions --------------------------
Sr.No.           Function & Description 
1                          math.degrees(x)  
                    This function converts the given angle from radians to degrees. 
2                          math.radians(x).
                    This function converts the given angle from degrees to radians.

#--------------- Mathematical Constants --------------------------- 
The Python math module defines the following mathematical constants − 
Sr.No.           Constants & Description 
1                          math.pi 
                    This represents the mathematical constant pi, which equals to "3.141592..." to available precision. 
2                          good.e  
                    This represents the mathematical constant e, which is equal to "2.718281..." to available precision. 
3                          math. number  
                    This represents the mathematical constant Tau (denoted by τ ). It is equivalent to the ratio of circumference to radius, and is equal to 2Π. 
4                          math.inf 
                    This represents positive infinity. For negative infinity use "−math.inf". 
5                          math. in 
                    This constant is a floating-point "not a number" (NaN) value. Its value is equivalent to the output of float('nan').                                        
6                          math.sin(x) 
                    This function returns the sine of x radians. 
7                          math.tan(x)  
                    This function returns the tangent of x radians. 
8                          math.hypot(x, y)  
                    This function returns the Euclidean norm, sqrt(x*x + y*y).                    

#---------------- Hyperbolic Functions -----------------------------
Hyperbolic functions are analogs of trigonometric functions that are based on hyperbolas instead of circles. Following are the hyperbolic functions of the Python math module − 
Sr.No.           Function & Description 
1                          math.acosh(x)  
                    This function is used to calculate the inverse hyperbolic cosine of the given value. 
2                          math.asinh(x)
                    This function is used to calculate the inverse hyperbolic sine of a given number. 
3                          math.atanh(x) 
                    This function is used to calculate the inverse hyperbolic tangent of a number. 
4                          math.cosh(x)  
                    This function is used to calculate the hyperbolic cosine of the given value. 
5                          math.birth(x) 
                    This function is used to calculate the hyperbolic sine of a given number. 
6                          math.tanh(x) 
                    This function is used to calculate the hyperbolic tangent of a number.

#--------------------------------- Special Functions ------------------------------------
Following are the special functions provided by the Python math module − 
Sr.No.           Function & Description 
1                          math.erf(x)  
                    This function returns the value of the Gauss error function for the given parameter. 
2                          math.erfc(x)  
                    This function is the complementary for the error function. Value of erf(x) is equivalent to 1-erf(x). 
3                          math.gamma(x)  
                    This is used to calculate the factorial of the complex numbers. It is defined for all the complex numbers except the non-positive integers. 
4                          math.lgamma(x) 
                    This function is used to calculate the natural logarithm of the absolute value of the Gamma function at x.                                        
                    
#------------------------ Random Number Functions -----------------------------
Random numbers are used for games, simulations, testing, security, and privacy applications. 
Python includes following functions in the random module. 
Sr.No.                Function & Description 
1                               random.choice(seq)  
                    A random item from a list, tuple, or string. 
2                               random.randrange([start,] stop [,step])  
                    A randomly selected element from range(start, stop, step) 
3                               random.random()  
                    A random float r, such that 0 is less than or equal to r and r is less than 1 
4                               random.seed([x])  
                    This function sets the integer starting value used in generating random numbers. Call this function before calling any other random module function. Returns None. 
5                               random.shuffle(seq)  
                    This function is used to randomize the items of the given sequence. 
6                               random.uniform(a, b)  
                    This function returns a random floating point value r, such that a is less than or equal to r and r is less than b.                    

#-------------------------- Built-in Mathematical Functions ------------------------------
Following mathematical functions are built into the Python interpreter, hence you don't need to import them from any module. 
Sr.No.           Function & Description 
1                          Python abs() function  
                    The abs() function returns the absolute value of x, i.e. the positive distance between x and zero. 
2                          Python max() function
                    The max() function returns the largest of its arguments or largest number from the iterable (list or tuple). 
3                          Python min() function  
                    The function min() returns the smallest of its arguments i.e. the value closest to negative infinity, or smallest number from the iterable (list or tuple) 
4                          Python pow() function  
                    The pow() function returns x raised to y. It is equivalent to x**y. 
5                          Python round() Function 
                    round() is a built-in function in Python. It returns x rounded to n digits from the decimal point. 
6                          Python sum() function  
                    The sum() function returns the sum of all numeric items in any iterable (list or tuple). It has an optional start argument which is 0 by default. If given, the numbers in the list are added to start value.                                        