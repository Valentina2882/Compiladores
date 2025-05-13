load "ventas.csv";
filter column "id_cliente" != 25 and column "precio_total" == 26188;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "precio_total";
print;

//Filtra por id_cliente ≠ 25 y precio_total = 26188,
//luego calcula count y suma de cantidad, y promedio de precio_total.