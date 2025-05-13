load "ventas.csv";
filter column "id_cliente" == 5 and column "precio_total" < 150000;
aggregate count column "precio_total";
aggregate average column "precio_total";
aggregate sum column "precio_total";
print;

//Filtra por precio_total > 10000 y id_cliente = 5, 
//luego calcula count, promedio y suma de precio_total.