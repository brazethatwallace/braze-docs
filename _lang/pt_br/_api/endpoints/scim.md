---
nav_title: SCIM
article_title: Endpoints SCIM
search_tag: Endpoint
page_order: 5
layout: dev_guide
alias: /scim/

description: "Essa landing page lista os endpoints SCIM da Braze."
page_type: landing

guide_top_header: "Endpoints SCIM"
guide_top_text: "A especificação <a href=\"http://www.simplecloud.info/\">System for Cross-domain Identity Management (SCIM)</a> foi criada para facilitar o gerenciamento de identidades de usuários em aplicativos e serviços baseados em nuvem, fornecendo um esquema definido para representar usuários e grupos. Use os endpoints SCIM da Braze para gerenciar o provisionamento automatizado de usuários."

guide_featured_title: ""
guide_featured_list:
  - name: "POST: Criar nova conta de usuário do dashboard"
    link: /docs/post_create_user_account
    image: /assets/img/braze_icons/plus-circle.svg
  - name: "GET: Procurar uma conta de usuário de dashboard existente por ID de recurso"
    link: /docs/get_see_user_account_information
    image: /assets/img/braze_icons/eye.svg
  - name: "GET: Pesquisar conta de usuário existente do dashboard por e-mail"
    link: /docs/api/endpoints/scim/get_search_existing_dashboard_user
    image: /assets/img/braze_icons/eye.svg
  - name: "PUT: Atualizar a conta de usuário do dashboard"
    link: /docs/post_update_existing_user_account
    image: /assets/img/braze_icons/pencil-01.svg
  - name: "DELETE: Remover conta de usuário do dashboard"
    link: /docs/delete_existing_dashboard_user
    image: /assets/img/braze_icons/trash-01.svg
---


{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' subject='endpoints' %}

## Como exportar uma lista de usuários com acesso ao dashboard {#how-to-export-a-list-of-users-with-dashboard-access}

Use este fluxo de trabalho para auditar os usuários que têm acesso ao dashboard da Braze.

1. Baixe o relatório de eventos de segurança em **Configurações** > **Configuração de administrador** > **Configuração de segurança** > **Descarga de evento de segurança**.
2. Extraia os e-mails dos usuários do relatório.
3. Para cada e-mail, use [GET: Pesquisar conta de usuário existente do dashboard por e-mail]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user) para recuperar os detalhes do usuário.
4. Se necessário, use o `id` do recurso retornado com [GET: Procurar uma conta de usuário de dashboard existente]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information) para obter detalhes adicionais do usuário.

Para a lista completa de endpoints SCIM, consulte [Endpoints SCIM]({{site.baseurl}}/api/endpoints/scim). Para saber mais sobre a origem do relatório, consulte [Baixando um relatório de eventos de segurança]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report).