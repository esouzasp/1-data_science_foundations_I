BASICS
home = "~" dir inicial onde shell instalado
pwd = "print working directory" + "enter" or "return"
ls = visualizar arquivos do diretorio
1s -a = visualizar arquivos + ocultos (Arquivos ocultos aparecerão com um .)
start(win)/open(mac) = abrir um arquivo/diretorio, i.e.: ~ $ start downloads
open . = abrir diretorio selecionado com o "start"

MOVE BETWEEN DIRETORIES
cd desktop = mover para o diretorio "desktop"
cd 'top secret' OR "top secret" OR top\ secret = usar ' or " or \ ..-->  nome c/ espaços
cd .. = voltar um nível acim da pasta
cd desktop/'top secret'/photos = mover diretamente para um diretorio
cd desktop/top\ secret/photos $

OPEN FILES
start adorable.jpg = abrir arquivo imagem
start 'adorable\sample.jpg' = abrir segundo tipo de arq, nome com espaços

CREATE DIRETORIES
mkdir = "make-dir",
mkdir animals = cria um diretorio na localização atual
mkdir -p animals/rodents = criar pasta animals, +pasta rodents dentro de animals
mkdir marsupials cloven_hoofed_animals carnivores = mult dirs actual dir
"\ " = shell understands "spaces"

CREATE FILES
touch = criar um arquivo com a extensão fornecida
touch first_file.txt = criar arquivo no diretorio direcionado
touch animals/rodents/capybara.txt = cria arq dentro no diretorio direcionada
touch animals/marsupials/kangaroo.txt animals/cloven_hoodfed_animals/giraffe.txt = criando multiplos arquivos, separados por espaço

REMOVE (PERMANENTE)
~/desktop $ = diretorio atual
~/desktop $ rm first_file.txt = delete one file
~/desktop $ rm apples.txt carrots.txt fruits.txt = delete multiple files

REMOVENDO DIRETORIOS
~/desktop $ rmdir = remove SOMENTE diretorio VAZIO
~/desktop $ rmdir -r = remove qualquer diretorio
rm flags (execuções adicionais) = rm -
rm option (function, ie. recursive) = p
rm flags + options = rm -p
rm -ri or rm -r -i = "i" or "-i" = confirmação de eliminação de itens individuais, necessario digitar "y" para confirmar individualmente para cada dir ou file/arq


### --------------------------------------------------------------

word = 'assume'
print word[0] # = 'a'
print word[4:6] # = 'me'
print word[1:] # = 'ssume'
print word[2:4] # = 'sum
print word[:2] # = 'ass'

# -----------------------
# STRINGS
s = 'audacity' #upper case "U"
print "U" + s[2:]
'Udacity'

# -----------------------
# FIND
pythagoras = "There is geometry in the humming of the strings, there is music in the spacing of the spheres"
print pythagoras.find('string')  # = '40'
print pythagoras[40:46]  # = 'string'
print pythagoras.find('algebra')  # = -1

danton = "de l'audace, encore de l'audace, et toujours de l'audace"
print danton.find('audace')
print danton.find('audace', 0)  # = 5
print danton.find('audace', 5)  # = 5
print danton.find('audace', 6)  # = 25 #stars findind from 6th position
print danton[6:]  # = udace, encore de l'audace, et toujours de l'audace"
print danton[6:]  # = "de l'audace, et toujours de l'audace"
print danton.find('audace', 25)  # = 25
print danton.find('audace', 26)  # = 47
print danton[47:]  # = "audace"
print danton.find('audace', 48)  # = -1

-- comparison operators
#: x > y
#: x < y
#: x == y
#: x >= y
#: x <= y
#: x =! y
#: x * y
#: x / y
#: x % y = "%" is modulo operator(to find the remainder of division of two number).
            #For example 10 % 5 equals to 0 and 7 % 3 equals to 1 .

# D = d . q + r
# D = dividendo
# d = divisor
# q = quociente
# r = resto
