
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