load "ventas.csv";
filter column "id_cliente" > 93763;
aggregate average column "precio_total";
aggregate sum column "cantidad";
aggregate sum column "id_venta";
print;