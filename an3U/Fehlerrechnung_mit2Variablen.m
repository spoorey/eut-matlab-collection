
%Fehlerrechnung mit 2 Variablen

syms x y dx dy

f(x,y)=(x*y)/(x+y)

fx(x,y)=diff(f(x,y),x);
fy(x,y)=diff(f(x,y),y);

dx=1
dy=2

F(x,y)=simplify(sqrt(fx(x,y)^2*dx^2+fy(x,y)^2*dy^2),100);

x0=25

y0=100

%z=Fehler, u=berechneter Wert
z=double(F(x0,y0))
u=double(f(x0,y0))