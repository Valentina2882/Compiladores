load "ventas.csv";
filter column "id_venta" != 11972;
filter column "id_cliente" < 113264;
filter column "precio_total" <= 130813;
aggregate average column "cantidad";
print;