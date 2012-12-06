program Kolo;
var
	r,d,pole: real;
begin
	read(r);
	read(d);
	pole := (r*r-0.25*d*d)*3.141592654;
	write(pole);
end.
