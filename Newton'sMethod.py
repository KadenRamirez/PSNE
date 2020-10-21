"""
Creator: Kaden Ramirez
File Name: Newton's Method
Overall Program Goal: Finds the approximate launch angle of a projectile
	from the initail height, velocity and horizontal distance traveled
	using Newton's method
"""
import numpy as np

"""
f is the method to create a function.

@param yo: yo is the intial height.
@param vo: vo is the intial velocity.
@param x0: x0 is the given x value or distance.
@param theta: theta is the estimated value for the angle.

@var fx: fx is the finished calculation using the derived equation
yo+tan(theta)*x-9.8*x^2/(2*vo^2*cos^2(theta)).
This equation results in the finished function value of theta.
"""
def f(yo,vo,x0,theta):
	fx=yo+np.tan(theta)*x0-9.8*np.square(x0)/(2*np.square(vo)*np.square((np.cos(theta))))
	return fx

"""
df is the method used to create the derivative of the function.
It accomplishes this by using the limit definition of derivative 
or limit as x aproaches h of f(x+h)-f(x)/h, where h is, in this case,
a very small value.

@param yo: yo is the intial height.
@param vo: vo is the intial velocity.
@param x0: x0 is the given x value or distance.
@param theta: theta is the estimated value for the angle.
@param limH: limH is the h within f(x+h)-f(x)/h of the limiit definition

@var f1: f1 is the f(x+h) of the derivative definition
@var f2: f2 is the f(x) of the derivative definition
@var df: df is the completed derivative of the function
"""
def df(yo,vo,x0,theta,limH=1**-10):
	f1=f(yo,vo,x0,theta)
	f2=f(yo,vo,x0,theta+limH)
	df=(f2-f1)/limH
	return df

"""
newtonMethod finds the approximate lauch angle of the projectile.
	The method is as follows: Xn+1= Xn -f(Xn)/f'(Xn) where Xn is the
	intial guess and n is the number of times the method has looped.

@param yo: yo is the intial height.
@param vo: vo is the intial velocity.
@param x0: x0 is the given x value or distance.
@param maxIterations: maxIterations is the maximum number of times
	newton's method is allowed to loop until the angle is found.
@param guess: guess is the guessed angle that may be close to the launch
	angle of the projectile

@var theta: theta is the intitail guess that is optimized until is the 
	launch angle.
@var fx: fx is the function.
@var dfx: dfx is the derivative of the function.
"""
def newtonMethod(yo,vo,x0,maxIterations,guess):
	theta=guess
	for i in range (maxIterations):
		fx=f(yo,vo,x0,theta)
		dfx= df(yo,vo,x0,theta)
		theta= theta-fx/dfx
	return theta


#input variables and newtons method requirements
yo=input("Input the initail height in meters: ")
vo=input("Input the initail velocity in meters squared: ")
x0=input("Input the horzizontal distance traveled in meters: ")
yo=float(yo)
vo=float(vo)
x0=float(x0)
guesses = [3.0,2.5,1.5,.5,-1.5,-2.5,-3.0] #guesses are in radians
maxIterations=1000

#loops the number of guesses in the array guesses or in this case two
for guess in guesses:
	a1=np.degrees(newtonMethod(yo,vo,x0,maxIterations,guess))%180
	if a1>90:
		a1-=180
		print("The possible angle is "+str(a1)+" degrees.")
	elif 30<a1<40:
		a1-=20
		print("The possible angle is "+str(a1)+" degrees.")
	else:
		print("The possible angle is "+str(a1)+" degrees.")
