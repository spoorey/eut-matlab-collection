%Gradient Rechnungen für 2 Dimensionen

clear all
syms x y

%Funktion eingeben:
f(x,y)=(2*x+y)/(1+x*y)

g(x,y)=simplify(gradient(f(x,y)))

%Funktion im Punkt...eingeben:
x0=1 ;
y0=1 ;

%Richtung des stärksten Anstiegs:
G=g(x0,y0)

%Richtung des stärksten Abstiegs:
A=-g(x0,y0)

%In Richtung des Vektors U....eingeben:
Ux=1/sqrt(2)  ;
Uy=1/sqrt(2)  ;

U=[Ux;Uy];
U_n=norm(U);

%Richtungsableitung im Punkt (x0,y0) in Richtung U:
L=simplify(U(1,1)/U_n*G(1,1)+U(2,1)/U_n*G(2,1))

%plot
%[X,Y]=meshgrid(-10:1:10);
%Z=(2*x+y)/(1+x*y);
%[px,py]=gradient(Z);
%quiver(X,Y,px,py)