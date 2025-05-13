load "ventas.csv";
filter column "id_venta" >= 30;
aggregate average column "cantidad";
aggregate sum column "cantidad";
aggregate count column "cantidad";
print;

//Filtra por id_venta ≥ 30, 
//luego calcula promedio, suma y count de cantidad.