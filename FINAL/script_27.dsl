load "ventas.csv";
filter column "cantidad" <= 179441;
filter column "id_cliente" < 158215;
filter column "cantidad" != 158087;
aggregate count column "precio_total";
aggregate count column "cantidad";
print;