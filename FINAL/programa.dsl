load "ventas.csv";
filter column "precio_total" > 1000;
filter column "cantidad" >= 2;
aggregate sum column "precio_total";
aggregate count column "id_venta";
aggregate average column "cantidad";
print;
