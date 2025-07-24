# ⚽ Copa do Mundo 2022 – Sistema de Gerenciamento de Grupos e Estatísticas

**Terceiro projeto na área de programação**, desenvolvido com o objetivo de aplicar conceitos mais avançados em Python, como **manipulação de arquivos**, **validação de dados**, **modularização** e **persistência de informações**. O sistema simula um software para **gerenciar os grupos, jogos e estatísticas da Copa do Mundo FIFA 2022**, permitindo controle total da fase de grupos e geração de relatórios.

## 🧠 Sobre o Projeto

Inspirado na grandiosidade do evento e na necessidade de acompanhar as informações de forma prática, o sistema permite:

- Cadastrar os 8 grupos (A a H) com 4 seleções cada;
- Cadastrar os 6 jogos da fase de grupos, incluindo:
  - Placar
  - Data
  - Horário
  - Local
  - Cartões
- Editar seleções e partidas;
- Visualizar grupos e jogos cadastrados;
- Gerar um relatório estatístico completo.

## 📊 Relatórios e Estatísticas

O sistema fornece dados detalhados como:

- Confrontos das oitavas de final (1º vs 2º colocado de cada grupo);
- Média de gols por grupo e geral;
- Jogo com maior goleada;
- Relatório completo com todas as informações acima.

## 💾 Persistência de Dados

Ao fechar o programa, todos os dados são armazenados automaticamente em arquivos de texto, garantindo que nada seja perdido. Ao iniciar novamente, os dados são carregados do arquivo e podem ser editados normalmente.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.8.10  
- **IDE**: Visual Studio Code  
- **Sistema Operacional**: Windows 7 Ultimate

## 📌 Aprendizados

Este projeto permitiu aprofundar o uso de:

- Dicionários aninhados e listas;
- Validações com múltiplos critérios de desempate (gols, saldo, cartões...);
- Leitura e escrita em arquivos `.txt`;
- Modularização com funções reutilizáveis;
- Estrutura de menus interativos com navegação clara;
- Organização de código com lógica escalável.

## 💡 Melhorias Futuras

- Adição das fases seguintes: quartas de final, semifinal e final;
- Adição de interface gráfica;
- Suporte para exportação em PDF dos relatórios;
- Uso de arquivos JSON ou banco de dados SQLite para maior robustez.
