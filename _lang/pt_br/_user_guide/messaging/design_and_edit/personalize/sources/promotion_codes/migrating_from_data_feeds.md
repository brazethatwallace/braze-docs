---
nav_title: Migrar de Data Feeds
article_title: Migrar de Data Feeds para Códigos de promoção
page_order: 10
description: "Este artigo de referência fornece orientações sobre como migrar de Data Feeds para códigos de promoção."
---

# Migrar de Data Feeds para códigos de promoção

{% alert note %}
Data Feeds está sendo descontinuado. A Braze recomenda que os clientes que usam Data Feeds migrem para listas de códigos de promoção.
{% endalert %}

> Esta página orienta você na migração de Data Feeds para códigos de promoção. É um processo simples que envolve criar manualmente listas de códigos de promoção com as informações dos seus Data Feeds e atualizar as referências nas suas mensagens.

## Recursos e funcionalidades

Existem algumas diferenças entre listas de códigos de promoção e Data Feeds.

| Recurso          | Códigos de promoção | Data Feeds   |
|------------------|---------------------|--------------|
| Descrições       | Sim                 | Não          |
| Datas de expiração | Sim               | Não          |
| Método de criação | Fazer upload de um CSV | Colar texto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Como migrar

Para substituir um Data Feed por uma lista de códigos de promoção, faça o seguinte:

1. Acesse **Configurações de dados** e selecione **Criar lista de códigos de promoção**.
2. [Configure sua lista de códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes).
3. Navegue até as mensagens que anteriormente referenciavam o Data Feed e atualize-as para usar a lista de códigos de promoção.