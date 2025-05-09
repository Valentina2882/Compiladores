load "ventas.csv";
filter column "precio_total" >= 113516;
filter column "id_cliente" <= 196424;
filter column "id_cliente" < 13210;
aggregate average column "precio_total";
aggregate count column "id_venta";
aggregate sum column "id_venta";
print;