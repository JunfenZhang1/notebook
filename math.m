clc;
clear;

t=-1:0.01:1;
[x,y]=meshgrid(t,t);
z=(x.^2.*y)./(x.^4+y.^2);
surf(x,y,z);
xlabel('X')
ylabel('Y')
zlabel('Z')
title('3D Surface Plot')