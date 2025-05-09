load "ventas.csv";
filter column "precio_total" == 147332;
aggregate sum column "cantidad";
aggregate count column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por precio_total = 147332 y calcula suma, 
//count y promedio de cantidad.