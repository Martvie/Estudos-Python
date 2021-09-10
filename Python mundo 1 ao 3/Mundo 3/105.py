def notas(*n, sit=False):
    aluno = {}
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['média'] = sum(n)/len(n)
    if sit:
        if aluno['média']> 7:
            aluno['situação'] = 'Boa'
        elif aluno['média']<= 7:
            aluno['situação'] = 'ravoavel'
        elif aluno['média'] <5:
            aluno['situação'] = 'Fodeu'
    return aluno


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)