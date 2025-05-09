load "ventas.csv";
filter column "id_cliente" != 97321;
filter column "id_venta" > 23776;
filter column "precio_total" < 149132;
aggregate sum column "cantidad";
aggregate sum column "id_venta";
aggregate sum column "cantidad";
print;