
figure
c=stem(0,abs(a0_2));
set(c,'Color','blue','MarkerSize',0.1,'LineWidth',2);
for n=1:10 
A(n)=vpa(sqrt(a(n)^2+b(n)^2));
hold on
d=stem(n*w0,A(n),'o');
set(d,'Color','blue','MarkerSize',0.1,'LineWidth',2);

end

xlabel wn
ylabel An