---
nav_title: Pixel de abertura e rastreamento de cliques
article_title: Pixel de abertura e rastreamento de cliques de e-mail
page_order: 9
page_type: reference
description: "Este artigo de referência aborda como implementar o pixel de rastreamento de abertura e o rastreamento de cliques."

---

# Pixel de abertura e rastreamento de cliques de e-mail {#email-open-pixel-and-click-tracking}

> O [rastreamento por pixel de abertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) e o rastreamento de cliques podem ser ativados ou desativados para cada perfil de usuário. Essa flexibilidade ajuda você a seguir as leis regionais de privacidade, nos casos em que um perfil de usuário individual indica que não deseja mais ser rastreado.

## Ativando o pixel de abertura ou o rastreamento de cliques {#turning-on-open-pixel-or-click-tracking}

Ao importar ou atualizar um perfil de usuário por meio de [API]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields), [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) ou [Ingestão de dados na nuvem (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), dois campos estão disponíveis para modificação:

- `email_open_tracking_disabled`: Aceita `true` ou `false`. Defina como `false` para adicionar o pixel de rastreamento de abertura a todos os e-mails futuros enviados a esse usuário. Disponível apenas para SparkPost e SendGrid.
- `email_click_tracking_disabled`: Aceita `true` ou `false`. Defina como `false` para adicionar o rastreamento de cliques a todos os links em e-mails futuros enviados a esse usuário. Disponível apenas para SparkPost e SendGrid.

Para referência, essas informações são exibidas no perfil de usuário nas **Configurações de contato** de e-mail, localizadas na guia **Engajamento**.

![Campos de pixel de rastreamento de abertura e cliques de e-mail na guia Engajamento do perfil de um usuário]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

## Requisitos de links para rastreamento de cliques {#click-tracking-link-requirements}

O rastreamento de cliques da Braze só reescreve links que usam URLs com `http://` ou `https://`. Links que usam outros esquemas, como `mailto:` ou `tel:`, não são rastreados.

Para rastrear cliques em números de telefone ou endereços de e-mail, use uma URL de redirecionamento `https://` que encaminhe para o destino `tel:` ou `mailto:`.