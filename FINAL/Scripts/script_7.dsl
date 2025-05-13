load "ventas.csv";
filter column "id_cliente" == 21;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por id_cliente = 21 y calcula count, 
//suma y promedio de cantidad.