load "ventas.csv";
filter column "precio_total" > 185136;
filter column "precio_total" >= 32996;
filter column "cantidad" == 194830;
aggregate average column "cantidad";
print;