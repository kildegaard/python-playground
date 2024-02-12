from car import Car

auto_01 = Car('Ford', 'Mustang', 100)

auto_02 = Car('Chevrolet', 'Camaro', 200)

# print(f'El auto {auto_01.modelo} tiene {auto_01.vida} de vida')
# print(f'El auto {auto_02.modelo} tiene {auto_02.vida} de vida')

# auto_01.chocar()
# print(f'El auto {auto_01.modelo} chocó! Ahora tiene {auto_01.vida} de vida')

# print(f'El auto {auto_01.modelo} choca a {auto_02.modelo}!')
# auto_01.chocar_a_otro(auto_02)
# print(f'Ahora el {auto_02.modelo} tiene {auto_02.vida} de vida')

print(auto_01.valor_nafta)
print(Car.valor_nafta)

auto_01.modif_valor_nafta(300)

print(auto_01.valor_nafta)
print(Car.valor_nafta)

Car.modif_valor_nafta(500)

print(auto_01.valor_nafta)
print(Car.valor_nafta)
