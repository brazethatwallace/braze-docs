---
nav_title: Tableau de bord de diagnostic des messages
article_title: Tableau de bord de diagnostic des messages
description: "Cet article de référence présente le tableau de bord de diagnostic des messages, qui vous aide à comprendre pourquoi les messages de vos campagnes ou Canvas n'ont peut-être pas été envoyés comme prévu."
alias: /ccdd/
page_order: 2
toc_headers: h2
---

# Tableau de bord de diagnostic des messages {#messaging-diagnostics-dashboard}

> Le tableau de bord **Messaging Diagnostics** fournit une vue d'ensemble des résultats d'envoi de messages, vous permettant de repérer les tendances et de diagnostiquer les problèmes potentiels dans votre configuration d'envoi de messages. Ce tableau de bord peut vous aider à comprendre pourquoi les messages de vos campagnes ou Canvas n'ont peut-être pas été envoyés comme prévu.

{% alert important %}
Le tableau de bord **Messaging Diagnostics** est disponible de manière générale. Contactez votre gestionnaire du succès des clients si vous souhaitez obtenir l'accès à cette fonctionnalité.
{% endalert %}

{% alert note %}
Pour accéder au tableau de bord **Messaging Diagnostics**, vous devez disposer des [permissions utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) « View Dashboard Reports » et « View PII » pour votre espace de travail.
{% endalert %}

## Concepts clés {#key-concepts}

### Envoyé et distribué {#sent-and-delivered}

Il est essentiel de comprendre que ce tableau de bord rend compte de la manière dont Braze a traité un message en interne, et non du statut final de distribution du message.

Un message marqué comme « envoyé » dans ce tableau de bord signifie que Braze a traité et expédié le message avec succès. Pour la plupart des canaux, cela signifie que Braze a transmis le message au partenaire d'envoi tiers concerné. Cependant, cela ne garantit pas la distribution finale sur l'appareil de l'utilisateur.

Lorsque Braze « envoie » un message, la distribution finale peut dépendre de services externes. Voici des exemples pour chaque canal.

| Canal | Exemple de distribution finale |
| --- | --- |
| Content Cards | La carte a été envoyée et est éligible à la consultation. |
| E-mail | Braze transmet le message à un fournisseur de services d'e-mailing (ESP). L'ESP est ensuite responsable de la distribution finale. Cet ESP peut, par exemple, signaler un « rebond » si l'adresse e-mail est invalide ou si la boîte de réception est pleine. |
| In-App Messages | Le message a été consulté par l'utilisateur et une impression a été enregistrée. |
| LINE | Le message a été transmis avec succès à un partenaire d'envoi. |
| Push | Braze transmet le message au service de notification push approprié (comme Apple Push Notification service pour iOS ou Firebase Cloud Messaging pour Android). Ce service est responsable de la distribution finale de la notification sur l'appareil. |
| SMS/MMS/RCS | Braze transmet le message à une passerelle SMS (comme Twilio). Cette passerelle est responsable de la distribution finale auprès de l'opérateur mobile. |
| Webhooks | La requête webhook a été effectuée avec succès, renvoyant une réponse `2xx`. |
| WhatsApp | Le message a été transmis avec succès à un partenaire d'envoi. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Envoyé et distribué" }

### Fraîcheur des données {#data-freshness}

La fréquence de mise à jour des données dans ce tableau de bord peut varier en fonction de la charge du système. Bien que la fréquence de mise à jour ne soit pas garantie, elle est généralement inférieure à une heure dans la plupart des cas.

## Configuration du tableau de bord {#configuring-the-dashboard}

Vous pouvez accéder au tableau de bord de diagnostics en allant dans **Analytics** > **Dashboard Builder** et en sélectionnant **Messaging Diagnostics** dans la liste des tableaux de bord créés par Braze.

Pour exécuter le tableau de bord et visualiser vos données :

1. Choisissez **Campaigns** ou **Canvas** comme source pour vos rapports de tableau de bord.
2. Sélectionnez une ou plusieurs Campaigns ou Canvas.
3. Sélectionnez **Run Dashboard** pour charger les données correspondant aux filtres sélectionnés.

![Exemple de diagnostics de Campaigns et Canvas du 25 au 31 mai 2025 pour une campagne de série de bienvenue.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Exemple de diagnostics de Campaigns et Canvas avec graphique au survol du 25 au 31 mai 2025 pour une campagne de série de bienvenue.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

## Interpréter les données {#interpreting-the-data}

{% alert note %}
Le tableau de bord affiche uniquement les données des sept derniers jours au maximum. Tous les horodatages sont affichés dans le fuseau horaire de votre espace de travail.
{% endalert %}

### Tuiles récapitulatives {#summary-tiles}

En haut de la page, des tuiles récapitulatives clés pour la période sélectionnée affichent :

- **Sent :** Le nombre total de messages que Braze a traités et envoyés avec succès.
  - **E-mail, SMS/MMS/RCS, WhatsApp, LINE et push :** Le message a été transmis avec succès à un partenaire d'envoi.
  - **Webhooks :** La requête webhook a été effectuée avec succès, renvoyant une réponse `2xx`.
  - **Content Cards :** La carte a été envoyée et est éligible à l'affichage.
  - **In-App Messages :** Le message a été affiché à l'utilisateur.
- **Not Sent :** Le nombre total de messages qui ont été abandonnés. Cela inclut les membres de l'audience d'un Canvas qui n'ont pas intégré le Canvas ou qui en sont sortis parce qu'ils ont rencontré un échec d'étape ou rempli les critères de sortie lors de l'exécution d'un événement de sortie.

### Résultats des messages au fil du temps {#message-outcomes-over-time}

Ce graphique chronologique présente une ventilation horaire des raisons pour lesquelles un message a été abandonné ou un utilisateur a été retiré d'un Canvas. Les libellés de résultats dans ce graphique sont des libellés normalisés du tableau de bord, et non des valeurs brutes de la charge utile des événements. Ce graphique n'affiche pas le nombre d'envois.

### Journal granulaire des résultats de messages {#message-outcomes-granular-log}

Le tableau de bord affiche un tableau granulaire des résultats individuels des messages pour les filtres et la période sélectionnés. Utilisez ce tableau pour examiner des enregistrements spécifiques, notamment l'horodatage, l'ID utilisateur, l'étape du Canvas, le résultat, les détails et le canal.

Vous pouvez filtrer le tableau pour vous concentrer sur des enregistrements spécifiques :

- **Filtrer par résultat :** Sélectionnez un résultat dans le filtre de résultats pour afficher uniquement les lignes correspondant à ce résultat (par exemple, `Frequency capped` ou `User not eligible for channel`).
- **Rechercher par ID utilisateur :** Saisissez un ID utilisateur dans le champ de recherche pour afficher les lignes correspondant à cet utilisateur spécifique.

Lorsque vous appliquez les deux filtres, le tableau renvoie les lignes correspondant à la fois au résultat sélectionné et à l'ID utilisateur saisi.

Sélectionnez une ligne dans le tableau pour ouvrir le panneau de détails. Le panneau de détails fournit un contexte supplémentaire sur ce résultat, et Ask Operator propose des recommandations de remédiation pour vous aider à résoudre le problème sous-jacent.

![Journal granulaire des résultats de Messaging Diagnostics avec une ligne sélectionnée et accès au panneau de détails.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Panneau de détails de Messaging Diagnostics développé avec le contexte du résultat et les recommandations de remédiation.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

{% alert note %}
Les filtres de canal s'appliquent aux résultats liés à un canal de communication spécifique. Certains résultats sont indépendants du canal, ils peuvent donc toujours apparaître dans les vues agrégées même lorsque vous appliquez un filtre de canal.
{% endalert %}

### Résultats d'abandon {#abort-outcomes}

Les définitions suivantes expliquent les résultats d'abandon affichés sur le tableau de bord. Les résultats sont regroupés par catégorie pour faciliter la recherche de celui que vous examinez.

{% alert note %}
Les résultats d'abandon dans Messaging Diagnostics sont des libellés lisibles du tableau de bord. Dans les [événements d'engagement liés aux messages de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), les informations d'abandon sont représentées par des champs tels que `abort_type` et `abort_log`. Comme ces jeux de données ont des représentations et des chemins de traitement différents, les comptages ou les noms peuvent différer entre Currents et Messaging Diagnostics.
{% endalert %}

#### Contenu et rendu {#content-and-rendering}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Content Card expired | La Content Card a expiré avant que l'utilisateur ne la voie. |
| Content Card invalid | La Content Card contenait des erreurs et n'a pas été envoyée à l'utilisateur. Parmi les raisons courantes : {::nomarkdown}<ul><li> Taille maximale dépassée (2 Ko) </li><li> La date d'expiration est invalide </li><li> Le message contient des caractères invalides </li></ul>{:/} |
| Connected Content failed | Braze a tenté d'envoyer le message, mais le contenu connecté a échoué après le nombre maximal de tentatives (cinq par défaut). **Remarque :** Ce comptage représente le nombre de messages abandonnés en raison de l'atteinte du nombre maximal de tentatives, et non le nombre total de requêtes de contenu connecté ayant échoué. |
| In-app-message rendering timeout | Après plusieurs tentatives, le Liquid n'a pas pu être rendu et a expiré. |
| Liquid abort | L'étiquette Liquid [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) a été appelée, l'envoi a donc été annulé. |
| Liquid rendering timeout | Le rendu du modèle Liquid a pris trop de temps. Cela se produit le plus souvent pour les bannières, les messages in-app et les e-mails. |
| Liquid syntax error | Le modèle Liquid contenait une erreur d'analyse, le message a donc été annulé. |
| Media URL failure | Braze n'a pas pu traiter l'URL média dans le message. Cela peut se produire lorsque l'URL est bloquée, invalide, expire, renvoie un statut HTTP invalide ou échoue à la validation SSL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Contenu et rendu" }

#### État de la Campaign et du Canvas {#campaign-and-canvas-state}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Delay step failure | L'[étape de délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) a échoué, entraînant la sortie de l'utilisateur du Canvas. Cet échec peut se produire lorsque : {::nomarkdown}<ul><li> La variable fournie à l'étape de délai personnalisé était vide ou d'un type invalide </li><li> Le délai dépasse la durée maximale autorisée dans le Canvas</li></ul>{:/} |
| Exception or exit event | L'utilisateur était précédemment éligible pour recevoir le message, mais soit {::nomarkdown}<ul><li> a effectué un <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-3-select-exception-events">événement d'exception</a> pour une campagne déclenchée par une action, le message a donc été abandonné, soit </li><li> a rempli les <a href="/docs/user_guide/messaging/canvas/create_a_canvas#setting-exit-criteria">critères de sortie</a> du Canvas et a donc été retiré en cours de parcours.</li></ul>{:/} |
| Inactive campaign | La Campaign a été arrêtée alors que le message était en cours d'envoi, il a donc été abandonné. |
| Inactive Canvas | Le Canvas a été arrêté avant que l'utilisateur n'entre dans le parcours. |
| Inactive Canvas step | Cela peut se produire dans le Canvas si : {::nomarkdown}<ul><li> L'étape du Canvas a été supprimée </li> <li>Le Canvas a été arrêté, ce qui rend toutes les étapes inactives </li></ul>{:/} |
| Volume limited | La Campaign a atteint la limite de volume définie, l'envoi a donc été annulé. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="État de la Campaign et du Canvas" }

#### Limitation du débit et timing {#rate-limiting-and-timing}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Frequency capped | L'utilisateur a déjà reçu le nombre maximal de messages autorisé selon les règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) de votre espace de travail, l'envoi a donc été annulé. |
| Quiet Hours abort | Les heures calmes étaient activées pour la Campaign ou l'étape du Canvas avec l'option de repli définie sur **Abort message**. L'utilisateur a déclenché la Campaign ou est entré dans l'étape de message du Canvas pendant les heures calmes, le message a donc été abandonné. Cependant, cela ne fait pas sortir l'utilisateur du Canvas. |
| Rate limited over 72 hours | Le message a été limité pendant plus de 72 heures en raison des [limites de débit de vitesse de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), l'envoi a donc été abandonné. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitation du débit et timing" }

#### Éligibilité et profil de l'utilisateur {#user-eligibility-and-profile}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Duplicate user identifier | Plusieurs utilisateurs avec un identifiant correspondant (tel qu'un ID externe, une adresse e-mail ou un numéro de téléphone) étaient éligibles pour recevoir ce message. Pour éviter les envois en double au même utilisateur, ce message a été abandonné. |
| User failed pre-check for Message step | Braze effectue un premier ensemble de vérifications de base concernant l'éligibilité de l'audience, la rééligibilité et l'éligibilité du canal avant les validations complètes de distribution pour une étape de message du Canvas. Ce résultat signifie que l'utilisateur ou le message a échoué à l'une de ces vérifications, le message a donc été abandonné pour cette étape. |
| User failed pre-check for triggered message | Braze effectue un premier ensemble de vérifications de base concernant l'éligibilité de l'audience, la rééligibilité et l'éligibilité du canal avant de créer un message à envoyer à partir de ce déclencheur. Ce résultat signifie que l'utilisateur ou le message a échoué à l'une de ces vérifications, le message a donc été abandonné. |
| User no longer eligible | L'utilisateur faisait initialement partie de l'audience cible, mais ne correspondait plus aux critères d'audience avant que Braze n'envoie le message ou n'intègre l'utilisateur dans le Canvas. Le délai entre le moment où l'utilisateur a initialement rempli les critères d'audience et celui où il en est sorti peut être dû à des retards liés à : {::nomarkdown}<ul><li>Timing intelligent</li><li>Heures calmes</li><li>Heure locale</li><li>Limites de débit de vitesse de distribution (non applicable pour l'entrée dans le Canvas)</li><li>Retards du pipeline de communication</li></ul>{:/} |
| User not eligible for step | L'utilisateur n'a pas rempli les [validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) définies pour l'étape de message ou faisait partie d'une [liste de suppression]({{site.baseurl}}/user_guide/audience/suppression_lists). Selon les paramètres de **Delivery validations**, l'utilisateur peut avoir quitté le Canvas ou être passé à l'étape suivante. |
| User not re-eligible | L'utilisateur était éligible pour recevoir le message ou entrer dans le Canvas, mais l'envoi a été annulé en raison des paramètres de rééligibilité ou de réentrée. Cela peut se produire si l'utilisateur a déjà reçu la Campaign ou est entré dans le Canvas trop récemment, si un autre envoi pour la même Campaign est déjà en cours pour cet utilisateur, ou si la rééligibilité ou la réentrée est désactivée. |
| User profile not found | L'utilisateur n'a jamais existé ou n'existe plus dans Braze. Parmi les cas courants : {::nomarkdown}<ul><li> L'utilisateur a été ciblé via l'API de communication, mais n'a jamais existé dans Braze. </li><li>L'utilisateur a été supprimé avant l'envoi du message ou l'exécution de l'étape du Canvas. </li><li>L'utilisateur a été fusionné avec un autre profil avant l'envoi du message.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Éligibilité et profil de l'utilisateur" }

#### Canal et distribution {#channel-and-delivery}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Partner delivery error | Braze a tenté d'envoyer ce message à votre partenaire de distribution pendant 24 heures, mais le partenaire a renvoyé des erreurs temporaires pendant toute la durée. |
| Push credentials invalid | Les [identifiants push]({{site.baseurl}}/user_guide/channels/push/faqs#why-doesnt-an-opted-in-user-have-a-push-token) pour cette application sont manquants ou invalides, l'envoi a donc été annulé. Mettez à jour vos identifiants dans **App Settings**. |
| Subscription group failure | Le message n'a pas pu être envoyé en raison de problèmes de configuration du groupe d'abonnement ou du service de communication. Parmi les raisons courantes : numéros d'envoi manquants pour SMS ou WhatsApp, ou MMS non pris en charge sur le service de communication configuré. |
| User not eligible for channel | L'utilisateur n'est pas éligible pour recevoir ce message sur le canal sélectionné. Parmi les raisons courantes : identifiants de canal manquants ou invalides, aucun jeton push éligible, restrictions liées à l'état d'abonnement, fonctionnalité de canal non prise en charge ou pays bloqués pour les canaux téléphoniques. |
| Webhook failed | Le webhook a reçu un code de réponse non réussi (non-`2xx`). Les codes d'erreur courants peuvent être des erreurs client `4XX`, des erreurs serveur ou des délais d'expiration `5XX`, ou `598 Host Unhealthy` ou des requêtes brièvement interrompues. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canal et distribution" }

## Questions fréquentes {#frequently-asked-questions}

### Que signifie un échec de « pré-vérification » ? {#what-does-a-pre-check-failure-mean}

Une « pré-vérification » désigne un contrôle de validation rapide et groupé qui s'exécute tout au début d'une étape du pipeline (par exemple, lorsqu'un message est déclenché ou lors de l'envoi d'une étape de message Canvas). Considérez-la comme une sortie anticipée conçue pour une vitesse maximale. Au lieu d'exécuter de nombreuses vérifications séparées et gourmandes en ressources (comme la validation de chaque détail du profil d'un utilisateur), Braze regroupe plusieurs validations de base en une seule « première passe ».

Si un utilisateur échoue à cette vérification groupée unique, il est immédiatement exclu. Cette approche groupée permet à Braze de traiter des volumes massifs de messages à grande vitesse et peut contribuer à des performances plus rapides et plus stables pour vos Campaigns et Canvas en réduisant la latence de traitement de chaque message.

### Que signifie un résultat d'abandon « autre » ? {#what-does-an-other-abort-outcome-mean}

Il s'agit d'abandons qui ne correspondent à aucune catégorie existante du tableau de bord. Si vous constatez toujours une proportion importante d'abandons avec la mention « Autre », contactez le [support Braze]({{site.baseurl}}/braze_support) pour obtenir de l'aide.

### Pourquoi la somme de _Non envoyé_ et _Envoyé_ est-elle inférieure à la taille d'audience attendue ? {#why-is-the-sum-of-_not-sent_-and-_sent_-lower-than-my-expected-audience-size}

Cela peut se produire pour plusieurs raisons :

- **Critères d'audience :** Moins d'utilisateurs que prévu ont pu satisfaire les critères d'audience (par exemple, ils n'étaient pas dans le Segment ou ne possédaient pas les attributs nécessaires) au moment du lancement de la Campaign ou du Canvas.
- **Traitement en cours :** Les messages peuvent encore être en cours de traitement. Des utilisateurs peuvent encore se trouver dans des étapes antérieures du Canvas et ne pas avoir atteint les étapes de message.
- **Fraîcheur des données :** Les données du tableau de bord sont mises à jour environ toutes les 15 minutes, mais cela n'est pas garanti. Les données les plus récentes pour cette Campaign ou ce Canvas peuvent ne pas encore être disponibles dans le tableau de bord.
- **Cas limites :** Il existe une faible probabilité que vous rencontriez un cas limite qui n'est pas pris en compte dans ce tableau de bord pour le moment. Si vous pensez que c'est le cas, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Pourquoi la somme de _Non envoyé_ et _Envoyé_ est-elle supérieure à l'audience d'une Campaign ou d'un Canvas ? {#why-is-the-sum-of-_not-sent_-and-_sent_-greater-than-the-audience-for-a-campaign-and-canvas}

Cela peut se produire pour les raisons suivantes :

- **Messages multicanaux :** La Campaign ou l'étape Canvas a été configurée pour envoyer sur plusieurs canaux (tels que SMS et e-mail). Un même utilisateur peut recevoir un résultat « envoyé » pour un canal (comme l'e-mail) et un résultat « abandon » pour un autre (comme « Utilisateur non éligible pour le canal »). Dans ce cas, cet utilisateur serait compté deux fois dans le graphique : une fois comme « envoyé » et une fois comme « abandon ».
  - **Exemple :** Vous envoyez une Campaign de notification push à 100 utilisateurs, ciblant à la fois iOS et Android. Si un utilisateur ne possède qu'un appareil iOS, il reçoit la notification push iOS (« envoyé ») mais déclenche également un abandon pour la notification push Android (« Utilisateur non éligible pour le canal »).
- **Étapes de message multiples (Canvas uniquement) :** Votre Canvas peut comporter plus d'une étape de message dans un parcours donné. Ce tableau de bord agrège tous les résultats, de sorte qu'un même utilisateur peut être compté plusieurs fois s'il passe par plusieurs étapes de message au cours de la période sélectionnée.
- **Messages de test :** Les envois de test (qui sont comptabilisés dans le tableau de bord) font que les totaux sont supérieurs à la taille de l'audience.