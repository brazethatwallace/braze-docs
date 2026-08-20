---
nav_title: Dados de usuários
article_title: Dados de usuários na Braze
page_order: 4
layout: dev_guide
guide_top_header: "Dados de usuários na Braze"
guide_top_text: "Antes de concluir a implementação da Braze, certifique-se de ter uma conversa entre a equipe de marketing e a equipe de desenvolvimento sobre suas metas de marketing. É útil considerar essas metas e trabalhar de trás para frente ao decidir quais dados rastrear e como rastrear esses dados com a Braze."

page_type: landing
description: "Esta landing page reúne artigos sobre a coleta de dados de usuários. Aqui, você pode encontrar recursos sobre definições de arquivamento, importação de usuários, o ciclo de vida do perfil de usuário, casos de uso, práticas recomendadas e mais."

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Coleta de dados do SDK
    link: /docs/user_guide/data/unification/user_data/sdk_data_collection
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Ciclo de vida do perfil do usuário
    link: /docs/user_guide/data/unification/user_data/user_profile_lifecycle
    image: /assets/img/braze_icons/refresh-ccw-05.svg
  - name: Caso de uso da coleção
    link: /docs/user_guide/data/unification/user_data/collection_use_case
    image: /assets/img/braze_icons/data.svg
  - name: Práticas recomendadas de coleta
    link: /docs/user_guide/data/unification/user_data/best_practices
    image: /assets/img/braze_icons/thumbs-up.svg
  - name: Importar usuários
    link: /docs/user_guide/audience/manage_audience/import_users
    image: /assets/img/braze_icons/users-01.svg
  - name: Excluir usuários
    link: /docs/user_guide/audience/manage_audience/user_profiles/delete_users
    image: /assets/img/braze_icons/edit-05.svg
  - name: Usuários anônimos
    link: /docs/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users
    image: /assets/img/braze_icons/user-circle.svg
  - name: Códigos de idioma
    link: /docs/user_guide/data/unification/user_data/language_codes
    image: /assets/img/braze_icons/globe-04.svg
---

<br>

{% alert important %}
A Braze bloqueia perfis de usuários ("usuários fictícios") com mais de 5.000.000 de sessões, mais de 20.000 nomes distintos de eventos personalizados ou mais de 20.000 nomes distintos de produtos em compras, pois eles geralmente são resultado de uma integração incorreta. Depois que um perfil é bloqueado, a Braze para de processar todos os dados de entrada desse perfil, tanto dos SDKs quanto da REST API. Se isso acontecer com um usuário legítimo, entre em contato com o gerente da sua conta na Braze.
{% endalert %}

<br>