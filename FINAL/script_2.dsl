load "ventas.csv";
filter column "id_cliente" < 5;
filter column "cantidad" > 2;
aggregate sum column "id_venta";
aggregate sum column "id_venta";
print;