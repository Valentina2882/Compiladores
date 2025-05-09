load "ventas.csv";
filter column "id_cliente" == 11;
aggregate sum column "cantidad";
aggregate average column "cantidad";
aggregate count column "cantidad";
print;

//Filtra por id_cliente = 11 y calcula 
//suma, promedio y count de cantidad.