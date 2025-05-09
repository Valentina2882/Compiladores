load "ventas.csv";
filter column "id_venta" > 187281;
filter column "id_cliente" != 143306;
filter column "id_venta" > 10768;
aggregate average column "id_venta";
aggregate count column "id_venta";
print;