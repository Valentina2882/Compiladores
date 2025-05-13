load "ventas.csv";
filter column "precio_total" >= 20000;
aggregate sum column "cantidad";
aggregate average column "cantidad";
aggregate count column "cantidad";
print;

//Filtra por precio_total ≥ 20000, luego calcula 
//suma, promedio y count de cantidad.