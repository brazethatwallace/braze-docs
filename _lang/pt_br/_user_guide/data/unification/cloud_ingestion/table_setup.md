---
nav_title: Configuração de tabela
article_title: Configuração de tabela da Ingestão de dados na nuvem
toc_headers: h2
page_order: 2
page_type: reference
description: "Saiba como configurar sua tabela de origem CDI e como essa configuração difere dos requisitos de formatação de carga útil."
---

# Configuração de tabela da Ingestão de dados na nuvem {#cloud-data-ingestion-table-setup}

> Use esta página para separar dois requisitos relacionados, mas diferentes, da Ingestão de dados na nuvem (CDI): configuração da tabela de origem e formatação de carga útil.

## Entenda a configuração de tabela em comparação com a formatação de carga útil {#understand-table-setup-compared-to-payload-formatting}

Para sincronizações de dados de usuários via CDI, configure ambos:

| Camada | O que ela controla |
| --- | --- |
| Configuração da tabela de origem | Colunas obrigatórias, identificadores de usuário e comportamento de sincronização de `UPDATED_AT` |
| Formatação de carga útil | Campos JSON em `PAYLOAD`, incluindo a estrutura do objeto para atributos, eventos e compras |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entenda a configuração de tabela em comparação com a formatação de carga útil" }

A Braze lê as linhas da sua tabela de origem primeiro e, em seguida, valida o campo `PAYLOAD` com base no tipo de dados selecionado.

## Configure sua tabela de origem {#set-up-your-source-table}

Para sincronizações de dados de usuários via data warehouse, sua tabela ou visualização de origem deve incluir:

- `UPDATED_AT`
- `PAYLOAD`
- Uma ou mais colunas de identificador de usuário compatíveis:
  - `EXTERNAL_ID`
  - `ALIAS_NAME` e `ALIAS_LABEL`
  - `BRAZE_ID`
  - `EMAIL`
  - `PHONE`

Cada linha deve incluir um tipo de identificador por vez, mesmo que sua tabela contenha múltiplas colunas de identificador.

### Requisitos de `UPDATED_AT` {#updated_at-requirements}

- Armazene os valores de `UPDATED_AT` em UTC para evitar problemas com horário de verão.
- A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado.
- Linhas no limite exato do timestamp podem ser ressincronizadas se novas linhas compartilharem esse timestamp.

Para orientações sobre timestamps duplicados e atualizações incrementais, consulte [Práticas recomendadas da Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).

{% alert note %}
Fontes de armazenamento de arquivos usam requisitos de configuração diferentes e não suportam `UPDATED_AT`. Para mais informações, consulte [Integrações de armazenamento de arquivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#required-file-formats).
{% endalert %}

## Configure a coluna `PAYLOAD` {#set-up-the-payload-column}

O valor de `PAYLOAD` segue os mesmos formatos de objeto usados pelo endpoint `/users/track` da Braze para o tipo de dados selecionado.

| Tipo de dados | Referência de formatação |
| --- | --- |
| `attributes` | [Objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens) |
| `events` | [Objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | [Objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configure a coluna PAYLOAD" }

Para atributos aninhados, inclua datas usando o formato descrito em [Capturando datas como propriedades de objeto]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#capturing-dates-as-object-properties).

### Exemplos de carga útil {#payload-examples}

{% tabs local %}
{% tab Atributos personalizados aninhados %}
Você pode incluir atributos personalizados aninhados na coluna de carga útil para uma sincronização de atributos personalizados.

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab Evento %}
Para sincronizar eventos, um nome de evento é obrigatório. Formate o campo `time` como uma string ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Se o campo `time` não estiver presente, a Braze usará o valor da coluna `UPDATED_AT` como o horário do evento. Outros campos, incluindo `app_id` e `properties`, são opcionais.

Você pode sincronizar um evento por linha.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
    }
}
```

{% endtab %}
{% tab Compra %}
Para sincronizar eventos de compra, `product_id`, `currency` e `price` são obrigatórios. Formate o campo opcional `time` como uma string ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Se o campo `time` não estiver presente, a Braze usará o valor da coluna `UPDATED_AT` como o horário do evento. Outros campos, incluindo `app_id`, `quantity` e `properties`, são opcionais.

Você pode sincronizar um evento de compra por linha.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
        ]
    }
}
```

{% endtab %}
{% tab Grupos de inscrições %}
Para sincronizar status de grupos de inscrições, inclua um ou mais pares de `subscription_group_id` e `subscription_state` em cada linha.
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

## Documentação relacionada de configuração CDI {#related-cdi-setup-docs}

- Para exemplos de DDL específicos por fonte, consulte [Integrações de data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).
- Para configuração baseada em arquivos, consulte [Integrações de armazenamento de arquivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).
- Para orientações sobre comportamento de sincronização e otimização, consulte [Práticas recomendadas da Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices).