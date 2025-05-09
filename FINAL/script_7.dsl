load "ventas.csv";
filter column "precio_total" != 15808;
filter column "cantidad" != 103153;
aggregate average column "cantidad";
aggregate count column "id_venta";
print;