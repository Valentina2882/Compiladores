load "ventas.csv";
filter column "cantidad" > 1;
filter column "precio_total" <= 173896;
aggregate average column "id_venta";
aggregate sum column "precio_total";
print;