load "ventas.csv";
filter column "id_cliente" == 28 and column "precio_total" >= 30000;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por id_cliente = 28 y precio_total ≥ 30000, 
//luego calcula count, suma y promedio de cantidad.