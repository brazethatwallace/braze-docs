---
nav_title: Endpoints de API or interface de programação do aplicativo (API) e SDK or kit de desenvolvimento de software
article_title: Endpoints de API or interface de programação do aplicativo (API) e SDK or kit de desenvolvimento de software
page_order: 5
page_type: reference
description: "Consulte a URL correta do dashboard, o endpoint da REST or transferir estado representacional API or interface de programação do aplicativo (API) e o endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software para sua instância da Braze."

---

# Endpoints de API or interface de programação do aplicativo (API) e SDK or kit de desenvolvimento de software {#api-and-sdk-endpoints}

> Consulte a URL correta do dashboard, o endpoint da REST or transferir estado representacional API or interface de programação do aplicativo (API) e o endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software para sua instância da Braze. Você precisa dessas URLs para fazer login, realizar chamadas de API or interface de programação do aplicativo (API) e integrar o SDK or kit de desenvolvimento de software.

A Braze gerencia diversas instâncias diferentes para nosso dashboard, SDK or kit de desenvolvimento de software e endpoints REST or transferir estado representacional, que chamamos de "clusters." Seu gerente de integração da Braze informará em qual cluster você está. Para saber mais sobre o SDK or kit de desenvolvimento de software da Braze, confira o [Braze 101](https://learning.braze.com/braze-101), um curso do Braze Learning.

Fazer login em [dashboard.braze.com](https://dashboard.braze.com) enviará você automaticamente para o endereço correto do cluster.

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

{% alert important %}
Ao integrar seu SDK or kit de desenvolvimento de software, use o endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software. Ao fazer chamadas para nossa REST or transferir estado representacional API or interface de programação do aplicativo (API), use o endpoint REST or transferir estado representacional.
{% endalert %}

Para mais informações sobre como acessar a API or interface de programação do aplicativo (API), consulte nosso [artigo de visão geral da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics).