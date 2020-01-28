
clear all

syms s  t a


f(t)=piecewise(0&lt;=t&lt;2,1,2&lt;=t,t^2-4*t+4)

%assume(a,'real')
assume(real(s)&gt;0)

%f&uuml;r 2 Bereiche:

%F(s)=int(1*exp(-s*t),t,0,2)+int((t^2-4*t+4)*exp(-s*t),t,2,inf)

F(s)=int(f(t)*exp(-s*t),t,0,inf)

simplify(F(s),100)

Z(s)=laplace(f(t))