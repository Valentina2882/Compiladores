load "ventas.csv";
filter column "cantidad" <= 4;
aggregate sum column "precio_total";
print;