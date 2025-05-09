load "ventas.csv";
filter column "id_cliente" > 10;
filter column "precio_total" < 180000;
aggregate sum column "precio_total";
aggregate count column "precio_total";
aggregate average column "precio_total";
print;

//Filtra por id_cliente > 10 y precio_total < 180000, 
//luego calcula suma, conteo y promedio de precio_total.