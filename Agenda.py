from time import sleep
from sys import stderr


def menu():
    print(ANYADIR, 'Añadir contacto')
    print(BORRAR, 'Borrar contacto')
    print(MODIFICAR, 'Modificar contacto')
    print(BUSCAR, 'Buscar contacto')
    print(LISTAR, 'Listar contacto')
    print(SALIR, 'Salir')
    try:
        op = int(input('Escoge una opción: '))
        return op
    except ValueError as e:
        return None


def introduce_contacto():
    nombre = input('Introduce un nombre: ')
    tel = input('Introduce un teléfono: ')
    dir = input('Introduce una dirección: ')
    email = input('Introduce un email: ')

    return nombre, tel, dir, email


def anyadir_contacto(agenda):
    contacto = introduce_contacto()
    agenda.append(contacto)

def buscar(agenda, nombre_a_buscar):
    for i in range(len(agenda)):
        contacto = agenda[i]
        nombre, tel, dir, email = contacto
        if nombre_a_buscar == nombre:
            return i

    return -1


def borrar_contacto(agenda):
    nombre = input('Introduce el nombre: ')
    pos = buscar(agenda, nombre)
    if pos != -1:
        del agenda[pos]
    else:
        msg('Ese contacto no existe.')


def modificar_contacto(agenda):
    nombre = input('Introduce el nombre: ')
    pos = buscar(agenda, nombre)
    if pos != -1:
        print('Introduce los nuevos datos de ese contacto.')
        contacto = introduce_contacto()
        agenda[pos] = contacto
    else:
        msg('Ese contacto no existe.')


def msg(texto):
    print(texto, file=stderr)
    sleep(1)


def buscar_contacto(agenda):
    nombre = input('Introduce un nombre: ')
    pos = buscar(agenda, nombre)
    if pos != -1:
        imprime_contacto(agenda[pos])
    else:
        msg('Ese contacto no existe.')


def imprime_contacto(contacto):
    nombre, tel, dir, email = contacto
    print('Nombre:', nombre)
    print('Teléfono:', tel)
    print('Dirección:', dir)
    print('email:', email)


def listar_contactos(agenda):
    for contacto in agenda:
        imprime_contacto(contacto)
        print()


ANYADIR = 1
BORRAR = 2
MODIFICAR = 3
BUSCAR = 4
LISTAR = 5
SALIR = 6
agenda = []
op = None
while op != SALIR:
    op = menu()
    if op == ANYADIR:
        anyadir_contacto(agenda)
    elif op == BORRAR:
        borrar_contacto(agenda)
    elif op == MODIFICAR:
        modificar_contacto(agenda)
    elif op == BUSCAR:
        buscar_contacto(agenda)
    elif op == LISTAR:
        listar_contactos(agenda)
    elif op != SALIR:
        msg('Opción incorrecta, vuelva a intentarlo.')

print('Bye!')