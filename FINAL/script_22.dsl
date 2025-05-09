load "ventas.csv";
filter column "precio_total" <= 100000;
aggregate average column "precio_total";
aggregate sum column "precio_total";
aggregate count column "precio_total";
print;

//Filtra por precio_total ≤ 100000 y calcula 
//su promedio, suma y conteo.