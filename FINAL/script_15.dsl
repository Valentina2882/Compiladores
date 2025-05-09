load "ventas.csv";
filter column "id_cliente" <= 50;
filter column "precio_total" <= 90000;
aggregate sum column "precio_total";
aggregate count column "precio_total";
aggregate average column "precio_total";
print;

//Filtra por id_cliente ≤ 50 y precio_total ≤ 90000, 
//luego calcula suma, conteo y promedio de precio_total.