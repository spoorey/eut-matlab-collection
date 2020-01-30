
clear all
syms x y z x0 y0 z0 k

%f(x,y)=input("f(x,y)=")

f(x,y)=x^2+y^2+(6-3*x-2*y)^2

fx(x,y)=diff(f,x);
fy(x,y)=diff(f,y);

S = solve([fx(x,y)==0, fy(x,y)==0], [x y]);

X=S.x;
Y=S.y;

fxx(x,y)=diff(f,x,2);
fyy(x,y)=diff(f,y,2);
fxy(x,y)=diff(f,x,y);

for i=1:length(X)

x0=double(X(i));
y0=double(Y(i));

z=double(f(x0,y0));

k=fxx(x0,y0)*fyy(x0,y0)-fxy(x0,y0)^2;

if fx(x0,y0)==0 && fy(x0,y0)==0
if fxx(x0,y0)<0 && fyy(x0,y0)<0 && k>0
disp("Maximum im Punkt ("+x0+","+y0+","+z+")")
elseif fxx(x0,y0)>0 && fyy(x0,y0)>0 && k>0
disp("Minimum im Punkt ("+x0+","+y0+","+z+")")
elseif k<0
disp("Sattelpunkt im Punkt ("+x0+","+y0+","+z+")")
end
end
end



