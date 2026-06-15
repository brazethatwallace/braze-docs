Você pode usar esse modelo para criar qualquer página ou seção para a documentação da Braze. Para configuração de ambiente, pré-visualizações e tipos de conteúdo, colaboradores com acesso ao repositório devem seguir o handbook em `docs/contributing/` (por exemplo, `generating_a_preview.md` e `content_types.md`). O restante do público pode usar [Feedback da documentação]({{site.baseurl}}/feedback/) para entrar em contato com a equipe de documentação.

{% details Mostrar modelo %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
---

<!-- O título da sua página, usado para renderizar o título exibido na página. -->
# ARTICLE_TITLE

<!-- A visão geral começa com o caractere '>' e descreve o que será abordado. Em um parágrafo opcional seguinte, contextualize o tópico em alto nível em uma introdução. -->
> DESCRIPTION.

INTRODUCTION.

<!-- Os pré-requisitos para essa tarefa. Se nenhum pré-requisito for necessário, você pode remover esta seção. -->
## Pré-requisitos

Antes de começar, você precisará concluir o seguinte:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- Uma explicação opcional e breve de como funciona o fluxo de trabalho do recurso. -->
## Como funciona

CONTENT.

<!-- Guie o usuário pela integração e ativação do recurso. -->
 ## Integração
CONTENT.

<!-- Um guia prático com etapas aninhadas. -->
## TASK_TO_COMPLETE

<!-- Visão geral opcional da tarefa. -->
CONTENT.

<!-- Cabeçalho orientado a ações que descreve o objetivo da etapa. -->
### Etapa 1: ACTION_TO_COMPLETE

<!-- Use marcadores numerados ou parágrafos para descrever como concluir esta ação -->
CONTENT.

### Etapa 2: ACTION_TO_COMPLETE

CONTENT.
<!-- Referências opcionais, como tipos de dados compatíveis, campos, definições e similares. -->
### REFERENCE_TO_ASSIST_WITH_ACTION

CONTENT.

<!-- Para etapas opcionais, adicione "(opcional)" ao final do cabeçalho. -->
### Etapa 3: OPTIONAL_ACTION_TO_COMPLETE (opcional)

CONTENT.
<!-- Uma seção opcional para o que é compatível. Adicione cabeçalhos aninhados para ser mais específico. -->
## Tipos de dados compatíveis / Atributos compatíveis / Eventos compatíveis / ETC. compatíveis
CONTENT.
<!-- Uma seção opcional com considerações importantes para os usuários revisarem antes de usar o recurso. -->
## Considerações

CONTENT.

<!-- Uma seção opcional que orienta os usuários na solução de problemas comuns. -->
## Solução de problemas

### ISSUE_TO_TROUBLESHOOT
CONTENT.

`````
{% endraw %}
{% enddetails %}