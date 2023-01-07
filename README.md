# LectorAnime

Este módulo ayuda a gestionar la lista de visualización —*watchlist*, por su nombre en inglés— por temporada televisiva, de aquellos amantes de la animación japonesa. El módulo está escrito en Python y se apoya de los módulos

- `datetime`
- y `tabulate`,

los cuales son necesario instalar. Puedes hacerlo mediante el siguiente comando,

> ~~~
> pip instalar datetime tabulate
> ~~~

## Introducción: ¿Cómo funcionan las temporadas anime?


La mayoría de las series anime, son emitidas en la televisión japonesa, y por lo tanto, estas deben ajustarse al calendario de dicho medio[^1]. Las temporadas dividen al año en cuatro, que coinciden con las estaciones **Invierno**, **Primavera**, **Verano** y **Otoño**, en ese mismo orden. Cada temporada consta de 13 semanas.

Cada serie suele comenzar a emitir entre la primera o segunda semana —salvo algunas excepciones— de la temporada, constando de entre 12 y 13 episodios que se emiten de forma semanal. El horario destinado a cada serie es fijo y regular.

## Funcionamiento del módulo

### Preparando el módulo

El módulo obtiene la watchlist de un archivo TXT. El nombre del archivo debe tener un formato específico,

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

La salida del módulo es un archivo TXT llamado *salida.txt*. Esta contiene información crucial para gestionar la watchlist de la temporada. El contenido del TXT está dividido en 4 bloques:

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
> 	Título 1
> 	Título 2
> ~~~

#### Bloque plataforma

Se pueden definir animes con diferentes plataformas de visualización, y cada una tendrá una división. Las plataformas también se ordenarán alfabéticamente, y la primera de la de ellas se listará de la siguiente forma,

> ~~~
>
> De los cuales, en PrimeraPlataforma se verán:
>
> 	Título 1
> 	Título 2
> ~~~

dando una continuación lógica al bloque anterior. Las siguientes tendrán un formato un tanto diferente,

> ~~~
>
> En SegundoPlataforma:
>
> 	Título 1
> 	Título 2
>
> En TerceraPlataforma:
>
> 	Título 1
> 	Título 2
> ~~~

hasta llegar a la última de la lista,

> ~~~
>
> Y en UltimaPlataforma:
>
> 	Título 1
> 	Título 2
> ~~~

En caso de que existan animes cuya plataforma no ha sido definida, el bloque concluiría mostrando esos títulos.

> ~~~
>
> Faltan por definir:
>
> 	Título 1
> 	Título 2
> ~~~

#### Bloque de estrenos

Este bloque se destina únicamente para hacer un seguido de la temporada de anime en las primeras semanas, cuando el episodio 1 de todos los títulos se irá estrenando. El formato es simple, muy parecido a los bloques anteriores,

> ~~~
>
> El calendario de estrenos es el siguiente:
>
> Fecha
>
> 	Título 1
> 	Título 2
> ~~~

comenzando con el encabezado que se muestra, seguido de sub bloques con fecha y lo títulos que se estrena ese día. Como ejemplo de sub bloque podríamos incluir el título de ejemplo que empleamos anteriormente del título *The Demon Lord*,

> ~~~
>
> 5 enero
>
> 	The Demon Lord	(Maou)	(En AnimeLegal)
> 	Otro Título
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

Ya que el ancho de cada columna se adapta a los nombres listados, se recomienda usar nombres cortos cuando se crea necesario.

### Watchlist ejemplo

Veamos un ejemplo. El archivo `anime_otoño_2021.txt` contiene la watchlist de la temporada anime otoño 2021, como su nombre lo indica. El archivo lista 20 títulos diferentes:
> ~~~
> 86: Eighty Six (2da temp)................................................ 2 octubre ....... Crunchyroll ..... shortname: 86: Eighty Six
> Blue Period................................................................ 2 octubre ....... Netflix
> Build Divide: Code Black................................................... 10 octubre ...... Crunchyroll ..... shortname: Build Divide
> Deep Insanity: The Lost Child.............................................. 13 octubre ...... AnimeLegal  ...... shortname: Deep Insanity
> Kimetsu no Yaiba: Yuukaku-hen.............................................. 10 octubre ...... Crunchyroll ...... shortname: Kimetsu no Yaiba
> Komi-san wa, Komyushou desu................................................ 6 octubre ....... Netflix ...... shortname: Komi-san
> Kyoukai Senki.............................................................. 4 octubre ....... AnimeLegal
> Kyuuketsuki Sugu Shinu..................................................... 4 octubre ....... AnimeLegal
> Lupin III: Part VI......................................................... 9 octubre
> Mieruko-chan............................................................... 3 octubre ...... AnimeLegal
> Muv-Luv Alternative........................................................ 6 octubre ...... Crunchyroll
> Platinum End............................................................... 7 octubre ...... Crunchyroll
> Saihate no Paladin......................................................... 9 octubre ...... Crunchyroll
> Sakugan!!.................................................................. 7 octubre ...... Crunchyroll
> Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru................... 6 octubre ...... Crunchyroll ...... shortname: Ansatsu Kizoku
> Senpai ga Uzai Kouhai no Hanashi........................................... 9 octubre ...... AnimeLegal
> Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei............................ 4 octubre ...... Crunchyroll ...... shortname: Shinka no Mi
> Taishou Otome Otogibanashi................................................. 8 octubre ...... AnimeLegal
> takt op,Destiny............................................................ 6 octubre ...... Crunchyroll
> Tsuki to Laika to Nosferatu................................................ 3 octubre ...... AnimeLegal
>
> ~~~

El uso de uno varios puntos como separador es bastante conveniente para darle a la lista un aspecto más legible, usando fuente monoespaciada. Esto ayuda cuando hay nombres muy largos, que no es poco común en la industria. Nótese también que los títulos especialmente largos tienen definido el nombre corto; en algunos caso también se usa para dejar de lado el subtítulo.

Ahora solo es cuestión de preparar el módulo y ejecutarlo, con lo cual obtendremos el archivo `salida.txt`, con el siguiente contenido:

> ~~~
>
> Los animes que se estrenan en la siguiente temporada son:
>
> 	86: Eighty Six (2da temp) 	 (86: Eighty Six)
> 	Blue Period
> 	Build Divide: Code Black 	 (Build Divide)
> 	Deep Insanity: The Lost Child 	 (Deep Insanity)
> 	Kimetsu no Yaiba: Yuukaku-hen 	 (Kimetsu no Yaiba)
> 	Komi-san wa, Komyushou desu 	 (Komi-san)
> 	Kyoukai Senki
> 	Kyuuketsuki Sugu Shinu
> 	Lupin III: Part VI
> 	Mieruko-chan
> 	Muv-Luv Alternative
> 	Platinum End
> 	Saihate no Paladin
> 	Sakugan!!
> 	Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru 	 (Ansatsu Kizoku)
> 	Senpai ga Uzai Kouhai no Hanashi
> 	Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei 	 (Shinka no Mi)
> 	Taishou Otome Otogibanashi
> 	takt op,Destiny
> 	Tsuki to Laika to Nosferatu
>
> De los cuales, en AnimeLegal se veran:
>
> 	Deep Insanity: The Lost Child 	 (Deep Insanity)
> 	Kyoukai Senki
> 	Kyuuketsuki Sugu Shinu
> 	Mieruko-chan
> 	Senpai ga Uzai Kouhai no Hanashi
> 	Taishou Otome Otogibanashi
> 	Tsuki to Laika to Nosferatu
>
> En Crunchyroll :
>
> 	86: Eighty Six (2da temp) 	 (86: Eighty Six)
> 	Build Divide: Code Black 	 (Build Divide)
> 	Kimetsu no Yaiba: Yuukaku-hen 	 (Kimetsu no Yaiba)
> 	Muv-Luv Alternative
> 	Platinum End
> 	Saihate no Paladin
> 	Sakugan!!
> 	Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru 	 (Ansatsu Kizoku)
> 	Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei 	 (Shinka no Mi)
> 	takt op,Destiny
>
> Y en Netflix :
>
> 	Blue Period
> 	Komi-san wa, Komyushou desu 	 (Komi-san)
>
> Faltan por definir:
>
> 	Lupin III: Part VI
>
> El calendario de estrenos es el siguiente:
>
> 2 Octubre
>
> 	86: Eighty Six (2da temp) 	 (86: Eighty Six)  (En Crunchyroll)
> 	Blue Period  (En Netflix)
>
> 3 Octubre
>
> 	Mieruko-chan  (En AnimeLegal)
> 	Tsuki to Laika to Nosferatu  (En AnimeLegal)
>
> 4 Octubre
>
> 	Kyoukai Senki  (En AnimeLegal)
> 	Kyuuketsuki Sugu Shinu  (En AnimeLegal)
> 	Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei 	 (Shinka no Mi)  (En Crunchyroll)
>
> 6 Octubre
>
> 	Komi-san wa, Komyushou desu 	 (Komi-san)  (En Netflix)
> 	Muv-Luv Alternative  (En Crunchyroll)
> 	Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru 	 (Ansatsu Kizoku)  (En Crunchyroll)
> 	takt op,Destiny  (En Crunchyroll)
>
> 7 Octubre
>
> 	Platinum End  (En Crunchyroll)
> 	Sakugan!!  (En Crunchyroll)
>
> 8 Octubre
>
> 	Taishou Otome Otogibanashi  (En AnimeLegal)
>
> 9 Octubre
>
> 	Lupin III: Part VI
> 	Saihate no Paladin  (En Crunchyroll)
> 	Senpai ga Uzai Kouhai no Hanashi  (En AnimeLegal)
>
> 10 Octubre
>
> 	Build Divide: Code Black 	 (Build Divide)  (En Crunchyroll)
> 	Kimetsu no Yaiba: Yuukaku-hen 	 (Kimetsu no Yaiba)  (En Crunchyroll)
>
> 13 Octubre
>
> 	Deep Insanity: The Lost Child 	 (Deep Insanity)  (En AnimeLegal)
>
> El horario semanal queda de la siguiente forma:
>
> Domingo                      Lunes                   Martes    Miércoles            Jueves        Viernes                     Sábado
> ---------------------------  ----------------------  --------  -------------------  ------------  --------------------------  --------------------------------
> Build Divide                 Kyoukai Senki                     Deep Insanity        Platinum End  Taishou Otome Otogibanashi  86: Eighty Six
> Kimetsu no Yaiba             Kyuuketsuki Sugu Shinu            Komi-san             Sakugan!!                                 Blue Period
> Mieruko-chan                 Shinka no Mi                      Muv-Luv Alternative                                            Lupin III: Part VI
> Tsuki to Laika to Nosferatu                                    Ansatsu Kizoku                                                 Saihate no Paladin
>                                                                takt op,Destiny                                                Senpai ga Uzai Kouhai no Hanashi
>
> ~~~

[^1]: ANIME MAGAZINE 24, Dart tv, <https://youtu.be/hx4LrEPJ0dQ>
