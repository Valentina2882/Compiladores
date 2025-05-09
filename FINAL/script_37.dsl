load "ventas.csv";
filter column "id_cliente" >= 20;
filter column "precio_total" <= 60000;
aggregate average column "cantidad";
aggregate sum column "cantidad";
aggregate count column "cantidad";
print;

//Filtra por id_cliente ≥ 20 y precio_total ≤ 60000, 
//luego calcula promedio, suma y count de cantidad.