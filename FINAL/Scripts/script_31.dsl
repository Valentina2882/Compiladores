load "ventas.csv";
filter column "id_venta" > 10 and column "precio_total" >= 30000;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por id_venta > 10 y precio_total ≥ 30000, 
//luego calcula count, suma y promedio de cantidad.