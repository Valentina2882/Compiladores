load "ventas.csv";
filter column "precio_total" < 39571;
aggregate average column "id_venta";
aggregate sum column "precio_total";
print;