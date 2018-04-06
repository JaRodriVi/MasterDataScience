#Este script copia el historial de los comandos que hacemos en el terminal desde un punto. 
#Antes de empezar la clase es imprescindible poner un comando echo "Empezamos" con algo característico para que el script lo busque.

## $1 es un parametro del Script
## Ejecutamos el Script de la siguiente manera
## En el directorio donde este el script ejecutamos
## ./writeTodayHistory.sh nombreDelArchibo

START=`grep Empecemos -n ~/.history | grep "^[0-9]*" -o | tail -n -1`
cat ~/.history | tail -n +$START > $1.txt
