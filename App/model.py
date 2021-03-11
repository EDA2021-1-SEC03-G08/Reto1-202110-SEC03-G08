"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""




# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'video_ids': None,
               'titles': None,
               'channels_title': None,
               'trending_date': None,
               'country': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'categories': None
               }

    catalog['video_ids'] = lt.newList()
    catalog['titles'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=comparetitles)
    catalog['channels_titles'] = lt.newList('ARRAY_LIST',
                                 cmpfunction=comparechannels)
    catalog['country'] = lt.newList('ARRAY_LIST',
                                 cmpfunction=compare)country                           
    catalog['categories'] = lt.newList('ARRAY_LIST')
    return catalog
# Funciones para agregar informacion al catalogo

def addTitle(catalog, title):
    lt.addLast(catalog['titles'], title)
    authors = title['channels_title'].split(",")
    for channel in channels_title:
        addChannelTitle(catalog, chennel.strip(), title)

def addChannelTitle(catalog, channel, title):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    channels_title = catalog['channels_title']
    poschannel = lt.isPresent(channels_title, channel)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['books'], book)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def comparetitles(title1, title):
    if (title1.lower() in title['name'].lower()):
        return 0
    return -1


def compareratings(book1, book2):
    return (float(book1['average_rating']) > float(book2['average_rating']))


def comparetagnames(name, tag):
    return (name == tag['name'])
# Funciones de ordenamiento