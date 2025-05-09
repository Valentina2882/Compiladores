load "ventas.csv";
filter column "cantidad" < 35638;
aggregate sum column "precio_total";
print;