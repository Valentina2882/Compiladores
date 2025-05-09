load "ventas.csv";
filter column "id_cliente" < 50;
filter column "precio_total" < 80000;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por id_cliente < 50 y precio_total < 80000, 
//luego calcula count, suma y promedio de cantidad.