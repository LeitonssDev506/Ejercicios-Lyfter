| **Método** | **Descripción** | **Ejemplo pequeño** |
|---|---|---|
| **`close()`** | Cierra el archivo y libera los recursos que estaba utilizando. | `archivo.close()` |
| **`detach()`** | Separa el flujo de datos sin procesar del búfer del archivo. | `archivo.detach()` |
| **`fileno()`** | Retorna un número que identifica el archivo para el sistema operativo. | `archivo.fileno()` |
| **`flush()`** | Vacía el búfer y fuerza la escritura de los datos pendientes. | `archivo.flush()` |
| **`isatty()`** | Indica si el archivo está conectado a un dispositivo interactivo, como una terminal. | `archivo.isatty()` |
| **`read()`** | Lee y retorna el contenido del archivo. | `archivo.read()` |
| **`readable()`** | Indica si el archivo permite realizar operaciones de lectura. | `archivo.readable()` |
| **`readline()`** | Lee y retorna una línea del archivo. | `archivo.readline()` |
| **`readlines()`** | Lee las líneas del archivo y retorna una lista con cada línea. | `archivo.readlines()` |
| **`seek()`** | Cambia la posición actual dentro del archivo. | `archivo.seek(0)` |
| **`seekable()`** | Indica si es posible cambiar la posición dentro del archivo. | `archivo.seekable()` |
| **`tell()`** | Retorna la posición actual del cursor dentro del archivo. | `archivo.tell()` |
| **`truncate()`** | Reduce o modifica el tamaño del archivo. | `archivo.truncate(10)` |
| **`writable()`** | Indica si el archivo permite realizar operaciones de escritura. | `archivo.writable()` |
| **`write()`** | Escribe una cadena de texto en el archivo. | `archivo.write("Hola")` |
| **`writelines()`** | Escribe varias cadenas de texto en el archivo. | `archivo.writelines(["Hola\n", "Adiós\n"])` |