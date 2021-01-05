import sys
from parse import JSParser

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: programa.exe [ruta del código]', file=sys.stderr)
        exit(1)

    try:
        parser = JSParser(sys.argv[1])
        parser.parse()
    except FileNotFoundError as fe:
        print(f'No existe el fichero {fe.filename}', file=sys.stderr)
    except Exception as e:
        print(e, file=sys.stderr)
        print('Error encontrado', file=sys.stderr)