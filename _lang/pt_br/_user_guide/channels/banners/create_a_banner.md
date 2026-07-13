---
nav_title: "Criar um Banner"
article_title: "Criar um Banner"
page_order: 1
description: "Este artigo de referência aborda como criar, redigir, configurar e enviar Banners usando Campaigns e Canvas da Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Criar um Banner {#create-a-banner}

> Saiba como criar Banners ao construir Campaigns e Canvas na Braze. Para saber mais, consulte [Sobre Banners]({{site.baseurl}}/user_guide/channels/banners).

## Pré-requisitos {#prerequisites}

Antes de lançar seu Banner, sua equipe de desenvolvimento precisa [configurar os posicionamentos no seu app ou website]({{site.baseurl}}/developer_guide/banners/placements). Você ainda pode rascunhar sua campanha de Banner enquanto isso, mas não poderá lançá-la até que os posicionamentos estejam configurados.

## Criar uma mensagem de Banner {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### Etapa 2: Escolha onde criar sua mensagem {#step-2-choose-where-to-build-your-message}

Não tem certeza se sua mensagem deve ser enviada usando uma Campaign ou um Canvas? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas são melhores para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **Banner**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário. Tags facilitam encontrar suas campanhas e criar relatórios. Por exemplo, ao usar o Criador de relatórios, você pode filtrar pelas tags relevantes.
5. Selecione o posicionamento que você criou anteriormente para associá-lo à sua campanha.
6. Adicione variantes conforme necessário. Você pode escolher um tipo de mensagem e disposição diferentes para cada uma. Para saber mais sobre variantes, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).
7. Escolha uma data e hora de início para sua campanha de Banner. Por padrão, os Banners duram indefinidamente. Você pode alterar isso selecionando **End Time** e especificando uma data e hora de encerramento.

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes extras. Depois, selecione **Copy from Variant** no menu suspenso **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando o criador de Canvas.
2. Após configurar seu Canvas, adicione uma etapa de Mensagem no construtor de Canvas. Dê à sua etapa um nome claro e significativo.
3. Selecione **Banner** como seu canal de envio de mensagens.
4. Selecione um posicionamento para o Banner.
5. Defina a prioridade. A [prioridade do Banner]({{site.baseurl}}/user_guide/channels/banners#priority) determina a ordem em que os Banners são exibidos quando compartilham o mesmo posicionamento.
6. Defina uma expiração para o Banner. Pode ser após um período de tempo depois que a etapa estiver disponível ou em uma data e hora específicas. A duração máxima de expiração é de 31 dias após a etapa ficar disponível para o usuário.

{% endtab %}
{% endtabs %}

### Etapa 3: Redigir um Banner {#compose-a-banner}

Em seguida, escolha como deseja começar a construir:

- **Editor de arrastar e soltar:** comece com um Banner em branco e construa visualmente com blocos e linhas.
- **Editor de HTML:** comece com um Banner em branco e trabalhe diretamente em HTML.
- **Modelos:** abra a biblioteca de modelos e selecione um design em **Braze Templates** ou **Your Templates**. Os modelos são abertos no editor de arrastar e soltar para personalização.

![Opções para escolher o editor de arrastar e soltar, o editor de HTML ou modelos para o seu Banner.]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### Etapa 3.1: Estilizar o Banner {#step-31-style-the-banner}

{% tabs %}
{% tab Editor de arrastar e soltar %}

Você pode arrastar e soltar blocos e linhas na área do canvas para começar a construir sua mensagem. Para uma referência dos blocos do editor de Banner e links para detalhes de propriedades compartilhadas, consulte [Blocos do editor (Banners)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Para personalizar as propriedades de fundo, configurações de borda e mais da sua mensagem, selecione **Styles**. Se quiser personalizar o estilo apenas de um bloco ou linha específica, selecione-o para fazer as alterações.

![Painel de estilos do criador de Banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% endtab %}
{% tab Editor de HTML %}

O editor de HTML é ideal para equipes que já mantêm seus próprios modelos HTML ou desejam controle total sobre a marcação e o estilo. Você pode escrever ou colar HTML personalizado diretamente no editor. Tags de personalização Liquid são totalmente suportadas, permitindo que você referencie atributos de usuário, atributos personalizados, itens de catálogo e mais.

{% alert tip %}
Precisa de ajuda para construir o HTML do seu Banner? Selecione **Ask Operator** no editor de HTML e descreva o Banner que deseja. O [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) gera HTML que você pode revisar e inserir no editor. Para saber mais, consulte [Gerar mensagens]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).
{% endalert %}

Para rastreamento de cliques e dispensas no seu HTML personalizado, você deve chamar os métodos da ponte JavaScript explicitamente. Para a referência completa, consulte [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code).

{% endtab %}
{% endtabs %}

{% alert note %}
Para direcionar usuários em diferentes idiomas dentro de uma única campanha de Banner, consulte [Mensagens multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).
{% endalert %}

#### Etapa 3.2: Definir o comportamento ao clicar (opcional) {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab Editor de arrastar e soltar %}

Quando um usuário clica em um link no Banner, você pode optar por direcioná-lo para uma área mais profunda do seu app ou redirecioná-lo para outra página da web. Além disso, você pode escolher [registrar um atributo personalizado ou evento]({{site.baseurl}}/developer_guide/analytics), que atualiza o perfil do usuário com dados personalizados quando ele clica no Banner. Para um rastreamento de cliques mais granular, atribua um identificador personalizado a cada elemento interativo usando o campo **Identifier for Reporting** no painel de propriedades.

{% alert important %}
{::nomarkdown}
O comportamento ao clicar pode ser substituído se um elemento específico (como um botão, link ou imagem do Banner) tiver seu próprio comportamento ao clicar. Por exemplo, considerando os seguintes comportamentos ao clicar:<br><ul><li>Um Banner tem um comportamento ao clicar que redireciona para a página inicial de um site.</li><li>Uma imagem no Banner tem um comportamento ao clicar que redireciona para a página de produto de um site.</li></ul>Se um usuário clicar na imagem, ele será redirecionado para a página de produto. No entanto, clicar na área ao redor no Banner o redireciona para a página inicial.
{:/}
{% endalert %}

{% endtab %}
{% tab Editor de HTML %}

No editor de HTML, o rastreamento de cliques não é automático. Você deve chamar `brazeBridge.logClick()` dentro do seu HTML para cada elemento clicável que deseja rastrear. Por exemplo:

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

Para a referência completa da ponte JavaScript, consulte [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Etapa 3.3: Configurar o comportamento de dispensa (opcional) {#dismiss-behavior}

{% tabs %}
{% tab Editor de arrastar e soltar %}

Marque a caixa de seleção **Banner can be dismissed** na seção **Dismiss behavior** para permitir que os usuários dispensem o Banner. Essa opção é útil quando você deseja promover uma oferta por tempo limitado para um público amplo, mas ainda permitir que usuários desinteressados ocultem a mensagem.

Quando a dispensa está ativada, você pode personalizar o botão de dispensa na seção **Dismiss behavior**:

| Configuração | Descrição |
|---------|-------------|
| **Button size** | O tamanho do botão de dispensa exibido no Banner. |
| **Button color** | A cor do botão de dispensa. |
| **ARIA label** | O rótulo acessível para o botão de dispensa, usado por leitores de tela. O padrão é "Close" se deixado em branco. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurações do botão de dispensa" }

Quando um usuário dispensa um Banner, ele não aparece novamente para esse usuário, mesmo que ele ainda atenda aos critérios de direcionamento da campanha.

{% endtab %}
{% tab Editor de HTML %}

No editor de HTML, a dispensa é tratada no seu HTML usando `brazeBridge.closeMessage()`. Combine com `brazeBridge.logClick()` para também rastrear a ação de dispensa como um evento de clique. Por exemplo:

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

Quando um usuário dispensa um Banner dessa forma, ele não aparece novamente para esse usuário, mesmo que ele ainda atenda aos critérios de direcionamento da campanha.

Para a referência completa da ponte JavaScript, consulte [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Etapa 3.4: Adicionar propriedades personalizadas (opcional) {#custom-properties}

Você pode adicionar propriedades personalizadas a um Banner para anexar metadados estruturados, como strings ou objetos JSON. Essas propriedades não afetam como o Banner é exibido, mas podem ser [acessadas pelo SDK da Braze]({{site.baseurl}}/developer_guide/banners/placements) para modificar o comportamento ou a aparência do seu app. Por exemplo, você poderia:

- Enviar metadados para análise de dados de terceiros ou integrações.
- Usar metadados como um `timestamp` ou objeto JSON para acionar lógica condicional.
- Controlar o comportamento de um Banner com base em metadados incluídos como `ratio` ou `format`.

As propriedades personalizadas funcionam da mesma forma no editor de arrastar e soltar e no editor de HTML. Para adicionar uma propriedade personalizada, selecione **Settings** > **Properties** > **Add property**.

![A página de propriedades mostrando a opção de adicionar a primeira propriedade personalizada a uma campanha de Banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propriedade que deseja adicionar, preencha o seguinte:

| Campo | Descrição | Exemplo |
|-------|-------------|---------|
| Tipo de propriedade | O tipo de dado da propriedade. Os tipos suportados incluem string, booleano, número, timestamp, URL de imagem e objeto JSON. | String |
| Chave da propriedade | O identificador único da propriedade. Essa chave é usada no SDK para acessar a propriedade. | `color` |
| Valor | O valor atribuído à propriedade. Deve corresponder ao tipo de propriedade selecionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Adicionar propriedades personalizadas" }

Quando terminar, selecione **Done**.

![A página de propriedades com uma propriedade do tipo string com a chave color e o valor #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Etapa 4: Construir o restante da sua campanha ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Definir a prioridade do Banner (opcional) {#set-banner-priority-optional}

A [prioridade do Banner]({{site.baseurl}}/user_guide/channels/banners#priority) determina a ordem em que os Banners são exibidos quando compartilham o mesmo posicionamento. Para definir a prioridade manualmente:

1. Selecione **Set exact priority**.
2. Arraste e solte as campanhas para ordená-las com a prioridade correta.
3. Selecione **Apply Sort**.

{% alert tip %}
Se você tem várias campanhas de Banner usando o mesmo ID de posicionamento, recomendamos usar o organizador de prioridade por arrastar e soltar para definir a prioridade exata.
{% endalert %}

#### Configurar reelegibilidade (opcional) {#re-eligibility}

Por padrão, os usuários que dispensam um Banner nunca se tornam reelegíveis para essa campanha. Para permitir que usuários que dispensaram o Banner o vejam novamente, acesse a etapa **Delivery Controls** e selecione **Allow users to become re-eligible to receive campaign**. Quando ativado, defina um período de espera em minutos, horas, dias ou semanas.

A contagem regressiva começa a partir do momento em que o usuário dispensa o Banner. Após o período expirar, o usuário se torna automaticamente reelegível — sem necessidade de reiniciar a campanha. A reelegibilidade é rastreada por usuário e por campanha.

#### Escolher seu público {#choose-your-audience}

1. Em **Target Audiences**, escolha Segments ou filtros para refinar seu público. Você recebe automaticamente uma prévia da população aproximada do Segment. A associação exata ao Segment é calculada antes do envio da mensagem.

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. Em **Assign Conversions**, acompanhe a frequência com que os usuários realizam ações específicas após receberem uma campanha, definindo eventos de conversão com um período de até 30 dias para contar a ação como uma conversão.

#### Escolher eventos de conversão {#choose-conversion-events}

A Braze permite que você acompanhe [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), ou seja, a frequência com que os usuários realizam ações específicas após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão é contabilizada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não fez isso, conclua as seções restantes do seu componente de Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar [testes multivariantes]({{site.baseurl}}/user_guide/messaging/ab_testing) e [seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection), e mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-3-build-your-canvas) da nossa documentação de Canvas.

Para controlar a reelegibilidade em etapas de Banner no Canvas, use as configurações de reentrada do Canvas. Para saber mais, consulte [Reelegibilidade para Campaigns e Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

{% endtab %}
{% endtabs %}

### Etapa 5: Testar sua mensagem (opcional) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### Etapa 6: Revisar e implantar {#step-6-review-and-deploy}

Após terminar de construir sua campanha ou Canvas, revise os detalhes, [teste-a]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) e envie quando estiver tudo pronto.