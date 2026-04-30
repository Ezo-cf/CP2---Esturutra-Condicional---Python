def notas(valor):
    nota = float(input(f"Digite a nota de {valor}: "))
    if nota < 0 or nota > 10:
        print("Digite uma nota de 0 a 10")
        return notas(valor)
    return nota

cp1 = notas("Checkpoint 1 (cp1)")
cp2 = notas("Checkpoint 2 (cp2)")
cp3 = notas("Checkpoint 3 (cp3)")
menor = cp1
if cp2 < menor:
    menor = cp2
if cp3 < menor:
    menor = cp3
print(f"A menor nota dos checkpoints é: {menor:.1f}")
sp1 = notas("Sprint 1 (sp1)")
sp2 = notas("Sprint 2 (sp2)")
gs  = notas("Global solution (gs)")

media_sem_peso = (cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4

mediaPeso = media_sem_peso * 0.4 + gs * 0.6

print(f"\nMédia do semestre (sem peso): {media_sem_peso:.1f}\n")
print(f"Média do semestre com peso:   {mediaPeso:.1f}")