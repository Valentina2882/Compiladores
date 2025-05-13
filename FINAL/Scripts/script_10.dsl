load "ventas.csv";
filter column "id_cliente" == 26;
aggregate sum column "precio_total";
aggregate count column "cantidad";
aggregate average column "cantidad";
print;

//Filtra por id_cliente = 26 y calcula suma de 
//precio_total, y count y promedio de cantidad.