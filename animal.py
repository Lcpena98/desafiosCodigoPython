'''
DESAFIO
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''

animais={
"aguia":{"tipo":"vertebrado","classe":"ave","subclasse":"carnivoro"},
"pomba":{"tipo":"vertebrado","classe":"ave","subclasse":"onivoro"},
"homem":{"tipo":"vertebrado","classe":"mamifero","subclasse":"onivoro"},
"vaca":{"tipo":"vertebrado","classe":"mamifero","subclasse":"herbivoro"},
"pulga":{"tipo":"invertebrado","classe":"inseto","subclasse":"hematofago"},
"lagarta":{"tipo":"invertebrado","classe":"inseto","subclasse":"herbivoro"},
"sanguessuga":{"tipo":"invertebrado","classe":"anelideo","subclasse":"hematofago"},
"minhoca":{"tipo":"invertebrado","classe":"anelideo","subclasse":"onivoro"}
}
a = input()
b = input() 
c = input() 

for animal,dados in animais.items():
      if a == dados["tipo"] and b== dados["classe"] and c==dados["subclasse"]:
        print(animal)