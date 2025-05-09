load "ventas.csv";
filter column "id_cliente" > 10;
filter column "precio_total" < 100000;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "cantidad";
print;

//iltra por id_cliente > 10 y precio_total < 100000, 
//y calcula count, suma y promedio de cantidad.