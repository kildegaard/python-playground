def lista_plana(lst):
    res = []
    for elemento in lst:
        if not isinstance(elemento, list):
            res.append(elemento)
        else:
            res.extend(lista_plana(elemento))

    return res
