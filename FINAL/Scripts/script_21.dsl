load "ventas.csv";
filter column "id_cliente" > 50 and column "precio_total" >= 15000;
aggregate sum column "cantidad";
aggregate average column "cantidad";
aggregate count column "cantidad";
print;

//Filtra por id_cliente > 50 y precio_total ≥ 15000, 
//y calcula suma, promedio y count de cantidad.