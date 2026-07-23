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
O Shopify Markets está atualmente em beta. Para saber mais, entre em contato com seu gerente de sucesso do cliente da Braze.
{% endalert %}

## Como a integração funciona {#how-the-integration-works}

O Shopify Markets estende sua integração existente com o Shopify. Conecte sua vitrine padrão por meio do caminho de integração [padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou [personalizado (SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration), e depois selecione os mercados que deseja que a Braze sincronize a partir dos mercados configurados na sua loja. Integrações existentes podem adicionar mercados sem interromper catálogos, grupos de inscrições ou eventos. Para instruções passo a passo, consulte [Configuração do Shopify Markets](#shopify-markets-setup).

O Shopify Markets oferece as seguintes capacidades:

- **Perfis com reconhecimento de mercado.** A integração captura o locale do Shopify de cada usuário junto com os atributos padrão de país e idioma da Braze, para que você possa segmentar e disparar por mercado sem nenhuma configuração personalizada.
- **Catálogos localizados.** Dados de produtos específicos por mercado são sincronizados diariamente: preços, moeda e disponibilidade por mercado, além de títulos, descrições e URLs de produtos traduzidos.
- **Personalização com reconhecimento de mercado.** Use a Liquid tag {% raw %}`{% shopify_market %}`{% endraw %} para personalizar com produtos do catálogo de cada mercado do usuário, incluindo o conteúdo traduzido do Shopify. Você também pode referenciar detalhes do mercado, como a moeda de apresentação, a partir de eventos do Shopify compatíveis como `ecommerce.order_placed`.
- **Fallback para a loja padrão.** Quando um usuário não pertence a nenhum dos seus mercados conectados, a Braze usa as configurações e produtos da sua loja padrão, para que cada usuário receba uma mensagem completa e precisa.

Para exemplos, consulte [Usar dados de usuários de Markets](#use-markets-user-data) e [caso de uso de catálogo com reconhecimento de mercado](#tutorial-show-products-and-prices-per-market).

## Tipos de mercado do Shopify compatíveis {#supported-shopify-market-types}

Durante esta fase do beta, você pode selecionar até 25 mercados de país único na Braze, sujeito às seguintes regras:

- Cada mercado selecionado deve ser um [mercado de país único](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets) ativo. Mercados B2B e de varejo não são compatíveis.
  - A configuração "Usar moedas locais" do Shopify não é compatível
- Um país só pode pertencer a um mercado selecionado.
- Mercados com vários países não são compatíveis nesta fase do beta.

Cada mercado selecionado requer um catálogo de mercado com produtos ativos para que a Braze ofereça suporte:

- Preços específicos por mercado nos produtos, usando a moeda definida no catálogo de mercado
- Disponibilidade de produtos por mercado
- Traduções de produtos feitas por meio do app Shopify Translate & Adapt (como título do produto ou título da variante)

![Perfil de mercado do Shopify para um mercado da Austrália.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### Considerações {#considerations}

#### Geral {#general}

- **Uma loja conectada:** Você pode conectar apenas uma loja Shopify habilitada para Markets a um espaço de trabalho da Braze por vez.
- **Escopo de locale:** Os locales trazem títulos e descrições de produtos traduzidos com base no que você configurou usando o app Shopify Translate & Adapt, além de URLs específicas por locale. Preço, moeda e outros campos compartilhados do catálogo permanecem os mesmos entre locales dentro de um mercado. Por padrão, a Braze usa o [idioma padrão](https://help.shopify.com/en/manual/markets/languages) de cada mercado, o locale principal que o Shopify atribui a esse mercado. Se o suporte expandido a locales estiver ativado para sua conta, a Braze sincroniza locales adicionais configurados para esse mercado.

#### Catálogo de mercado {#market-catalog}

- **Novas visualizações de mercado no seu catálogo original do Shopify:** O Markets não cria catálogos separados. Em vez disso, eles são exibidos como parte do seu catálogo original do Shopify. Os dados de Markets são adicionados como novas linhas de catálogo ao seu catálogo do Shopify.
- **Seleções de catálogo:** Até 30 seleções de catálogo.
- **Tempo de atualização:** Os dados de produtos do catálogo de mercado são atualizados uma vez por dia.
- **Catálogos de mercado somente com preços:** Um catálogo de mercado somente com preços define preços específicos por mercado sem publicar produtos em um canal de vendas. O inventário e a disponibilidade de produtos são sincronizados a partir do catálogo da sua loja padrão, enquanto o preço reflete a lista de preços do catálogo de mercado ou o preço contextual.

### Recursos não compatíveis {#unsupported-features}

Os seguintes recursos não são compatíveis neste beta:

- Disparos de queda de preço e volta ao estoque para catálogos de mercado
- Double opt-in de e-mail e SMS para grupos de inscrições configurados por mercado
- Grupos de mercado aninhados ou fluxos de trabalho de grupo de países além do modelo atual de seleção de país único e vários países
- Seleção de mais de 25 mercados
- Exportação de catálogo para catálogos habilitados para Markets
- Paridade total com a conversão de moeda local do Shopify, regras de arredondamento e comportamento de menor preço em múltiplos catálogos na navegação e no checkout

## Configuração do Shopify Markets {#shopify-markets-setup}

### Etapa 1: Conecte sua loja habilitada para Shopify Markets {#step-1-connect-your-shopify-markets-enabled-store}

1. Conecte sua loja usando a [integração padrão do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou a [integração personalizada do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). Após a conexão da sua loja, configure o Shopify Markets no criador de configuração.
2. Conclua o fluxo OAuth e confirme que a Braze solicita os escopos de mercados no OAuth:
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. Após a autorização ser bem-sucedida e o criador de configuração abrir, selecione **Begin Setup**.
4. Ative os SDKs da Braze.

### Etapa 2: Selecione seu mercado e configurações de dados {#step-2-select-your-market-and-data-settings}

1. Em **Track Shopify Data**, selecione **Sync Shopify Markets data**.
2. Selecione **Select Markets** para escolher seu mercado e certifique-se de que você optou por rastrear eventos comportamentais e atributos de usuário.
   - (Opcional) Ative o preenchimento retroativo de dados históricos

#### Dados de usuários de Markets {#markets-user-data}

Para oferecer suporte ao Shopify Markets, a Braze sincroniza mais dados do que os [eventos e atributos padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events) da integração.

A Braze grava estes contextos de mercado adicionais em cada perfil de usuário:

| Tipo de dado | Valor | Fonte de dados |
| --- | --- | --- |
| Atributo personalizado | `shopify_locale` | Shopify |
| Atributo padrão | idioma do navegador | SDKs da Braze |
| Atributo padrão | país | SDKs da Braze |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipo de dado do perfil de usuário"}

A Braze também coleta as seguintes propriedades adicionais de eventos de pedido para oferecer suporte ao contexto de mercados:

| Tipo de dado | Eventos impactados | Novas propriedades adicionadas |
| --- | --- | --- |
| Eventos recomendados de eCommerce | `ecommerce.order_placed`<br>`ecommerce.order_cancelled`<br>`ecommerce.order_refunded` | `country`, `presentment_currency`, `market_handle` |
| Eventos personalizados | `shopify_paid_order`<br>`shopify_fulfilled_order`<br>`shopify_partially_fulfilled_order` | `country`, `presentment_currency`, `market_handle` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipo de dado de evento de pedido"}

Cada propriedade é derivada das seguintes fontes:

| Propriedade | Fonte de dados |
| --- | --- |
| `country` | `default_address` do cliente Shopify; se indisponível, a Braze usa `shipping_address` |
| `presentment_currency` | Valor monetário de apresentação do Shopify |
| `market_handle` | Mercado do Shopify configurado para o país do pedido; definido apenas quando os mercados estão configurados e o país corresponde |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fontes de dados das propriedades de evento de pedido"}

### Etapa 3: Gerenciar usuários {#step-3-manage-users}

1. Selecione o tipo de `external_id` no menu suspenso.
2. Ative as aceitações de e-mail e SMS do Shopify, o que permite que a Braze sincronize os estados de inscrição de e-mail e SMS do Shopify. Você tem duas opções:
  - **Usar a integração:** A Braze sincroniza os estados de e-mail e SMS. Você só precisa escolher os grupos de inscrições para os quais eles serão sincronizados.
  - **Criar sua própria:** Para mais controle sobre o gerenciamento de estados, você pode criar uma integração personalizada usando os endpoints de grupo de inscrições da Braze.
3. Crie grupos de inscrições padrão para cada país associado aos seus mercados sincronizados durante a configuração.
  - **Nova integração do Shopify:** Atribua um grupo de inscrições padrão de e-mail e SMS por país.
  - **Integração existente do Shopify:** O grupo padrão atual da sua loja para de sincronizar. Atribua novos grupos padrão de e-mail e SMS por país. Sua configuração anterior não é transferida automaticamente.

#### Como funcionam as aceitações e os cancelamentos de inscrição {#how-opt-ins-and-unsubscribes-work}

Durante a configuração, você define grupos de inscrições padrão de e-mail e SMS para cada país associado aos seus mercados sincronizados (até 25 países). Isso é obrigatório antes de salvar a configuração do país. Você também pode atribuir grupos de inscrições adicionais por país se quiser direcionar o consentimento para mais de uma lista.

##### O consentimento se aplica a todos os países configurados {#consent-applies-to-all-configured-countries}

Quando o estado de consentimento de um usuário muda no Shopify, a Braze aplica essa mudança em todos os grupos de inscrições padrão de cada país vinculado à sua loja conectada, não apenas ao país específico do usuário:
  - Se um usuário se torna inscrito no Shopify, ele é inscrito no grupo de inscrições padrão de e-mail ou SMS de cada país que você configurou.
  - Se um usuário cancela a inscrição no Shopify, ele é removido do grupo de inscrições padrão de e-mail ou SMS de cada país que você configurou.

{% alert important %}
O consentimento do Shopify é por loja, não por país. No Shopify, o consentimento é rastreado uma vez para e-mail e uma vez para SMS por registro de cliente, e não inscreve ou cancela inscrição por país ou por tipo de lista. Por isso, a Braze não pode aplicar mudanças de consentimento a um único país ou grupo de inscrições. Um evento de inscrição ou cancelamento de inscrição no Shopify sempre se aplica a todos os grupos de inscrições padrão dos seus países configurados de uma vez. <br><br> Dentro da Braze, no entanto, você pode ter um controle mais granular de aceitações e cancelamentos no nível do grupo de inscrições conforme os usuários interagem com os canais de envio de mensagens.
{% endalert %}

### Etapa 4: Sincronizar produtos {#step-4-sync-products}

1. Para sincronizar produtos dentro do seu mercado, selecione **Sync Shopify products and variants to Braze**.
2. Atribua o **catalog ID** da Braze e defina quaisquer configurações adicionais.

Seu catálogo inclui uma visualização por mercado para os produtos padrão da sua loja. Para cada produto publicado no seu mercado, a Braze adiciona uma linha de mercado ao seu catálogo existente, além dos [campos padrão do catálogo do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data) já compatíveis. Pode levar alguns minutos para a sincronização se você ativar o Shopify Markets em uma integração existente.

Nas linhas de mercado, estes campos possuem valores específicos por mercado:

| Campo | Descrição |
| --- | --- |
| {% raw %}`market_handle`{% endraw %} | Identifica o mercado para a linha. Linhas do mercado padrão usam `default`; mercados adicionais usam seu identificador (por exemplo, `au`). |
| {% raw %}`locale`{% endraw %} | Quando o suporte expandido a locales está ativado, identifica o locale para a linha (por exemplo, `fr`). |
| {% raw %}`price`{% endraw %} | Preço específico do mercado a partir do preço contextual do mercado. |
| {% raw %}`compare_at_price`{% endraw %} | Preço de comparação específico do mercado, ou `0` quando o Shopify não tem preço de comparação para esse mercado. |
| {% raw %}`product_title`{% endraw %} | Título do produto traduzido quando existe uma tradução do Shopify para o locale da linha. |
| {% raw %}`variant_title`{% endraw %} | Título da variante traduzido quando existe uma tradução do Shopify para o locale da linha. |
| {% raw %}`product_url`{% endraw %} | URL da vitrine para o mercado e locale quando URLs localizadas estão ativadas; caso contrário, é a URL padrão do produto em `myshopify.com`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de catálogo de linha de mercado"}

As linhas de mercado usam um `id` composto prefixado com o identificador do mercado, como `<market>_<variant_id>`. Quando o suporte expandido a locales está ativado, o ID também inclui o locale (por exemplo, `<market>_<locale>_<variant_id>`). Seus produtos padrão mantêm seus IDs originais.

### Etapa 5: Ativar canais {#step-5-activate-channels}

1. (Opcional) Escolha se deseja ativar o **envio de mensagens no navegador**.
2. Selecione **Finish Setup**.

## Usar dados de usuários de Markets {#use-markets-user-data}

Depois que esses atributos e propriedades estiverem nos perfis de usuário, você pode usá-los para segmentar usuários por mercado e personalizar mensagens.

### Segmentar por mercado na segmentação {#target-by-market-in-segmentation}

Filtre por país, idioma do navegador ou `shopify_locale` em Segments e nos critérios de entrada de Campaign ou Canvas. Por exemplo, crie um público de usuários em um mercado específico ou divida um Canvas por locale.

### Personalizar e disparar com Liquid {#personalize-and-trigger-with-liquid}

Referencie os dados diretamente nas suas mensagens.

| Dados do usuário para referenciar | Liquid a usar |
| --- | --- |
| O locale do usuário | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| O país do usuário | {% raw %}`{{${country}}}`{% endraw %} |
| O país de um pedido (em uma mensagem disparada) | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| O mercado de um pedido (em uma mensagem disparada) | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| A moeda de um pedido (em uma mensagem disparada) | {% raw %}`{{event_properties.${presentment_currency}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dados do usuário para referenciar com Liquid"}

### Disparar mensagens a partir de atividade de pedidos {#trigger-messages-from-order-activity}

As novas propriedades de pedido acompanham cada evento de pedido, então você pode disparar uma mensagem a partir de um pedido e personalizar o conteúdo usando detalhes com reconhecimento de mercado.

Uma versão simples no corpo da mensagem pode ser assim:

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${presentment_currency}}} {{event_properties.${total_value}}}
```
{% endraw %}

Como as propriedades estão no próprio evento, a mensagem permanece precisa para o mercado de cada usuário sem configuração adicional.

## Tutorial: Exibir produtos e preços por mercado {#tutorial-show-products-and-prices-per-market}

Use um catálogo com reconhecimento de mercado para criar uma única mensagem que exiba para cada usuário os produtos e preços do seu próprio mercado.

1. Crie uma seleção que use dados de mercados.
2. Referencie a seleção em uma mensagem com Liquid.

Você pode usar um mercado fixo quando uma mensagem é direcionada a um mercado específico.

### Etapa 1: Criar uma seleção usando dados de mercados {#step-1-create-a-selection-using-markets-data}

[Seleções]({{site.baseurl}}/catalog_selections) são conjuntos curados de produtos que você referencia em mensagens. Para catálogos do Shopify com mercados sincronizados, a seção **Filter settings** inclui uma área **Market scope** que delimita os dados de produtos a um mercado ou os personaliza por usuário.

1. Acesse seu catálogo do Shopify e abra a guia **Selections**.
2. Selecione **Create Selection**, nomeie a seleção, adicione uma descrição opcional e defina um limite de resultados.
3. Em **Filter settings**, em **Market scope**, use o menu suspenso **Market** para escolher como a seleção resolve produtos específicos por mercado:
   - **Personalized:** Cada destinatário vê produtos e preços do mercado que corresponde ao atributo `country` do seu perfil.
   - **A synced market:** Selecione um mercado pelo nome para fixar a seleção nos produtos e preços desse mercado. Use isso quando uma mensagem é direcionada a um único mercado.
4. Finalize quaisquer critérios de filtro adicionais e salve a seleção.
5. Em **Preview for user**, selecione um usuário para ver o que a seleção retorna para esse perfil. Seleções que usam **Personalized** só podem ser visualizadas após selecionar um usuário.

| Alvo | Filtro |
| --- | --- |
| Um mercado específico | `market_handle` = `au` |
| Somente produtos padrão | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Alvos e filtros associados"}

{% alert note %}
Se você não especificar um mercado, a Braze usa seus produtos padrão.
{% endalert %}

### Etapa 2: Adicionar seleções de catálogo com reconhecimento de mercado às mensagens {#step-2-add-market-aware-catalog-selections-to-messages}

Para servir a cada usuário os produtos do seu próprio mercado em uma única mensagem, crie uma seleção com este filtro:

| Nome da seleção | Campo | Operador | Valor |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | igual a | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | igual a | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Nome da seleção e filtros associados"}

No momento do envio, a Braze substitui {% raw %}`{{shopify_market.handle}}`{% endraw %} pelo mercado de cada usuário, então `market_products` entrega a todos os produtos corretos. `default_products` é o fallback para usuários sem mercado correspondente.

Referencie sua seleção na mensagem com a tag {% raw %}`{% shopify_market %}`{% endraw %}:

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
- Substitua `<your_catalog_name>` pelo seu catálogo e use seus próprios nomes de seleção se forem diferentes.
- A verificação {% raw %}`{{shopify_market.handle}}`{% endraw %} direciona usuários sem mercado correspondente para `default_products`, para que eles ainda recebam produtos em vez de uma mensagem vazia.

Visualize como um usuário no seu mercado para confirmar que a mensagem exibe os produtos, preços e títulos traduzidos desse mercado.