load "ventas.csv";
filter column "id_cliente" < 300;
aggregate sum column "cantidad";
aggregate average column "cantidad";
aggregate count column "cantidad";
print;

//Filtra por id_cliente < 300 y calcula suma, 
//promedio y count de cantidad.