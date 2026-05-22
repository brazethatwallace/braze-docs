---
nav_title: Choisir vos fonctionnalités
article_title: Choisir vos fonctionnalités pour Decisioning Studio
page_order: 7
page_type: reference
description: "Cet article de référence explique comment construire des fonctionnalités client efficaces pour BrazeAI Decisioning Studio, y compris les types de fonctionnalités, les recommandations générales, la construction de fonctionnalités comportementales et la relation entre les fonctionnalités et l'espace d'actions."
---

# Choisir de bonnes fonctionnalités {#choose-good-features}

> Le modèle de Decisioning Studio utilise des fonctionnalités client comme entrées pour formuler des recommandations individualisées. Des fonctionnalités de haute qualité, bien adaptées à votre espace de décision, constituent l'un des leviers les plus efficaces pour améliorer les performances du modèle. Cet article couvre les types de fonctionnalités que vous pouvez fournir, comment les construire correctement et comment aligner les fonctionnalités avec les actions entre lesquelles votre agent devra choisir.

Si vous disposez d'équipes internes de data science ou de data engineering, elles sont les mieux placées pour construire et sélectionner les fonctionnalités, car elles ont le plus de contexte sur les signaux significatifs dans vos données.

{% alert note %}
Pour les clients Braze, les fonctionnalités client sont généralement transmises à Decisioning Studio via des attributs personnalisés sur les profils utilisateur. Pour plus de détails sur les attributs personnalisés par rapport aux événements personnalisés et leurs stratégies de mise à jour respectives, consultez [Instantanés versus flux d'événements]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams/).
{% endalert %}

## Types de fonctionnalités client {#types-of-customer-features}

Il existe quatre catégories courantes de fonctionnalités client :

| Type de fonctionnalité | Ce qu'elle capture | Exemples |
|-------------|-----------------|---------|
| **Profilage utilisateur** | Faits objectifs sur le statut du client | `age`, `loyalty_tier`, `days_enrolled`, `city`, `acquisition_channel` |
| **Propension utilisateur** | Scores dérivés de modèles pour la probabilité qu'un client effectue une action | `churn_risk_score`, `purchase_intent_score`, `upsell_affinity` |
| **Comportement utilisateur** | Résumés de l'activité client sur une fenêtre temporelle | `clicks_past_30d`, `purchases_past_7d`, `app_logins_past_14d` |
| **Environnemental** | Signaux contextuels externes au client | `is_promotional_period`, `is_holiday`, `regional_economic_index` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Types de fonctionnalités client" }

Ensemble, ces types de fonctionnalités fournissent au modèle les informations nécessaires pour identifier des segments, distinguer les clients entre eux et adapter les recommandations en conséquence.

## Recommandations générales {#general-guidelines}

Gardez les points suivants à l'esprit lors de la sélection et de la construction de fonctionnalités :

- **Couverture :** les fonctionnalités doivent couvrir tous les clients de votre audience cible. Une fonctionnalité manquante ou nulle pour une grande partie de votre audience donne moins d'informations au modèle pour ces clients.
- **Granularité :** toutes les fonctionnalités doivent être agrégées au niveau du client. Consultez [Utiliser l'ID externe Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/braze_external_id/) pour comprendre ce que signifie « niveau client » en pratique.
- **Fraîcheur :** les fonctionnalités doivent être mises à jour selon un calendrier temporel, et non en réaction à des événements. Consultez [Instantanés versus flux d'événements]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams/) pour comprendre pourquoi c'est important.
- **Validité :** les valeurs des fonctionnalités doivent se situer dans des plages cohérentes avec leur définition. Une fonctionnalité pour « achats au cours des 30 derniers jours » ne devrait jamais être négative.
- **Parcimonie :** évitez les fonctionnalités qui sont à zéro ou nulles pour la grande majorité des clients, sauf s'il existe une raison métier claire. Les fonctionnalités éparses ajoutent du bruit sans apporter de signal.
- **Corrélation :** évitez d'inclure des fonctionnalités fortement corrélées entre elles. Les fonctionnalités redondantes peuvent introduire des biais et ralentir l'entraînement sans améliorer les prédictions.

## Construire des fonctionnalités comportementales {#construct-behavioral-features}

Les fonctionnalités comportementales résument l'historique des actions d'un client sur une fenêtre temporelle définie (par exemple, « nombre d'achats au cours des 28 derniers jours »). Elles comptent parmi les fonctionnalités les plus précieuses pour un système de recommandation, car elles capturent le comportement réel du client, et pas seulement des caractéristiques de profil statiques.

### Choisir les fenêtres temporelles {#choose-time-windows}

La bonne fenêtre temporelle dépend de la fréquence à laquelle les clients effectuent l'action que vous mesurez :

- **Fenêtres courtes (7 à 28 jours) :** à utiliser pour les activités à haute fréquence telles que les connexions à l'application, les ouvertures d'e-mails ou les visites de site web.
- **Fenêtres longues (90 à 365 jours) :** à utiliser pour les activités peu fréquentes telles que les achats de produits, les renouvellements d'abonnement ou les contacts avec le service client.

Un diagnostic utile : si un pourcentage élevé de vos valeurs de fonctionnalités est à zéro, la fenêtre temporelle est probablement trop courte. Élargissez-la jusqu'à observer une variance significative entre les clients.

### Choisir les agrégations {#choose-aggregations}

- **Pour les événements sans valeur associée** (quelque chose s'est produit ou non) : utilisez des agrégations de type **comptage**. Par exemple, `email_opens_past_30d`.
- **Pour les événements avec une valeur associée** (chiffre d'affaires, durée, quantité) : utilisez à la fois des agrégations de type **somme** et **moyenne**. Par exemple, `purchase_value_sum_past_90d` et `purchase_value_avg_past_90d`. Celles-ci fournissent des informations complémentaires sur le volume total et l'amplitude par événement.

## Aligner les fonctionnalités avec l'espace d'actions {#align-features-with-the-action-space}

Decisioning Studio n'est pas un modèle de propension ; c'est un système de classement. Son objectif est d'identifier, pour chaque client, quelle action parmi un ensemble défini d'options est la plus susceptible de produire le meilleur résultat. Cela crée une exigence spécifique : **les fonctionnalités doivent, dans la mesure du possible, fournir au modèle des informations qui l'aident à distinguer les options disponibles pour un client donné.**

### Pourquoi c'est important {#why-this-matters}

Par exemple, supposons que l'espace d'actions de votre agent consiste à recommander l'un de trois éléments de menu : café, thé noir ou bubble tea.

Si vos fonctionnalités décrivent les clients à un niveau général (« commande fréquemment des boissons » ou « fort engagement par e-mail »), le modèle peut segmenter les clients en groupes larges. Mais lorsqu'il s'agit de classer café versus bubble tea pour un client spécifique, les fonctionnalités générales n'aident pas beaucoup. Deux clients peuvent sembler identiques sur des fonctionnalités de haut niveau tout en ayant des préférences complètement opposées.

Lorsque le modèle rencontre des signaux contradictoires, comme recommander du café à deux clients apparemment similaires alors qu'un seul convertit, il ne peut pas apprendre efficacement. Le bruit réduit sa capacité à produire des classements précis.

### Construire des fonctionnalités alignées avec l'espace d'actions {#build-features-that-match-the-action-space}

Les fonctionnalités qui correspondent à la même granularité que votre espace d'actions donnent au modèle des signaux de classement beaucoup plus forts. Dans l'exemple du café, une fonctionnalité comme `coffee_orders_past_14d` indique directement au modèle si un client préfère le café. Une fonctionnalité comme `black_tea_orders_past_14d` fait de même pour le thé noir. Le modèle peut alors prendre une décision de classement bien informée.

Avec des fonctionnalités alignées sur les actions, le modèle peut également détecter la saturation et la lassitude. Si un client a une valeur élevée pour `coffee_orders_past_14d` mais n'a pas converti lors d'une recommandation récente de café, le modèle apprend que recommander à nouveau du café n'est peut-être pas le meilleur choix et commence à tester des alternatives.

### Quand un alignement exact n'est pas possible {#when-exact-alignment-isnt-available}

L'alignement exact entre fonctionnalités et actions est l'idéal, mais il est souvent limité par la disponibilité des données. Deux approches peuvent aider lorsque vous ne pouvez pas construire des fonctionnalités parfaitement alignées :

**Résumé des données :** si vous ne pouvez pas distinguer les achats de thé noir de ceux de bubble tea, utilisez une fonctionnalité agrégée `tea_orders_past_14d`. Cela perd en précision mais aide tout de même le modèle à distinguer les clients qui préfèrent le thé de ceux qui préfèrent le café.

**Signaux indirects :** les fonctionnalités qui ne sont pas directement dans l'espace d'actions peuvent tout de même être précieuses si elles ont une relation logique avec celui-ci. Par exemple, `dessert_purchased_past_30d` est un indicateur raisonnable de la préférence pour les produits sucrés, qui est probablement corrélée avec la préférence pour le bubble tea. Le modèle peut apprendre de ces signaux indirects même sans correspondance directe avec une fonctionnalité.

Le principe sous-jacent est que des informations plus pertinentes et granulaires sont toujours utiles, mais le modèle peut aussi apprendre à partir de fonctionnalités imparfaites. Commencez avec ce dont vous disposez et affinez au fil du temps à mesure que davantage de données deviennent disponibles.