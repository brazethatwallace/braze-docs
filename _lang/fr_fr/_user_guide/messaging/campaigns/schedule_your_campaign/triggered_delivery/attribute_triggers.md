---
nav_title: Déclencheurs d'attributs
article_title: Déclencheurs d'attributs
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Cet article de référence donne un aperçu des déclencheurs d'attributs et explique comment les utiliser pour envoyer des messages par événement aux utilisateurs."
tool:
  - Campaigns

---

# Déclencheurs d'attributs {#attribute-triggers}

> Les déclencheurs d'attributs vous permettent d'envoyer des messages par événement lorsque le statut d'abonnement ou les valeurs d'attributs personnalisés d'un utilisateur changent.

Les déclencheurs d'attributs sont disponibles pour les scénarios suivants :

- Mises à jour du statut d'abonnement.
- Changement de la valeur d'un attribut personnalisé de type booléen, nombre, chaîne de caractères ou date vers n'importe quelle valeur.
- Changement de la valeur d'un attribut personnalisé de type booléen, nombre ou chaîne de caractères vers une valeur spécifique.

{% alert important %}
Dans le tableau de bord, les attributs de type nombre entier utilisent le type **Number**, et les dates ou horodatages utilisent le type **Time** (ils ne sont pas étiquetés « integer » ou « date » dans l'interface). Les attributs de type **Time** prennent en charge l'option **Change Custom Attribute Value** avec l'option **any new value** uniquement — ils ne prennent pas en charge l'option **specific value**.
{% endalert %}

Pour commencer à utiliser les déclencheurs d'attributs, créez une Campaign ou un composant Canvas et sélectionnez **Livraison par événement** comme méthode de distribution. Ensuite, sélectionnez le déclencheur d'attribut que vous souhaitez utiliser.

![Section « Livraison par événement » avec un menu déroulant pour sélectionner un déclencheur.]({% image_buster /assets/img_archive/trigger_attribute.png %})

## Mettre à jour le statut d'abonnement {#update-subscription-status}

Utilisez le déclencheur `Update Subscription Status` pour cibler les utilisateurs lorsque leur statut d'abonnement est mis à jour.

Par exemple, vous pouvez cibler les utilisateurs lorsque leur statut d'abonnement e-mail ou push passe à « opted in » (inscrit), et les remercier de s'être inscrits. Vous pouvez également envoyer un webhook à vos systèmes chaque fois qu'un utilisateur se désabonne des e-mails, afin que vos systèmes internes disposent des informations les plus récentes sur le statut d'abonnement.

{% alert important %}
Ce déclencheur ne s'applique pas lorsqu'un nouvel utilisateur est créé avec le statut global d'e-mail par défaut `subscribed` et qu'une requête ultérieure met à jour le statut à `subscribed`, car le statut d'abonnement n'a pas changé.
{% endalert %}

## Mettre à jour le statut du groupe d'abonnement {#update-subscription-group-status}

Utilisez le déclencheur `Update Subscription Group Status` pour cibler les utilisateurs lorsque le statut de leur groupe d'abonnement pour l'e-mail, le SMS ou WhatsApp est mis à jour.

Par exemple, vous pouvez cibler les utilisateurs avec un SMS de bienvenue lorsqu'ils s'inscrivent à votre programme. Vous pouvez également spécifier la source de la mise à jour pour un contrôle plus précis du moment où un message est envoyé.

Les sources de mise à jour disponibles varient selon le canal :
- Étape de mise à jour utilisateur Canvas
- Import CSV
- List-Unsubscribe
- Centre de préférences
- REST API
- SDK
- Shopify (e-mail, SMS)
- Message entrant (SMS)

Par exemple, vous pouvez souhaiter envoyer votre SMS de bienvenue uniquement lorsque la mise à jour provient de la REST API et non d'un message entrant, car Braze répond déjà automatiquement à certains SMS entrants.

## Modifier la valeur d'un attribut personnalisé {#change-custom-attribute-value}

Pour le changement d'attribut, le déclencheur est évalué en premier, puis les critères d'audience. Ce comportement diffère du fonctionnement par défaut, où les critères d'audience sont évalués en premier, puis le déclencheur. Pour éviter une condition de concurrence, assurez-vous que l'attribut utilisé comme déclencheur n'est pas le même que celui utilisé pour qualifier votre audience.

### Option « N'importe quelle nouvelle valeur » {#any-new-value-option}

Utilisez le déclencheur `Change Custom Attribute Value` avec l'option `any new value` pour cibler les utilisateurs lorsqu'une valeur de type booléen, nombre, chaîne de caractères ou date change vers n'importe quelle nouvelle valeur.

Par exemple, ciblez les utilisateurs lorsque leur nombre de points de fidélité change pour leur indiquer combien de points ils possèdent désormais. Dans cet exemple, supposons qu'un utilisateur dispose de 85 points de fidélité et que vous avez configuré une Campaign qui se déclenche lorsque l'attribut de points de fidélité change vers n'importe quelle nouvelle valeur. Si la valeur de l'attribut de points de fidélité de cet utilisateur change vers une nouvelle valeur (comme 83, 84, 86, etc.), la Campaign se déclenche.

Prenons un autre cas d'utilisation avec une notification de changement de niveau. Vous pourriez vouloir alerter les utilisateurs si leur niveau de fidélité change. Pour ce faire, configurez une Campaign qui se déclenche sur `Change Custom Attribute Value` et paramétrez-la pour se déclencher lorsque l'attribut personnalisé de niveau de fidélité change vers n'importe quelle nouvelle valeur.

{% alert important %}
Les déclencheurs d'attributs ne sont actuellement pas disponibles pour les attributs de type tableau.
{% endalert %}

![Un déclencheur « Change Custom Attribute Value » pour « AA_current_rewards_tier » changeant vers n'importe quelle valeur.]({% image_buster /assets/img_archive/any_value.png %})

Vous pouvez également utiliser Liquid pour personnaliser le corps du message avec le nouveau niveau de fidélité du client et lui fournir plus d'informations sur le changement.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

### Valeur spécifique {#specific-value}

Utilisez le déclencheur `Change Custom Attribute Value` avec l'option `specific value` pour cibler les utilisateurs lorsqu'un attribut personnalisé de type booléen, nombre ou chaîne de caractères change vers une valeur spécifique.

Par exemple, ciblez les utilisateurs lorsque leur niveau de fidélité passe au meilleur niveau. Dans cet exemple, supposons que le meilleur niveau de fidélité est Super VIP. Vous pouvez configurer une Campaign qui se déclenche lorsque l'attribut personnalisé de niveau de fidélité d'un utilisateur passe à `Super VIP` afin de le féliciter d'être devenu Super VIP.

![Un déclencheur « Change Custom Attribute Value » pour « AA_current_rewards_tier » changeant vers la valeur spécifique « super vip ».]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Les déclencheurs d'attributs pour des valeurs spécifiques d'attributs personnalisés ne sont pas disponibles pour les attributs personnalisés de type tableau et date.
- Le déclencheur de changement de valeur d'attribut personnalisé ne se déclenche pas lorsque la valeur de l'attribut personnalisé est mise à jour à null.
- Le déclencheur de changement de valeur d'attribut personnalisé ne se déclenche que lorsque la valeur d'un attribut personnalisé change réellement. Si la valeur actuelle d'un attribut personnalisé est renvoyée à Braze (par exemple, la valeur de l'attribut couleur préférée est rouge et vous renvoyez la valeur rouge à Braze), le déclencheur ne s'active pas.
- Le déclencheur de changement de valeur d'attribut personnalisé s'applique également aux nouveaux utilisateurs créés.
{% endalert %}