load "ventas.csv";
filter column "id_cliente" >= 5 and column "precio_total" >= 150000;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por id_cliente ≥ 1 y precio_total < 50000, 
//luego calcula count, suma y promedio de cantidad.