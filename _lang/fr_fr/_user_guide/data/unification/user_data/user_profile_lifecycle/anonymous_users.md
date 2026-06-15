---
nav_title: Utilisateurs anonymes
article_title: Utilisateurs anonymes
page_order: 0
page_type: reference
description: "Cet article donne un aperçu des utilisateurs anonymes et des alias d'utilisateurs, en soulignant leur importance et la manière dont ils peuvent être exploités dans vos messages."

---

# Utilisateurs anonymes {#anonymous-users}

> Les utilisateurs qui visitent votre site web ou votre application sans se connecter, comme un visiteur invité, sont reconnus comme des utilisateurs anonymes. Ces utilisateurs n'ont pas d'`external_ids`, qui sont utilisés pour mettre à jour les profils utilisateurs avec l'API Braze, mais des [points de données]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) leur sont toujours attribués et ils peuvent être ciblés dans vos segments.

Lorsqu'un utilisateur anonyme visite votre site web ou votre application, le SDK de Braze crée et lui affecte un profil utilisateur « anonyme ». Pendant que l'utilisateur navigue, le SDK capture automatiquement des données pour son profil utilisateur anonyme, telles que des informations d'utilisation, des informations sur l'appareil, et plus encore si vous avez configuré des attributs personnalisés et des événements personnalisés.

Vous pouvez effectuer les opérations suivantes avec les utilisateurs anonymes capturés :

- Envoyer des messages aux utilisateurs avant qu'ils ne se connectent
- Collecter le profil d'un utilisateur avant qu'il ne se connecte, afin de ne pas passer à côté de données pertinentes
- Encourager l'utilisateur à compléter son profil en lui envoyant un message lorsqu'il ne le fait que partiellement
- Compléter le profil d'un utilisateur lorsqu'il se connecte, afin de pouvoir annuler l'envoi de messages sur d'autres plateformes (par exemple, ne pas envoyer un message « livraison gratuite sur la 1ère commande de l'app » lorsque l'utilisateur a déjà effectué des commandes sur l'app)
- Engager les utilisateurs qui montrent une intention de sortie en les encourageant à créer un profil, à passer à la caisse ou à effectuer une autre action

## Fonctionnement {#how-it-works}

{% multi_lang_include anonymous_users/about_anonymous_users.md section='user_guide' %}

## Attribution d'alias d'utilisateur {#assigning-user-aliases}

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## Fusionner des utilisateurs anonymes {#merging-anonymous-users}

Parfois, les profils utilisateurs anonymes sont des doublons qui ont le même numéro de téléphone ou la même adresse e-mail que d'autres profils utilisateurs. L'un des doublons peut même être un profil utilisateur identifié. Ces doublons peuvent être fusionnés en un seul profil utilisateur en utilisant l'[endpoint POST : Fusionner des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) ou l'un des outils de fusion de la plateforme Braze, comme la [fusion basée sur des règles]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#rules-based-merging).

## Rechercher un utilisateur anonyme {#looking-up-an-anonymous-user}

Comme les utilisateurs anonymes n'ont pas d'`external_id`, vous pouvez utiliser un identifiant d'appareil pour rechercher un profil spécifique. Les étapes suivantes montrent comment obtenir l'identifiant d'appareil de l'utilisateur actuel dans votre intégration du SDK Web :

1. Ouvrez les outils de développement de votre navigateur (par exemple, dans Chrome, appuyez sur **Commande + Option + J** sur Mac ou **Ctrl + Maj + I** sur Windows).
2. Dans l'onglet **Console**, exécutez la commande suivante :

```javascript
console.log(braze.getDeviceId());
```

{:start="3"}
3. Dans le tableau de bord de Braze, utilisez la [Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/) pour rechercher l'identifiant d'appareil renvoyé.

## Cas d'utilisation {#use-cases}

### Cibler les utilisateurs anonymes dans votre segment {#target-anonymous-users-in-your-segment}

Comme les utilisateurs anonymes n'ont pas d'`external_id`, vous pouvez les cibler en masse en utilisant le filtre de segmentation **External User ID is blank**. Pour plus de précision, vous pouvez ajouter un attribut personnalisé aux utilisateurs anonymes que vous souhaitez cibler et filtrer en conséquence.

Supposons que vous attribuiez l'attribut personnalisé « is_lead_profile » à chaque profil utilisateur anonyme. Vous pourriez cibler ces profils avec l'un de ces filtres ou les deux :

- **External User ID is blank**
- « is_lead_profile » **est vrai**

![Filtres de segmentation pour un identifiant externe vide et un attribut personnalisé « is_lead_profile » défini sur vrai.]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### Capturer les données de paiement d'un utilisateur anonyme {#capture-checkout-data-from-an-anonymous-user}

Vous pouvez capturer les données de paiement d'un utilisateur anonyme (ou d'un visiteur invité) en créant un profil avec alias d'utilisateur au cours du processus de paiement. Lorsqu'un utilisateur anonyme passe à la caisse à l'aide d'un formulaire de capture web, déclenchez un appel API pour créer un profil avec alias d'utilisateur et enregistrer un événement d'achat. Vous pourrez ensuite mettre à jour le profil utilisateur créé via l'API de Braze.

Voici un exemple de payload qui sera généré lorsque le formulaire de capture web sera soumis :

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}