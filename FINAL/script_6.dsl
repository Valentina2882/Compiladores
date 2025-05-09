load "ventas.csv";
filter column "id_cliente" == 2;
filter column "precio_total" <= 90000;
aggregate count column "precio_total";
aggregate sum column "precio_total";
aggregate average column "precio_total";
print;

//Filtra por id_cliente = 2 y precio_total ≤ 90000, 
//luego calcula count, suma y promedio de precio_total.