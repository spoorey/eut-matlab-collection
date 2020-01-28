
clear all
syms x y z

f(x,y)=x^2-y-x*exp(y)

fx(x,y)=diff(f(x,y),x);
fy(x,y)=diff(f(x,y),y);

x0=1 ;
y0=0 ;
z0=f(x0,y0);

z=fx(x0,y0)*(x-x0)+fy(x0,y0)*(y-y0)+z0