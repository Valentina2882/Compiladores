load "ventas.csv";
filter column "id_venta" <= 183433;
filter column "id_cliente" != 197092;
filter column "id_venta" > 18162;
aggregate count column "precio_total";
print;