load "ventas.csv";
filter column "cantidad" <= 4;
filter column "id_venta" == 123;
filter column "id_cliente" == 70;
aggregate sum column "id_venta";
print;