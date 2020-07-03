# Etiquetas
Atualmente trabalho numa ISP onde há uma necessidade de criar etiquetas para colar em roteadores instalados nas residências dos clientes. Como os roteadores vão préconfigurados com configuração personalizada, precisávamos de uma forma de informar os clientes qual o SSID e senha do wifi sempre que precisarem. Apartir dessa necessidade, desenvolvi esse script, que gera qualquer quantidade de etiquetas, além de gerar uma senha aleatória para cada uma. Por enquanto, o script funciona apenas pelo terminal. Mas estou no processo (lento, pois meu foco atual está em outros projetos) de migrar para uma aplicação web utilizando django.

Segue abaixo como instalar, configurar e executar.


## Instalar
Primeiro é necessário instalar o pacote de gerenciamento de ambientes virtuais `pipenv`, para um melhor gerenciamento dos pacotes de seus projetos.
```
pip3 install pipenv
```
Em seguida, instale o pacote `openpyxl`
```
pipenv install openpyxl
```
Para finalizar, dê permissão de execução ao script principal.
```
sudo chmod +x email_aviso.py
```


## Configurar
Certifique que no diretório `Etiquetas/templates/` existem 2 arquivos xlsx (`template-ac.xlsx` e `template-bgn.xlsx`), sendo que os títulos de cada coluna deve ser *NOME 2GHz*, *NOME 5GHz*, e *SENHA*.

Eu vou eliminar a necessidade desses templates, quando fiz isso ainda estava aprendendo a manipular arquivos xlsx.

## Executar

Ao executar o script `gera-etiquetas.py`, passe argumentos para indicar a numeração inicial das etiquetas, numeração final, e o modelo escolhido. Por padrão, etiquetas do modo AC (5GHz) será selecionado. Segue abaixo um exemplo onde gero etiquetas de numeração 100 até 299 (total de 200 etiquetas) do modelo AC. Abaixo as opções.
```
./gera-etiquetas.py -i 100 -f 299
-i | -I    -  Númeração inicial
-f | -F    -  Numeração final
-c | -C    -  Modelo de etiqueta
-d | -D    -  Modo "debug" (printa na tela o resultado, além de criar o arquivo)
```