load "ventas.csv";
filter column "cantidad" >= 2;
filter column "id_venta" >= 10;
filter column "id_cliente" <= 50;
aggregate count column "cantidad";
print;
