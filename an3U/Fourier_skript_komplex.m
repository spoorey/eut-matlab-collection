
clear all

syms t n
assume(n,'integer')

%f(t)=piecewise(2*n,)

%fplot(f(t),[0,4*pi])

syms pi

T=2*pi

w0=(2*pi)/T

c0=1/T*int(f(t),t,0,4*pi)

c(n)=1/T*simplify(int(f(t)*exp(-j*n*w0*t),t,-pi/2,pi/2),100)

p(n)=atan(imag(c(n))/real(c(n)))

an=2*real(c(n))
bn=-2*imag(c(n))

B(n)=abs(c(n))
figure
c=stem(0,abs(c0));
set(c,'Color','blue','MarkerSize',0.1,'LineWidth',2);
for n=-10:-1 
hold on
d=stem(n*w0,B(n),'o');
set(d,'Color','blue','MarkerSize',0.1,'LineWidth',2);
end
for n=1:10
hold on
c=stem(n*w0,B(n),'o')
set(c,'Color','blue','MarkerSize',0.1,'LineWidth',2);
end
xlabel wn
ylabel cn