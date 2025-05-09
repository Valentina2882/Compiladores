load "ventas.csv";
filter column "id_venta" <= 165542;
aggregate sum column "precio_total";
print;