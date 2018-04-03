#Este script copia el historial de los comandos que hacemos en el terminal desde un punto. 
#Antes de empezar la clase es imprescindible poner un comando echo con algo característico para que el script lo busque.

START= grep Empecemos -n ~/.history | grep "^[0-9]*" -o | tail -n -1

echo $START

cat ~/.history | tail -n +$START

##EN PROCESO