# Automação de cadastro

## Sobre o projeto
Automação do processo de cadastro de milhares de produtos do Sistema usando Python para ser executado de forma diária e sob demanda.

- Link do sistema usado logo abaixo: 
    - [https://dlp.hashtagtreinamentos.com/python/intensivao/login](https://dlp.hashtagtreinamentos.com/python/intensivao/login)

Este projeto foi desenvolvido durante a *Jornada Python* da **Hashtag Treinamentos**.


## Estrutura de Pastas
```bash
.
├── database
|   └── produtos.csv
├── doc
|   └── README.md
├── setting
|   └── pegar_posicao.py
└── main.py
```

## Tecnologia utilizada
- **Python**: Ambiente de execução Python para automação e captura precisa da posição na tela do monitor.

## Rodando Localmente
Clone o repositório:
```bash
git clone https://github.com/SilvioNascimento/automacao-de-cadastro-python.git
```

Instalando as bibliotecas:
```bash
pip install pandas pyautogui 
```

Executando o programa:
```bash
python main.py
```

**OBS**: Antes de executar o programa, deve acessar o link do sistema e capturar suas posições do campo do formulário. Pois as posições inseridas no *main.py* estão voltadas para a tela do monitor do meu notebook.

Para verificar as posições da sua tela, execute este programa abaixo e direcione o cursor do seu mouse para o campo do formulário antes de passar 4 segundos:
```bash
python pegar_posicao.py
```
Ou acesse a pasta ***setting*** e execute o programa *pegar_posicao.py*.

Após pegar as posições do campo de login e do código do produto, insere as novas coordenadas nas linhas 23 e 32 no código *main.py* respectivamente.


## Funcionalidades
A seguir será informado sobre cada programa e sua respectiva funcionalidade:

* **main.py**:

    * Realiza o cadastro de produtos no sistema de forma automática

* **pegar_posicao.py**:

    * Pega a posição do cursor do mouse está na tela do monitor do computador ou notebook