---
nav_title: Préférences des e-mails
article_title: Préférences des e-mails
page_type: reference
page_order: 2
description: "Cet article de référence couvre les préférences des e-mails dans le tableau de bord de Braze, y compris les configurations d'envoi, les pixels de suivi d'ouverture, les pages et pieds de page d'abonnement, et plus encore."
tool: Dashboard
channel: email
toc_headers: h2

---

# Préférences des e-mails {#email-preferences}

> Les préférences des e-mails vous permettent de définir des paramètres spécifiques pour les e-mails sortants, comme les pieds de page personnalisés, les pages d'abonnement et de désabonnement personnalisées, et plus encore. L'inclusion de ces options dans vos e-mails sortants offre une expérience fluide et cohérente à vos utilisateurs.

Les **Préférences des e-mails** se trouvent sous **Paramètres** dans le tableau de bord.

## Configuration de l'envoi {#sending-configuration}

Les paramètres d'e-mail de la section **Configuration de l'envoi** déterminent quels détails sont inclus dans vos campagnes d'e-mail. En particulier, ces paramètres sont principalement liés à ce que votre utilisateur voit lorsqu'il reçoit un e-mail de Braze.

### Paramètres des e-mails sortants {#outbound-email-settings}

Lors de la configuration de vos paramètres d'e-mail, vos paramètres d'e-mails sortants identifient quels noms et adresses e-mail sont utilisés lorsque Braze envoie des e-mails à vos utilisateurs.

{% tabs local %}
{% tab Nom d'affichage et adresse %}

Dans cette section, vous pouvez ajouter les noms et adresses e-mail que vous pouvez utiliser lorsque Braze envoie des e-mails à vos utilisateurs. Les noms d'affichage et les adresses e-mail sont disponibles dans les options **Sending Info** lorsque vous composez votre campagne d'e-mail. Notez que les mises à jour apportées aux paramètres des e-mails sortants n'affectent pas rétroactivement les envois existants.

![Section « Outbound Email Settings » avec des champs pour différents noms d'affichage et domaines.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Personnaliser avec Liquid {#personalize-with-liquid}

Vous pouvez également utiliser [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) dans les champs **From Display Name**, **Local Part** et **Domain** pour créer dynamiquement le nom et l'adresse e-mail de l'expéditeur en fonction d'attributs personnalisés. Notez que pour utiliser Liquid dans le champ **Domain**, vous devez accéder aux options **Sending Info** d'une campagne d'e-mail et cocher la case **Customize from display name + address**.

![Paramètres d'envoi avec des champs pour personnaliser le nom d'affichage de l'expéditeur, l'adresse et le domaine.]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

Par exemple, vous pouvez utiliser une logique conditionnelle pour envoyer depuis différentes marques ou régions :

{% raw %}
```liquid
{% if ${language} == 'en' %}
English Display Name
{% elsif ${language} == 'de' %}
German Display Name
{% else %}
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Adresse de réponse %}

L'ajout d'une adresse e-mail dans cette section vous permet de la sélectionner comme adresse de réponse pour votre campagne d'e-mail. Vous pouvez également définir une adresse e-mail par défaut en sélectionnant **Make Default**. Ces adresses e-mail seront disponibles dans les options **Sending Info** lorsque vous composez votre campagne d'e-mail.

![Section « Reply-To Address » avec des champs pour saisir plusieurs adresses de réponse.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% alert note %}
Les domaines d'envoi de Braze n'acceptent pas les e-mails entrants. Si un destinataire répond à un e-mail envoyé depuis un domaine d'envoi configuré par Braze, sa réponse sera rejetée avec une erreur `550 5.7.1 relaying denied`. L'adresse de réponse n'a pas besoin de partager le même domaine que l'adresse d'expédition. Si vous devez recevoir des réponses — par exemple, pour collecter des confirmations d'invitations de calendrier — utilisez un sous-domaine qui n'est pas configuré pour l'envoi et qui dispose d'une boîte de réception configurée pour accepter les e-mails.
{% endalert %}

#### Personnaliser avec Liquid

Vous pouvez également utiliser [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) dans le champ **Reply-To Address** pour créer dynamiquement l'adresse de réponse en fonction d'attributs personnalisés. Par exemple, vous pouvez utiliser une logique conditionnelle pour envoyer les réponses à différentes régions ou départements :

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@example.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@example.com" %}
{% else %}
{% assign address = "global-support@example.com" %}{% endif %}{{address}}
```
{% endraw %}

{% endtab %}
{% tab Adresse CCI %}

Cette section vous permet de gérer les adresses CCI que vous pouvez ajouter aux e-mails sortants envoyés depuis Braze. L'ajout d'une adresse CCI à un e-mail envoie une copie identique du message que votre utilisateur reçoit à votre boîte de réception CCI. C'est un outil utile pour conserver des copies des messages envoyés à vos utilisateurs à des fins de conformité ou de support client. Les e-mails CCI ne sont pas inclus dans les rapports et analyses d'e-mails.

Les adresses CCI sont disponibles pour Amazon SES, SendGrid et SparkPost. Comme alternative aux adresses CCI, nous recommandons d'utiliser l'[archivage des messages]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving) pour enregistrer une copie des messages envoyés aux utilisateurs à des fins d'archivage ou de conformité.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

Après avoir ajouté une adresse, celle-ci sera disponible pour sélection lors de la composition d'un e-mail dans des Campaigns ou des étapes Canvas. Sélectionnez **Make Default** à côté d'une adresse pour que cette adresse soit sélectionnée par défaut lors du lancement d'une nouvelle campagne d'e-mail ou d'un composant Canvas. Pour remplacer ce paramètre au niveau du message, vous pouvez sélectionner **No BCC** lors de la configuration de votre message.

Si vous exigez que tous les e-mails envoyés depuis Braze incluent une adresse CCI, vous pouvez activer le bouton **Require a BCC address for all your email campaigns**. Cela vous obligera à sélectionner une adresse par défaut, qui sera automatiquement sélectionnée pour les nouvelles campagnes d'e-mail ou étapes Canvas. L'adresse par défaut sera également automatiquement ajoutée à tous les messages déclenchés via notre REST API. Il n'est pas nécessaire de modifier la requête API existante pour inclure l'adresse.

#### CCI dynamique {#dynamic-bcc}

Avec la CCI dynamique, vous pouvez utiliser Liquid dans votre adresse CCI. Notez que cette fonctionnalité est uniquement disponible dans les **Préférences des e-mails** et ne peut pas être définie au niveau de la campagne elle-même. Une seule adresse CCI par destinataire d'e-mail est autorisée.

Par exemple, vous pouvez ajouter {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %} comme adresse CCI pour les e-mails de votre équipe de support.

![Section BCC Address de l'onglet Paramètres des e-mails avec une adresse CCI utilisant Liquid.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## Pixel de suivi d'ouverture {#open-tracking-pixel}

[![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Le pixel de suivi d'ouverture des e-mails est une image invisible de 1 x 1&nbsp;px qui est automatiquement insérée dans le HTML de votre e-mail. Ce pixel aide Braze à détecter si vos utilisateurs ont ouvert votre e-mail. Lorsque le client de messagerie d'un utilisateur effectue une requête vers notre pixel de suivi, la requête peut contenir des informations telles que l'adresse IP, l'agent utilisateur et l'horodatage. Les informations d'ouverture des e-mails peuvent être très utiles, vous aidant à déterminer des stratégies marketing efficaces en comprenant les taux d'ouverture correspondants.

### Emplacement {#placement}

Le comportement par défaut dans Braze est d'ajouter le pixel de suivi en bas de votre e-mail, généralement dans une balise `<body>`. Pour la majorité des utilisateurs, c'est l'emplacement idéal pour le pixel.

Bien que le pixel soit déjà stylisé pour causer le moins de changements visuels possible, tout changement visuel involontaire serait le moins visible en bas d'un e-mail. C'est également le comportement par défaut pour les fournisseurs d'e-mails tels que SendGrid et SparkPost.

Pour réduire les comportements inattendus, gardez le Liquid à l'intérieur des balises `<html>`. Les balises de niveau document imbriquées ou dupliquées peuvent modifier la façon dont l'e-mail est analysé et l'emplacement du pixel, ce qui peut affecter le suivi d'ouverture et la mise en page. Pour plus d'informations, consultez [Utiliser Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

### Modifier l'emplacement {#update-the-placement}

Braze prend actuellement en charge le remplacement de l'emplacement par défaut du pixel de suivi d'ouverture de l'ESP (la dernière balise dans le `<body>` d'un e-mail) pour le déplacer vers la première balise du `<body>`.

![Section « Open Tracking Pixel » avec les options de déplacement pour SendGrid, SparkPost ou Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Pour modifier l'emplacement :

1. Dans Braze, accédez à **Paramètres** > **Préférences des e-mails**.
2. Sélectionnez l'une des options suivantes : **Move for SendGrid**, **Move for SparkPost** ou **Move for Amazon SES**.
3. Sélectionnez **Save**.

Après l'enregistrement, Braze envoie des instructions spéciales à l'ESP pour placer le pixel de suivi d'ouverture en haut de tous les e-mails HTML.

{% alert important %}
L'activation du SSL enveloppe l'URL du pixel de suivi avec HTTPS au lieu de HTTP. Si votre SSL est mal configuré, cela peut affecter l'efficacité du pixel de suivi.
{% endalert %}

{% alert important %}
Le suivi des clics s'applique uniquement aux liens commençant par `http://` ou `https://`. Les liens `mailto:` (par exemple `mailto:support@example.com`) ne sont pas réécrits pour le suivi.
{% endalert %}

## En-tête list-unsubscribe {#list-unsubscribe}

{% alert note %}
Depuis le 15 février 2024, les nouvelles entreprises ont l'en-tête list-unsubscribe (avec désabonnement en un clic) activé par défaut.
{% endalert %}

L'utilisation d'un en-tête list-unsubscribe permet à vos destinataires de se désabonner facilement des e-mails marketing en affichant un bouton **Se désabonner** dans l'interface de la boîte de réception, et non dans le corps du message.

Les envois de test n'incluent généralement **pas** les en-têtes list-unsubscribe. L'affichage de l'en-tête en production dépend du fournisseur de messagerie et est basé sur la réputation — une meilleure réputation d'expéditeur améliore généralement la visibilité.

![Interface de la boîte de réception d'un client de messagerie avec une option Se désabonner à côté du message, où le list-unsubscribe apparaît en dehors du corps du message.]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Lorsqu'un destinataire sélectionne **Se désabonner**, le fournisseur de messagerie envoie la demande de désabonnement à la destination définie dans l'en-tête de l'e-mail.

L'activation du list-unsubscribe est une bonne pratique de livrabilité et une exigence chez certains des principaux fournisseurs de messagerie. Elle encourage les utilisateurs finaux à se retirer en toute sécurité des messages indésirables, plutôt que d'appuyer sur le bouton spam dans un client de messagerie, ce dernier étant préjudiciable à la réputation de l'expéditeur et à la livrabilité des e-mails.

Lors de la [gestion de vos abonnements dans Gmail](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC), Gmail peut également récupérer le lien de désabonnement dans le corps du message, mais donne la priorité au list-unsubscribe s'il est présent dans l'en-tête.

### La désactivation de l'en-tête list-unsubscribe supprime-t-elle le bouton Se désabonner de Gmail ? {#does-turning-off-the-list-unsubscribe-header-remove-the-gmail-unsubscribe-button}

Non. La désactivation du paramètre d'en-tête list-unsubscribe de Braze supprime l'en-tête `List-Unsubscribe` des messages envoyés par Braze, mais ne contrôle pas si Gmail affiche une option **Se désabonner** dans l'interface de la boîte de réception. Comme indiqué ci-dessus, Gmail peut toujours afficher une option de désabonnement à partir des liens dans le corps du message ou utiliser d'autres logiques du fournisseur. La présence de l'en-tête dans le message brut est distincte de l'affichage d'une option de désabonnement par Gmail aux destinataires. Pour plus d'informations, consultez la [FAQ des directives pour les expéditeurs de Gmail](https://support.google.com/a/answer/14229414).

### Prise en charge par les fournisseurs de messagerie {#mailbox-provider-support}

Le tableau suivant résume la prise en charge par les fournisseurs de messagerie de l'en-tête « mailto: », de l'URL list-unsubscribe et du désabonnement en un clic ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| En-tête list-unsubscribe | En-tête mailto: | URL list-unsubscribe | Désabonnement en un clic (RFC 8058) |
| ----- | --- | --- | --- |
| Gmail | Pris en charge* | Pris en charge | Pris en charge |
| Gmail Mobile | Non pris en charge | Non pris en charge | Non pris en charge |
| Apple Mail | Pris en charge | Non pris en charge | Non pris en charge |
| Outlook.com | Pris en charge | Non pris en charge | Non pris en charge |
| Yahoo! Mail | Pris en charge* | Non pris en charge | Pris en charge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Prise en charge par les fournisseurs de messagerie" }

_*Yahoo et Gmail abandonnent progressivement l'en-tête « mailto: » et ne prendront en charge que le désabonnement en un clic._

L'affichage de l'en-tête est en fin de compte déterminé par le fournisseur de messagerie. Pour vérifier si l'en-tête list-unsubscribe est inclus dans l'e-mail brut (texte) pour le destinataire dans Gmail, procédez comme suit :

1. Sélectionnez **Show Original** dans l'e-mail. Cela ouvre un nouvel onglet avec la version brute de l'e-mail et ses en-têtes.
2. Recherchez « List-Unsubscribe ». Pour le désabonnement en un clic, de nombreux fournisseurs incluent également un en-tête « List-Unsubscribe-Post ». Vérifiez que les deux apparaissent dans le message brut lorsque vous vous attendez à ce que le désabonnement en un clic soit disponible.

Si l'en-tête est dans la version brute de l'e-mail mais n'est pas affiché, le fournisseur de messagerie a décidé de ne pas afficher l'option de désabonnement, ce qui signifie que nous n'avons pas plus d'informations sur la raison pour laquelle le fournisseur n'affiche pas l'en-tête. La visibilité de l'en-tête list-unsubscribe est en fin de compte basée sur la réputation. Dans la plupart des cas, meilleure est votre réputation d'expéditeur auprès du fournisseur de messagerie, plus l'en-tête list-unsubscribe a de chances d'apparaître.

### En-tête de désabonnement des e-mails dans les espaces de travail {#email-unsubscribe-header-in-workspaces}

![Sélection de « utilisateurs abonnés ou ayant donné leur accord » pour les utilisateurs à cibler.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Lorsque la fonctionnalité d'en-tête de désabonnement des e-mails est activée, ce paramètre s'applique à l'ensemble de l'espace de travail, et non au niveau de l'entreprise. Il est ajouté aux Campaigns et Canvas configurés pour envoyer aux utilisateurs abonnés ou ayant donné leur accord, ou aux utilisateurs ayant donné leur accord dans l'étape **Audience cible** des générateurs de Campaigns et Canvas.

Lors de l'utilisation de la « valeur par défaut de l'espace de travail », Braze n'ajoute pas l'en-tête de désabonnement en un clic pour les Campaigns considérées comme transactionnelles, qui sont configurées pour « envoyer à tous les utilisateurs, y compris les utilisateurs désabonnés ». Pour remplacer ce comportement et ajouter l'en-tête de désabonnement en un clic lors de l'envoi aux utilisateurs désabonnés, vous pouvez sélectionner **Unsubscribe globally from all emails** dans les paramètres de désabonnement en un clic au niveau du message.

### En-tête list-unsubscribe par défaut {#default-list-unsubscribe-header}

{% alert important %}
Gmail exige que les expéditeurs implémentent le désabonnement en un clic pour tous leurs messages commerciaux et promotionnels sortants à compter du 1er juin 2024. Pour plus d'informations, consultez les [directives pour les expéditeurs de Gmail](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) et la [FAQ des directives pour les expéditeurs de Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo a annoncé un calendrier début 2024 pour la mise à jour des exigences. Pour plus d'informations, consultez [Plus sûr, moins de spam : appliquer les normes d'e-mail pour une meilleure expérience](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Pour utiliser la fonctionnalité de désabonnement de Braze afin de traiter les désabonnements directement, sélectionnez **Include a one-click list-unsubscribe (mailto and HTTP) email header for emails sent to subscribed or opted-in users** et sélectionnez **Braze default** comme URL et mail-to standard de Braze.

![Option pour inclure automatiquement un en-tête list-unsubscribe pour les e-mails envoyés aux utilisateurs abonnés ou ayant donné leur accord.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze prend en charge les versions suivantes de l'en-tête list-unsubscribe :

| Version du list-unsubscribe | Description |
| ----- | --- |
| Un clic (RFC 8058) | Offre un moyen simple pour les destinataires de se désabonner des e-mails en un seul clic. C'est une exigence de Yahoo et Gmail pour les expéditeurs en masse. |
| URL list-unsubscribe ou HTTPS | Fournit aux destinataires un lien qui les dirige vers une page web où ils peuvent se désabonner. |
| Mailto | Spécifie une adresse e-mail comme destination pour le message de demande de désabonnement envoyé par le destinataire à la marque. <br><br> _Pour traiter les demandes de désabonnement mailto list-unsubscribe, ces demandes doivent inclure l'adresse e-mail telle qu'elle est stockée dans Braze pour l'utilisateur final qui se désabonne. Celle-ci peut être fournie par l'adresse « from » de l'e-mail à partir duquel l'utilisateur final se désabonne, le sujet encodé ou le corps encodé de l'e-mail reçu par l'utilisateur final dont il se désabonne. Dans de très rares cas, certains fournisseurs de messagerie ne respectent pas le protocole [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), ce qui empêche la transmission correcte de l'adresse e-mail. Cela peut entraîner l'impossibilité de traiter une demande de désabonnement dans Braze._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="En-tête list-unsubscribe par défaut" }

Lorsque Braze reçoit une demande de désabonnement d'un utilisateur via l'une des méthodes ci-dessus, l'état d'abonnement global aux e-mails de cet utilisateur est défini sur désabonné. S'il n'y a pas de correspondance, Braze ne traite pas cette demande.

### Désabonnement en un clic {#one-click-unsubscribe}

L'utilisation du désabonnement en un clic pour l'en-tête list-unsubscribe ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) vise à fournir un moyen simple pour les destinataires de se désabonner des e-mails.

### Désabonnement en un clic au niveau du message {#message-level-one-click-list-unsubscribe}

Le paramètre de désabonnement en un clic au niveau du message remplace la fonctionnalité d'en-tête de désabonnement des e-mails définie pour les espaces de travail. Appliquez le comportement de désabonnement en un clic par Campaign ou étape Canvas pour les utilisations suivantes :

- Ajouter un désabonnement en un clic Braze pour un groupe d'abonnement spécifique afin de prendre en charge plusieurs marques/listes au sein d'un même espace de travail
- Basculer entre le désabonnement par défaut de Braze ou une URL personnalisée
- Ajouter votre URL de désabonnement en un clic personnalisée
- Omettre le désabonnement en un clic pour ce message

{% alert note %}
Le paramètre de désabonnement en un clic au niveau du message est uniquement disponible avec l'éditeur par glisser-déposer et l'éditeur HTML mis à jour. Si vous utilisez l'ancien éditeur HTML, passez à l'éditeur HTML mis à jour pour utiliser cette fonctionnalité.
{% endalert %}

Dans votre éditeur d'e-mail, accédez à **Sending Settings** > **Sending Info**. Sélectionnez parmi les options suivantes :

- **Use workspace default** : utilise les paramètres **Email Unsubscribe Header** définis dans les **Préférences des e-mails**. Toute modification apportée à ce paramètre s'applique à tous les messages.
- **Unsubscribe globally from all emails** : utilise l'en-tête de désabonnement en un clic par défaut de Braze. Les utilisateurs qui cliquent sur le bouton de désabonnement voient leur état d'abonnement global aux e-mails défini sur « Unsubscribed ».
- **Unsubscribe from specific subscription group** : utilise le groupe d'abonnement spécifié. Braze désabonne les utilisateurs qui cliquent sur le bouton de désabonnement du groupe d'abonnement sélectionné.
    - Lors de la sélection d'un groupe d'abonnement, ajoutez le filtre **Subscription Group** dans **Target Audiences** pour cibler uniquement les utilisateurs abonnés à ce groupe spécifique. Le groupe d'abonnement sélectionné pour le désabonnement en un clic doit correspondre au groupe d'abonnement que vous ciblez. En cas de non-correspondance du groupe d'abonnement, vous risquez d'envoyer un message à un utilisateur qui tente de se désabonner d'un groupe d'abonnement dont il est déjà désabonné.

{% alert important %}
Le paramètre **Unsubscribe from specific subscription group** s'applique uniquement à l'en-tête de désabonnement en un clic. L'en-tête mailto list-unsubscribe n'est pas affecté lors de la sélection de cette option. Cela signifie qu'un destinataire qui se désabonne par cette méthode enregistre un désabonnement global, et non un désabonnement du groupe d'abonnement spécifique. Pour exclure l'en-tête mailto list-unsubscribe du désabonnement global des utilisateurs lors de la sélection de ce paramètre, contactez l'[Assistance]({{site.baseurl}}/support_contact).
{% endalert %}

- **Custom** : ajoute votre URL de désabonnement en un clic personnalisée pour que vous puissiez traiter les désabonnements directement.
- **Exclude unsubscribe**

{% alert important %}
L'exclusion du désabonnement en un clic ou de tout mécanisme de désabonnement ne doit être utilisée que pour les messages transactionnels, tels que les réinitialisations de mot de passe, les reçus et les e-mails de confirmation.
{% endalert %}

L'ajustement de ce paramètre remplace le comportement par défaut du désabonnement en un clic pour cet e-mail.

![Paramètres d'envoi dans l'éditeur d'e-mail avec les options de désabonnement en un clic au niveau du message, y compris la valeur par défaut de l'espace de travail et l'URL personnalisée.]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Exigences {#requirements}

Si vous envoyez des e-mails avec votre propre fonctionnalité de désabonnement personnalisée, vous devez respecter les exigences suivantes pour vous assurer que l'URL de désabonnement en un clic que vous avez configurée est conforme à la RFC 8058 :

* L'URL doit être capable de traiter les requêtes POST de désabonnement.
* L'URL doit commencer par `https://`.
* L'URL ne doit pas retourner de redirection HTTPS ni de corps de réponse. Les liens de désabonnement en un clic qui mènent à une page de destination ou à un autre type de page web ne sont pas conformes à la RFC 8058.
* Les requêtes POST ne doivent pas définir de cookies.

Sélectionnez **Custom list-unsubscribe header** pour ajouter votre propre endpoint de désabonnement en un clic configuré, et un « mailto: » optionnel. Braze exige une saisie pour l'URL afin de prendre en charge un en-tête list-unsubscribe personnalisé, car le désabonnement en un clic HTTP est une exigence de Yahoo et Gmail pour les expéditeurs en masse.

![Préférences des e-mails avec les champs d'en-tête list-unsubscribe personnalisé pour une URL de désabonnement en un clic et un mailto optionnel.]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Ajouter un préfixe aux lignes d'objet des e-mails {#append-email-subject-lines}

Utilisez le bouton pour inclure « [TEST] » et « [SEED] » dans les lignes d'objet de vos e-mails de test et initiateurs. Cela peut aider à identifier les campagnes d'e-mail envoyées en tant que tests.

![Bouton de préférence d'e-mail de l'espace de travail qui ajoute les préfixes TEST et SEED aux lignes d'objet des e-mails de test et initiateurs.]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## Insertion CSS par défaut pour les nouveaux e-mails {#inline-css-on-new-emails-by-default}

L'insertion CSS est une technique qui intègre automatiquement les styles CSS pour vos e-mails et nouveaux e-mails. Pour certains clients de messagerie, cela peut améliorer le rendu de vos e-mails.

La modification de ce paramètre n'affecte aucun de vos messages ou modèles d'e-mail existants. Vous pouvez remplacer cette valeur par défaut à tout moment lors de la composition de messages ou de modèles. Pour plus d'informations, consultez [Insertion CSS]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline).

## Réabonner les utilisateurs lorsque leur e-mail change {#resubscribe-users-when-their-email-changes}

Vous pouvez automatiquement réabonner les utilisateurs lorsqu'ils changent leur adresse e-mail. Par exemple, si un utilisateur d'espace de travail précédemment désabonné change son adresse e-mail pour une adresse qui ne figure pas sur la liste de désabonnement de Braze, il sera automatiquement réabonné.

![Paramètre de l'espace de travail qui réabonne automatiquement les utilisateurs lorsque leur adresse e-mail change.]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Pages et pieds de page d'abonnement {#subscription-pages-and-footers}

{% tabs local %}
{% tab Pied de page personnalisé %}

Pour les e-mails commerciaux, la [loi CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que tous les e-mails commerciaux incluent une option de désabonnement. Avec les paramètres de pied de page personnalisé, vous pouvez rester conforme à la loi CAN-SPAM tout en personnalisant votre pied de page de désabonnement. Pour rester conforme, vous devez ajouter votre pied de page personnalisé à tous les e-mails envoyés dans le cadre des Campaigns de cet espace de travail.

Notez les exigences suivantes lors de la création d'un pied de page personnalisé pour vos e-mails :
- Doit inclure une URL de désabonnement et une adresse postale physique.
- Doit faire moins de 100 Ko.

![Éditeur de pied de page d'e-mail personnalisé avec les champs de lien de désabonnement et d'adresse postale pour la conformité CAN-SPAM.]({% image_buster /assets/img/email_settings/custom_footer.png %})

Pour en savoir plus sur le templating Liquid des pieds de page personnalisés, consultez [Pieds de page personnalisés]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions).

{% endtab %}
{% tab Page de désabonnement personnalisée %}

Braze vous permet de définir une **Page de désabonnement personnalisée** avec votre propre HTML. Cette page apparaît après qu'un utilisateur a choisi de se désabonner en bas d'un e-mail. Notez que cette page doit faire moins de 750 Ko.

![Éditeur HTML et prévisualisation de la page de désabonnement personnalisée affichée après qu'un utilisateur se désabonne d'un e-mail.]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Pour les bonnes pratiques de gestion des listes d'e-mails, consultez [Gérer les abonnements aux e-mails]({{site.baseurl}}/user_guide/channels/email/faq#unsubscribed-email-addresses).

{% endtab %}
{% tab Page d'abonnement personnalisée %}

Vous pouvez créer une page d'abonnement personnalisée en utilisant votre propre HTML. L'inclusion de cette page dans vos e-mails peut être particulièrement bénéfique si vous souhaitez que votre image de marque et votre message restent cohérents tout au long du cycle de vie de l'utilisateur. Notez que cette page doit faire moins de 750 Ko.

![Éditeur HTML et prévisualisation de la page d'abonnement personnalisée pour la confirmation d'abonnement aux e-mails avec votre image de marque.]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Pour les bonnes pratiques de gestion des listes d'e-mails, consultez [Gérer les abonnements aux e-mails]({{site.baseurl}}/user_guide/channels/email/faq#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

{% alert tip %}
Dans la section **Prévisualisation** d'une page d'abonnement ou d'un pied de page, sélectionnez **Copy preview link** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemble le pied de page de l'e-mail, la page de désabonnement ou la page d'abonnement pour un utilisateur aléatoire. Le lien est valide pendant sept jours avant de devoir être régénéré.
{% endalert %}

## Questions fréquemment posées {#frequently-asked-questions}

### Désabonnement en un clic

{% details L'URL de désabonnement en un clic (via l'en-tête list-unsubscribe) peut-elle renvoyer vers un centre de préférences ? %}
Non, cela ne respecte pas la RFC 8058, ce qui signifie que vous ne serez pas conforme aux exigences de désabonnement en un clic de Yahoo et Gmail.
{% enddetails %}

{% details Pourquoi est-ce que je reçois le message d'erreur « Le corps de votre e-mail ne contient pas de lien de désabonnement » lors de la composition de mon centre de préférences ? %}
Un centre de préférences n'est pas considéré comme un lien de désabonnement. Vos destinataires d'e-mails doivent avoir la possibilité de se désabonner de tout e-mail commercial pour rester conforme à la loi CAN-SPAM.
{% enddetails %}

{% details Dois-je modifier les Campaigns d'e-mail et Canvas existants pour appliquer le paramètre de désabonnement en un clic après l'avoir activé ? %}
Si vous n'avez aucun des cas d'utilisation pour le paramètre de désabonnement en un clic au niveau du message, aucune action n'est requise tant que le paramètre est activé dans les **Préférences des e-mails**. Braze ajoute automatiquement les en-têtes de désabonnement en un clic à tous les messages marketing et promotionnels sortants. Cependant, si vous devez configurer le comportement de désabonnement en un clic au niveau de chaque message, vous devez mettre à jour les Campaigns d'e-mail et les étapes Canvas existantes en conséquence.
{% enddetails %}

{% details Je peux voir l'en-tête list-unsubscribe et de désabonnement en un clic dans le message original ou les données brutes, mais pourquoi ne vois-je pas le bouton Se désabonner dans Gmail ou Yahoo ? %}
Gmail et Yahoo décident en fin de compte d'afficher ou non l'en-tête list-unsubscribe ou de désabonnement en un clic. Pour les nouveaux expéditeurs ou les expéditeurs ayant une faible réputation, cela peut occasionnellement empêcher l'affichage du bouton de désabonnement.
{% enddetails %}

{% details L'en-tête de désabonnement en un clic personnalisé prend-il en charge Liquid ? %}
Oui, Liquid et la logique conditionnelle sont pris en charge pour permettre des URL de désabonnement en un clic dynamiques dans l'en-tête.
{% enddetails %}

{% alert tip %}
Si vous ajoutez une logique conditionnelle, évitez les valeurs de sortie qui ajoutent des espaces à votre URL, car Braze ne supprime pas ces espaces.
{% endalert %}

### Désabonnement en un clic au niveau du message

{% details Si j'ajoute manuellement les en-têtes d'e-mail pour le désabonnement en un clic et que l'en-tête de désabonnement des e-mails est activé, quel est le comportement attendu ? %}
Les en-têtes d'e-mail ajoutés pour le désabonnement en un clic s'appliquent à tous les envois futurs de cette Campaign.
{% enddetails %}

{% details Pourquoi les groupes d'abonnement doivent-ils correspondre entre les variantes de message pour le lancement ? %}
Pour une Campaign avec test A/B, Braze envoie aléatoirement à un utilisateur l'une des variantes. Si vous avez deux groupes d'abonnement différents définis sur la même Campaign (la variante A est définie sur le groupe d'abonnement A, et la variante B est définie sur le groupe d'abonnement B), nous ne pouvons pas garantir que les utilisateurs abonnés uniquement au groupe d'abonnement B recevront la variante B. Il peut y avoir un scénario où des utilisateurs se désabonnent d'un groupe d'abonnement dont ils se sont déjà retirés.
{% enddetails %}

{% details Le paramètre d'en-tête de désabonnement des e-mails est désactivé dans les Préférences des e-mails, mais dans les informations d'envoi de ma Campaign, le paramètre de désabonnement en un clic est défini sur « Use workspace default ». Est-ce un bug ? %}
Non. Si le paramètre de l'espace de travail est désactivé et que le paramètre du message est défini sur **Use workspace default**, alors Braze suit ce qui est configuré dans les **Préférences des e-mails**. Cela signifie que nous n'ajoutons pas l'en-tête de désabonnement en un clic pour la Campaign.
{% enddetails %}

{% details Que se passe-t-il si un groupe d'abonnement est archivé ? Cela casse-t-il le désabonnement en un clic sur les e-mails envoyés ? %}
Si un groupe d'abonnement référencé dans les **Sending Info** pour le désabonnement en un clic est archivé, Braze continue de traiter les désabonnements en un clic. Le groupe d'abonnement n'apparaît plus dans le tableau de bord (filtre de segment, profil utilisateur et zones similaires).
{% enddetails %}

{% details Le paramètre de désabonnement en un clic est-il disponible pour les modèles d'e-mail ? %}
Non, nous n'avons actuellement pas prévu d'ajouter cette fonctionnalité pour les modèles d'e-mail, car ces modèles ne sont pas associés à un domaine d'envoi. Si cette fonctionnalité vous intéresse pour les modèles d'e-mail, soumettez un [retour produit]({{site.baseurl}}/user_guide/administer/personal/product_portal).
{% enddetails %}

{% details Cette fonctionnalité vérifie-t-elle que l'URL de désabonnement en un clic ajoutée à l'option personnalisée est valide ? %}
Non, nous ne vérifions ni ne validons aucun lien dans le tableau de bord de Braze. Assurez-vous de tester correctement votre URL avant le lancement.
{% enddetails %}