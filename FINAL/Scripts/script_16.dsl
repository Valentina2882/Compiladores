load "ventas.csv";
filter column "precio_total" > 20000;
aggregate count column "cantidad";
aggregate average column "cantidad";
aggregate sum column "cantidad";
print;

//Filtra por precio_total > 20000 y calcula 
//count, suma y promedio de cantidad.