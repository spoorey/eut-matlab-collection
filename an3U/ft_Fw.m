
clear all

syms t w pi

assume(w,'real')

f(t)=(1+t)*exp(-abs(t))

%f(t)=piecewise(abs(t)&lt;1,cos(pi*t),abs(t)&gt;=1,0)

F(w)=simplify(int(f(t)*exp(-j*w*t),t,-inf,inf),100)

F(w)=simplify(fourier(f(t)),100)