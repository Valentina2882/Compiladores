load "ventas.csv";
filter column "id_venta" <= 54110;
filter column "id_cliente" < 190991;
filter column "cantidad" <= 189477;
aggregate count column "id_venta";
aggregate average column "precio_total";
print;