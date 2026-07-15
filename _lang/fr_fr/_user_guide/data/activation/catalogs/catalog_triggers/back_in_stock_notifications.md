---
nav_title: Notifications de retour en stock
article_title: Configurer les notifications de retour en stock
page_order: 2
description: "Découvrez comment mettre en place des notifications de retour en stock à l'aide de votre catalogue et d'événements personnalisés, afin d'abonner automatiquement les clients à des notifications lorsqu'un article est de nouveau disponible."
---

# Notifications de retour en stock {#back-in-stock-notifications}

> Découvrez comment mettre en place des notifications de retour en stock à l'aide de votre catalogue et d'événements personnalisés, afin d'abonner automatiquement les clients à des notifications lorsqu'un article est de nouveau disponible. Gardez à l'esprit que cela ne s'applique qu'aux utilisateurs ayant déjà accepté de recevoir des notifications.

## Fonctionnement {#how-it-works}

Vous pouvez définir un événement personnalisé à utiliser comme événement d'abonnement, par exemple un événement `product_clicked`. Cet événement doit contenir une propriété correspondant à l'ID de l'article (ID des articles du catalogue). Nous vous recommandons d'inclure un nom de catalogue, mais ce n'est pas obligatoire. Vous devrez également fournir le nom d'un champ de quantité en stock, qui doit être de type numérique.

Notez que le stock d'un article du catalogue doit être à zéro pour qu'un utilisateur puisse s'y abonner avec succès. Lorsqu'un article a une quantité en stock supérieure à zéro, Braze recherche tous les utilisateurs abonnés à cet article et envoie un événement personnalisé que vous pouvez utiliser pour déclencher une Campaign ou un Canvas.

Les propriétés d'événement sont envoyées avec les données de l'utilisateur, ce qui vous permet d'intégrer les détails de l'article dans la Campaign ou le Canvas qui envoie le message.

## Mise en place des notifications de retour en stock {#setting-up-back-in-stock-notifications}

Suivez ces étapes pour configurer les notifications de retour en stock dans un catalogue spécifique.

1. Accédez à votre catalogue et sélectionnez l'onglet **Paramètres**.
2. Activez le basculeur **Back in stock**.
3. Si les paramètres globaux de retour en stock n'ont pas été configurés, vous serez invité à définir les événements personnalisés et les propriétés qui seront utilisés pour déclencher les notifications de retour en stock :
    <br> ![Tiroir des paramètres du catalogue.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Fallback Catalog** : il s'agit du catalogue qui sera utilisé pour l'abonnement aux notifications de retour en stock si aucune propriété `catalog_name` n'est présente dans l'événement personnalisé.
    - **Custom event for subscriptions** : il s'agit de l'événement personnalisé Braze qui sera utilisé pour abonner un utilisateur aux notifications de retour en stock. Lorsque cet événement se produit, l'utilisateur qui l'a déclenché est abonné.
    - **Custom event for unsubscribing** : il s'agit de l'événement personnalisé Braze qui sera utilisé pour désabonner un utilisateur des notifications de retour en stock. Cet événement est facultatif. Si l'utilisateur ne déclenche pas cet événement, il sera désabonné au bout de 90 jours ou lorsque l'événement de retour en stock se déclenchera, selon ce qui se produit en premier.
    - **Item ID event property** : il s'agit de la propriété de l'événement personnalisé mentionné plus haut dans cette section qui sera utilisée pour déterminer l'article concerné par un abonnement ou un désabonnement aux notifications de retour en stock. Cette propriété de l'événement personnalisé doit contenir un ID d'article (`id`) présent dans un catalogue. L'ID de l'article doit être envoyé sous forme de chaîne de caractères afin qu'il corresponde au type de données `id` stocké dans le catalogue cible. L'événement personnalisé doit également contenir une propriété `catalog_name` pour spécifier dans quel catalogue se trouve cet article.

    - Voici un exemple d'événement personnalisé :

```json
{
    "events": [
        {
            "external_id": "<external_id>",
            "name": "subscription",
            "time": "2024-04-15T19:22:28Z",
            "properties": {
                "id": "shirt-xl",
                "catalog_name": "on_sale_products",
                "type": ["back_in_stock"]
            }
        }
    ]
}
```

{% alert note %}
Les déclencheurs de retour en stock et de baisse de prix utilisent le même événement pour abonner l'utilisateur à la notification. Vous pouvez donc utiliser la propriété `type` pour définir à la fois les notifications de baisse de prix et de retour en stock dans le même événement. Notez que la propriété `type` doit être un tableau.
{% endalert %}

{: start="4"}
4. Sélectionnez **Save** et continuez vers la page **Paramètres** du catalogue.
5. Définissez votre règle de notification. Deux options sont disponibles :
    - **Notify all subscribed users** : avertit tous les clients en attente lorsque l'article est de nouveau en stock.
    - **Set notification limits** : notifie un nombre spécifié de clients toutes les 10 minutes. Braze informera le nombre spécifié de clients par incréments jusqu'à ce qu'il n'y ait plus de clients à notifier ou que l'article soit de nouveau en rupture de stock. Votre taux de notification ne peut pas dépasser 10 000 utilisateurs par minute.
6. Définissez le champ **Inventory field in catalog**. Ce champ du catalogue sera utilisé pour déterminer si l'article est en rupture de stock. Le champ doit être de type numérique.
7. Sélectionnez **Save settings**.

![Paramètres du catalogue montrant la fonctionnalité de retour en stock activée. Les règles de notification prévoient d'avertir un millier d'utilisateurs toutes les dix minutes.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
Les règles de notification de ces paramètres ne remplacent pas les paramètres de notification de Canvas, tels que les heures calmes.
{% endalert %}

## Utiliser les notifications de retour en stock dans un Canvas {#using-back-in-stock-notifications-in-a-canvas}

Après avoir configuré la fonctionnalité de retour en stock dans un catalogue, suivez ces étapes pour l'utiliser avec Canvas.

1. Mettez en place un Canvas basé sur l'action.
2. Sélectionnez **Back in stock** comme déclencheur.
3. Sélectionnez le nom du catalogue contenant les notifications de retour en stock.
4. Continuez à [configurer]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) votre Canvas comme vous le feriez habituellement.

Vos clients peuvent désormais être avertis lorsqu'un article est de nouveau en stock.

### Utilisation de Liquid {#using-liquid}

Pour intégrer les détails de l'article du catalogue qui est de nouveau en stock, vous pouvez utiliser l'étiquette Liquid `context` pour accéder à l'`item_id`.

L'utilisation de {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} renvoie l'ID de l'article de nouveau disponible. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} renvoie la valeur d'inventaire de l'article avant la mise à jour, et {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} renvoie la nouvelle valeur d'inventaire après la mise à jour.

Utilisez l'étiquette Liquid {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} en haut de votre message, puis utilisez {%raw%}``{{ items[0].<field_name> }}``{%endraw%} pour accéder aux données relatives à cet article dans l'ensemble du message.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Points à retenir {#considerations}

- Les utilisateurs ne sont abonnés que pour 90 jours. Si l'article n'est pas de nouveau en stock dans les 90 jours, l'utilisateur est désabonné.
- Lorsque vous utilisez la règle de notification **Notify all subscribed users**, Braze notifie 100 000 utilisateurs en 10 minutes.
- Braze prend en charge jusqu'à 50 000 articles mis à jour quotidiennement pouvant déclencher des notifications de retour en stock. Vous pouvez disposer de jusqu'à 100 millions d'abonnements actifs à un moment donné, chaque abonnement représentant un profil utilisateur abonné au suivi d'un article du catalogue.