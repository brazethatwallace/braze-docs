---
nav_title: Ferramentas do dashboard
article_title: Ferramentas do dashboard para personalização
page_order: 0
description: "Este artigo de referência descreve a experiência de Adicionar Personalização nos editores de mensagens e landing pages da Braze, incluindo Liquid pré-formatado, valores padrão e melhorias no editor de Liquid, como rótulos de cores e sugestões preditivas."
---

# Ferramentas do dashboard para personalização {#dashboard-tools-for-personalization}

> Use as ferramentas do dashboard da Braze para inserir personalização com Liquid sem precisar escrever cada tag manualmente. O fluxo **Adicionar Personalização** cria a sintaxe correta para você, e o editor de Liquid ajuda a ler e estender modelos rapidamente.

Para regras de sintaxe Liquid, tags compatíveis e padrões avançados, consulte [Usando Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) e [Tags de personalização compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Adicionar Personalização em criadores e configurações {#add-personalization-in-composers-and-settings}

A ferramenta **Adicionar Personalização** aparece próxima a campos de texto com suporte a modelos em todo o dashboard, incluindo:

- **Etapas de Campaign e Canvas** para canais que suportam Liquid no corpo ou nos cabeçalhos (por exemplo, e-mail, push, SMS, mensagens no app, Content Cards e webhooks).
- **Editores de arrastar e soltar**, onde o controle geralmente está na barra de ferramentas do bloco ou do editor. Por exemplo, em mensagens no app de arrastar e soltar, você pode selecionar **Adicionar Personalização**, escolher um tipo de personalização e então inserir o snippet gerado no seu conteúdo antes de pré-visualizar em **Pré-visualização e teste**. Para notas específicas de cada canal, consulte o artigo de arrastar e soltar ou do criador do seu canal (como [Configurações de estilo de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#adding-liquid) ou [Criar um e-mail com arrastar e soltar]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)).
- **Criadores especializados** que expõem um seletor de personalização — por exemplo, [recomendações de itens]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations) usam opções de **Tipo de Personalização** como **Recomendação de Item** dentro do mesmo estilo de janela.
- **Landing pages**, onde você pode adicionar personalização com Liquid no editor de arrastar e soltar ou nas configurações de página e bloco. Para mais detalhes, consulte [Personalizar landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages).

## Inserir variáveis pré-formatadas e valores padrão {#insert-pre-formatted-variables-and-defaults}

A ferramenta **Adicionar Personalização** ajuda você a inserir Liquid com valores padrão opcionais para que dados de perfil vazios não quebrem seu texto.

![O modal Adicionar Personalização que aparece após selecionar inserir personalização. O modal possui campos para tipo de personalização, atributo, valor padrão opcional e exibe uma pré-visualização da sintaxe Liquid.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

A ferramenta insere o Liquid com o valor padrão especificado no ponto onde seu cursor estava. O ponto de inserção também é indicado pela caixa de pré-visualização, que mostra o texto antes e depois. Se um bloco de texto estiver destacado, o texto destacado será substituído.

![Um GIF do modal Adicionar Personalização mostrando o usuário inserindo "fellow traveler" como valor padrão, e o modal substituindo o texto destacado "name" no criador pelo snippet Liquid.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

Você ainda pode digitar {% raw %}`{{`{% endraw %} em muitos criadores para usar o autocompletar, ou colar tags de outro lugar. Para mais detalhes, consulte [Inserindo tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#inserting-tags) em **Usando Liquid**.

### Atribuir variáveis {#assign-variables}

{% raw %}
Algumas operações em Liquid exigem que você armazene o valor que deseja manipular como uma variável. Isso é comum quando sua instrução Liquid inclui múltiplos atributos, propriedades de eventos ou filtros.

Por exemplo, digamos que você queira somar dois inteiros de dados personalizados.

#### Exemplo incorreto de Liquid {#incorrect-liquid-example}

Você não pode usar:

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Esse Liquid não funciona porque você não pode referenciar múltiplos atributos em uma única linha. É necessário atribuir uma variável a pelo menos um desses valores antes que as funções matemáticas sejam executadas. Somar dois atributos personalizados requer duas linhas de Liquid: uma para atribuir o atributo personalizado a uma variável e outra para realizar a adição.

#### Exemplo correto de Liquid {#correct-liquid-example}

Você pode usar:

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### Tutorial: usando variáveis para calcular um saldo {#tutorial-using-variables-to-calculate-a-balance}

Vamos calcular o saldo atual de um usuário somando o saldo do cartão-presente com o saldo de recompensas:

Primeiro, use a tag `assign` para substituir o atributo personalizado `current_rewards_balance` pelo termo "balance". Isso significa que agora você tem uma variável chamada `balance`, que pode ser manipulada.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Em seguida, usaremos o filtro `plus` para combinar o saldo do cartão-presente de cada usuário com o saldo de recompensas, representado por `{{balance}}`.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
Está sempre atribuindo as mesmas variáveis em cada mensagem? Em vez de escrever a tag `assign` repetidamente, você pode salvar essa tag como um bloco de conteúdo e colocá-la no topo da sua mensagem.<br><br>

1. [Crie um bloco de conteúdo]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block).
2. Dê um nome ao seu bloco de conteúdo (sem espaços ou caracteres especiais).
3. Selecione **Editar** na parte inferior da página.
4. Insira suas tags `assign`.

Desde que o bloco de conteúdo esteja no topo da sua mensagem, toda vez que a variável for inserida na mensagem como um objeto, ela fará referência ao atributo personalizado escolhido!
{% endalert %}

## Melhorias do editor de Liquid {#liquid-editor-enhancements}

Esses comportamentos do dashboard facilitam o trabalho com Liquid enquanto você compõe mensagens.

### Rótulos de cores {#color-labels}

Cada elemento Liquid corresponde a uma cor, permitindo que você diferencie seu Liquid rapidamente no editor de Liquid.

![Diagrama de vários rótulos de cores para diferentes elementos Liquid.]({% image_buster /assets/img/liquid_color_code.png %})

### Liquid preditivo {#predictive-liquid}

Você também pode usar o Liquid preditivo para atributos personalizados, nomes de atributos e mais enquanto cria suas mensagens personalizadas.

![A Braze recomendando diferentes atributos Liquid conforme mais texto é digitado em um campo.]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Próximas etapas {#next-steps}

- [Usando Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) — sintaxe, `assign`, condicionais e filtros na Braze
- [Definindo valores padrão]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) — valores padrão em Liquid além do modal
- [Filtros]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters) — formatar datas, matemática, strings e mais