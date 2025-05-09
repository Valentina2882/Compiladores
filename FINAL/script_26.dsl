load "ventas.csv";
filter column "id_cliente" < 10;
aggregate sum column "precio_total";
aggregate count column "precio_total";
aggregate average column "precio_total";
print;

//Filtra por id_cliente < 10 y calcula suma, 
//count y promedio de precio_total.