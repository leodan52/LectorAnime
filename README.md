# LectorAnime

Este módulo ayuda a gestionar la lista de visualización —*watchlist*, por su nombre en inglés— por temporada televisiva, de aquellos amantes de la animación japonesa.

## Introducción: ¿Cómo funcionan las temporadas anime?


La mayoría de las series anime, son emitidas en la televisión japonesa, y por lo tanto, estas deben ajustarse al calendario de dicho medio[^1]. Las temporadas dividen al año en cuatro, que coinciden con las estaciones **Invierno**, **Primavera**, **Verano** y **Otoño**, en ese mismo orden. Cada temporada consta de 13 semanas.

Cada serie suele comenzar a emitir entre la primera o segunda semana —salvo algunas excepciones— de la temporada, constando de entre 12 y 13 episodios que se emiten de forma semanal. El horario destinado a cada serie es fijo y regular.

## Funcionamiento del módulo

### Preparando el módulo

El módulo escrito en Python obtiene la watchlist de un archivo TXT. El nombre del archivo debe tener un formato específico,

> anime\_SEASON\_YEAR.txt,

donde SEASON es la temporada actual de las cuatro mencionadas antes, y YEAR es el año en curso. Estos datos son importantes para el buen funcionamiento del módulo.

Debido a que el proyecto está en etapas temprana, y es meramente para uso personal, la ubicación del archivo debe ser indicada de momento directamente en el código del módulo. En la linea 7 se encuentra la variable que contiene la ruta de la carpeta contenedora, y en la linea 9 la que contiene el nombre del archivo.

### Preparando el archivo TXT

El nombre de cada serie debe colocarse uno por línea. Se recomienda usar el nombre completo del título al principio, seguido la **fecha de estreno** en su país, usando como separación uno o varios puntos. Por ejemplo,

> ~~~
> The Demon Lord..................... 5 enero.
> ~~~

El año no se incluye porque la información se extrae del nombre del archivo. Adicionalmente, se puede agregar el nombre de la **plataforma de streaming** donde se visualizará la serie,

> ~~~
> The Demon Lord..................... 5 enero ...... AnimeLegal,
> ~~~

recordando que debe respetarse el orden Título-Fecha-Plataforma.

Algunos títulos anime se caracterizan por tener nombres muy largos, frases enteras que complicarían la salida del módulo. Para esto se pude agregar un nombre corto a cada anime, usando la etiqueta *shortname*. Esta debe colocarse luego de los tres primeros datos, siempre separando con puntos,

> ~~~
> The Demon Lord..................... 5 enero ...... AnimeLegal ..... shortname: Maou.
> ~~~

Con estos pasos realizados, es posible comenzar a utilizar el gestor.

### Salida del módulo

La salida del módulo es un archivo TXT llamado *salida.txt*. Esta contiene información crucial para gestionar la watchlist de la temporadal. El contenido del TXT está dividido en 4 bloques:

1. Bloque lista.

	Listado completo ordenado alfabéticamente.

2. Bloque plataforma.

	Divide la lista por plataforma de visualización.

3. Bloque de estrenos.

	Desglosa un calendario en cascada por fechas que contienen los anime que se estrenan ese mismo día.

4. Bloque calendario semanal.

	Crea una tabla con un calendario semanal de los estrenos de cada episodio.

Del bloque uno al tres el formato que se utiliza es de lista de cascada, organizando los títulos por sub bloques definidos por su temática. El formato de la linea de cada título incluirá el nombre corto y la plataforma de visualización, si es que está definidos, como lo siguiente

> ~~~
> Título	(shortname) (En PlataformaDefinida)
> ~~~

#### Bloque lista

Este bloque es bastante simple, ya que es solo una lista ordenada. El bloque tiene el siguiente formato,

> ~~~
>
> Los animes que se estrenan en la siguiente temporada son:
>
> 		Título 1
> 		Título 2
> ~~~

#### Bloque plataforma

Se pueden definir animes con diferentes plataformas de visualización, y cada una tendrá una división. Las plataformas también se ordenarán alfabéticamente, y la primera de la lista se listará de la siguiente forma,

> ~~~
>
> De los cuales, en PrimeraPlataforma se veran:
>
> 		Título 1
> 		Título 2
> ~~~

dando una continuación lógica al bloque anterior. Las siguietes tendrán un formato un tanto diferente,

> ~~~
>
> En SegundoPlataforma:
>
> 		Título 1
> 		Título 2
>
> En TerceraPlataforma:
>
> 		Título 1
> 		Título 2
> ~~~

hasta llegar a la última de la lista,

> ~~~
>
> Y en UltimaPlataforma:
>
> 		Título 1
> 		Título 2
> ~~~

En caso de que existan animes cuya plataforma no ha sido definida, el bloque concluiría mostrando esos títulos.

> ~~~
>
> Faltan por definir:
>
> 		Título 1
> 		Título 2
> ~~~

#### Bloque de estrenos

Este bloque se destina únicamente para hacer un seguido de la temporada de anime en las primeras semanas, cuando el episodio 1 de todos los títulos se irá estrenando. El formato es simple, muy parecido a los bloques anteriores,

> ~~~
>
> El calendario de estrenos es el siguiente:
>
> Fecha
>
> 		Título 1
> 		Título 2
> ~~~

comenzando con el encabezado que se muestra, seguido de sub bloques con fecha y lo títulos que se estrena ese día. Como ejemplo de sub bloque podríamos incluir el título de ejemplo que empleamos anteriormente del título *The Demon Lord*,

> ~~~
>
> 5 enero
>
> 		The Demon Lord	(Maou)	(En AnimeLegal)
> 		Otro Título
> ~~~

#### Bloque calendario semanal

Este bloque representa una calendario semanal, es decir, de domingo a sábado, mostrando el horario de cada título de anime. Ya que este formato necesita ser compacto, se usa para listar el nombre corto, si es que fue definido. En caso contrario, usará el título completo. El formato que se usa está dado por el módulo de Python *tabulate*,

> ~~~
> El horario semanal queda de la siguiente forma:
>
> Domingo       Lunes         Martes        Miércoles     Jueves        Viernes       Sábado
> ------------  ------------  ------------  ------------  ------------  ------------  ------------
> Título        Título        Titulo                      Titulo                       Título
>                             Titulo                                                   Titulo
>                                                                                      Titulo
> ~~~

Ya que el ancho de cada columna se adapta a los nombres listados, se recomiedo usar nombres cortos cuando se crea necesario.

[^1]: ANIME MAGAZINE 24, Dart tv, <https://youtu.be/hx4LrEPJ0dQ>
