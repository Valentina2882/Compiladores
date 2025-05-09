load "ventas.csv";
filter column "id_cliente" < 100;
filter column "precio_total" >= 15000;
aggregate sum column "cantidad";
aggregate average column "cantidad";
aggregate count column "cantidad";
print;

//Filtra por id_cliente < 100 y precio_total ≥ 15000, 
//y calcula suma, promedio y count de cantidad.