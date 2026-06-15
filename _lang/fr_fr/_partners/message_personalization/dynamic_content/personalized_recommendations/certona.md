---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "Cet article de référence décrit le partenariat entre Braze et Certona, une solution de personnalisation omnicanal en temps réel qui offre une personnalisation tout au long du cycle de vie du client. Utilisez Certona avec le partenaire Contenu connecté de Braze pour insérer facilement des recommandations de contenu dans les campagnes multicanal."
page_type: partner
search_tag: Partner

---

# Certona

> La plateforme de [Certona](https://www.certona.com/) favorise la personnalisation tout au long du cycle de vie du client. Des campagnes d'e-mail hautement individualisées aux recommandations de produits alimentées par le machine learning, Certona garantit que vous exploitez la puissance de la personnalisation.

_Cette intégration est maintenue par Certona._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Certona utilise les recommandations produit basées sur le machine learning de Certona dans les Campaigns et les Canvas de Braze grâce au Contenu connecté.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| [Compte Certona](https://manage.certona.com/) | Un compte Certona est requis pour profiter de ce partenariat. |
| [Endpoint de l'API REST Certona](https://manage.certona.com/) | Cet endpoint est utilisé directement dans votre message de Campaign Braze pour extraire le contenu recommandé en fonction de l'ID utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration {#integration}

Utilisez l'API REST de Certona pour insérer du contenu personnalisé dans vos messages. Pour ce faire, ajoutez le modèle de Contenu connecté suivant dans votre compositeur de messages Braze avec votre endpoint API REST Certona.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

Ensuite, définissez le contenu que vous souhaitez appeler, tel que le texte ou les images pertinents. Par exemple, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![Image d'une campagne push avec du Contenu connecté lié à Certona inclus dans le corps du message.]({% image_buster /assets/img/certona.png %})

Une fois ce message inséré dans le corps du compositeur, prévisualisez votre appel de Contenu connecté pour vous assurer que les bonnes informations s'affichent.

![Image montrant l'onglet « Test », encourageant les utilisateurs à tester soigneusement leur message avant de l'envoyer.]({% image_buster /assets/img/certona2.png %})