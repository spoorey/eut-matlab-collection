
clear all
syms x n
assume(n,'integer')

f(x)=x/(1+x)

x0=2

Order=2

T(x)=taylor(f(x),'ExpansionPoint',x0,'Order',Order+1)

%F=double(abs(T(0.2)-f(0.2)))