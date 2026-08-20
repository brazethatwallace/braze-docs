---
nav_title: Filtrar por intervalo de datas
article_title: Filtrar itens de catálogo por intervalo de datas
page_order: 1
page_type: reference
description: "Use seleções de catálogo com expressões de data em Liquid para exibir itens de catálogo dentro de uma janela de tempo contínua, como eventos nos próximos sete dias."
---

# Filtrar itens de catálogo por intervalo de datas {#filter-catalog-items-by-date-range}

> Este exemplo mostra como um marketplace fictício de ingressos usa seleções de catálogo e expressões de data em Liquid para enviar por e-mail aos consumidores apenas eventos que ocorrerão nos próximos sete dias a partir do momento do envio. Você cria uma seleção com filtros de tempo contínuos e, em seguida, renderiza os itens correspondentes do catálogo em uma Campaign ou mensagem de Canvas.

## Sobre este exemplo {#about-this-example}

MovieCanon, um marketplace fictício de ingressos, usa esse padrão para garantir que as Campaigns de e-mail listem apenas shows e concertos relevantes no tempo.

O padrão usa dois recursos da Braze juntos:

- Uma [seleção de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) com filtros de campo `time` cujos valores são snippets Liquid que calculam uma janela de tempo contínua no momento do envio
- A tag Liquid {% raw %}`{% catalog_selection_items %}`{% endraw %} no corpo da mensagem para renderizar as linhas correspondentes do catálogo

## Considerações {#considerations}

- Crie um campo `time` no catálogo para a coluna de data/hora que você deseja filtrar, não um campo de string. Armazene os valores no formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), como `2026-06-20T19:30:00Z`. Para os tipos compatíveis, consulte [Tipos de dados compatíveis]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types).
- Os operadores `before` e `after` usam comparações estritas. Eventos exatamente iguais a um timestamp limite podem ser excluídos. Use timestamps completos quando precisar que a janela comece no momento do envio. Valores somente de data `YYYY-MM-DD` são convertidos para meia-noite UTC naquele dia.
- O Liquid nos filtros de seleção é avaliado no momento do envio. A variável `'now'` reflete quando a mensagem é renderizada, normalmente em UTC. Confirme se a janela resultante corresponde à sua intenção em diferentes fusos horários.
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), tags de catálogo e `abort_message` não são compatíveis com valores de filtro de seleção de catálogo. Se um filtro incluir uma tag não permitida, a seleção não retorna nenhum item sem gerar um erro.
- Você pode adicionar até 10 filtros por seleção e retornar até 50 itens. Ajuste a janela de sete dias alterando os segundos adicionados a `'now'` (`604800` = 7 dias multiplicados por `86400` segundos por dia).
- Os arrays de resultado de seleção de catálogo são indexados a partir de zero (`items[0]` é o primeiro item).
- Teste o Liquid dos filtros, o Liquid da mensagem e a lógica de interrupção fora do seu espaço de trabalho de produção antes de enviar para públicos de produção.

## Configuração {#setup}

Este exemplo assume um catálogo chamado `live_events` com os seguintes campos:

| Campo | Tipo | Valor de exemplo |
| ----- | ---- | ---------------- |
| `id` | String | `show-1042` |
| `event_name` | String | `Summer Jazz Night` |
| `event_date_time` | Time | `2026-06-20T19:30:00Z` |
| `ticket_price` | Number | `45` |
| `city` | String | `Austin` |
| `venue` | String | `Riverside Amphitheater` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos do catálogo" }

Se você ainda não tem um catálogo semelhante, [crie um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create) e faça upload ou sincronize seus dados de eventos primeiro.

### Etapa 1: Criar a seleção de catálogo {#step-1-create-the-catalog-selection}

1. Acesse **Data Settings** > **Catalogs** e selecione o catálogo `live_events`.
2. Abra a guia **Selection** e selecione **Create Selection**.
3. Nomeie a seleção como `seven_day_window` e adicione uma descrição opcional, como "Eventos que ocorrem nos próximos sete dias."
4. Defina um **Results limit** para o número máximo de eventos a retornar (até 50).
5. Não salve ainda. Adicione os filtros de data nas próximas etapas.

### Etapa 2: Adicionar o filtro de limite superior {#step-2-add-the-upper-bound-filter}

Adicione um filtro no campo `event_date_time`:

| Configuração | Valor |
| ------------ | ----- |
| **Filter field** | `event_date_time` |
| **Operator** | `before` |
| **Value** | Snippet Liquid |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurações do filtro de limite superior" }

No campo de valor do filtro, insira este snippet Liquid. Ele calcula um timestamp sete dias a partir do momento do envio:

{% raw %}
```liquid
{% assign seven_days = 'now' | date: '%s' | plus: 604800 %}{{ seven_days | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

Isso define o limite superior da janela para que apenas eventos antes desse timestamp sejam incluídos.

### Etapa 3: Adicionar o filtro de limite inferior {#step-3-add-the-lower-bound-filter}

Adicione um segundo filtro no mesmo campo:

| Configuração | Valor |
| ------------ | ----- |
| **Filter field** | `event_date_time` |
| **Operator** | `after` |
| **Value** | Snippet Liquid |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurações do filtro de limite inferior" }

Insira este snippet Liquid para o limite inferior. Ele usa o horário atual de envio para que eventos que já começaram sejam excluídos:

{% raw %}
```liquid
{{ 'now' | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

Juntos, os dois filtros retornam itens do catálogo em que `event_date_time` é posterior ao horário atual de envio e anterior a sete dias a partir do horário de envio. Selecione **Create Selection** para salvar.

### Etapa 4: Referenciar a seleção em uma mensagem {#step-4-reference-the-selection-in-a-message}

Na sua Campaign ou mensagem de Canvas, insira o Liquid que busca itens da seleção. Você pode usar **Add personalization** (**Catalog Items** > **Use a selection**) ou colar a tag manualmente:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
Here are some upcoming events:

{{ items[0].event_name }} — ${{ items[0].ticket_price }}
{{ items[0].city }} · {{ items[0].venue }}

{{ items[1].event_name }} — ${{ items[1].ticket_price }}
{{ items[1].city }} · {{ items[1].venue }}
```
{% endraw %}

Substitua os índices de array fixos por um loop se precisar renderizar um número variável de resultados.

### Etapa 5: Lidar com resultados vazios {#step-5-handle-empty-results}

Quando nenhum item do catálogo corresponde à seleção, o array `items` fica vazio e o bloco com a tag não renderiza nada. Para pular o envio ou exibir um conteúdo de fallback, envolva a tag em uma condicional:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
{% if items.size == 0 %}
{% abort_message('Catalog selection returned 0 items') %}
{% endif %}

Here are some upcoming events:
{{ items[0].event_name }}
```
{% endraw %}

Para saber mais, consulte [Interrompendo mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

## Artigos relacionados {#related-articles}

- [Criar um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [Seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Usando catálogos em Campaigns]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Filtro `date` do Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter)
- [Biblioteca de casos de uso do Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)