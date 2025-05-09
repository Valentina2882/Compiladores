load "ventas.csv";
filter column "id_cliente" <= 122241;
filter column "id_venta" != 146839;
filter column "cantidad" > 41817;
aggregate sum column "precio_total";
aggregate average column "id_venta";
aggregate average column "id_venta";
print;