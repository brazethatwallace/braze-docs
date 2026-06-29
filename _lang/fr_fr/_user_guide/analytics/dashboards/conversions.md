---
nav_title: Conversions
article_title: Tableau de bord des conversions
alias: "/conversions_dashboard_v2/"
description: "Le tableau de bord des conversions vous permet d'analyser les conversions de vos campagnes, Canvas et canaux à l'aide de différentes méthodes d'attribution."
page_order: 3
page_type: reference
tool:
  - Reports
---

# Tableau de bord des conversions {#conversions-dashboard}

> Le tableau de bord des conversions analyse les conversions de vos campagnes, Canvas et canaux à l'aide de différentes [méthodes d'attribution](#attribution-methods). Lors de la mesure de vos conversions, vous pouvez spécifier la période, l'événement de conversion et la fenêtre de conversion.

## Configurer votre rapport {#setting-up-your-report}

Pour configurer votre rapport dans le tableau de bord des conversions :

1. Accédez à **Analytics** > **Conversions**.
2. Sélectionnez une **plage de dates** pour votre rapport, sur une fenêtre allant jusqu'à 90 jours.
3. Sélectionnez les campagnes ou Canvas (ou les deux) à analyser.
   - (facultatif) Filtrez les campagnes et Canvas en sélectionnant une étiquette.
4. Sélectionnez le ou les **canaux** à analyser pour vos messages.
5. Sélectionnez un niveau de **ventilation** pour afficher différentes dimensions de données, par exemple par variante, étape du canvas, pays ou langue.
6. (Facultatif) Si vous souhaitez calculer les conversions d'un événement qui n'a pas été configuré comme événement de conversion dans la campagne ou le Canvas, activez [Utiliser des événements personnalisés](#using-custom-events).
7. Sélectionnez une [méthode d'attribution](#attribution-methods) pour analyser les messages sélectionnés.

{% alert note %}
Si vous analysez les conversions pour plusieurs canaux, votre **méthode d'attribution** sera définie par défaut sur **Attribution au dernier point de contact**.
{% endalert %}

{:start="8"}
8. Sélectionnez **Create** pour générer le rapport.

Une fois la page chargée, sélectionnez un **événement de conversion** pour filtrer le rapport sur les données de conversion. Les sélections disponibles incluent les événements préconfigurés dans les Canvas et campagnes. Si vous avez sélectionné un événement personnalisé lors de la configuration de votre rapport (étape 6), cette option n'est pas disponible.

### Utiliser des événements personnalisés {#using-custom-events}

Pour que les indicateurs d'événements personnalisés apparaissent dans le tableau de bord des conversions, vous devez disposer d'un événement de conversion et d'un événement d'entrée dans le Canvas dans la plage de dates spécifiée sur la page.

Pour calculer les conversions d'un événement qui n'a pas été configuré comme événement de conversion dans la campagne ou le Canvas, sélectionnez un événement personnalisé spécifique à utiliser comme événement de conversion.

1. Lors de la configuration de votre rapport, activez **Use custom events**.
2. Sélectionnez un événement personnalisé à utiliser comme événement de conversion.
3. Sélectionnez la fenêtre de conversion au cours de laquelle cet événement doit avoir eu lieu pour être comptabilisé comme une conversion.

{% alert note %}
Si vous sélectionnez un événement personnalisé, le menu déroulant **Conversion Event** ne s'affichera pas sur la page et vous devrez relancer le rapport pour consulter les conversions d'autres événements personnalisés.
{% endalert %}

### Points à prendre en compte {#considerations}

Pour qu'un utilisateur soit comptabilisé dans le rapport, il doit remplir les critères suivants au cours de la plage de dates sélectionnée :
1. Entrer dans le Canvas ou la campagne.
2. Enregistrer une [méthode d'attribution]({{site.baseurl}}/user_guide/analytics/dashboards/conversions/#attribution-methods).
3. Réaliser l'événement de conversion.

Par exemple, imaginons qu'un utilisateur effectue les actions suivantes :
1. Il entre dans le Canvas le 30 septembre.
2. Il enregistre une méthode d'attribution le 1er octobre.
3. Il réalise l'événement de conversion le 2 octobre.

Cet utilisateur **n'apparaîtra pas** dans un rapport dont la plage de dates va du 1er au 7 octobre. En effet, l'utilisateur est entré dans le Canvas avant la période du rapport, même si l'événement de conversion a eu lieu dans la plage de dates définie. Pour que l'utilisateur apparaisse dans le rapport, la plage de dates doit inclure le 30 septembre.

## Comprendre votre rapport {#understanding-your-report}

Votre rapport est divisé en trois sections :

- [Détails des conversions](#conversion-details)
- [Tunnel de conversion](#conversion-funnel)
- [Conversions au fil du temps](#conversions-over-time)

### Détails des conversions {#conversion-details}

Le tableau des détails des conversions affiche toujours une colonne pour les *destinataires* et une autre pour les *conversions* (taux et total). Les deux autres colonnes du tableau dépendent des options que vous avez sélectionnées lors de la configuration de votre rapport.

![Tableau des détails des conversions montrant les points de contact comme méthode d'attribution pour les colonnes trois et quatre.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

Le tableau suivant décrit les indicateurs possibles.

| Indicateur affiché | Description |
| --- | --- |
| Destinataires | Le nombre d'utilisateurs ayant reçu un message via le canal sélectionné au cours de la plage de dates du rapport |
| Taux de conversion (destinataires) | Calculé comme suit : (Nombre de conversions) / (Nombre de destinataires) |
| Méthode d'attribution | Définie par la [méthode d'attribution](#attribution-methods) que vous avez sélectionnée lors de la configuration du rapport. Pour l'attribution au dernier point de contact ou si plusieurs canaux sont sélectionnés, cela apparaît sous la forme [Points de contact](#terms-to-know). |
| Taux de conversion (méthode d'attribution) | Défini par la [méthode d'attribution](#attribution-methods) que vous avez sélectionnée lors de la configuration du rapport. Si plusieurs canaux sont sélectionnés, l'attribution au dernier point de contact est appliquée par défaut. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détails des conversions" }

Si vous avez sélectionné un niveau de ventilation pour les campagnes ou Canvas lors de la [configuration de votre rapport](#setting-up-your-report) (étape 5), vous pouvez sélectionner <i class="fas fa-angle-down"></i> **Développer** pour développer le tableau.

### Tunnel de conversion {#conversion-funnel}

Ce graphique à barres affiche les valeurs absolues pour chaque [événement d'engagement]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) en fonction du canal sélectionné. Le nombre de conversions sera défini selon la méthode d'attribution sélectionnée.

Par défaut, toutes les campagnes et tous les Canvas sélectionnés sont affichés. Pour désélectionner une campagne ou un Canvas, sélectionnez le nom de la campagne ou du Canvas que vous souhaitez exclure. Pour obtenir des détails supplémentaires sur un événement d'engagement, survolez la barre correspondante.

Pour télécharger les données de la série temporelle, sélectionnez une option de téléchargement : PNG, JPEG, PDF, SVG ou CSV.

{% alert note %}
Ce graphique n'affiche les données que pour un seul canal à la fois. Utilisez le menu déroulant **Channel** sur le graphique pour sélectionner un canal unique.
{% endalert %}

![Graphique à barres du tunnel de conversion pour deux campagnes e-mail montrant des résultats similaires pour e-mails distribués, e-mails ouverts, e-mails cliqués et conversions.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Conversions au fil du temps {#conversions-over-time}

Ce graphique de série temporelle représente les conversions par campagne ou Canvas au fil du temps. Par défaut, toutes les campagnes et tous les Canvas sélectionnés sont affichés. Pour désélectionner une campagne ou un Canvas, cliquez sur le nom de la campagne ou du Canvas que vous souhaitez exclure.

Pour télécharger les données de la série temporelle, sélectionnez <i class="fas fa-bars" title="Menu contextuel du graphique"></i> **Menu contextuel du graphique** puis choisissez votre option de téléchargement. Les options disponibles sont PNG, JPEG, PDF, SVG ou CSV.

![Graphique de série temporelle des conversions au fil du temps pour deux campagnes e-mail, montrant les conversions par jour.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Méthodes d'attribution {#attribution-methods}

| Méthode d'attribution | Définition | Calcul du taux | Options spécifiques au canal |
| --- | --- | --- | --- |
| À la réception | Nombre total de conversions survenues après la réception du message | Calculé comme suit : (Conversions uniques à la réception) / (Destinataires uniques) | {::nomarkdown}<ul><li>À la distribution de l'e-mail</li><li>À la distribution du SMS</li></ul>{:/} |
| À l'envoi | Nombre total de conversions survenues après l'envoi du message | Calculé comme suit : (Conversions uniques à l'envoi) / (Destinataires uniques) | {::nomarkdown}<ul><li>À l'envoi de la notification push</li><li>À l'envoi de la carte de contenu</li><li>À l'envoi du SMS</li></ul>{:/} |
| À l'ouverture | Nombre total de conversions survenues après l'ouverture du message | Calculé comme suit : (Conversions uniques à l'ouverture) / (Destinataires uniques) | {::nomarkdown}<ul><li>À l'ouverture de l'e-mail</li><li>À l'ouverture de la notification push</li></ul>{:/} |
| Au clic | Nombre total de conversions survenues après un clic sur le message | Calculé comme suit : (Conversions uniques au clic) / (Destinataires uniques) | {::nomarkdown}<ul><li>Au clic sur l'e-mail</li><li>Au clic sur la carte de contenu</li><li>Au clic sur le message in-app</li></ul>{:/} |
| À l'impression | Nombre total de conversions survenues après une impression | Calculé comme suit : (Conversions uniques à l'impression) / (Destinataires uniques) | {::nomarkdown}<ul><li>À l'impression du message in-app</li><li>À l'impression de la carte de contenu</li></ul>{:/} |
| Au dernier point de contact | Conversions attribuant tout le crédit au dernier message touché ou cliqué pendant la fenêtre de conversion | Calculé comme suit : (Nombre de points de contact) / (Destinataires uniques) | L'attribution au dernier point de contact est automatiquement sélectionnée si plusieurs canaux sont ajoutés au rapport. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Méthodes d'attribution" }

## Termes à connaître {#terms-to-know}

| Terme | Définition |
| --- | --- |
| Point de contact | Une interaction physique ou un point de contact avec un message.<br><br>Les points de contact peuvent inclure :<br>{::nomarkdown}<ul><li>Clic sur l'e-mail</li><li>Ouverture de la notification push</li><li>Clic sur la carte de contenu</li><li>Clic sur le message in-app</li><li>Clic sur le SMS</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Termes à connaître" }

## Résolution des problèmes {#troubleshooting}

### Pourquoi mes conversions de campagne ou de Canvas sont-elles faibles ? {#why-do-i-have-low-campaign-or-canvas-conversions}

Vos conversions peuvent être inférieures à vos attentes par rapport à des campagnes précédentes ou à vos prévisions. Les conversions dépendent de deux facteurs clés : le suivi des événements et les délais de conversion.

Pour résoudre le problème, vérifiez votre suivi des événements et vos délais de conversion.

#### Suivi des événements {#event-tracking}

Lorsqu'une campagne déclenche un début de session ou un événement personnalisé, vous devez vous assurer que cet événement ou cette session se produit suffisamment fréquemment pour déclencher le message. Consultez le [tableau de bord d'accueil]({{site.baseurl}}/user_guide/analytics/dashboards/home/) pour les données de session, ou votre rapport sur les [événements personnalisés]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting/).

#### Délais de conversion {#conversion-deadlines}

Pour chaque événement de conversion que vous sélectionnez par campagne, vous définissez un [délai]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#creating-a-campaign-with-conversion-tracking). Cela signifie que vous fixez une limite de temps au cours de laquelle une conversion doit avoir lieu pour être comptabilisée dans la campagne concernée.

Vérifiez que vous avez bien consulté les informations sur les [règles de suivi des conversions]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#conversion-tracking-rules) pour comprendre les indicateurs de votre campagne. Pour les conversions des utilisateurs dans un Canvas, consultez la [FAQ Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas).