load "ventas.csv";
filter column "id_cliente" != 24012;
aggregate count column "cantidad";
print;