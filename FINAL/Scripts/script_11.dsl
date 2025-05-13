load "ventas.csv";
filter column "precio_total" > 15000 and column "id_cliente" == 43;
aggregate sum column "precio_total";
aggregate average column "precio_total";
aggregate count column "cantidad";
print;

//Filtra por precio_total > 15000 y id_cliente = 43, 
//luego suma y promedia precio_total y cuenta cantidad.