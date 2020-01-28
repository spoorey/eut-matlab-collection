
clear all
syms t U0 s R L C

I(s)=U0/s*1/(R+L*s)

i(t)=ilaplace(I(s))
%heaviside(t) nicht vergessen E(t)!!!