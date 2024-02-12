'''
try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass
'''

try:
    f = open('text.txt', encoding='utf-8')
    # var = bad_var
except FileNotFoundError as FNFE:
    print(f'No se encontro el archivo: {FNFE.filename}')
except NameError as NE:
    print(f'Error en variable! - {NE}')
    print(len(NE.args))
else:
    print(f'Archivo abierto!')
    print(f.read())
    f.close()
finally:
    print('Finally')
