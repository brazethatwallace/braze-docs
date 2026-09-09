---
nav_title: Shopify Markets
article_title: Shopify Markets
description: "Este artigo de referência aborda como configurar e usar a integração do Shopify Markets com a Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_markets/"
hidden: true
---

# Shopify Markets

> Este artigo aborda a integração do Shopify Markets (atualmente em beta), incluindo o que está no escopo, como funciona e como usar os dados de mercados no seu envio de mensagens. A Braze está lançando progressivamente funcionalidades adicionais de Markets ao longo do período de beta, ampliando o suporte para estruturas de mercado mais complexas ao longo do tempo.

{% alert important %}
O Shopify Markets está atualmente em beta. Para saber mais, entre em contato com seu CSM da Braze.
{% endalert %}

## Como funciona a integração {#how-the-integration-works}

O Shopify Markets amplia sua integração existente com o Shopify. Conecte sua loja padrão pela integração [padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou [personalizada (SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration) e, em seguida, selecione os mercados que você deseja que a Braze sincronize a partir dos mercados configurados na sua loja. Integrações existentes podem adicionar mercados sem afetar catálogos, grupos de inscrições ou eventos. Para instruções passo a passo, consulte [Configuração do Shopify Markets](#shopify-markets-setup).

O Shopify Markets oferece os seguintes recursos:

- **Perfis com reconhecimento de mercado:** A integração captura o local do Shopify de cada usuário, juntamente com os atributos padrão de país e idioma da Braze, para que você possa segmentar e disparar por mercado sem nenhuma configuração personalizada.
- **Catálogos localizados:** Os dados de produtos específicos de cada mercado são sincronizados diariamente, incluindo preços e moeda, além de títulos, descrições e URLs de produtos traduzidos.
- **Personalização com reconhecimento de mercado:** Use a Liquid tag {% raw %}`{% shopify_market %}`{% endraw %} para personalizar com produtos do catálogo do mercado de cada usuário, incluindo o conteúdo traduzido do Shopify. Você também pode referenciar detalhes do mercado, como a moeda de apresentação, a partir de eventos do Shopify compatíveis, como `ecommerce.order_placed`.
- **Fallback da loja padrão:** Quando um usuário não pertence a um dos seus mercados conectados, a Braze utiliza as configurações e os produtos da sua loja padrão, garantindo que cada usuário receba uma mensagem completa e precisa.

Para exemplos, consulte [Usar dados de usuários do Markets](#use-markets-user-data) e [Tutorial: Exibir produtos e preços por mercado](#tutorial-show-products-and-prices-per-market).

## Tipos de mercado Shopify compatíveis {#supported-shopify-market-types}

Você pode selecionar até 25 [mercados ativos de um único país ou de vários países](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets). Cada país pode pertencer a apenas um mercado selecionado.

Mercados de sub-região, mercados de varejo, mercados B2B e mercados de canal não são compatíveis.

### O que cada mercado precisa {#what-each-market-needs}

Cada mercado selecionado precisa de um catálogo de mercado com produtos ativos. A Braze lê as seguintes informações desse catálogo:

| Dados | Descrição |
| --- | --- |
| Preços | Definidos no catálogo do mercado, na moeda especificada daquele mercado. A configuração "Use local currencies" do Shopify não é compatível. |
| Traduções | Traduções adaptadas feitas por meio do app Shopify Translate & Adapt, como título do produto e título da variante. Atualmente, a Braze não oferece suporte a configurações de idioma específicas de mercado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="O que cada mercado precisa" }

![Perfil de mercado do Shopify para um mercado da Austrália.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### Considerações {#considerations}

#### Geral {#general}

- **Uma loja conectada:** Você pode conectar apenas uma loja Shopify habilitada para Markets a um espaço de trabalho da Braze por vez.
- **Escopo de localidade:** As localidades importam títulos e descrições de produtos traduzidos com base no que você configurou usando o app Shopify Translate & Adapt, além de URLs específicos de localidade. Preço, moeda e outros campos compartilhados do catálogo permanecem os mesmos entre localidades dentro de um mercado. Por padrão, a Braze usa o [idioma padrão](https://help.shopify.com/en/manual/markets/languages) de cada mercado, a localidade principal que o Shopify atribui a esse mercado. Se você ativar o suporte expandido de localidades, a Braze sincroniza localidades adicionais configuradas para esse mercado.

#### Catálogo de mercado {#market-catalog}

- **Novas visualizações de mercado no seu catálogo Shopify original:** Markets não cria catálogos separados. Em vez disso, a Braze os exibe como parte do seu catálogo Shopify original. Os dados de Markets são adicionados como novas linhas de catálogo ao seu catálogo Shopify.
- **Seleções de catálogo:** Até 30 seleções de catálogo.
- **Tempo de atualização:** Os dados de produtos do catálogo de mercado são atualizados uma vez por dia.
- **Preços de mercado e conteúdo localizado:** As linhas de mercado incluem o preço do mercado e o `compare_at_price`, incluindo títulos de produto e variante localizados e URLs de produto quando as traduções são configuradas por meio do app Shopify Translate & Adapt.
- **Quantidade em estoque:** As linhas de mercado incluem valores de estoque agregados. Atualmente, a Braze não oferece a capacidade de diferenciar o estoque entre locais.
- **Queda de preço:** Compatível com catálogos de mercado. Uma alteração de preço em um catálogo de mercado é disparada com base no preço daquele mercado, e não no preço padrão da sua loja. Como os dados de produtos do catálogo de mercado são atualizados uma vez por dia, as quedas de preço são detectadas diariamente, em vez de quando o preço muda no Shopify.
- **Volta ao estoque:** [Volta ao estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) é compatível com produtos no catálogo padrão da sua loja. As linhas de mercado não disparam notificações de volta ao estoque. A volta ao estoque verifica o estoque total disponível para uma variante de produto em todos os locais do Shopify, então estoque adicionado em um local de varejo pode disparar uma notificação.

## Configuração do Shopify Markets {#shopify-markets-setup}

### Se você já tem uma integração ativa com o Shopify {#if-you-already-have-an-active-shopify-integration}

O Markets complementa sua integração atual. Você não precisa desconectá-la nem refazer sua configuração.

- Seus grupos de inscrições se tornam seus grupos de toda a loja e continuam recebendo todas as aceitações, incluindo quaisquer grupos adicionais que você atribuiu.
- Seus inscritos existentes permanecem nos grupos em que já estão. Se você adicionar grupos de país depois, a Braze não adiciona inscritos existentes a eles.
- Seu catálogo continua sincronizando. As linhas de mercado são adicionadas a ele em vez de a um novo catálogo, e suas seleções existentes continuam funcionando com suas linhas padrão.
- Sua loja padrão aparece junto com os mercados selecionados, permitindo que você atribua grupos de inscrições e crie seleções de catálogo para ela da mesma forma.

Se sua loja já está conectada, comece pela [Etapa 2](#step-2-select-your-market-user-data) para saber mais sobre cada configuração e como ela funciona.

### Etapa 1: Conecte sua loja habilitada para Shopify Markets {#step-1-connect-your-shopify-markets-enabled-store}

1. Conecte sua loja usando a [integração padrão do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou a [integração personalizada do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). Depois que sua loja estiver conectada, configure o Shopify Markets no criador de configuração.
2. Conclua o fluxo OAuth e confirme que a Braze solicita os escopos de mercados no OAuth:
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. Depois que a autorização for bem-sucedida e o criador de configuração abrir, selecione **Begin Setup**.
4. Ative os SDKs da Braze.

### Etapa 2: Selecione os dados de usuários do seu mercado {#step-2-select-your-market-user-data}

1. Em **Track Shopify Data**, selecione **Sync Shopify Markets data**.
2. Selecione **Select Markets** para escolher seu mercado e certifique-se de ter selecionado rastrear eventos comportamentais e atributos de usuários.
   - (Opcional) Ative o preenchimento retroativo de histórico

#### Dados de usuários do Markets {#markets-user-data}

Para oferecer suporte ao Shopify Markets, a Braze sincroniza dados adicionais além dos [eventos e atributos padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events) da integração.

##### Atributos do perfil de usuário {#user-profile-attributes}

| Atributo | Tipo de dados | Descrição | Fonte de dados |
| --- | --- | --- | --- |
| `shopify_locale` | Atributo personalizado | O idioma em que o cliente está navegando na sua loja, como `en` ou `fr-CA`. Ele muda quando o cliente altera o idioma da vitrine. | Localidade do cliente no Shopify |
| `browser_language` | Atributo padrão | O idioma configurado no navegador do cliente. | SDKs da Braze |
| `country` | Atributo padrão | O país do cliente. | SDKs da Braze |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atributos do perfil de usuário"}

##### Propriedades de eventos de pedido {#order-event-properties}

| Propriedade | Descrição | Fonte de dados |
| --- | --- | --- |
| `country` | Código de país de duas letras do cliente. | O `default_address` do cliente no Shopify, ou o `shipping_address` do pedido se nenhum endereço padrão estiver definido |
| `presentment_currency` | A moeda em que o cliente pagou, que pode ser diferente da moeda da sua loja. | Moeda de apresentação do pedido no Shopify |
| `market_handle` | Identificador do mercado correspondente ao país do cliente. Vazio quando nenhum mercado configurado corresponde. | Braze, a partir da sua configuração de mercado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Propriedades de eventos de pedido"}

Essas propriedades são adicionadas a:

- Eventos recomendados de eCommerce: `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`
- Eventos personalizados: `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order`

##### Como funcionam essas propriedades de evento de mercado {#how-these-market-event-properties-work}

| Propriedade | Como funciona |
| --- | --- |
| `market_handle` | `market_handle` é o identificador que você atribuiu ao mercado no Shopify, como `france`. O mesmo identificador prefixa os IDs das linhas de mercado no seu catálogo, como `france_46714756268231`. Ele fica vazio quando você não configurou mercados, ou quando o país do pedido não corresponde a um mercado que você configurou. Verifique se o valor está vazio antes de usá-lo em Liquid ou em um filtro de Segment. |
| `country` | `country` vem do endereço padrão do cliente e usa o `shipping_address` se o padrão não existir. Por exemplo, um cliente na França que envia um pedido para o Japão ainda é associado ao mercado da França. |
| Propriedades de evento | As propriedades de evento são um instantâneo do momento em que o evento ocorreu e não mudam depois. Se um cliente atualizar seu endereço padrão posteriormente, novos eventos usam o novo país, enquanto eventos passados mantêm o país com o qual foram registrados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Como funcionam as propriedades de evento de mercado"}

##### Moeda {#currency}

Eventos de carrinho, checkout e pedido do Shopify que são suportados carregam dois conjuntos de valores:
- A moeda da sua loja nos campos de preço e total existentes, sem alteração
- O objeto `presentment_currency` contendo os valores que o cliente viu e pagou

Use `presentment_currency` quando estiver mostrando ao cliente o que ele pagou, como em uma confirmação de pedido ou uma mensagem de carrinho abandonado. Use os valores na moeda da loja quando estiver comparando receita entre mercados, já que eles já estão em uma moeda única.

##### Informações localizadas do produto {#localized-product-information}

Os eventos do Shopify suportados carregam títulos de produtos e variantes no idioma padrão da sua loja. A Braze não traduz as cargas úteis dos eventos.

Títulos traduzidos, descrições e URLs de produtos ficam nas linhas de mercado do seu catálogo. Para mostrar informações localizadas do produto em uma mensagem, busque o produto no seu catálogo usando o ID do produto ou da variante do evento.

### Etapa 3: Gerenciar usuários {#step-3-manage-users}

1. Selecione o tipo de `external_id` no menu suspenso.
2. Ative as aceitações de e-mail e SMS do Shopify, o que permite que a Braze sincronize os estados de inscrição de e-mail e SMS do Shopify. Você tem duas opções:
   - **Usar a integração:** A Braze sincroniza os estados de e-mail e SMS. Selecione os grupos de inscrições para os quais eles sincronizam.
   - **Criar sua própria:** Para mais controle sobre o gerenciamento de estados, crie uma integração personalizada usando os endpoints de grupo de inscrições da Braze.
3. Selecione os grupos de inscrições para os quais o consentimento do Shopify sincroniza:
   - **Grupos de toda a loja (obrigatório):** Selecione pelo menos um grupo de e-mail e um grupo de SMS. Toda aceitação que a Braze recebe do Shopify é registrada aqui.
   - **Grupos de país (opcional):** Atribua um ou mais grupos a qualquer país nos seus mercados sincronizados. As aceitações também são registradas aqui quando a Braze consegue determinar o país do cliente.

#### Como funcionam as aceitações e recusas {#how-opt-ins-and-opt-outs-work}

No Shopify, cada cliente tem um estado de consentimento de e-mail e um estado de consentimento de SMS. Quando os clientes aceitam, eles se inscrevem na sua marca, não em um país ou uma lista.

A Braze registra cada aceitação nos seus grupos de toda a loja. Se você configurar grupos de país e a Braze conseguir identificar em qual país o cliente está, a aceitação também é registrada nos grupos daquele país.

Se você não configurar grupos de país, as aceitações vão apenas para os seus grupos de toda a loja, o que corresponde à forma como o Shopify lida com o consentimento atualmente.

#### Como a Braze determina o país {#how-braze-determines-country}

| Canal | Determinação do país |
| ------- | ---------------------------- |
| E-mail   | Usa primeiro a localidade do Shopify do cliente; se indisponível, usa o atributo de país no perfil da Braze. |
| SMS     | Usa o país do número de telefone, conforme determinado pelos padrões de roteamento por país E.164. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Determinação de país da Braze por canal"}

Uma localidade identifica um país somente quando inclui uma região, como `fr-FR`. Uma localidade como `fr` sozinha não identifica.

Para SMS, o país vem do número de telefone. O comprador deve ser adicionado a um grupo de inscrições que possa enviar mensagens para aquele número.

#### O que acontece quando alguém aceita {#what-happens-when-someone-opts-in}

| Status do país                           | Grupos de toda a loja | Grupos de país                        |
|------------------------------------------|-------------------|---------------------------------------|
| Determinado e configurado nos seus mercados | Inscrito        | Inscrito nos grupos daquele país   |
| Não pode ser determinado                      | Inscrito        | Não inscrito                        |
| Determinado, mas não configurado nos seus mercados | Inscrito    | Não inscrito                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Resultados de aceitação por status do país"}

A associação ao grupo de inscrições é baseada em eventos de consentimento do Shopify. Se o país ou a localidade de um comprador mudar, a associação ao grupo não muda. A Braze atualiza somente quando o Shopify envia um novo evento de consentimento, como quando o consentimento é coletado novamente do comprador no Shopify após o país ou a localidade ter mudado.

{% alert note %}
Grupos de país controlam consentimento, não idioma. Um país pode ter mais de um idioma. Clientes que falam inglês e francês no Canadá, `en-CA` e `fr-CA`, pertencem ao mesmo grupo de país. Use `shopify_locale` dentro das suas mensagens para especificar o idioma.
{% endalert %}

#### O que acontece quando alguém recusa {#what-happens-when-someone-opts-out}

Uma recusa no Shopify remove o usuário de todos os grupos de inscrições atribuídos à sua integração com o Shopify. Isso é igual independentemente de terem recusado por meio de um site de mercado ou pela página da conta do Shopify.

Grupos de inscrições no seu espaço de trabalho que não estão atribuídos à integração não são afetados.

#### Aceitações de países que você não configurou {#opt-ins-from-countries-you-havent-configured}

Se um cliente aceitar de um país que não faz parte dos seus mercados configurados, seja porque você nunca o adicionou ou porque removeu aquele mercado, ele é inscrito nos seus grupos de toda a loja. Ele não é adicionado a nenhum grupo de país.

Configurar mercados não restringe quem pode receber mensagens. Se você não puder enviar mensagens para um país por motivos legais ou regulatórios, exclua esses usuários com um filtro de Segment ou direcione-os para um grupo de inscrições separado.

{% alert tip %}
Crie esse Segment como uma lista de permissão dos países que você atende, não uma lista de bloqueio dos que não atende. Usuários cujo país não pôde ser determinado não têm valor de país, então uma lista de bloqueio não os capturará.
{% endalert %}

Para SMS, as permissões de país de cada grupo de inscrições ainda controlam a entrega. Um usuário cujo país não é permitido no grupo não receberá mensagens dele.

#### Usuários não são adicionados a grupos de país depois {#users-arent-added-to-country-groups-later}

Se a Braze não conseguir determinar o país de um cliente quando ele aceitar, ele é adicionado apenas aos seus grupos de toda a loja. Se o país dele se tornar conhecido depois, ele não é adicionado automaticamente aos grupos daquele país.

Quando você ativa o Markets em uma loja já integrada, seus grupos de inscrições existentes se tornam seus grupos de toda a loja. Os inscritos existentes permanecem inscritos nesses grupos e não são adicionados automaticamente a novos grupos de país.

Para adicioná-los você mesmo, crie um Segment para esses usuários e inscreva-os usando uma etapa [User Update]({{site.baseurl}}/user_update) do Canvas.

#### Contando inscritos entre grupos {#counting-subscribers-across-groups}

Uma aceitação pode adicionar um usuário a mais de um grupo de inscrições, então somar os totais dos grupos conta a mesma pessoa várias vezes. Use um Segment quando precisar de uma contagem de inscritos únicos.

#### Como funciona {#how-it-works}

1. Um cliente se inscreve para SMS no checkout ou por meio de um formulário.
2. O Shopify envia a inscrição para a Braze.
3. A Braze define o usuário como pendente e envia seu texto de confirmação.
4. O cliente responde com sua palavra-chave de confirmação e se torna inscrito.
5. Se ele não responder antes do fim da janela de confirmação, ele permanece pendente.

Para saber mais, consulte [Double opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in).
### Etapa 4: Sincronizar produtos {#step-4-sync-products}

1. Para sincronizar produtos dentro do seu mercado, selecione **Sync Shopify products and variants to Braze**.
2. Atribua o ID do catálogo da Braze e defina quaisquer configurações adicionais.

Seu catálogo inclui uma visualização por mercado para os produtos padrão da sua loja. Para cada produto publicado no seu mercado, a Braze adiciona uma linha de mercado ao seu catálogo existente, além dos [campos padrão do catálogo do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data) já suportados. Pode levar alguns minutos para que esses dados sincronizem se você ativar o Shopify Markets em uma integração existente.

Nas linhas de mercado, esses campos possuem valores específicos do mercado:

| Campo | Descrição |
| --- | --- |
| `id` | Um ID composto prefixado com o identificador do mercado, como `france_46714756268231`. As linhas padrão mantêm seus IDs de item originais. |
| `market_handle` | O identificador que você atribuiu ao mercado no Shopify, como `france`. |
| `locale` | A localidade do mercado, que determina o idioma do conteúdo traduzido. |
| `price` | Preço específico do mercado a partir da precificação contextual do mercado, após quaisquer ajustes de lista de preços serem aplicados. |
| `compare_at_price` | Preço de comparação específico do mercado após ajustes. A Braze retorna `0` quando nenhum preço de comparação é resolvido para aquele mercado, incluindo quando a lista de preços do mercado está configurada para anular preços de comparação. |
| `product_title` e `variant_title` | Títulos traduzidos, quando as traduções são configuradas por meio do app Shopify Translate & Adapt. |
| `product_url` | A URL do produto para aquele mercado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos do catálogo de linhas de mercado"}

{% alert important %}
`inventory_quantity` não está incluído nas linhas de mercado. Ele aparece somente nas linhas padrão, onde reflete o inventário total disponível para uma variante de produto em todas as localizações do Shopify.<br><br>Quando você usar `compare_at_price` em Liquid, verifique se o valor é "0" antes de exibi-lo ou calcular um desconto. Um mercado sem preço de comparação renderiza um preço zero ou um desconto incorreto.
{% endalert %}

### Etapa 5: Ativar canais {#step-5-activate-channels}

1. (Opcional) Selecione se deseja ativar o envio de mensagens no navegador.
2. Selecione **Finish Setup**.

## Use os dados de usuários de Markets {#use-markets-user-data}

Depois que esses atributos e propriedades estiverem nos perfis de usuário, você pode usá-los para direcionar usuários por mercado e para personalizar mensagens.

### Direcionar por mercado na segmentação {#target-by-market-in-segmentation}

Filtre por país, idioma do navegador ou `shopify_locale` em Segments e nos critérios de entrada de Campaign ou Canvas. Por exemplo, crie um público de usuários em um mercado específico ou divida um Canvas por localidade.

### Disparar e personalizar com Liquid {#trigger-and-personalize-with-liquid}

Referencie dados de mercado nas suas mensagens com estas variáveis Liquid.

#### Do perfil de usuário {#from-the-user-profile}

| Atributo | Liquid |
| --- | --- |
| O idioma do cliente | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| O país do cliente | {% raw %}`{{${country}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variáveis Liquid do perfil de usuário de Markets"}

#### De eventos de pedido {#from-order-events}

| Propriedade do evento | Liquid |
| --- | --- |
| O país do pedido | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| O mercado do pedido | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| A moeda em que o cliente pagou | {% raw %}`{{event_properties.${metadata}.presentment_currency.code}}`{% endraw %} |
| O total do pedido nessa moeda | {% raw %}`{{event_properties.${metadata}.presentment_currency.<total_value>}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variáveis Liquid de eventos de pedido de Markets"}

#### Exibir preços na moeda do cliente {#show-prices-in-the-customers-currency}

Sempre associe um valor ao seu código de moeda. Um valor exibido sozinho é o erro mais comum em mensagens multimercado, porque "129,95" significa algo diferente em cada mercado.

Use o total do pedido para mensagens no nível do pedido, como uma confirmação, e o preço do produto para conteúdos no nível do produto, como um carrinho ou uma recomendação.

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${metadata}.presentment_currency.code}}
{{event_properties.${metadata}.presentment_currency.<total field>}}
```
{% endraw %}

Como essas propriedades acompanham o evento, a mensagem permanece precisa para o mercado de cada cliente sem configuração adicional.

#### Verificar valores vazios {#check-for-empty-values}

Dois valores nem sempre estarão presentes, e ambos são exibidos incorretamente quando estão ausentes.

`market_handle` fica vazio quando o país do cliente não corresponde a um mercado configurado. Verifique antes de criar uma ramificação com base nele:

{% raw %}
```liquid
{% if event_properties.${market_handle} != blank %}
  ...
{% endif %}
```
{% endraw %}

`compare_at_price` retorna `0` quando nenhum preço comparativo é resolvido para aquele mercado. Verifique se é `0` antes de exibi-lo ou calcular um desconto, ou o cliente verá um preço riscado de zero.

#### Exibir informações localizadas do produto {#show-localized-product-information}

Os nomes de produtos nos eventos estão no idioma padrão da sua loja. Para exibir títulos, descrições ou URLs de produtos traduzidos, consulte o produto no seu catálogo usando o ID do produto ou da variante do evento. Para ver um exemplo, consulte [Tutorial: Exibir produtos e preços por mercado](#tutorial-show-products-and-prices-per-market).

### Disparar mensagens a partir da atividade de pedidos {#trigger-messages-from-order-activity}

As propriedades de mercado são incluídas nos eventos Shopify compatíveis, então uma Campaign ou Canvas disparados por um pedido podem usá-las sem configuração adicional. Esses eventos incluem `country`, `presentment_currency` e `market_handle`.

| Tipo de evento | Eventos |
| --- | --- |
| Eventos recomendados de eCommerce | `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded` |
| Eventos personalizados | `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos de pedido Shopify Markets com propriedades de mercado"}

`presentment_currency` tem a cobertura mais ampla em comparação com os outros. Ela é incluída nos eventos compatíveis de carrinho, checkout e pedido, então uma mensagem de carrinho abandonado pode exibir o valor que o cliente viu, mesmo que os eventos de carrinho não contenham `country` ou `market_handle`. Para saber mais, consulte [Moeda](#currency).

## Relatórios de Markets {#markets-reporting}

Quando o Markets está ativado, a Braze detalha a receita e o desempenho das mensagens por país.

### Receita por país {#revenue-by-country}

Seu relatório de receita inclui um detalhamento por país junto com o detalhamento por app, tanto para o período total quanto para um intervalo de tempo selecionado.

Cada pedido é atribuído a um país, e sua receita total é direcionada a esse país. O país é selecionado primeiro a partir do pedido e, em seguida, do perfil do comprador. Pedidos em que nenhum dos dois está disponível aparecem em **Desconhecido**.

A receita é exibida em USD, da mesma forma que o restante do relatório de receita. Para ver o que um comprador realmente pagou, use `presentment_currency` no evento do pedido.

### Desempenho por país {#performance-by-country}

As análises de Campaign e Canvas incluem uma tabela de **Desempenho por país** que mostra como uma mensagem performou em cada país e uma linha de total para cada país. A moeda e a receita total são agregadas a partir do `presentment_currency` do pedido.

| Coluna | O que mostra |
| --- | --- |
| País | Cada país que sua mensagem alcançou. |
| Moeda | A moeda da receita daquele país, agregada pelo presentment_currency. |
| Receita total | Receita atribuída àquele país. |
| Compras | Compras atribuídas àquele país. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="O que cada coluna de desempenho por país mostra"}

## Remover um mercado {#remove-a-market}

Remover um mercado faz com que a Braze pare de sincronizar novos dados para os países desse mercado. Os dados que você já possui não são excluídos.

### Grupos de inscrições {#subscription-groups}

Remover um mercado atualiza sua configuração de Markets. Isso não exclui grupos de inscrições do seu espaço de trabalho nem remove usuários que já estão inscritos em grupos de países.

#### O que muda na sua configuração {#what-changes-in-your-setup}

- Os países do mercado removido não aparecem mais na interface de Markets.
- A Braze remove as atribuições de grupos de inscrições desses países da sua configuração de integração.

#### O que permanece igual {#what-stays-the-same}

- Os grupos de inscrições por país permanecem no seu espaço de trabalho e continuam disponíveis para direcionamento, mas o Shopify não sincroniza mais as desativações para eles. Usuários que optarem por não receber mensagens no Shopify podem continuar aparecendo como inscritos nesses grupos de países, a menos que você atualize o status de inscrição de outra forma — por exemplo, por meio dos [endpoints de grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups) ou de um fluxo de cancelamento de inscrição na Braze.
- Usuários já inscritos nos grupos de países de um mercado removido permanecem inscritos.

#### Sincronização futura de consentimento {#future-consent-sync}

- Novas aceitações de compradores em países removidos são sincronizadas apenas para os grupos gerais da loja, da mesma forma que as [aceitações de países que você não configurou](#opt-ins-from-countries-you-havent-configured).
- A Braze não sincroniza mais novas aceitações ou cancelamentos para os grupos de países removidos.
- Os grupos de inscrições gerais da loja continuam recebendo atualizações de consentimento.

### Dados de usuários {#user-data}

- Os atributos já presentes no perfil de um usuário, incluindo `shopify_locale` e `country`, não são alterados.
- O `market_handle` em novos eventos de pedido não está mais disponível.
- Os filtros de Segment do Shopify Market para mercados removidos não estão mais disponíveis.
- Referências em Liquid a um mercado removido não estão mais disponíveis.

### Catálogos {#catalogs}

- As linhas de mercado correspondentes param de ser atualizadas e são removidas do seu catálogo.
- As seleções de catálogo baseadas nessas linhas de mercado param de retornar produtos. Atualize ou remova essas seleções antes do seu próximo envio.
- Suas linhas padrão, e quaisquer seleções baseadas nelas, não são afetadas.

## Tutorial: Exibir produtos e preços por mercado {#tutorial-show-products-and-prices-per-market}

Use um catálogo com reconhecimento de mercados para criar uma única mensagem que mostre a cada usuário os produtos e preços do seu próprio mercado.

1. Crie uma seleção que usa dados de mercados.
2. Faça referência à seleção em uma mensagem com Liquid.

Você pode usar um mercado fixo quando uma mensagem é direcionada a um mercado específico.

### Etapa 1: Criar uma seleção usando dados de mercados {#step-1-create-a-selection-using-markets-data}

[Seleções]({{site.baseurl}}/catalog_selections) são conjuntos curados de produtos que você referencia em mensagens. Para catálogos Shopify com mercados sincronizados, a seção **Configurações de filtro** inclui uma área **Escopo de mercado** que limita os dados de produtos a um mercado ou os personaliza por usuário.

1. Acesse seu catálogo Shopify e abra a guia **Seleções**.
2. Selecione **Criar seleção**, nomeie a seleção, adicione uma descrição opcional e defina um limite de resultados.
3. Em **Configurações de filtro**, em **Escopo de mercado**, selecione como a seleção resolve produtos específicos de mercado no menu suspenso **Mercado**:
   - **Personalizado:** Cada destinatário vê produtos e preços do mercado que corresponde ao atributo `country` do seu perfil.
   - **Um mercado sincronizado:** Selecione um mercado pelo nome para fixar a seleção nos produtos e preços desse mercado. Use esta opção quando uma mensagem é direcionada a um único mercado.
4. Conclua quaisquer critérios de filtro adicionais e salve a seleção.
5. Em **Prévia para o usuário**, selecione um usuário para ver o que a seleção retorna para aquele perfil. Seleções que usam **Personalizado** só podem ser pré-visualizadas após você selecionar um usuário.

| Alvo | Filtro |
| --- | --- |
| Um mercado específico | `market_handle` = `au` |
| Somente produtos padrão | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Alvos e filtros associados"}

{% alert note %}
Se você não especificar um mercado, a Braze usará seus produtos padrão.
{% endalert %}

### Etapa 2: Adicionar seleções de catálogo com reconhecimento de mercado às mensagens {#step-2-add-market-aware-catalog-selections-to-messages}

Para entregar a cada usuário os produtos do seu próprio mercado em uma única mensagem, crie uma seleção com este filtro:

| Nome da seleção | Campo | Operador | Valor |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Nome da seleção e filtros associados"}

No momento do envio, a Braze substitui {% raw %}`{{shopify_market.handle}}`{% endraw %} pelo mercado de cada usuário, então `market_products` entrega a todos os produtos corretos. `default_products` é o fallback para usuários sem mercado correspondente.

Faça referência à sua seleção na mensagem com a tag {% raw %}`{% shopify_market %}`{% endraw %}:

{% raw %}
```liquid
{% shopify_market %}
{% if shopify_market.handle %}
  {% catalog_selection_items <your_catalog_name> <your_market-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% else %}
  {% catalog_selection_items <your_catalog_name> <your_default-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% endif %}
```
{% endraw %}

- Coloque {% raw %}`{% shopify_market %}`{% endraw %} antes de {% raw %}`{% catalog_selection_items %}`{% endraw %} para que o mercado do usuário seja definido antes da execução da seleção.
- Substitua `<your_catalog_name>` pelo nome do seu catálogo e use os nomes das suas próprias seleções, se forem diferentes.
- A verificação {% raw %}`{{shopify_market.handle}}`{% endraw %} direciona usuários sem mercado correspondente para `default_products`, garantindo que ainda recebam produtos em vez de uma mensagem vazia.
- Ao usar `compare_at_price` em Liquid, verifique se o valor é "0" antes de exibi-lo ou calcular um desconto. Um mercado sem preço de comparação renderiza um preço zero ou produz um desconto incorreto.

Faça a prévia como um usuário no seu mercado para confirmar que a mensagem exibe os produtos, preços e títulos traduzidos desse mercado.