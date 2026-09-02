---
nav_title: Enregistrer les achats
article_title: Enregistrer les achats pour Windows Universal
platform: Windows Universal
page_order: 4
description: "Cet article de référence explique comment enregistrer les achats sur la plateforme Windows Universal."
hidden: true
---

# Enregistrer les achats {#log-purchases}
{% multi_lang_include archive/windows_deprecation.md %}

Enregistrez les achats in-app afin de pouvoir suivre vos chiffres d'affaires au fil du temps et selon les différentes sources, tout en segmentant vos utilisateurs par leur valeur vie client.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu'USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

Avant le déploiement, assurez-vous de consulter des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans notre article sur les [meilleures pratiques]({{site.baseurl}}/developer_guide/analytics#best-practices). Nous vous recommandons également de vous familiariser avec nos [conventions de nommage des événements]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

Pour utiliser cette fonctionnalité, ajoutez cet appel de méthode après un achat réussi dans votre application :

Les achats sont enregistrés à l'aide de l'`EventLogger`, qui est une propriété exposée dans IAppboy. Pour obtenir une référence à l'`EventLogger`, appelez `Appboy.SharedInstance.EventLogger`.

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## Enregistrer les achats au niveau de la commande {#log-purchases-at-the-order-level}
Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de la commande comme `product_id`. Consultez notre [spécification de l'objet achat]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions) pour en savoir plus.

## REST API

Vous pouvez également utiliser notre REST API pour enregistrer les achats. Reportez-vous à la documentation de l'[API des utilisateurs]({{site.baseurl}}/api/endpoints/user_data) pour plus de détails.