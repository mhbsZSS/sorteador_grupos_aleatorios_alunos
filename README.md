# 🎓 Sorteador de Grupos Escolar (Pro Edition)

Uma ferramenta prática e imparcial desenvolvida em **Python** para auxiliar professores na formação de grupos em sala de aula. O sistema permite a entrada manual de dados ou o carregamento automatizado via arquivos de texto.

## 🧠 Contexto Pedagógico
Como professor de matemática, entendo a importância da imparcialidade na dinâmica de grupo. Este software utiliza algoritmos de embaralhamento aleatório para garantir que a distribuição dos alunos seja puramente estatística, eliminando tendências e promovendo a integração da turma.

## 🚀 Funcionalidades

- **Entrada Dupla:** Suporte para inserção manual (vírgula) ou leitura de arquivo `alunos.txt` (um nome por linha).
- **Lógica Flexível:** O usuário define a quantidade de integrantes por grupo e o sistema realiza o fatiamento (*slicing*) automático.
- **Exportação de Dados:** Opção para salvar o resultado do sorteio em um arquivo `.txt`, facilitando o compartilhamento via WhatsApp ou Google Classroom.
- **Interface Limpa:** Navegação simples via menus no terminal.

## 🛠️ Conceitos Técnicos Aplicados

- **Biblioteca `random`**: Uso do método `shuffle` para permutação aleatória.
- **I/O (Input/Output)**: Manipulação de leitura e escrita de arquivos de texto com codificação UTF-8.
- **List Comprehension**: Criação de sublistas de forma otimizada e legível.
- **Tratamento de Exceções**: Proteção contra arquivos inexistentes ou entradas numéricas inválidas.

## 📂 Estrutura do Projeto

```text
.
├── sorteador_grupos.py   # Script principal
├── alunos.txt            # Exemplo de lista de chamada (opcional)
├── LICENSE               # Licença do projeto
└── README.md             # Documentação