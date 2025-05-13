load "ventas.csv";
filter column "id_cliente" < 50 or column "precio_total" > 25000;
aggregate average column "precio_total";
aggregate sum column "precio_total";
aggregate count column "precio_total";
print;

//Filtra por id_cliente < 200 y precio_total > 25000, 
//luego calcula promedio, suma y count de precio_total. 