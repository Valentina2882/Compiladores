load "ventas.csv";
filter column "id_venta" > 125581;
aggregate average column "precio_total";
aggregate sum column "cantidad";
print;