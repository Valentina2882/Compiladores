load "ventas.csv";
filter column "id_venta" <= 138497;
filter column "id_venta" >= 96933;
filter column "id_cliente" < 52042;
aggregate sum column "precio_total";
aggregate sum column "precio_total";
aggregate count column "cantidad";
print;