load "ventas.csv";
filter column "id_cliente" <= 125041;
filter column "cantidad" >= 9808;
aggregate sum column "precio_total";
print;