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

Antes de lançar seu Banner, sua equipe de desenvolvimento precisa [configurar os posicionamentos no seu app ou website]({{site.baseurl}}/developer_guide/banners/placements). Você ainda pode rascunhar sua campanha de Banner enquanto isso, mas não poderá lançar a campanha até que os posicionamentos estejam configurados.

## Criar uma mensagem de Banner {#create-a-banner-message}

{% multi_lang_include banners/creating_placements.md section="user" %}

### Etapa 2: Escolha onde criar sua mensagem {#step-2-choose-where-to-build-your-message}

Não tem certeza se sua mensagem deve ser enviada usando uma campanha ou um Canvas? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas são melhores para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Envio de mensagens** > **Campaigns** e selecione **Criar Campaign**.
2. Selecione **Banner**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário. Tags facilitam a localização e a criação de relatórios das suas campanhas. Por exemplo, ao usar o Report Builder, você pode filtrar pelas tags relevantes.
5. Selecione o posicionamento criado anteriormente para associá-lo à sua campanha.
6. Adicione variantes conforme necessário. Você pode escolher um tipo de mensagem e layout diferentes para cada uma. Para saber mais sobre variantes, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).
7. Escolha uma data e hora de início para sua campanha de Banner. Por padrão, Banners duram indefinidamente. Você pode alterar isso selecionando **Hora de término** e especificando uma data e hora de término.

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, selecione **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando o criador de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa de mensagem no criador de Canvas. Dê à sua etapa um nome claro e significativo.
3. Selecione **Banner** como canal de envio de mensagens.
4. Selecione um posicionamento para o Banner.
5. Defina a prioridade. A [prioridade do Banner]({{site.baseurl}}/user_guide/channels/banners#priority) determina a ordem na qual os Banners são exibidos quando compartilham o mesmo posicionamento.
6. Defina uma expiração para o Banner. Isso pode ser após um período de tempo depois que a etapa estiver disponível ou em uma data e hora específicas. A duração máxima de expiração é de 31 dias após a etapa ficar disponível para o usuário.

{% endtab %}
{% endtabs %}

### Etapa 3: Criar um Banner {#compose-a-banner}

Em seguida, escolha como você deseja começar a criar:

- **Editor de arrastar e soltar:** Comece com um Banner em branco e crie visualmente com blocos e linhas.
- **Editor de HTML:** Comece com um Banner em branco e trabalhe diretamente em HTML.
- **Modelos:** Abra a biblioteca de modelos e selecione um design em **Modelos Braze** ou **Seus modelos**. Os modelos são abertos no editor de arrastar e soltar para personalização.

![Opções para escolher o editor de arrastar e soltar, editor de HTML ou modelos para o seu Banner.]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### Etapa 3.1: Estilizar o Banner {#step-31-style-the-banner}

{% tabs %}
{% tab Editor de arrastar e soltar %}

Você pode arrastar e soltar blocos e linhas na área do canvas para começar a criar sua mensagem. Para uma referência dos blocos do editor de Banner e links para detalhes de propriedades compartilhadas, consulte [Blocos do editor (Banners)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Para personalizar as propriedades de fundo da sua mensagem, configurações de borda e mais, selecione **Estilos**. Se quiser personalizar o estilo apenas de um bloco ou linha específica, selecione-o para fazer alterações.

![Painel de estilos do criador de Banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='banner' %}

{% endtab %}
{% tab Editor de HTML %}

O editor de HTML é ideal para equipes que já mantêm seus próprios modelos de HTML ou desejam controle total sobre a marcação e a estilização. Você pode escrever ou colar HTML personalizado diretamente no editor. Tags de personalização Liquid são totalmente suportadas, então você pode referenciar atributos de usuário, atributos personalizados, itens de catálogo e mais.

{% alert tip %}
Precisa de ajuda para criar o HTML do seu Banner? Selecione **Ask Operator** no editor de HTML e descreva o Banner desejado. O [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) gera o HTML que você pode revisar e inserir no editor. Para saber mais, consulte [Gerar mensagens]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages).
{% endalert %}

Para rastreamento de cliques e dispensas no seu HTML personalizado, você precisa chamar os métodos do ponte JavaScript explicitamente. Para a referência completa, consulte [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code).

{% endtab %}
{% endtabs %}

{% alert note %}
Para direcionar usuários em diferentes idiomas dentro de uma única campanha de Banner, consulte [Mensagens multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).
{% endalert %}

#### Etapa 3.2: Definir o comportamento ao clicar (opcional) {#step-32-define-on-click-behavior-optional}

{% tabs %}
{% tab Editor de arrastar e soltar %}

Quando um usuário clica em um link no Banner, você pode optar por navegar para uma parte mais profunda do seu app ou redirecioná-lo para outra página da web. Além disso, você pode optar por [registrar um atributo personalizado ou evento]({{site.baseurl}}/developer_guide/analytics), que atualiza o perfil do usuário com dados personalizados quando ele clica no Banner. Para um rastreamento de cliques mais granular, atribua um identificador personalizado a cada elemento interativo usando o campo **Identificador para relatório** no painel de propriedades.

{% alert important %}
{::nomarkdown}
O comportamento ao clicar pode ser substituído se um elemento específico (como um botão, link ou imagem do Banner) tiver seu próprio comportamento ao clicar. Por exemplo, considere os seguintes comportamentos ao clicar:<br><ul><li>Um Banner tem um comportamento ao clicar que redireciona para a página inicial de um website.</li><li>Uma imagem no Banner tem um comportamento ao clicar que redireciona para a página de produto de um website.</li></ul>Se um usuário clicar na imagem, ele será redirecionado para a página de produto. No entanto, clicar na área ao redor no Banner o redireciona para a página inicial.
{:/}
{% endalert %}

{% endtab %}
{% tab Editor de HTML %}

No editor de HTML, o rastreamento de cliques não é automático. Você deve chamar `brazeBridge.logClick()` de dentro do seu HTML para cada elemento clicável que deseja rastrear. Por exemplo:

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

Para a referência completa do ponte JavaScript, consulte [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Etapa 3.3: Configurar o comportamento de dispensa (opcional) {#dismiss-behavior}

{% alert important %}
As dispensas de Banner exigem as seguintes versões mínimas do SDK. Versões mais antigas do SDK não renderizam Banners com a dispensa ativada.
{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 reactnative:22.0.0 flutter:20.0.0 %}
{% endalert %}

{% tabs %}
{% tab Editor de arrastar e soltar %}

Marque a caixa de seleção **O Banner pode ser dispensado** na seção **Comportamento de dispensa** para permitir que os usuários dispensem o Banner. Isso é útil quando você deseja promover uma oferta por tempo limitado para um público amplo, mas ainda permite que usuários desinteressados ocultem a mensagem.

Quando a dispensa está ativada, você pode personalizar o botão de dispensar na seção **Comportamento de dispensa**:

| Configuração | Descrição |
|---------|-------------|
| **Tamanho do botão** | O tamanho do botão de dispensar exibido no Banner. |
| **Cor do botão** | A cor do botão de dispensar. |
| **Rótulo ARIA** | O rótulo acessível para o botão de dispensar, usado por leitores de tela. O padrão é "Fechar" se deixado em branco. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurações do botão de dispensar" }

Quando um usuário dispensa um Banner, ele não aparece novamente para esse usuário, mesmo que ele ainda atenda aos critérios de direcionamento da campanha.

{% endtab %}
{% tab Editor de HTML %}

No editor de HTML, a dispensa é tratada no seu HTML usando `brazeBridge.closeMessage()`. Combine-o com `brazeBridge.logClick()` para também rastrear a ação de dispensa como um evento de clique. Por exemplo:

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

Quando um usuário dispensa um Banner dessa forma, ele não aparece novamente para esse usuário, mesmo que ele ainda atenda aos critérios de direcionamento da campanha.

Para a referência completa do ponte JavaScript, consulte [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Etapa 3.4: Adicionar propriedades personalizadas (opcional) {#custom-properties}

Você pode adicionar propriedades personalizadas a um Banner para anexar metadados estruturados, como strings ou objetos JSON. Essas propriedades não afetam como o Banner é exibido, mas podem ser [acessadas por meio do SDK da Braze]({{site.baseurl}}/developer_guide/banners/placements) para modificar o comportamento ou a aparência do seu app. Por exemplo, você poderia:

{% multi_lang_include banners/metadata_use_cases.md %}

As propriedades personalizadas funcionam da mesma forma no editor de arrastar e soltar e no editor de HTML. Para adicionar uma propriedade personalizada, selecione **Configurações** > **Propriedades** > **Adicionar propriedade**.

![A página de propriedades mostrando a opção de adicionar a primeira propriedade personalizada a uma campanha de Banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propriedade que deseja adicionar, preencha o seguinte:

| Campo | Descrição | Exemplo |
|-------|-------------|---------|
| Tipo de propriedade | O tipo de dado da propriedade. Os tipos suportados incluem string, booleano, número, timestamp, URL de imagem e objeto JSON. | String |
| Chave da propriedade | O identificador exclusivo da propriedade. Essa chave é usada no SDK para acessar a propriedade. | `color` |
| Valor | O valor atribuído à propriedade. Deve corresponder ao tipo de propriedade selecionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 3.4: Adicionar propriedades personalizadas (opcional)" }

Quando terminar, selecione **Concluído**.

![A página de propriedades com uma propriedade de string com a chave color e valor #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

#### Etapa 3.5: Personalizar com Connected Content (opcional) {#step-35-personalize-with-connected-content-optional}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

Como os Banners são renderizados de forma inline durante uma atualização de sessão, o Connected Content neste canal funciona de maneira diferente de outros canais:

- Apenas requisições GET são suportadas.
- Todos os posicionamentos em uma única atualização (até 10) compartilham um orçamento de renderização de aproximadamente dois segundos. Se uma chamada for lenta, atingir o tempo limite ou o orçamento for excedido, o resultado do Connected Content para esse posicionamento é tratado como nulo. Os Banners não fazem novas tentativas.

Para melhores resultados:

- Mantenha seus endpoints rápidos e faça [cache das respostas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) sempre que possível.
- Limite o número de URLs exclusivos de Connected Content entre os posicionamentos que renderizam juntos.
- Evite encadear chamadas em que uma resposta de Connected Content determina a URL da próxima. Cada chamada adicional contribui para o orçamento compartilhado.
- Use instruções de proteção Liquid ou o [filtro `default`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) para lidar com resultados nulos e evitar Banners em branco.

### Etapa 4: Construir o restante da sua campanha ou Canvas {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Definir a prioridade do Banner (opcional) {#set-banner-priority-optional}

A [prioridade do Banner]({{site.baseurl}}/user_guide/channels/banners#priority) determina a ordem na qual os Banners são exibidos quando compartilham o mesmo posicionamento. Para definir a prioridade manualmente:

1. Selecione **Set exact priority**.
2. Arraste e solte as campanhas para ordená-las com a prioridade correta.
3. Selecione **Apply Sort**.

{% alert tip %}
Se você tiver várias campanhas de Banner usando o mesmo ID de posicionamento, recomendamos usar o organizador de prioridade de arrastar e soltar para definir a prioridade exata.
{% endalert %}

#### Configurar reelegibilidade (opcional) {#re-eligibility}

Por padrão, usuários que dispensam um Banner nunca são reelegíveis para essa campanha. Para permitir que usuários que dispensaram vejam o Banner novamente, acesse a etapa **Controles de entrega** e selecione **Permitir que os usuários se tornem reelegíveis para receber a campanha**. Quando ativado, defina uma janela de espera em minutos, horas, dias ou semanas.

A contagem regressiva começa quando o usuário dispensa o Banner. Após a janela expirar, o usuário é automaticamente reelegível — sem necessidade de reiniciar a campanha. A reelegibilidade é rastreada por usuário, por campanha.

#### Escolher seu público {#choose-your-audience}

1. Em **Públicos-alvo**, escolha segmentos ou filtros para refinar seu público. Você recebe automaticamente uma prévia da população aproximada do segmento. A associação exata ao segmento é calculada antes do envio da mensagem.

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. Em **Atribuir conversões**, rastreie a frequência com que os usuários realizam ações específicas após receberem uma campanha, definindo eventos de conversão com uma janela de até 30 dias para contar a ação como uma conversão.

#### Escolher eventos de conversão {#choose-conversion-events}

A Braze permite rastrear [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), a frequência com que os usuários realizam ações específicas após receberem uma campanha. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão é contada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não o fez, conclua as seções restantes do seu componente Canvas. Para detalhes sobre como construir o restante do seu Canvas, incluindo testes multivariantes e [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consulte [Construir seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

Para controlar a reelegibilidade para etapas de Banner no Canvas, use as configurações de reentrada do Canvas. Para saber mais, consulte [Reelegibilidade para campanhas e Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

{% endtab %}
{% endtabs %}

### Etapa 5: Testar sua mensagem (opcional) {#step-5-test-your-message-optional}

{% multi_lang_include banners/testing.md page="campaigns" %}

### Etapa 6: Revisar e implantar {#step-6-review-and-deploy}

Após terminar de construir sua campanha ou Canvas, revise os detalhes, [teste-a]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) e envie quando estiver pronto.