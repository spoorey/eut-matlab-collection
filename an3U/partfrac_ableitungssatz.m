
clear all

syms w t s u 


%x=partfrac((s^2+2*s+10)/(s^3+3*s^2+4*s+12))
%simplify(x,100)

%simplify(-diff(1/(s^2-1),s,1),100)

F(u)=5/(u^2+1)-3/(u^2+9)

simplify(int(F(u),u,0,inf),100)
