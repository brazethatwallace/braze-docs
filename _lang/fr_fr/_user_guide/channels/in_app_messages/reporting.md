---
nav_title: Rapports
article_title: Rapports sur les messages in-app
page_order: 21
description: "Cet article de référence présente les rapports et analyses des messages in-app, notamment les détails de la campagne, les performances des messages et les performances historiques."
channel:
  - in-app messages
tool:
  - Reports

---

# Rapports sur les messages in-app {#iam-reporting}

> Cet article de référence présente les rapports et analyses des messages in-app, notamment les détails de la campagne, les performances des messages et les performances historiques.

{% multi_lang_include analytics/campaign_analytics.md channel="in-app message" %}

## Indicateurs des messages in-app {#in-app-message-metrics}

Voici les principaux indicateurs des messages in-app que vous pouvez retrouver dans vos analyses. Pour les définitions de tous les indicateurs utilisés dans Braze, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% alert note %}
Pour les messages in-app, cette page définit les impressions uniques en utilisant une limite de jour calendaire dans le fuseau horaire de votre espace de travail.
{% endalert %}

| Terme | Définition |
| --- | --- |
| Impressions uniques | Le nombre total de personnes ayant effectivement vu le message in-app. Si un utilisateur reçoit le message plusieurs fois au cours du même jour calendaire dans le fuseau horaire de votre espace de travail, une seule impression unique est comptabilisée pour ce jour. <br><br> **Si la rééligibilité est activée :** les impressions uniques peuvent s'incrémenter à nouveau lors d'un nouveau jour calendaire dans le fuseau horaire de votre espace de travail si l'utilisateur effectue à nouveau l'action de déclenchement. Pour les messages in-app, *Impressions uniques* est équivalent à *Destinataires uniques*, car les deux s'incrémentent lors d'un nouveau jour calendaire. |
| Impressions totales | Le nombre de fois où le message in-app est affiché. Une impression est enregistrée lorsque le message devient visible à l'écran. Si un utilisateur consulte le message deux fois, il est comptabilisé deux fois. <br><br> **S'il y a plusieurs appareils et que la rééligibilité est désactivée :** l'utilisateur ne voit le message in-app qu'une seule fois. Même s'il utilise plusieurs appareils, il ne le voit que sur le premier appareil ciblé. Cela suppose que le profil a consolidé les appareils et que l'utilisateur est connecté avec un seul ID utilisateur sur tous ses appareils. <br><br> **Si la rééligibilité est activée :** une impression est enregistrée chaque fois que l'utilisateur voit le message in-app. <br><br> **Remarque :** *Impressions totales* comptabilise chaque affichage. *Destinataires uniques* est un indicateur distinct suivi en utilisant une limite de jour calendaire dans le fuseau horaire de votre espace de travail. |
| Conversions | Le suivi des conversions commence après qu'un utilisateur a enregistré une impression d'un message in-app. Une conversion est comptabilisée si l'utilisateur a reçu et vu la campagne de message in-app, puis effectue l'événement de conversion spécifique dans la fenêtre de conversion définie, qu'il ait cliqué ou non sur le message. <br><br> Les conversions sont attribuées au message reçu le plus récemment. Si la rééligibilité est activée, la conversion est attribuée au dernier message in-app reçu, à condition qu'elle se produise dans la fenêtre de conversion définie. Cependant, si une conversion a déjà été attribuée au message in-app, une nouvelle conversion ne peut pas être enregistrée pour ce message spécifique. Cela garantit que chaque distribution de message in-app n'est associée qu'à une seule conversion. |
| Conversions totales | Lorsqu'un utilisateur ne voit une campagne de message in-app qu'une seule fois, une seule conversion est comptabilisée, même s'il effectue l'événement de conversion plusieurs fois par la suite. Cependant, si la rééligibilité est activée et que l'utilisateur voit la campagne de message in-app plusieurs fois, les *Conversions totales* peuvent augmenter d'une unité à chaque fois que l'utilisateur enregistre une impression pour une nouvelle instance de la campagne de message in-app. <br><br> Par exemple, si un utilisateur déclenche un message in-app deux fois et convertit après chaque impression (ce qui donne deux conversions), les *Conversions totales* augmentent de deux. En revanche, s'il n'y a eu qu'une seule impression suivie de deux événements de conversion, une seule conversion est enregistrée et les *Conversions totales* augmentent d'une unité. |
| Taux de conversion | L'indicateur d'impressions uniques quotidiennes (*Impressions uniques*) est utilisé pour calculer le taux de conversion. <br><br> Taux de conversion = (Conversions primaires) / (Impressions uniques) <br><br> Pour les messages in-app, les *Impressions uniques* ne peuvent être comptabilisées qu'une seule fois par jour calendaire dans le fuseau horaire de votre espace de travail. Le nombre de fois qu'un utilisateur effectue une action souhaitée (une « conversion ») peut augmenter au cours de ce même jour calendaire. Par conséquent, si un utilisateur effectue une conversion plusieurs fois dans la même journée, le *Taux de conversion* peut augmenter en conséquence, mais les *Impressions uniques* ne sont comptabilisées qu'une seule fois pour ce jour calendaire. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs des messages in-app" }

{% alert tip %}
Les *Impressions totales* peuvent dépasser les *Impressions uniques* lorsqu'un utilisateur consulte le message plusieurs fois au cours du même jour calendaire (voir les définitions des indicateurs dans le tableau précédent). Pour identifier les utilisateurs présentant un nombre d'impressions anormalement élevé, créez un segment avec le filtre **Nombre d'appareils** défini sur **supérieur à** `1` et le filtre **A reçu un message de la campagne** pour la campagne concernée.
{% endalert %}

### Suivi des clics {#click-tracking}

Braze enregistre une impression lorsqu'un message in-app devient visible à l'écran. Pour les messages in-app créés avec l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), le tableau suivant décrit ce qui est comptabilisé comme un clic.

| Action de l'utilisateur | Clic enregistré |
|-------------|--------------|
| L'utilisateur clique sur le corps du message lorsque le message ne comporte pas de boutons | Oui (clic sur le corps) |
| L'utilisateur clique sur un bouton | Oui (clic sur le bouton) |
| L'utilisateur clique sur le bouton de fermeture (X) | Non |
| L'utilisateur appuie ou clique en dehors du message pour le fermer (lorsque cette option est activée) | Non |
| L'utilisateur ferme l'application pendant que le message est affiché | Non |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Suivi des clics" }

Pour les définitions des clics sur le corps et des clics sur les boutons, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

Pour les déséquilibres d'impressions entre le groupe de contrôle et la variante dans les tests A/B, consultez [Écarts entre le groupe de contrôle et la variante]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#discrepancies-between-the-control-group-and-variant).

## Comment les conversions s'incrémentent-elles avec la rééligibilité ? {#how-do-conversions-increment-with-re-eligibility}

Braze n'attribue qu'une seule conversion à chaque distribution de message in-app et l'attribue au message reçu le plus récemment.

Lorsque la rééligibilité est activée, chaque nouvelle distribution peut générer sa propre conversion. Par exemple, si un utilisateur voit le même message in-app cinq fois et convertit après chaque impression, cinq conversions sont comptabilisées. Si un utilisateur ne voit le message qu'une seule fois mais convertit plusieurs fois par la suite, une seule conversion est comptabilisée.

Si un utilisateur consulte un message in-app sur deux jours distincts mais convertit le troisième jour, Braze enregistre la conversion sur l'impression du deuxième jour. Pour les Canvas, les conversions sont suivies par entrée dans le Canvas, et non par étape. Si un utilisateur convertit sur plusieurs étapes au cours de la même entrée, cela ne compte toujours que comme une seule conversion.

{% tabs local %}
{% tab Scénario 1 %}

*Un utilisateur reçoit le même message in-app cinq fois en une seule journée et convertit cinq fois ce même jour.*

Sarah reçoit un message in-app d'une application de shopping concernant une vente à durée limitée sur sa marque de chaussures préférée. Elle clique sur le message et achète deux paires de chaussures.

Quelques heures plus tard, elle reçoit à nouveau le même message in-app et décide d'acheter une autre paire de chaussures. Cela se produit au total cinq fois en une seule journée, et Sarah finit par effectuer cinq achats distincts, à chaque fois après avoir cliqué sur le message in-app.

**Résultats :** les *Conversions totales* et les *Impressions totales* de Sarah s'incrémentent chacune de cinq pour cette journée. Comme les *Impressions uniques* ne peuvent s'incrémenter à nouveau qu'après une limite de jour calendaire dans le fuseau horaire de l'espace de travail, les *Impressions uniques* restent inchangées. Cela entraîne une augmentation du *Taux de conversion* au cours de cette période.

{% alert note %}
Chaque impression et conversion dans ce scénario est traitée comme un événement SDK distinct. Si votre SDK regroupe une impression et un événement de conversion ensemble, le nombre de conversions peut différer.
{% endalert %}

{% endtab %}
{% tab Scénario 2 %}

*Un utilisateur reçoit un message in-app et convertit en une seule journée.*

Lena reçoit un message in-app concernant un nouveau cours d'apprentissage. Elle clique sur le message et commence le cours. Pendant qu'elle utilise l'application, elle s'inscrit également à quatre autres cours. Tout cela se produit le même jour après avoir reçu un seul message.

**Résultats :** les *Conversions totales* et les *Impressions totales* de Lena s'incrémentent chacune d'une unité.

{% endtab %}
{% tab Scénario 3 %}

*Un utilisateur reçoit un message in-app et convertit le lendemain.*

Tom est un client régulier d'une application d'e-commerce. Il reçoit un message in-app faisant la promotion d'une réduction à durée limitée sur un produit qui l'intéresse. Tom clique sur le message mais décide de ne pas acheter tout de suite. Le lendemain, Tom se souvient de la réduction et effectue l'achat, qui est attribué au message in-app qu'il a reçu la veille.

**Résultats :** les *Conversions totales* et les *Impressions totales* de Tom s'incrémentent chacune d'une unité.

{% endtab %}
{% tab Scénario 4 %}

*Un utilisateur reçoit un message in-app et convertit deux fois le lendemain.*

Alex a récemment téléchargé une application de jeux d'arcade. Un jour, Alex reçoit un message in-app l'encourageant à terminer un niveau dans un nouveau jeu. Alex clique sur le message mais se laisse distraire et ne termine pas de niveau. Le lendemain, Alex termine deux niveaux dans le même jeu.

**Résultats :** comme terminer un niveau est l'événement de conversion, Alex a converti deux fois le deuxième jour. Cependant, comme Alex n'a reçu qu'un seul message in-app, les *Conversions totales* et les *Impressions totales* s'incrémentent chacune d'une unité.

{% endtab %}
{% tab Scénario 5 %}

*Un utilisateur reçoit le même message in-app deux fois en une seule journée et convertit deux fois le lendemain.*

John est un professionnel occupé qui utilise une application de livraison pour commander des repas dans ses restaurants préférés. Pendant son trajet vers le travail, il déclenche un géorepérage et reçoit un message in-app faisant la promotion de restaurants à proximité. En rentrant chez lui plus tard, il reçoit à nouveau le même message car la rééligibilité est activée. Bien qu'il apprécie les offres, il décide de ne rien commander ce jour-là.

Le lendemain, John commande un déjeuner et un dîner via l'application, effectuant l'événement de conversion deux fois.

**Résultats :** les *Conversions totales* de John s'incrémentent d'une unité, et les *Impressions totales* s'incrémentent de deux. Comme la rééligibilité est activée, la conversion est attribuée au dernier message in-app reçu par John (la deuxième impression). Une conversion ne peut être enregistrée qu'une seule fois pour chaque distribution de message in-app.

{% endtab %}
{% endtabs %}