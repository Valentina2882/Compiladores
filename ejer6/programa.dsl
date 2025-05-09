load "empleados.csv";
filter column "edad" > 30;
filter column "salario" >= 1000;
filter column "dias_laborados" == 14;
print;