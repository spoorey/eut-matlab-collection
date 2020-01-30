
clear all
syms w t pi

assume(t,'real')
assume (w,'real')
%assume(w,'positive')
F(w)=w*exp(-abs(w))

%F(w)=piecewise(-pi<w<pi,1/4*(pi^2-w^2))

f(t)=simplify(1/(2*pi)*int(F(w)*exp(j*w*t),w,-inf,inf),100)

f(t)=simplify(ifourier(F(w),w,t),100)