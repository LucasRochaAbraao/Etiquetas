# Etiquetas
Atualmente trabalho numa ISP (QUICK FIBRA) onde há uma necessidade de criar etiquetas para colar em roteadores instalados nas residências dos clientes. Como os roteadores vão pré-configurados com configuração personalizada e única em cada roteador, precisávamos de uma forma de informar os clientes qual o SSID e senha do wifi sempre que precisarem. Apartir dessa necessidade, desenvolvi esse script, que gera qualquer quantidade de etiquetas, além de gerar uma senha aleatória para cada uma. Por enquanto, o script funciona apenas pelo terminal. Mas pretendo migrar para uma aplicação web utilizando django (processo lento, pois meu foco atual está em outros projetos). Eu até comecei a fazer um bot no telegram para gerenciar isso, mas acredito que será mais prático uma aplicação web mesmo. Vou manter o código do bot para referências futuras, mas não vou continuar o desenvolvimento dele por aqui.
Segue abaixo como instalar, configurar e executar.


## Instalar
Primeiro é necessário instalar o pacote de gerenciamento de ambientes virtuais `python3-venv`, para um melhor gerenciamento dos pacotes de seus projetos.
```
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```
Em seguida, instale os pacotes no `requirements.txt`
```
pip install -r requirements.txt
```
Para finalizar, dê permissão de execução ao script principal.
```
sudo chmod +x email_aviso.py
```
Outra opção seria usando o arquivo requirements.txt:
```
pip3 install -r requirements.txt
```
ou
```
pipenv install -r requirements.txt
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
