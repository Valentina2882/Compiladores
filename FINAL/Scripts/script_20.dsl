load "ventas.csv";
filter column "id_cliente" == 25 or column "precio_total" > 40000;
aggregate sum column "precio_total";
aggregate count column "precio_total";
aggregate average column "precio_total";
print;

//Filtra por id_cliente = 25 o precio_total > 40000, 
//luego calcula suma, conteo y promedio de precio_total.