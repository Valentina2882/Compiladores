load "ventas.csv";
filter column "precio_total" == 24831;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por precio_total = 24831 y calcula 
//count, suma y promedio de cantidad.