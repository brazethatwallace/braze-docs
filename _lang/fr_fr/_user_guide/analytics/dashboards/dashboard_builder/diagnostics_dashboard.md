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

## Concepts clés {#key-concepts}

### Envoyé et distribué {#sent-and-delivered}

Il est essentiel de comprendre que ce tableau de bord rend compte de la manière dont Braze a traité un message en interne, et non de l'état final de distribution du message.

Un message marqué comme « envoyé » dans ce tableau de bord signifie que Braze l'a traité et expédié avec succès. Pour la plupart des canaux, cela signifie que Braze a transmis le message au partenaire d'envoi tiers concerné. Cependant, cela ne garantit pas la distribution finale sur l'appareil de l'utilisateur.

Lorsque Braze « envoie » un message, la distribution finale peut dépendre de services externes. Voici quelques exemples pour chaque canal.

| Canal | Exemple de distribution finale |
| --- | --- |
| Content Cards | La carte a été envoyée et peut être consultée. |
| E-mail | Braze transmet le message à un fournisseur de services d'e-mailing (ESP). L'ESP est ensuite responsable de la distribution finale. Cet ESP peut, par exemple, signaler un « rebond » si l'adresse e-mail est invalide ou si la boîte de réception est pleine. |
| Messages in-app | Le message a été affiché à l'utilisateur. |
| LINE | Le message a été transmis avec succès à un partenaire d'envoi. |
| Push | Braze transmet le message au service de notification push approprié (comme Apple Push Notification service pour iOS ou Firebase Cloud Messaging pour Android). Ce service est responsable de la distribution finale de la notification sur l'appareil. |
| SMS/MMS/RCS | Braze transmet le message à une passerelle SMS (comme Twilio). Cette passerelle est responsable de la distribution finale à l'opérateur mobile. |
| Webhooks | La requête webhook a été effectuée avec succès, renvoyant une réponse `2xx`. |
| WhatsApp | Le message a été transmis avec succès à un partenaire d'envoi. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Envoyé et distribué" }

### Fraîcheur des données {#data-freshness}

La fréquence de mise à jour des données de ce tableau de bord peut varier en fonction de la charge du système. Bien que la fréquence de mise à jour ne soit pas garantie, elle est généralement inférieure à une heure dans la plupart des cas.

## Configuration du tableau de bord {#configuring-the-dashboard}

Vous pouvez accéder au tableau de bord de diagnostic en allant dans **Analytics** > **Dashboard Builder** et en sélectionnant **Messaging Diagnostics** dans la liste des tableaux de bord créés par Braze.

Pour exécuter le tableau de bord et afficher vos données :

1. Choisissez **Campaigns** ou **Canvas** comme source pour les rapports de votre tableau de bord.
2. Sélectionnez une ou plusieurs campagnes ou Canvas.
3. Sélectionnez **Run Dashboard** pour charger les données correspondant aux filtres sélectionnés.

![Exemple de diagnostic de Campaigns et Canvas du 25 au 31 mai 2025 pour une campagne de série de bienvenue.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Exemple de diagnostic de Campaigns et Canvas avec graphique au survol du 25 au 31 mai 2025 pour une campagne de série de bienvenue.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

## Interprétation des données {#interpreting-the-data}

{% alert note %}
Le tableau de bord affiche uniquement les données des sept derniers jours. Tous les horodatages sont affichés dans le fuseau horaire de votre espace de travail.
{% endalert %}

### Tuiles récapitulatives {#summary-tiles}

En haut de la page, des tuiles récapitulatives clés pour la période sélectionnée affichent :

- **Sent :** Le nombre total de messages que Braze a traités et envoyés avec succès.
  - **E-mail, SMS/MMS/RCS, WhatsApp, LINE et push :** Le message a été transmis avec succès à un partenaire d'envoi.
  - **Webhooks :** La requête webhook a été effectuée avec succès, renvoyant une réponse `2xx`.
  - **Content Cards :** La carte a été envoyée et peut être consultée.
  - **Messages in-app :** Le message a été affiché à l'utilisateur.
- **Not Sent :** Le nombre total de messages abandonnés. Cela inclut les membres de l'audience du Canvas qui n'ont pas intégré le Canvas ou qui en sont sortis parce qu'ils ont rencontré un échec d'étape ou rempli les critères de sortie lors de l'exécution d'un événement de sortie.

### Résultats des messages au fil du temps {#message-outcomes-over-time}

Ce graphique en série temporelle montre une ventilation heure par heure des raisons pour lesquelles un message a été abandonné ou un utilisateur a été retiré d'un Canvas. Les libellés de résultats dans ce graphique sont des libellés normalisés du tableau de bord, et non des valeurs brutes de payload d'événement. Ce graphique n'affiche pas le nombre d'envois.

### Journal détaillé des résultats des messages {#message-outcomes-granular-log}

Le tableau de bord affiche un tableau détaillé des résultats individuels des messages pour les filtres et la période sélectionnés. Utilisez ce tableau pour examiner des enregistrements spécifiques, notamment l'horodatage, l'ID utilisateur, l'étape du Canvas, le résultat, les détails et le canal.

Vous pouvez filtrer le tableau pour vous concentrer sur des enregistrements spécifiques :

- **Filtrer par résultat :** Sélectionnez un résultat dans le filtre de résultats pour afficher uniquement les lignes correspondant à ce résultat (par exemple, `Frequency capped` ou `User not eligible for channel`).
- **Rechercher par ID utilisateur :** Saisissez un ID utilisateur dans le champ de recherche pour afficher les lignes correspondant à cet utilisateur spécifique.

Lorsque vous appliquez les deux filtres, le tableau renvoie les lignes correspondant à la fois au résultat sélectionné et à l'ID utilisateur saisi.

Sélectionnez une ligne du tableau pour ouvrir le panneau de détails. Le panneau de détails fournit un contexte supplémentaire sur ce résultat, et Ask Operator propose des recommandations de remédiation pour vous aider à résoudre le problème sous-jacent.

![Journal détaillé des résultats de Messaging Diagnostics avec une ligne sélectionnée et accès au panneau de détails.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Panneau de détails de Messaging Diagnostics développé avec le contexte du résultat et les recommandations de remédiation.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

{% alert note %}
Les filtres de canal s'appliquent aux résultats liés à un canal de communication spécifique. Certains résultats sont indépendants du canal et peuvent donc apparaître dans les vues agrégées même lorsque vous appliquez un filtre de canal.
{% endalert %}

### Résultats d'abandon {#abort-outcomes}

Les définitions suivantes expliquent les résultats d'abandon affichés sur le tableau de bord. Les résultats sont regroupés par catégorie pour faciliter la recherche de celui que vous examinez.

{% alert note %}
Les résultats d'abandon dans Messaging Diagnostics sont des libellés lisibles du tableau de bord. Dans les [événements d'engagement liés aux messages de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), les informations d'abandon sont représentées par des champs tels que `abort_type` et `abort_log`. Comme ces jeux de données ont des représentations et des chemins de traitement différents, les comptages ou les noms peuvent différer entre Currents et Messaging Diagnostics.
{% endalert %}

#### Contenu et rendu {#content-and-rendering}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Content Card expirée | La Content Card a expiré avant que l'utilisateur ne la voie. |
| Content Card invalide | La Content Card contenait des erreurs et n'a pas été envoyée à l'utilisateur. Voici quelques raisons courantes : {::nomarkdown}<ul><li> Taille maximale dépassée (2 Ko) </li><li> La date d'expiration est invalide </li><li> Le message contient des caractères invalides </li></ul>{:/} |
| Échec du contenu connecté | Braze a tenté d'envoyer le message, mais le contenu connecté a échoué après le nombre maximal de tentatives (cinq par défaut). **Remarque :** Ce nombre représente le nombre de messages abandonnés en raison de l'atteinte du nombre maximal de tentatives, et non le nombre total de requêtes de contenu connecté ayant échoué. |
| Délai d'expiration du rendu du message in-app | Après plusieurs tentatives, le Liquid n'a pas pu être rendu et a expiré. |
| Abandon Liquid | L'étiquette Liquid [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) a été appelée, l'envoi a donc été annulé. |
| Délai d'expiration du rendu Liquid | Le rendu du modèle Liquid a pris trop de temps. Cela se produit le plus souvent pour les bannières, les messages in-app et les e-mails. |
| Erreur de syntaxe Liquid | Le modèle Liquid contenait une erreur d'analyse, le message a donc été annulé. |
| Échec de l'URL du média | Braze n'a pas pu traiter l'URL du média dans le message. Cela peut se produire lorsque l'URL est bloquée, invalide, expire, renvoie un statut HTTP invalide ou échoue à la validation SSL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Contenu et rendu" }

#### État de la campagne et du Canvas {#campaign-and-canvas-state}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Échec de l'étape de délai | L'[étape de délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) a échoué, provoquant la sortie de l'utilisateur du Canvas. Cet échec peut se produire lorsque : {::nomarkdown}<ul><li> La variable fournie à l'étape de délai personnalisé était vide ou d'un type invalide </li><li> Le délai dépasse la durée maximale autorisée dans le Canvas</li></ul>{:/} |
| Événement d'exception ou de sortie | L'utilisateur était précédemment éligible pour recevoir le message, mais {::nomarkdown}<ul><li> a effectué un <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-3-select-exception-events">événement d'exception</a> pour une campagne basée sur une action, le message a donc été abandonné, ou </li><li> a rempli les <a href="/docs/user_guide/messaging/canvas/create_a_canvas#setting-exit-criteria">critères de sortie</a> du Canvas et a donc été retiré en cours de parcours.</li></ul>{:/} |
| Campagne inactive | La campagne a été arrêtée alors que le message était en cours de traitement, il a donc été abandonné. |
| Canvas inactif | Le Canvas a été arrêté avant que l'utilisateur n'entre dans le parcours. |
| Étape du Canvas inactive | Cela peut se produire dans le Canvas si : {::nomarkdown}<ul><li> L'étape du Canvas a été supprimée </li> <li>Le Canvas a été arrêté, ce qui rend toutes les étapes inactives </li></ul>{:/} |
| Limite de volume atteinte | La campagne a atteint la limite de volume définie, l'envoi a donc été annulé. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="État de la campagne et du Canvas" }

#### Limitation du débit et timing {#rate-limiting-and-timing}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Limite de fréquence atteinte | L'utilisateur a déjà reçu le nombre maximal de messages autorisé selon les règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) de votre espace de travail, l'envoi a donc été annulé. |
| Abandon pour heures calmes | Les heures calmes étaient activées pour la campagne ou l'étape du Canvas avec l'option de repli définie sur **Abandon du message**. L'utilisateur a déclenché la campagne ou est entré dans l'étape Message du Canvas pendant les heures calmes, le message a donc été abandonné. Cependant, cela ne fait pas sortir l'utilisateur du Canvas. |
| Limite de débit dépassée pendant plus de 72 heures | Le message a été limité pendant plus de 72 heures en raison des [limites de débit de vitesse de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), l'envoi a donc été abandonné. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitation du débit et timing" }

#### Éligibilité de l'utilisateur et profil {#user-eligibility-and-profile}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Identifiant utilisateur en double | Plusieurs utilisateurs avec un identifiant correspondant (comme un ID externe, une adresse e-mail ou un numéro de téléphone) étaient éligibles pour recevoir ce message. Pour éviter les envois en double au même utilisateur, ce message a été abandonné. |
| L'utilisateur a échoué à la pré-vérification de l'étape Message | Braze exécute un premier ensemble de pré-vérifications de base concernant l'éligibilité de l'audience, la rééligibilité et l'éligibilité au canal avant les validations complètes de distribution pour une étape Message du Canvas. Ce résultat signifie que l'utilisateur ou le message a échoué à l'une de ces vérifications, le message a donc été abandonné pour cette étape. |
| L'utilisateur a échoué à la pré-vérification du message déclenché | Braze exécute un premier ensemble de pré-vérifications de base concernant l'éligibilité de l'audience, la rééligibilité et l'éligibilité au canal avant de créer un message à envoyer à partir de ce déclencheur. Ce résultat signifie que l'utilisateur ou le message a échoué à l'une de ces vérifications, le message a donc été abandonné. |
| L'utilisateur n'est plus éligible | L'utilisateur faisait initialement partie de l'audience cible, mais ne correspondait plus aux critères de l'audience avant que Braze n'envoie le message ou n'intègre l'utilisateur dans le Canvas. Le délai entre le moment où l'utilisateur a initialement satisfait les critères de l'audience et celui où il en est sorti peut être dû à : {::nomarkdown}<ul><li>Le timing intelligent</li><li>Les heures calmes</li><li>L'heure locale</li><li>Les limites de débit de vitesse de distribution (non applicable pour l'entrée dans le Canvas)</li><li>Les délais du pipeline d'envoi de messages</li></ul>{:/} |
| L'utilisateur n'est pas éligible pour l'étape | L'utilisateur ne satisfaisait pas les [validations de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) définies pour l'étape Message ou faisait partie d'une [liste de suppression]({{site.baseurl}}/user_guide/audience/suppression_lists). Selon les paramètres des **validations de distribution**, l'utilisateur peut avoir quitté le Canvas ou être passé à l'étape suivante. |
| L'utilisateur n'est pas rééligible | L'utilisateur était éligible pour recevoir le message ou entrer dans le Canvas, mais l'envoi a été annulé en raison des paramètres de rééligibilité ou de réentrée. Cela peut se produire si l'utilisateur a déjà reçu la campagne ou est entré dans le Canvas trop récemment, si un autre envoi pour la même campagne est déjà en cours pour cet utilisateur, ou si la rééligibilité ou la réentrée est désactivée. |
| Profil utilisateur introuvable | L'utilisateur n'a jamais existé ou n'existe plus dans Braze. Voici quelques cas courants : {::nomarkdown}<ul><li> L'utilisateur a été ciblé via l'API d'envoi de messages, mais n'a jamais existé dans Braze. </li><li>L'utilisateur a été supprimé avant l'envoi du message ou l'exécution de l'étape du Canvas. </li><li>L'utilisateur a été fusionné avec un autre profil avant l'envoi du message.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Éligibilité de l'utilisateur et profil" }

#### Canal et distribution {#channel-and-delivery}

| Résultat d'abandon | Explication |
| ---- | ---- |
| Erreur de distribution du partenaire | Braze a tenté d'envoyer ce message à votre partenaire de distribution pendant 24 heures, mais le partenaire a renvoyé des erreurs temporaires pendant toute la durée de cette fenêtre. |
| Identifiants push invalides | Les [identifiants push]({{site.baseurl}}/user_guide/channels/push/faqs#why-doesnt-an-opted-in-user-have-a-push-token) pour cette application sont manquants ou invalides, l'envoi a donc été annulé. Mettez à jour vos identifiants dans **Paramètres des applications**. |
| Échec du groupe d'abonnement | Le message n'a pas pu être envoyé en raison de problèmes de configuration du groupe d'abonnement ou du service d'envoi de messages. Les raisons courantes incluent l'absence de numéros d'envoi pour SMS ou WhatsApp, ou l'incompatibilité MMS sur le service d'envoi de messages configuré. |
| L'utilisateur n'est pas éligible pour le canal | L'utilisateur n'est pas éligible pour recevoir ce message sur le canal sélectionné. Les raisons courantes incluent des identifiants de canal manquants ou invalides, l'absence de jetons push éligibles, des restrictions liées à l'état d'abonnement, une fonctionnalité de canal non prise en charge ou des pays bloqués pour les canaux téléphoniques. |
| Échec du webhook | Le webhook a reçu un code de réponse non réussi (non-`2xx`). Les codes d'erreur courants peuvent être des erreurs client `4XX`, des erreurs serveur ou des délais d'expiration `5XX`, ou `598 Host Unhealthy` ou des requêtes brièvement interrompues. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canal et distribution" }

## Questions fréquentes {#frequently-asked-questions}

### Que signifie un échec de « pré-vérification » ? {#what-does-a-pre-check-failure-mean}

Une « pré-vérification » désigne un contrôle de validation rapide et groupé qui s'exécute au tout début d'une étape du pipeline (comme le déclenchement d'un message ou l'envoi d'une étape Message du Canvas). Considérez-la comme une sortie anticipée conçue pour une vitesse maximale. Au lieu d'exécuter de nombreuses vérifications séparées et gourmandes en ressources (comme la validation de chaque détail du profil d'un utilisateur), Braze regroupe plusieurs validations de base en un seul « premier passage ».

Si un utilisateur échoue à cette vérification groupée unique, il est immédiatement retiré. Cette approche groupée permet à Braze de traiter des volumes massifs de messages à grande vitesse et peut contribuer à des performances plus rapides et plus stables pour vos campagnes et Canvas en réduisant la latence de traitement de chaque message.

### Que signifie un résultat d'abandon « autre » ? {#what-does-an-other-abort-outcome-mean}

Il s'agit d'abandons qui ne correspondent à aucune des catégories existantes du tableau de bord. Si vous constatez une proportion importante d'abandons avec le résultat « autre », contactez l'[assistance Braze]({{site.baseurl}}/braze_support) pour obtenir de l'aide.

### Pourquoi la somme de *Not Sent* et *Sent* est-elle inférieure à la taille d'audience attendue ? {#why-is-the-sum-of-_not-sent_-and-_sent_-lower-than-my-expected-audience-size}

Cela peut se produire pour plusieurs raisons :

- **Critères d'audience :** Moins d'utilisateurs que prévu ont pu satisfaire les critères d'audience (par exemple, ils n'étaient pas dans le segment ou ne possédaient pas les attributs nécessaires) au moment du lancement de la campagne ou du Canvas.
- **Traitement en cours :** Les messages peuvent encore être en cours de traitement. Les utilisateurs peuvent encore se trouver dans des étapes antérieures du Canvas et ne pas avoir atteint les étapes Message.
- **Fraîcheur des données :** Les données du tableau de bord sont mises à jour environ toutes les 15 minutes, mais cela n'est pas garanti. Les données les plus récentes pour cette campagne ou ce Canvas peuvent ne pas encore être disponibles dans le tableau de bord.
- **Cas limites :** Il existe une faible probabilité que vous rencontriez un cas limite qui n'est pas pris en compte dans ce tableau de bord pour le moment. Si vous pensez que c'est le cas, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Pourquoi la somme de *Not Sent* et *Sent* est-elle supérieure à l'audience d'une campagne ou d'un Canvas ? {#why-is-the-sum-of-_not-sent_-and-_sent_-greater-than-the-audience-for-a-campaign-and-canvas}

Cela peut se produire pour les raisons suivantes :

- **Messages multicanaux :** La campagne ou l'étape du Canvas était configurée pour envoyer sur plusieurs canaux (comme SMS et e-mail). Un même utilisateur peut recevoir un résultat « envoyé » pour un canal (comme l'e-mail) et un résultat « abandonné » pour un autre (comme « L'utilisateur n'est pas éligible pour le canal »). Dans ce cas, cet utilisateur serait compté deux fois dans le graphique : une fois comme « envoyé » et une fois comme « abandonné ».
  - **Exemple :** Vous envoyez une campagne push à 100 utilisateurs, ciblant à la fois iOS et Android. Si un utilisateur ne possède qu'un appareil iOS, il reçoit la notification push iOS (« envoyé ») mais déclenche également un abandon pour la notification push Android (« L'utilisateur n'est pas éligible pour le canal »).
- **Étapes Message multiples (Canvas uniquement) :** Votre Canvas peut comporter plusieurs étapes Message dans un parcours donné. Ce tableau de bord agrège tous les résultats, un même utilisateur peut donc être compté plusieurs fois s'il passe par plusieurs étapes Message dans la période sélectionnée.
- **Messages de test :** Les envois de test (qui sont comptabilisés dans le tableau de bord) font augmenter les totaux au-delà de la taille de l'audience.