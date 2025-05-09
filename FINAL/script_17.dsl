load "ventas.csv";
filter column "id_cliente" == 43;
aggregate count column "precio_total";
aggregate average column "precio_total";
aggregate sum column "precio_total";
print;

//Filtra por id_cliente = 43 y calcula count, 
//suma y promedio de precio_total.