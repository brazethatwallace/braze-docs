---
nav_title: Landing pages
article_title: Landing pages
page_order: 8
guide_top_header: "Landing pages"
description: "Este artigo contém recursos sobre como criar e personalizar landing pages da Braze."
alias: /landing_pages/
---

# Sobre landing pages {#about-landing-pages}

> As landing pages da Braze são páginas web independentes que podem impulsionar sua estratégia de aquisição e engajamento de usuários.

Use landing pages para expandir seu público, capturar dados de usuários, promover ofertas especiais e dar suporte a campanhas multicanal. Para uma referência dos blocos de arrastar e soltar de landing pages, consulte [Blocos do editor (landing pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

{% alert note %}
A disponibilidade de landing pages e domínios personalizados depende do seu pacote Braze. Entre em contato com seu gerente de conta ou CSM para começar.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Pré-requisitos {#prerequisites}

Antes de poder acessar, criar e publicar landing pages, você precisa ter [permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) de administrador ou todas as permissões a seguir:

- View Landing Pages
- Edit Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Planos disponíveis {#plan-tiers}

O número de landing pages publicadas, domínios personalizados e recursos que você pode usar depende do tipo do seu plano: gratuito ou pro (incremental).

| Recurso                                                                                                   | Plano gratuito     | Plano pro (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Landing pages publicadas                                                                 | Cinco por empresa | 20 adicionais |
| Domínios personalizados          | Um por empresa | Cinco adicionais |
| [Personalização com Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages) | Não disponível | Disponível |
| Campos de formulário pré-preenchidos | Não disponível | Disponível |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Planos disponíveis" }

## Limites de frequência {#rate-limits}

A Braze aplica um limite de frequência de 500 requisições a cada três segundos (aproximadamente 167 requisições por segundo) por espaço de trabalho para landing pages não armazenadas em cache. Esse limite ajuda a manter o desempenho e a confiabilidade do sistema durante períodos de alto tráfego.

Visualizações de landing pages armazenadas em cache não contam para esse limite. Para saber como o cache afeta o tráfego, consulte [As landing pages conseguem lidar com cenários de alto tráfego?](#can-landing-pages-handle-high-traffic-scenarios).

## Adicionando o Google Tag Manager a uma landing page {#adding-google-tag-manager-to-a-landing-page}

Para adicionar o Google Tag Manager às suas landing pages, insira um bloco de **Custom Code** na sua landing page no editor de arrastar e soltar e, em seguida, insira o código do Tag Manager no bloco. Certifique-se de adicionar uma camada de dados antes do código do Tag Manager, como neste exemplo:

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Para mais detalhes sobre a implementação do Google Tag Manager, consulte a [documentação do Google](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

## Perguntas frequentes {#frequently-asked-questions}

### Qual é o tamanho máximo para landing pages? {#whats-the-maximum-size-for-landing-pages}

O corpo da landing page pode ter até 500 KB.

### As landing pages conseguem lidar com cenários de alto tráfego? {#can-landing-pages-handle-high-traffic-scenarios}

Sim. Landing pages não personalizadas lidam com cenários de alto tráfego de forma eficaz. Quando uma landing page é solicitada pela primeira vez, a Braze faz o cache dela pelo Cloudflare. As solicitações subsequentes para o mesmo link são servidas a partir do cache, o que ajuda durante períodos de alto tráfego. Esse cache dura 24 horas, e as visualizações de página em cache não contam para os [limites de frequência](#rate-limits).

Landing pages personalizadas usam um cache do Cloudflare mais curto e geram mais solicitações não cacheadas à Braze. Essas solicitações não cacheadas estão sujeitas ao limite de frequência por espaço de trabalho descrito em [Limites de frequência](#rate-limits).

Para limites de tamanho e outras orientações de desempenho para páginas personalizadas, consulte [Considerações sobre personalização]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#personalization-considerations).

### Existem requisitos técnicos para publicar uma landing page? {#are-there-any-technical-requirements-to-publish-a-landing-page}

Não, não existem requisitos técnicos.

### Existe um editor de HTML para landing pages? {#is-there-an-html-editor-for-landing-pages}

Sim. Use o bloco **Custom Code** no editor de arrastar e soltar para adicionar ou editar HTML. Para interagir com o SDK da Braze a partir do seu código personalizado, consulte [Ponte JavaScript para landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge). Para conectar uma interface totalmente personalizada a um formulário de landing page, consulte [Criar blocos de formulário personalizados]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks).

### Posso usar iframes em landing pages? {#can-i-use-iframes-on-landing-pages}

Sim. Adicione um bloco **Custom Code** no editor de arrastar e soltar e inclua um elemento iframe com a URL do conteúdo que deseja incorporar.

Se o website incorporado restringir o enquadramento por meio de `frame-ancestors` na sua Política de Segurança de Conteúdo (CSP) ou `X-Frame-Options`, a página pode não carregar no iframe. A Braze não pode sobrescrever essas configurações — o site incorporado precisa ser configurado para permitir o domínio da sua landing page.

### Posso criar um webhook dentro de uma landing page? {#can-i-create-a-webhook-inside-a-landing-page}

Não, mas o evento **Submitted a Landing Page form** pode funcionar como um disparador para Canvas ou Campaigns de webhook:

- **Canvas:** Use o evento **Submitted a Landing Page form** como um disparador de entrada do Canvas e adicione uma etapa de webhook.
- **Campaign:** Use o evento **Submitted a Landing Page form** para disparar com base no envio do formulário.

Quando a página não é enviada por um canal da Braze (como por meio de um website ou anúncio), um novo perfil de usuário pode ser criado no envio — mesmo que essa pessoa já exista na Braze. Para lidar com isso, configure um Canvas disparado por **Submitted a Landing Page form** e adicione uma etapa de webhook Braze-para-Braze que chame o endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) para mesclar o novo perfil ao existente.

Quando você usa a Liquid tag `landing_page_url` para compartilhar a página, os envios de formulário são automaticamente vinculados ao perfil de usuário existente. Você pode então referenciar os atributos de usuário enviados na landing page por meio de Liquid para templating subsequente.