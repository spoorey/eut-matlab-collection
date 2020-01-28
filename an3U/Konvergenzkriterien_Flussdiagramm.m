
%Konvergenzkriterien gem&auml;ss Flussdiagramm

clear all
syms x n

%Funktion nach dem Summenzeichen eingeben:
f(n)=exp(-sqrt(n))/sqrt(n)

%Erste Iteration der Summe:
n0=1

%Divergenzkriterium
D=limit(f(n),n,inf)

%Quotientenkriterium
Q=simplify(limit(abs(f(n+1)/f(n)),n,inf))

%Wurzelkriterium
W=simplify(limit((abs(f(n))^(1/n)),n,inf))

%1. Ableitung muss negativ sein f&uuml;r Integralkriterium
fn(n)=diff(f(n),n,1);

if D~=0
disp("divergent gem&auml;ss Divergenzkriterium")
elseif D==0
if W&lt;1||Q&lt;1
disp("konvergent gem&auml;ss W/Q-Kriterium")
elseif W&gt;1||Q&gt;1
disp("divergent gem&auml;ss W/Q-Kriterium")
elseif W==1||Q==1
if f(n0)&gt;0 &amp;&amp; fn(n0)&lt;0
I(n)=simplify(int(f(n),n0,inf))
if I(n0)==inf
disp("divergent gem&auml;ss Integralkriterium")
elseif I(n0)&lt;inf
disp("konvergent gem&auml;ss Integralkriterium")
else
disp("Selber ausrechnen!")
end
else
disp("Selber ausrechnen!")
end
end
end
