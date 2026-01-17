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

#---------------- Angular conversion Functions ------------------------------------
Following are the angular conversion function provided by Python math module −                                        
Sr.No.                Function & Description 
1                               math.degrees(x)  
                         This function converts the given angle from radians to degrees. 
2                               math.radians(x)
                         This function converts the given angle from degrees to radians.