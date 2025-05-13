load "ventas.csv";
filter column "id_cliente" > 5 and column "precio_total" > 40000;
aggregate average column "precio_total";
aggregate sum column "precio_total";
aggregate count column "precio_total";
print;

//Filtra por id_cliente > 5 y precio_total > 40000, 
//luego calcula promedio, suma y count de precio_total.