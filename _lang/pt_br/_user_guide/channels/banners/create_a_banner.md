---
nav_title: "Criar um Banner"
article_title: "Criar um Banner"
page_order: 1
description: "Este artigo de referência aborda como criar, redigir, configurar e enviar Banners usando campanhas e Canvas da Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Criar um Banner

> Saiba como criar Banners ao construir campanhas e Canvas na Braze. Para informações mais gerais, consulte [Sobre Banners]({{site.baseurl}}/user_guide/channels/banners).

## Pré-requisitos

Antes de lançar seu Banner, sua equipe de desenvolvimento precisa [configurar os posicionamentos no seu app ou site]({{site.baseurl}}/developer_guide/banners/placements/). Você ainda pode rascunhar sua campanha de Banner enquanto isso, mas não poderá lançá-la até que os posicionamentos estejam configurados.

## Criar uma mensagem de Banner

{% multi_lang_include banners/creating_placements.md section="user" %}

### Etapa 2: Escolha onde criar sua mensagem

Não tem certeza se sua mensagem deve ser enviada usando uma campanha ou um Canvas? Campanhas são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas são melhores para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **Banner**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) conforme necessário. Tags facilitam encontrar suas campanhas e criar relatórios. Por exemplo, ao usar o Criador de relatórios, você pode filtrar pelas tags relevantes.
5. Selecione o posicionamento que você criou anteriormente para associá-lo à sua campanha.
6. Adicione variantes conforme necessário. Você pode escolher um tipo de mensagem e disposição diferentes para cada uma. Para saber mais sobre variantes, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).
7. Escolha uma data e hora de início para sua campanha de Banner. Por padrão, os Banners duram indefinidamente. Você pode alterar isso selecionando **Horário de término** e especificando uma data e hora de encerramento.

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes extras. Depois, selecione **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) usando o criador de Canvas.
2. Após configurar seu Canvas, adicione uma etapa de Mensagem no construtor de Canvas. Dê à sua etapa um nome claro e significativo.
3. Selecione **Banner** como seu canal de envio de mensagens.
4. Selecione um posicionamento para o Banner.
5. Defina a prioridade do Banner. A [prioridade do Banner]({{site.baseurl}}/user_guide/channels/banners/#priority) determina a ordem em que os Banners são exibidos quando compartilham o mesmo posicionamento.
6. Defina uma expiração para o Banner. Pode ser após um período de tempo depois que a etapa estiver disponível ou em uma data e hora específicas.

{% endtab %}
{% endtabs %}

### Etapa 3: Redigir um Banner {#compose-a-banner}

Para redigir seu Banner, você pode escolher:

- Começar com um modelo em branco
- Usar um modelo de Banner da Braze
- Selecionar um modelo de Banner salvo

![Opção para escolher um Banner em branco ou um modelo.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Etapa 3.1: Estilizar o Banner

Você pode arrastar e soltar blocos e linhas na área do canvas para começar a construir sua mensagem.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Para personalizar as propriedades de fundo, configurações de borda e mais da sua mensagem, selecione **Estilos**. Se quiser personalizar o estilo apenas de um bloco ou linha específica, selecione-o para fazer as alterações.

![Painel de estilos do criador de Banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Etapa 3.2: Definir o comportamento ao clicar (opcional)

Quando um usuário clica em um link no Banner, você pode optar por direcioná-lo para uma área mais profunda do seu app ou redirecioná-lo para outra página da web. Além disso, você pode escolher [registrar um atributo personalizado ou evento]({{site.baseurl}}/developer_guide/analytics/), que atualiza o perfil do usuário com dados personalizados quando ele clica no Banner.

{% alert important %}
{::nomarkdown}
O comportamento ao clicar pode ser substituído se um elemento específico (como um botão, link ou imagem do Banner) tiver seu próprio comportamento ao clicar. Por exemplo, considerando os seguintes comportamentos ao clicar:<br><ul><li>Um Banner tem um comportamento ao clicar que redireciona para a página inicial de um site.</li><li>Uma imagem no Banner tem um comportamento ao clicar que redireciona para a página de produto de um site.</li></ul>Se um usuário clicar na imagem, ele será redirecionado para a página de produto. No entanto, clicar na área ao redor no Banner o redireciona para a página inicial.
{:/}
{% endalert %}

#### Etapa 3.3: Configurar o comportamento de dispensa (opcional) {#dismiss-behavior}

{% alert important %}
A dispensa de Banners está atualmente em acesso antecipado. Se você tem interesse em participar do acesso antecipado, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

Marque a caixa de seleção **O Banner pode ser dispensado** para permitir que os usuários dispensem o Banner. Essa opção pode ser útil em cenários em que você deseja promover uma venda por tempo limitado para todos os usuários do app, mas permitir que eles dispensem a mensagem caso não tenham interesse.

#### Etapa 3.4: Adicionar propriedades personalizadas (opcional) {#custom-properties}

Você pode adicionar propriedades personalizadas a um Banner para anexar metadados estruturados, como strings ou objetos JSON. Essas propriedades não afetam como o Banner é exibido, mas podem ser [acessadas pelo SDK da Braze]({{site.baseurl}}/developer_guide/banners/placements/) para modificar o comportamento ou a aparência do seu app. Por exemplo, você poderia:

- Enviar metadados para análise de dados de terceiros ou integrações.
- Usar metadados como um `timestamp` ou objeto JSON para acionar lógica condicional.
- Controlar o comportamento de um Banner com base em metadados incluídos como `ratio` ou `format`.

Para adicionar uma propriedade personalizada, selecione **Configurações** > **Propriedades** > **Adicionar propriedade**.

![A página de propriedades mostrando a opção de adicionar a primeira propriedade personalizada a uma campanha de Banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propriedade que deseja adicionar, preencha o seguinte:

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| Tipo de propriedade | O tipo de dado da propriedade. Os tipos suportados incluem string, booleano, número, timestamp, URL de imagem e objeto JSON. | String |
| Chave da propriedade | O identificador único da propriedade. Essa chave é usada no SDK para acessar a propriedade. | `color` |
| Valor | O valor atribuído à propriedade. Deve corresponder ao tipo de propriedade selecionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Quando terminar, selecione **Concluir**.

![A página de propriedades com uma propriedade do tipo string com a chave color e o valor #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Etapa 4: Construir o restante da sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

#### Definir a prioridade do Banner (opcional)

A [prioridade do Banner]({{site.baseurl}}/user_guide/channels/banners/#priority) determina a ordem em que os Banners são exibidos quando compartilham o mesmo posicionamento. Para definir a prioridade manualmente:

1. Selecione **Definir prioridade exata**.
2. Arraste e solte as campanhas para ordená-las com a prioridade correta.
3. Selecione **Aplicar ordenação**.

{% alert tip %}
Se você tem várias campanhas de Banner usando o mesmo ID de posicionamento, recomendamos usar o organizador de prioridade por arrastar e soltar para definir a prioridade exata.
{% endalert %}

#### Escolher seu público

1. Em **Público-alvo**, escolha segmentos ou filtros para refinar seu público. Você recebe automaticamente uma pré-visualização da população aproximada do segmento. A associação exata ao segmento é calculada antes do envio da mensagem.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2. Em **Atribuir conversões**, acompanhe a frequência com que os usuários realizam ações específicas após receberem uma campanha, definindo eventos de conversão com um período de até 30 dias para contar a ação como uma conversão.

{% multi_lang_include target_audiences.md %}

#### Escolher eventos de conversão

A Braze permite que você acompanhe [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), ou seja, a frequência com que os usuários realizam ações específicas após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão é contabilizada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não fez isso, conclua as seções restantes do seu componente de Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar [testes multivariantes]({{site.baseurl}}/user_guide/messaging/ab_testing/) e [Seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/), e mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação de Canvas.

{% endtab %}
{% endtabs %}

### Etapa 5: Testar sua mensagem (opcional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Etapa 6: Revisar e implantar

Após terminar de construir sua campanha ou Canvas, revise os detalhes, [teste-a]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) e envie quando estiver tudo pronto.