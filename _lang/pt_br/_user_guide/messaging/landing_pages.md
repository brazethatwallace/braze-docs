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

Use landing pages para expandir seu público, capturar dados de usuários, promover ofertas especiais e dar suporte a campanhas multicanal.

{% alert note %}
A disponibilidade de landing pages e domínios personalizados depende do seu pacote Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Pré-requisitos {#prerequisites}

Antes de acessar, criar e publicar landing pages, você precisa ter [permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions) de administrador ou todas as seguintes permissões:

- View Landing Pages
- Edit Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Níveis de plano {#plan-tiers}

O número de landing pages publicadas e domínios personalizados que você pode usar depende do seu tipo de plano: gratuito ou pago (incremental).

| Recurso                                                                                                   | Nível gratuito     | Nível pago (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Landing pages publicadas                                                                 | Cinco por empresa | 20 adicionais |
| Domínios personalizados          | Um por empresa | Cinco adicionais |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Adicionando o Google Tag Manager a uma landing page {#adding-google-tag-manager-to-a-landing-page}

Para adicionar o Google Tag Manager às suas landing pages, adicione um bloco **Custom Code** à sua landing page no editor de arrastar e soltar e insira o código do Tag Manager no bloco. Certifique-se de adicionar uma camada de dados antes do código do Tag Manager, como neste exemplo:

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

### Existem requisitos técnicos para publicar uma landing page? {#are-there-any-technical-requirements-to-publish-a-landing-page}

Não, não há requisitos técnicos.

### Existe um editor de HTML para landing pages? {#is-there-an-html-editor-for-landing-pages}

Sim. Use o bloco **Custom Code** no editor de arrastar e soltar para adicionar ou editar HTML.

### Posso criar um webhook dentro de uma landing page? {#can-i-create-a-webhook-inside-a-landing-page}

Não, isso não é suportado no momento.