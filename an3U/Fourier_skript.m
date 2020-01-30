
clear all

syms x n
assume(n,'integer')

f(x)=piecewise(-pi<=x<=pi,cos(x/2))

fplot(f(x))

syms pi

T=2*pi

w0=(2*pi)/T

a0_2=simplify(1/T*int(f(x),x,-pi,pi),100)

a(n)=simplify(2/T*int(f(x)*cos(n*w0*x),x,-pi,pi),100)
b(n)=simplify(2/T*int(f(x)*sin(n*w0*x),x,-pi,pi),100)

A(n)=sqrt(a(n)^2+b(n)^2)