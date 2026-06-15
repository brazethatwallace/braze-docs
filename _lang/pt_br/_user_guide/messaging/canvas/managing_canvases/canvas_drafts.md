---
nav_title: Salvar rascunhos para Canvas
article_title: Salvar rascunhos para Canvas
alias: "/save_as_draft/"
page_order: 1
description: "Este artigo de referência aborda como salvar um rascunho para um Canvas que já foi lançado."
page_type: reference
tool: Canvas
---

# Salvar rascunhos para Canvas

> Ao criar e lançar Canvas, você pode editar um Canvas ativo e salvá-lo como rascunho, permitindo testar suas alterações antes de outro lançamento.

Se você tem um Canvas ativo que requer mudanças em grande escala, pode usar esse recurso para criar, salvar e verificar a qualidade **antes** de lançar essas alterações no Canvas ativo.

Como em qualquer Canvas, apenas uma pessoa pode editar um rascunho por vez, e um Canvas só pode ter um rascunho por vez. Esses rascunhos não possuem análise de dados porque as alterações do rascunho ainda não foram lançadas.

![Um exemplo de rascunho de Canvas com um banner indicando que o usuário está editando um rascunho de Canvas, com a opção de visualizar o Canvas ativo. O rodapé tem opções para voltar à visualização de análise de dados, salvar como rascunho ou lançar o rascunho.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Criando um rascunho

Para criar um rascunho:

1. Acesse um Canvas ativo.
2. Selecione o botão **Salvar como rascunho** no rodapé do Canvas.

Observe que não é possível fazer edições no Canvas ativo enquanto existir um rascunho do Canvas. Você pode atualizar o Canvas para aplicar as alterações ou descartar o rascunho.

## Consultando o Canvas ativo

Para consultar o Canvas ativo, selecione **View Active Canvas** no rodapé da visualização de análise de dados ou no cabeçalho do Canvas a partir do rascunho. Para voltar a um Canvas ativo, selecione **Editar rascunho** na visualização de análise de dados ou na visualização do Canvas ativo.

Você só pode referenciar etapas que já foram lançadas antes da criação do rascunho. Isso significa que, se você criou uma etapa ou canal **após** a criação do rascunho, ela não poderá ser referenciada no seu rascunho.

{% alert note %}
Se um bloco de conteúdo for referenciado em um rascunho de Canvas, o Canvas será listado na contagem de inclusão do bloco de conteúdo. No entanto, se o bloco de conteúdo for referenciado em um rascunho de um Canvas **ativo**, o Canvas não será listado na contagem de inclusão do bloco de conteúdo.
{% endalert %}

### Priorização de mensagens no app

Para rascunhos de um Canvas ativo, a prioridade da mensagem no app dentro do construtor de Canvas será atualizada imediatamente quando o usuário alterar a prioridade. Isso significa que a prioridade de mensagem no app em nível de Canvas é aplicada ao Canvas ativo imediatamente, mesmo quando um rascunho existe.

No entanto, as alterações de prioridade de mensagem no app em nível de etapa são salvas como rascunho e aplicadas quando o Canvas é atualizado. Por exemplo, em uma etapa de Mensagem, o classificador de prioridade será atualizado quando o usuário lançar o rascunho, já que as configurações da etapa se aplicam em nível de etapa.