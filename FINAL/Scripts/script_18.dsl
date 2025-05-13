load "ventas.csv";
filter column "id_cliente" > 45 and column "precio_total" > 200000;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por id_cliente > 45 y precio_total < 200000, 
//luego calcula count, suma y promedio de cantidad.