load "ventas.csv";
filter column "precio_total" < 90000;
filter column "id_cliente" > 2;
aggregate count column "precio_total";
aggregate sum column "precio_total";
aggregate average column "precio_total";
print;

//Filtra por precio_total < 90000 y id_cliente > 2, 
//luego calcula count, suma y promedio de precio_total.