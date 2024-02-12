class Funcion:

    def __init__(self):
        pass

    def verificar_primo(self, num: int) -> bool:
        """Función que verifica si un dado número es o no primo

        Args:
            num (int): número a ser verificado

        Returns:
            bool: True si es primo
        """
        res_es_primo = True
        for divisor in range(2, int(num/2 + 1)):
            if num % divisor == 0:
                res_es_primo = False
                break
        return res_es_primo

    def valor_modal(self, lis: list) -> tuple:
        """Función que recibe una lista y calcula la moda de la misma

        Args:
            lis (list): Lista de enteros

        Returns:
            tuple: Retorna una tupla de la forma (valor modal, veces que se repitió en la lista inicial)
        """
        from collections import Counter
        c = Counter(lis)
        return c.most_common(1)[0]
