---
nav_title: Pages d'accueil
article_title: Pages d'accueil
page_order: 8
guide_top_header: "Pages d'accueil"
description: "Cet article contient des ressources sur la création et la personnalisation des pages d'accueil Braze."
alias: /landing_pages/
---

# À propos des pages d'accueil {#about-landing-pages}

> Les pages d'accueil Braze sont des pages web autonomes qui peuvent soutenir votre stratégie d'acquisition et d'engagement des utilisateurs.

Utilisez les pages d'accueil pour développer votre audience, capturer des données utilisateur, promouvoir des offres spéciales et soutenir des campagnes multicanales. Pour une référence des blocs glisser-déposer des pages d'accueil, consultez [Blocs éditeur (pages d'accueil)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

{% alert note %}
La disponibilité des pages d'accueil et des domaines personnalisés dépend de votre offre Braze. Contactez votre gestionnaire de compte ou votre gestionnaire du succès des clients pour commencer.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Conditions préalables {#prerequisites}

Avant de pouvoir accéder aux pages d'accueil, les créer et les publier, vous devez disposer des [autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) d'administrateur ou de toutes les autorisations suivantes :

- View Landing Pages
- Edit Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Niveaux d'offre {#plan-tiers}

Le nombre de pages d'accueil publiées, de domaines personnalisés et de fonctionnalités que vous pouvez utiliser dépend de votre type d'offre : gratuite ou payante (incrémentale).

| Fonctionnalité | Offre gratuite | Offre payante (incrémentale) |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Pages d'accueil publiées | Cinq par société | 20 supplémentaires |
| Domaines personnalisés | Un par société | Cinq supplémentaires |
| [Personnalisation Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages) | Non disponible | Disponible |
| Champs de formulaire préremplis | Non disponible | Disponible |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Niveaux d'offre" }

## Ajouter Google Tag Manager à une page d'accueil {#adding-google-tag-manager-to-a-landing-page}

Pour ajouter Google Tag Manager à vos pages d'accueil, ajoutez un bloc **Custom Code** à votre page d'accueil dans l'éditeur par glisser-déposer, puis insérez le code Tag Manager dans le bloc. Veillez à ajouter une couche de données avant le code Tag Manager, comme dans cet exemple :

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

Pour plus de détails sur l'implémentation de Google Tag Manager, consultez la [documentation de Google](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

## Questions fréquemment posées {#frequently-asked-questions}

### Quelle est la taille maximale des pages d'accueil ? {#whats-the-maximum-size-for-landing-pages}

Le corps de la page d'accueil peut atteindre 500 Ko.

### Les pages d'accueil peuvent-elles gérer des scénarios à fort trafic ? {#can-landing-pages-handle-high-traffic-scenarios}

Oui, les pages d'accueil non personnalisées peuvent gérer efficacement des scénarios à fort trafic. Lorsqu'une page d'accueil non personnalisée est demandée pour la première fois, Braze la met en cache via Cloudflare. Cela signifie que toutes les requêtes suivantes pour le même lien sont servies depuis le cache, de sorte que les performances ne sont pas dégradées lors de requêtes à fort volume. Ce cache dure 24 heures, et les pages vues en cache ne sont pas comptabilisées dans les limites de débit.

Pour les pages d'accueil personnalisées (utilisant la personnalisation Liquid), les limites de débit s'appliquent aux requêtes non mises en cache. Pour maintenir des performances optimales, consultez [Considérations relatives à la personnalisation]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#personalization-considerations).

### Y a-t-il des exigences techniques pour publier une page d'accueil ? {#are-there-any-technical-requirements-to-publish-a-landing-page}

Non, il n'y a aucune exigence technique.

### Existe-t-il un éditeur HTML pour les pages d'accueil ? {#is-there-an-html-editor-for-landing-pages}

Oui. Utilisez le bloc **Custom Code** dans l'éditeur par glisser-déposer pour ajouter ou modifier du HTML.

### Puis-je utiliser des iframes sur les pages d'accueil ? {#can-i-use-iframes-on-landing-pages}

Oui. Ajoutez un bloc **Custom Code** dans l'éditeur par glisser-déposer et incluez un élément iframe avec l'URL du contenu que vous souhaitez intégrer.

Si le site web intégré restreint l'encadrement via `frame-ancestors` dans sa politique de sécurité du contenu (CSP) ou `X-Frame-Options`, la page peut ne pas se charger dans l'iframe. Braze ne peut pas contourner ces paramètres — le site intégré doit être configuré pour autoriser le domaine de votre page d'accueil.

### Puis-je créer un webhook à l'intérieur d'une page d'accueil ? {#can-i-create-a-webhook-inside-a-landing-page}

Non, mais l'événement **Submitted a Landing Page form** peut servir de déclencheur pour des Canvas ou des campagnes webhook :

- **Canvas :** utilisez l'événement **Submitted a Landing Page form** comme déclencheur d'entrée dans un Canvas et ajoutez une étape webhook.
- **Campaign :** utilisez l'événement **Submitted a Landing Page form** pour déclencher un envoi en fonction de la soumission du formulaire.

Lorsque la page n'est pas envoyée via un canal Braze (par exemple via un site web ou une publicité), un nouveau profil utilisateur peut être créé lors de la soumission, même si cette personne existe déjà dans Braze. Pour gérer ce cas, configurez un Canvas déclenché par **Submitted a Landing Page form** et ajoutez une étape webhook Braze-to-Braze qui appelle l'endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) pour fusionner le nouveau profil avec le profil existant.

Lorsque vous utilisez l'étiquette Liquid `landing_page_url` pour partager la page, les soumissions de formulaire sont automatiquement associées au profil utilisateur existant. Vous pouvez ensuite référencer les attributs utilisateur soumis sur la page d'accueil via Liquid pour la personnalisation de vos messages suivants.