load "ventas.csv";
filter column "id_cliente" == 24 or column "cantidad" == 1;
aggregate sum column "precio_total";
aggregate count column "precio_total";
aggregate average column "precio_total";
print;

//Filtra por id_cliente = 24 y calcula suma, 
//conteo y promedio de precio_total.