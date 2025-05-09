load "ventas.csv";
filter column "id_cliente" != 56291;
aggregate count column "cantidad";
aggregate sum column "precio_total";
print;