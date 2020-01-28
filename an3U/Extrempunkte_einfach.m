
clear all
syms x y z x0 y0 z0 k pi

f(x,y)=sin(x)+cos(y)

fx(x,y)=diff(f,x)
fy(x,y)=diff(f,y)

S = solve([fx(x,y)==0, fy(x,y)==0], [x y])

X=S.x
Y=S.y


fxx(x,y)=diff(f,x,2)
fyy(x,y)=diff(f,y,2)
fxy(x,y)=diff(f,x,y)

%x=pi/2
%y=pi

fxy2=(fxy(x,y)^2)

satt=fxx(x,y)*fyy(x,y)-fxy2
