# Challenge Código Postal Argentino

Ver el [README](README2.md) original para entender el desafío.

## Enfoque

Simplemente desarrollamos el siguiente ejercicio. El código postal está formado de la siguiente manera:

> A1234BCD

esto es una letra, correspondiente a la provincia, el viejo código postal CP y tres letras más, que especifican mejor la dirección dentro del area que cubría el viejo código postal.

La pregunta es: ¿Qué pasa si scrapeamos todos los __posibles__ códigos postales de la web `https://codigo-postal.co/argentina/cpa/{VALOR_CPA}/` donde __posibles__ significa, las provincias y sus viejos CP's correctos y todos los posibles sufijos de tres letras del final?

La respuesta a ese enfoque es el siguiente: realizamos un script que hace aquello que propusimos en la rutina `sandbox.py`. La rutina pide mediante un input poner un límite de búsqueda en cantidad de consultas. Todas las respuestas de la consulta se imprimen en el archivo `resultado.csv`. Basta con probar algunos números bajos para ver que la respuesta de la web nos provee de 3 datos por segundo aproximadamente. Asumiendo relevantes todos los sufijos de tres letras, eso implicaría un tiempo de consulta de más de 250 días aproximadamente, fuera de nuestro alcance. 

Esta claro que no todos los sufijos son relevantes, sin embargo, un muestreo aleatorio muestra que aproximadamente un 10% de los sufijos lo son. Es por esto que, incluso si uno supiera de antemando cuáles son los sufijos relevantes, estaríamos hablando un unos 25 días aproximadamente, también fuera de nuestro alcance.