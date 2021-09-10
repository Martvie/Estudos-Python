sexo = str(input('Informe seu sexo [F/M]: ')).upper()
while sexo not in 'FM':
    sexo = str(input('Sexo inválido, por favor informe seu sexo corretamente: ')).upper()
if sexo == 'F':
    tipo = 'Feminino'
elif sexo == 'M':
    tipo = 'Masculino'
print('OK, seu sexo foi registrado como {}'.format(tipo))