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

## Prérequis {#prerequisites}

Avant de pouvoir accéder aux pages de destination, les créer et les publier, vous devez disposer des [autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) d'administrateur ou de toutes les autorisations suivantes :

- View Landing Pages
- Edit Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Niveaux de forfait {#plan-tiers}

Le nombre de pages de destination publiées, de domaines personnalisés et de fonctionnalités que vous pouvez utiliser dépend de votre type de forfait : gratuit ou pro (incrémental).

| Fonctionnalité                                                                                                   | Niveau gratuit     | Niveau pro (incrémental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Pages de destination publiées                                                                 | Cinq par entreprise | 20 supplémentaires |
| Domaines personnalisés          | Un par entreprise | Cinq supplémentaires |
| [Personnalisation Liquid]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages) | Non disponible | Disponible |
| Champs de formulaire préremplis | Non disponible | Disponible |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Niveaux de forfait" }

## Ajouter Google Tag Manager à une page de destination {#adding-google-tag-manager-to-a-landing-page}

Pour ajouter Google Tag Manager à vos pages de destination, ajoutez un bloc **Custom Code** à votre page de destination dans l'éditeur par glisser-déposer, puis insérez le code Tag Manager dans le bloc. Assurez-vous d'ajouter une couche de données avant le code Tag Manager, comme dans cet exemple :

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

## Questions fréquentes {#frequently-asked-questions}

### Quelle est la taille maximale des pages de destination ? {#whats-the-maximum-size-for-landing-pages}

La taille du corps de la page de destination peut atteindre 500 Ko.

### Les pages de destination peuvent-elles gérer des scénarios à fort trafic ? {#can-landing-pages-handle-high-traffic-scenarios}

Oui, les pages de destination non personnalisées peuvent gérer efficacement les scénarios à fort trafic. Lorsqu'une page de destination non personnalisée est demandée pour la première fois, Braze la met en cache via Cloudflare. Cela signifie que toutes les requêtes suivantes pour le même lien sont servies depuis le cache, de sorte que les performances ne sont pas dégradées lors de requêtes à fort volume. Ce cache dure 24 heures, et les pages vues en cache ne sont pas comptabilisées dans les limites de débit.

Pour les pages de destination personnalisées (utilisant la personnalisation Liquid), les limites de débit s'appliquent aux requêtes non mises en cache. Pour maintenir des performances optimales, consultez [Considérations relatives à la personnalisation]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#personalization-considerations).

### Y a-t-il des exigences techniques pour publier une page de destination ? {#are-there-any-technical-requirements-to-publish-a-landing-page}

Non, il n'y a aucune exigence technique.

### Existe-t-il un éditeur HTML pour les pages de destination ? {#is-there-an-html-editor-for-landing-pages}

Oui. Utilisez le bloc **Custom Code** dans l'éditeur par glisser-déposer pour ajouter ou modifier du HTML. Pour interagir avec le SDK Braze depuis votre code personnalisé, consultez [Pont JavaScript pour les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge). Pour connecter une interface utilisateur entièrement personnalisée à un formulaire de page de destination, consultez [Créer des blocs de formulaire personnalisés]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks).

### Puis-je utiliser des iframes sur les pages de destination ? {#can-i-use-iframes-on-landing-pages}

Oui. Ajoutez un bloc **Custom Code** dans l'éditeur par glisser-déposer et incluez un élément iframe avec l'URL du contenu que vous souhaitez intégrer.

Si le site web intégré restreint l'encadrement via `frame-ancestors` dans sa politique de sécurité du contenu (CSP) ou `X-Frame-Options`, la page peut ne pas se charger dans l'iframe. Braze ne peut pas outrepasser ces paramètres — le site intégré doit être configuré pour autoriser le domaine de votre page de destination.

### Puis-je créer un webhook à l'intérieur d'une page de destination ? {#can-i-create-a-webhook-inside-a-landing-page}

Non, mais l'événement **Submitted a Landing Page form** peut servir de déclencheur pour des Canvas ou des Campaigns webhook :

- **Canvas :** Utilisez l'événement **Submitted a Landing Page form** comme déclencheur d'entrée Canvas et ajoutez une étape webhook.
- **Campaign :** Utilisez l'événement **Submitted a Landing Page form** pour déclencher un envoi basé sur la soumission du formulaire.

Lorsque la page n'est pas envoyée via un canal Braze (par exemple via un site web ou une publicité), un nouveau profil utilisateur peut être créé lors de la soumission — même si cette personne existe déjà dans Braze. Pour gérer cela, configurez un Canvas déclenché par **Submitted a Landing Page form** et ajoutez une étape webhook Braze-to-Braze qui appelle l'endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) pour fusionner le nouveau profil avec le profil existant.

Lorsque vous utilisez l'étiquette Liquid `landing_page_url` pour partager la page, les soumissions de formulaire sont automatiquement associées au profil utilisateur existant. Vous pouvez ensuite référencer les attributs utilisateur soumis sur la page de destination via Liquid pour le templating ultérieur.