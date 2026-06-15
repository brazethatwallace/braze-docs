---
nav_title: Endpoints de API e SDK
article_title: Endpoints de API e SDK
page_order: 5
page_type: reference
description: "Consulte a URL correta do dashboard, o endpoint da REST API e o endpoint de SDK para sua instância da Braze."

---

# Endpoints de API e SDK {#api-and-sdk-endpoints}

> Consulte a URL correta do dashboard, o endpoint da REST API e o endpoint de SDK para sua instância da Braze. Você precisa dessas URLs para fazer login, realizar chamadas de API e integrar o SDK.

A Braze gerencia diversas instâncias diferentes para nosso dashboard, SDK e endpoints REST, que chamamos de "clusters." Seu gerente de integração da Braze informará em qual cluster você está. Para saber mais sobre o SDK da Braze, confira o [Braze 101](https://learning.braze.com/braze-101), um curso do Braze Learning.

Fazer login em [dashboard.braze.com](https://dashboard.braze.com) enviará você automaticamente para o endereço correto do cluster.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
Ao integrar seu SDK, use o endpoint de SDK. Ao fazer chamadas para nossa REST API, use o endpoint REST.
{% endalert %}

Para mais informações sobre como acessar a API, consulte nosso [artigo de visão geral da API]({{site.baseurl}}/api/basics/).