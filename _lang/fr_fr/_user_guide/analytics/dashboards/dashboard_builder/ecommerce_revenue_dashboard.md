---
nav_title: Tableau de bord des revenus eCommerce
article_title: Tableau de bord des revenus eCommerce
alias: "/ecommerce_revenue_dashboard/"
page_order: 1
description: "Cet article présente un aperçu du tableau de bord eCommerce Revenue - Last Touch Attribution."
---

# Tableau de bord des revenus eCommerce {#ecommerce-revenue-dashboard}

> Le tableau de bord **eCommerce Revenue - Last Touch Attribution** suit le chiffre d'affaires attribué au dernier point de contact pour les campagnes et les Canvas à l'aide des [événements recommandés eCommerce]({{site.baseurl}}/ecommerce_events/). Utilisez ce tableau de bord pour identifier les messages qui génèrent du chiffre d'affaires et suivre les performances globales de votre eCommerce au fil du temps.

{% alert note %}
Si vous utilisez le nouveau [connecteur Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), les événements recommandés eCommerce sont automatiquement disponibles via l'intégration. Dans le cas contraire, ces événements doivent être implémentés avant que les données n'apparaissent dans ce tableau de bord.
{% endalert %}

Pour accéder à votre tableau de bord des revenus eCommerce, rendez-vous dans **Analytics** > **Générateur de tableaux de bord**, puis sélectionnez **eCommerce Revenue - Last Touch Attribution**. Ce tableau de bord présente le chiffre d'affaires attribué à la dernière campagne ou au dernier Canvas avec lequel un utilisateur a interagi avant de passer une commande, dans la fenêtre de conversion sélectionnée.

![Tableau de bord eCommerce Revenue - Last Touch Attribution affichant des statistiques pour le chiffre d'affaires eCommerce, les commandes quotidiennes passées et le chiffre d'affaires eCommerce quotidien moyen, ainsi qu'un graphique du chiffre d'affaires eCommerce au fil du temps.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_dashboard.png %})

## Indicateurs disponibles {#available-metrics}

| Indicateur | Définition |
| --- | --- |
| Chiffre d'affaires eCommerce | Chiffre d'affaires total attribué au dernier point de contact, basé sur la plage de dates et la fenêtre de conversion sélectionnées. |
| Commandes quotidiennes passées | Nombre moyen de commandes distinctes passées par jour. |
| Chiffre d'affaires eCommerce quotidien moyen | Chiffre d'affaires moyen attribué par jour pour la période sélectionnée. |
| Chiffre d'affaires eCommerce au fil du temps | Série temporelle du chiffre d'affaires attribué sur la plage de dates sélectionnée. |
| Chiffre d'affaires eCommerce par campagne | Chiffre d'affaires attribué ventilé par campagne. |
| Chiffre d'affaires eCommerce par Canvas | Chiffre d'affaires attribué ventilé par Canvas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Available metrics" }

![Graphiques du chiffre d'affaires eCommerce par campagne et du chiffre d'affaires eCommerce par Canvas.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_charts.png %})

## Modèle d'attribution {#attribution-model}

Le tableau de bord **eCommerce Revenue - Last Touch Attribution** utilise l'attribution au dernier point de contact. Cela signifie que le chiffre d'affaires est attribué à la campagne ou au Canvas Braze le plus récent avec lequel un utilisateur a interagi avant de passer une commande.

Les interactions de message suivantes sont considérées comme des événements de contact pour l'attribution :

- Clic sur un e-mail
- Ouverture d'une notification push
- Clic sur une carte de contenu
- Clic sur un message in-app
- Clic sur un lien court SMS
- Clic sur un lien court WhatsApp

{% alert important %}
Les interactions de message doivent avoir eu lieu dans la fenêtre de conversion sélectionnée. Les commandes sans interaction de message éligible dans la fenêtre de conversion ne sont pas attribuées.
{% endalert %}

## Données incluses {#included-data}

Le tableau de bord **eCommerce Revenue - Last Touch Attribution** exploite les données des événements recommandés eCommerce :

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

{% alert note %}
Pour que les données s'affichent dans le tableau de bord **eCommerce Revenue - Last Touch Attribution**, les valeurs `total_value`, `product.price` et `product.quantity` de l'événement `ecommerce.order_placed` doivent être égales ou supérieures à `0`.
{% endalert %}

Le chiffre d'affaires et le nombre de commandes utilisent les calculs standardisés de Braze.

| Indicateur | Calcul |
| --- | --- |
| Chiffre d'affaires total | Somme des valeurs des commandes passées − Somme des valeurs remboursées |
| Total des commandes | Commandes distinctes passées − Commandes distinctes annulées |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Included data" }

### Données exclues {#excluded-data}

Les achats enregistrés via l'ancien événement d'achat (legacy purchase event) ne sont pas inclus. Le tableau de bord **eCommerce Revenue - Last Touch Attribution** ne prend actuellement pas en charge les fonctionnalités liées aux anciens événements d'achat, telles que le LTV ou le reporting des revenus au sein des campagnes ou des Canvas.

## Gestion des devises {#currency-handling}

Tous les revenus sont affichés en USD. Les devises autres que l'USD sont converties en USD au taux de change en vigueur à la date de l'événement. Pour éviter la conversion, définissez la devise en dur sur `USD` lors de l'envoi des événements.