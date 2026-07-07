---
nav_title: Escolha suas features
article_title: Escolha suas features para o Decisioning Studio
page_order: 7
page_type: reference
description: "Este artigo de referência aborda como construir features de clientes eficazes para o BrazeAI Decisioning Studio, incluindo tipos de features, diretrizes gerais, construção de features comportamentais e a relação entre features e o espaço de ações."
---

# Escolha boas features {#choose-good-features}

> O modelo do Decisioning Studio usa features de clientes como entradas para fazer recomendações individualizadas. Features de alta qualidade, bem alinhadas ao seu espaço de decisão, são uma das alavancas de maior impacto para melhorar o desempenho do modelo. Este artigo aborda os tipos de features que você pode fornecer, como construí-las bem e como pensar no alinhamento entre features e as ações entre as quais seu agente escolherá.

Se você tem equipes internas de ciência de dados ou engenharia de dados, elas estão na melhor posição para construir e curar features, já que possuem mais contexto sobre quais sinais nos seus dados são significativos.

{% alert note %}
Para clientes da Braze, as features de clientes são normalmente passadas ao Decisioning Studio por meio de atributos personalizados nos perfis de usuário. Para detalhes sobre atributos personalizados versus eventos personalizados e suas respectivas estratégias de atualização, consulte [Snapshots versus fluxos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams).
{% endalert %}

## Tipos de features de clientes {#types-of-customer-features}

Existem quatro categorias comuns de features de clientes:

| Tipo de feature | O que captura | Exemplos |
|-------------|-----------------|---------|
| **Perfil do usuário** | Fatos objetivos sobre o status do cliente | `age`, `loyalty_tier`, `days_enrolled`, `city`, `acquisition_channel` |
| **Propensão do usuário** | Scores derivados de modelos para a probabilidade do cliente fazer algo | `churn_risk_score`, `purchase_intent_score`, `upsell_affinity` |
| **Comportamental do usuário** | Resumos da atividade do cliente em um período de tempo | `clicks_past_30d`, `purchases_past_7d`, `app_logins_past_14d` |
| **Ambiental** | Sinais contextuais externos ao cliente | `is_promotional_period`, `is_holiday`, `regional_economic_index` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de features de clientes" }

Juntos, esses tipos de features fornecem ao modelo as informações necessárias para identificar segmentos, distinguir entre clientes e adaptar recomendações de acordo.

## Diretrizes gerais {#general-guidelines}

Tenha o seguinte em mente ao selecionar e construir features:

- **Cobertura:** As features devem cobrir todos os clientes no seu público-alvo. Uma feature que está ausente ou nula para uma grande parte do seu público dá ao modelo menos informação para trabalhar com esses clientes.
- **Granularidade:** Todas as features devem ser agregadas no nível do cliente. Consulte [Usar ID externo da Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/braze_external_id) para orientações sobre o que "nível do cliente" significa na prática.
- **Atualidade:** As features devem ser atualizadas em um cronograma baseado em tempo, não em eventos. Consulte [Snapshots versus fluxos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams) para entender por que isso importa.
- **Validade:** Os valores das features devem estar dentro de faixas que façam sentido dada a definição. Uma feature para "compras nos últimos 30 dias" nunca deve ser negativa.
- **Esparsidade:** Evite features que são zero ou nulas para a grande maioria dos clientes, a menos que haja uma razão de negócio clara. Features esparsas adicionam ruído sem adicionar sinal.
- **Correlação:** Evite incluir features que são altamente correlacionadas entre si. Features redundantes podem introduzir viés e desacelerar o treinamento sem melhorar as previsões.

## Construa features comportamentais {#construct-behavioral-features}

Features comportamentais resumem o histórico de ações de um cliente em um período de tempo definido (por exemplo, "número de compras nos últimos 28 dias"). Essas estão entre as features mais valiosas para um sistema de recomendação porque capturam como um cliente realmente se comporta, não apenas características estáticas de perfil.

### Escolha períodos de tempo {#choose-time-windows}

O período de tempo ideal depende da frequência com que os clientes realizam a ação que você está medindo:

- **Períodos curtos (7–28 dias):** Use para atividades de alta frequência, como logins no app, aberturas de e-mail ou visitas ao site.
- **Períodos longos (90–365 dias):** Use para atividades infrequentes, como compras de produtos, renovações de inscrição ou contatos com o atendimento ao cliente.

Um diagnóstico útil: se uma grande porcentagem dos valores da sua feature é zero, o período de tempo provavelmente é curto demais. Amplie-o até observar variância significativa entre os clientes.

### Escolha agregações {#choose-aggregations}

- **Para eventos sem um valor** (algo aconteceu ou não): use agregações de **contagem**. Por exemplo, `email_opens_past_30d`.
- **Para eventos com um valor associado** (receita, duração, quantidade): use agregações de **soma** e **média**. Por exemplo, `purchase_value_sum_past_90d` e `purchase_value_avg_past_90d`. Elas fornecem informações complementares sobre volume total e magnitude por evento.

## Alinhe features com o espaço de ações {#align-features-with-the-action-space}

O Decisioning Studio não é um modelo de propensão; é um sistema de ranqueamento. Seu objetivo é identificar, para cada cliente, qual ação de um conjunto definido de opções tem maior probabilidade de produzir o melhor resultado. Isso cria um requisito específico: **as features devem, sempre que possível, fornecer ao modelo informações que o ajudem a distinguir entre as opções disponíveis para um determinado cliente.**

### Por que isso importa {#why-this-matters}

Por exemplo, suponha que o espaço de ações do seu agente seja recomendar um de três itens do cardápio: café, chá preto ou bubble tea.

Se suas features descrevem clientes em um nível alto ("pede bebidas com frequência" ou "alto engajamento com e-mail"), o modelo pode segmentar clientes em grupos amplos. Mas quando se trata de ranquear café versus bubble tea para um cliente específico, features amplas não ajudam muito. Dois clientes podem parecer idênticos em features de alto nível, mas ter preferências completamente opostas.

Quando o modelo encontra sinais contraditórios — como recomendar café para dois clientes aparentemente semelhantes, mas apenas um converte — ele não consegue aprender de forma eficaz. O ruído reduz sua capacidade de fazer ranqueamentos precisos.

### Construa features que correspondam ao espaço de ações {#build-features-that-match-the-action-space}

Features que mapeiam para a mesma granularidade do seu espaço de ações fornecem ao modelo sinais de ranqueamento muito mais fortes. No exemplo do café, uma feature como `coffee_orders_past_14d` diz diretamente ao modelo se um cliente prefere café. Uma feature como `black_tea_orders_past_14d` faz o mesmo para chá preto. O modelo agora pode tomar uma decisão de ranqueamento bem informada.

Com features alinhadas às ações, o modelo também pode detectar saturação e fadiga. Se um cliente tem um valor alto de `coffee_orders_past_14d`, mas não converteu em uma recomendação recente de café, o modelo aprende que recomendar café novamente pode não ser a melhor escolha e começa a testar alternativas.

### Quando o alinhamento exato não está disponível {#when-exact-alignment-isnt-available}

O alinhamento exato entre feature e ação é o ideal, mas muitas vezes é limitado pela disponibilidade de dados. Duas abordagens podem ajudar quando você não consegue construir features perfeitamente alinhadas:

**Sumarização de dados:** Se você não consegue distinguir entre compras de chá preto e bubble tea, use uma feature agregada `tea_orders_past_14d`. Isso perde alguma precisão, mas ainda ajuda o modelo a distinguir clientes que preferem chá daqueles que preferem café.

**Sinais indiretos:** Features que não estão diretamente no espaço de ações ainda podem ser valiosas se tiverem uma relação lógica com ele. Por exemplo, `dessert_purchased_past_30d` é um proxy razoável para preferência por itens doces, que provavelmente está correlacionada com preferência por bubble tea. O modelo pode aprender com esses sinais indiretos mesmo sem uma correspondência direta de feature.

O princípio subjacente é que informações mais relevantes e granulares sempre ajudam, mas o modelo ainda pode aprender com features imperfeitas. Comece com o que você tem e refine ao longo do tempo conforme mais dados se tornam disponíveis.