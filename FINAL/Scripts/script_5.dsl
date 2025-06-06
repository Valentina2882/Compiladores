load "ventas.csv";
filter column "id_venta" > 50 or column "precio_total" >= 50000;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por precio_total ≥ 50000 y calcula count, 
//suma y promedio de cantidad.