load "ventas.csv";
filter column "precio_total" < 27675;
aggregate sum column "cantidad";
aggregate average column "precio_total";
print;