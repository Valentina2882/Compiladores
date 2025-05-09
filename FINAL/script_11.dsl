load "ventas.csv";
filter column "cantidad" < 3;
filter column "id_venta" > 50;
filter column "id_cliente" < 40;
aggregate average column "id_venta";
aggregate count column "precio_total";
aggregate count column "cantidad";
print;
