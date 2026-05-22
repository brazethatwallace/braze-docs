---
nav_title: FAQ
article_title: FAQ sur les e-mails
page_order: 30
description: "Cette page fournit des réponses aux questions fréquemment posées sur l'envoi de messages par e-mail."
channel: email

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article fournit des réponses à certaines questions fréquemment posées sur les e-mails.

### Que se passe-t-il lorsqu'un e-mail est envoyé et que plusieurs profils partagent la même adresse e-mail ? {#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address}

Si plusieurs utilisateurs ayant la même adresse e-mail se trouvent dans un segment destiné à recevoir une campagne, un profil utilisateur aléatoire associé à cette adresse e-mail est sélectionné au moment de l'envoi. Ainsi, l'e-mail n'est envoyé qu'une seule fois et dédupliqué, ce qui garantit qu'il n'atteint pas la même adresse e-mail plusieurs fois.

**Adresses e-mail uniques :** Braze n'impose pas l'unicité des adresses e-mail entre les profils. Si vous vous appuyez sur une relation un-à-un entre une adresse e-mail et un profil, surveillez les doublons en interne lors de la création des utilisateurs.

**Déduplication avant Liquid :** Pour les envois où Braze déduplique par adresse e-mail au sein d'un même envoi (par exemple, les campagnes planifiées où plusieurs membres du segment ayant la même adresse sont traités ensemble), cette déduplication se produit avant l'exécution de Liquid pour le profil choisi pour représenter cette adresse. Si Liquid interrompt l'envoi pour ce profil (par exemple avec [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)), cette adresse ne reçoit pas le message lors de cet envoi — y compris les profils déjà ignorés par la déduplication. Les envois déclenchés n'appliquent pas cette même déduplication par adresse au sein d'un envoi ; plusieurs profils partageant une adresse peuvent tous rester éligibles dans un même lot, de sorte que ce comportement d'interruption ne s'applique pas de la même manière (voir le paragraphe suivant).

Si plusieurs profils partagent une adresse e-mail et qu'un profil se désabonne, Braze met à jour les autres profils (jusqu'à 100) associés à cette adresse vers le même état d'abonnement. Cela s'applique aux désabonnements et aux autres modifications telles que l'état d'abonnement global et les statuts individuels des groupes d'abonnement.

**Groupes initiateurs :** Pour les campagnes avec des [groupes initiateurs]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#seed-groups), Braze sélectionne un profil pour la distribution principale lorsque plusieurs profils partagent une adresse. Ce destinataire principal peut ne pas faire partie de votre groupe initiateur, même si un autre profil ayant la même adresse en fait partie.

Les scénarios suivants peuvent donner l'impression qu'un utilisateur a reçu un e-mail deux fois :

- **Une erreur s'est produite lors de la création de la campagne ou du Canvas :** L'utilisateur peut ne pas recevoir littéralement le même envoi deux fois, mais peut recevoir deux e-mails distincts avec la même ligne d'objet. Lorsqu'une campagne ou un Canvas est dupliqué(e), vérifiez les détails de configuration de l'e-mail tels que les images ou les lignes d'objet. Vous pouvez également consulter les journaux des modifications pour voir si la campagne ou le Canvas a été modifié(e) après le lancement — un doublon peut partager la même ligne d'objet que l'original au moment où l'utilisateur l'a reçu.
- **Plusieurs profils utilisateur ont un transfert d'e-mails :** Si un utilisateur possède plusieurs comptes dans une application donnée mais qu'un compte transfère les e-mails, l'utilisateur reçoit la campagne une fois par boîte de réception ; le courrier peut apparaître deux fois dans la boîte de réception où les messages sont transférés. Seuls certains fournisseurs indiquent quand un e-mail a été transféré depuis un autre compte.
- **Configuration de l'e-mail chez le destinataire :** Certains clients fusionnent les boîtes de réception (« boîte de réception universelle »). Si la même campagne cible plusieurs comptes partageant une seule boîte de réception, cela peut donner l'impression qu'une personne a reçu la campagne deux fois alors que deux profils distincts ont effectivement été contactés. Le destinataire peut confirmer si plusieurs comptes sont combinés dans une seule boîte de réception.

Cette déduplication s'applique lorsque les utilisateurs ciblés sont inclus dans le même envoi. La rééligibilité est évaluée par profil, et non par adresse e-mail.

La rééligibilité des campagnes e-mail et des étapes de Canvas utilise le profil de chaque utilisateur — et non la boîte de réception — de sorte que plusieurs profils peuvent être éligibles à des envois distincts tant que cette logique est satisfaite. Combiné avec des déclencheurs, cela peut entraîner la distribution de plus d'un message à la même boîte de réception, même lorsque vous essayez de respecter une seule période d'inéligibilité au niveau de l'adresse. Les campagnes déclenchées (à l'exception des campagnes déclenchées par API) et les Canvas peuvent également envoyer deux fois à la même adresse lorsque différents profils ayant la même adresse e-mail déclenchent l'événement à des moments différents — par exemple, si l'utilisateur A et l'utilisateur B partagent l'adresse `johndoe@example.com` mais se trouvent dans des fuseaux horaires différents alors que la distribution utilise les fuseaux horaires locaux.

Les utilisateurs ne sont pas dédupliqués par e-mail à l'entrée du Canvas, ils peuvent donc ne pas être dédupliqués au-delà de la première étape d'un Canvas s'ils progressent à des moments légèrement différents en raison d'une entrée limitée en débit. Lorsqu'un utilisateur associé à une adresse e-mail donnée ouvre ou clique sur un e-mail, tous les profils utilisateur partageant cette adresse e-mail sont marqués comme ayant ouvert ou cliqué sur la campagne.

#### Exception : campagnes déclenchées par API {#exception-api-triggered-campaigns}

Les campagnes déclenchées par API dédupliquent ou envoient des doublons selon l'endroit où l'audience est définie. Les e-mails en double doivent être ciblés séparément dans l'appel API en utilisant des `user_ids` distincts pour recevoir plusieurs distributions. Voici trois scénarios possibles pour les campagnes déclenchées par API :

- **Scénario 1 : E-mails en double dans le segment cible :** Si le même e-mail apparaît dans plusieurs profils utilisateur regroupés dans les filtres d'audience du tableau de bord pour une campagne déclenchée par API, un seul des profils reçoit l'e-mail.
- **Scénario 2 : E-mails en double dans différents `user_ids` au sein de l'objet recipients :** Si le même e-mail apparaît dans plusieurs valeurs `external_user_id` référencées par l'objet `recipients`, l'e-mail est envoyé deux fois.
- **Scénario 3 : E-mails en double en raison de `user_ids` dupliqués au sein de l'objet recipients :** Si vous essayez d'ajouter le même profil utilisateur deux fois, un seul des profils reçoit l'e-mail.

{% alert important %}
Si vous envoyez une campagne API via un appel API (à l'exception des campagnes déclenchées par API) et que plusieurs utilisateurs sont spécifiés dans l'audience du segment avec la même adresse e-mail, l'envoi est effectué à cette adresse autant de fois qu'elle est listée dans l'appel. En effet, les appels API sont considérés comme intentionnellement construits.
{% endalert %}

### Que se passe-t-il pour l'état d'abonnement lorsque l'adresse e-mail d'un utilisateur est modifiée vers une adresse partagée par un autre utilisateur ? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

Si vous définissez ou mettez à jour l'adresse e-mail de l'utilisateur A vers une autre adresse e-mail partagée par un utilisateur B existant, l'utilisateur A hérite de l'état d'abonnement déjà existant de l'utilisateur B, sauf si le paramètre **Resubscribe users when they update their email** est activé.

### Les mises à jour de mes paramètres d'e-mails sortants s'appliqueront-elles rétroactivement ? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

Non. Les mises à jour apportées aux paramètres d'e-mails sortants ne s'appliquent pas rétroactivement aux envois existants. Par exemple, modifier votre nom d'affichage par défaut dans les paramètres d'e-mails ne remplacera pas automatiquement le nom d'affichage par défaut existant dans vos campagnes ou Canvas actifs.

### Qu'est-ce qu'un « bon » taux de distribution des e-mails ? {#what-is-a-good-email-delivery-rate}

En général, le « chiffre magique » se situe autour de 98 % de messages distribués avec un taux de rebond ne dépassant pas 3 %. Si votre taux de distribution descend en dessous de ce seuil, il y a généralement lieu de s'inquiéter.

Cependant, un taux supérieur à 98 % peut tout de même présenter des problèmes de livrabilité. Par exemple, si tous vos rebonds proviennent d'un seul domaine, c'est un signal clair d'un problème de réputation avec ce fournisseur.

De plus, les messages peuvent être distribués mais finir dans les courriers indésirables, ce qui indique des problèmes de réputation potentiellement graves. Il est important de surveiller non seulement le nombre de messages distribués, mais aussi les taux d'ouverture et de clics pour déterminer si les utilisateurs voient réellement les messages dans leur boîte de réception. Étant donné que les fournisseurs ne signalent généralement pas chaque instance de courrier indésirable, un taux de spam même de 1 % pourrait être préoccupant et nécessiter une analyse plus approfondie.

Enfin, votre activité et les types d'e-mails que vous envoyez peuvent également affecter la distribution. Par exemple, quelqu'un qui envoie principalement des [e-mails transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) devrait s'attendre à un meilleur taux que quelqu'un qui envoie de nombreux messages marketing.

### Pourquoi mes indicateurs de distribution d'e-mails ne totalisent-ils pas 100 % ? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

Les indicateurs de distribution d'e-mails (distributions, rebonds et taux de spam) peuvent ne pas totaliser 100 % en raison des e-mails ayant subi un échec provisoire d'envoi et n'ayant pas été distribués après la période de nouvelle tentative pouvant aller jusqu'à 72 heures.

Les échecs provisoires d'envoi sont des e-mails qui rebondissent en raison d'un problème temporaire ou transitoire, comme « boîte aux lettres pleine », « serveur temporairement indisponible », etc. Si un e-mail ayant subi un échec provisoire d'envoi n'est toujours pas distribué après 72 heures, cet e-mail ne sera pas comptabilisé dans les indicateurs de distribution de la campagne.

### Qu'est-ce qu'une boucle de rétroaction par e-mail ? {#what-is-an-email-feedback-loop}

Une boucle de rétroaction par e-mail (FBL) permet aux expéditeurs de surveiller leur réputation en identifiant les campagnes qui reçoivent un volume élevé de plaintes. Pour les étapes de mise en œuvre d'une boucle de rétroaction Gmail, consultez l'article [Boucle de rétroaction de Google](https://support.google.com/a/answer/6254652).

### Que sont les pixels de suivi d'ouverture ? {#what-are-open-tracking-pixels}

Les [pixels de suivi d'ouverture]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#changing-location-of-tracking-pixel) utilisent le domaine de suivi des clics de l'expéditeur pour suivre les événements d'ouverture d'e-mails. Le pixel est une balise image ajoutée au HTML de l'e-mail. Il s'agit le plus souvent du dernier élément HTML dans la balise body. Lorsqu'un utilisateur charge son e-mail, une requête est effectuée pour charger l'image depuis le domaine de suivi personnalisé, ce qui enregistre un événement d'ouverture.

### Que se passe-t-il lorsqu'une campagne e-mail ou un Canvas est arrêté(e) ? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

Les utilisateurs ne peuvent plus entrer dans le Canvas et aucun message supplémentaire n'est envoyé.

Pour les campagnes e-mail et les Canvas, le bouton d'arrêt ne stoppe pas immédiatement l'envoi. Lorsque les demandes d'envoi sont transmises, elles ne peuvent pas être empêchées d'être distribuées à l'utilisateur, ce qui peut se produire après un certain délai.

Bien que Braze n'envoie plus de demandes une fois la campagne ou le Canvas arrêté(e), les analyses peuvent encore augmenter pendant que l'ESP termine le traitement des demandes déjà en cours.

### Pourquoi est-ce que je vois plus de _Clics totaux_ que d'_Ouvertures totales_ dans mes analyses d'e-mails ? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

_Ouvertures totales_ correspond au nombre de fois où l'e-mail a été ouvert par les utilisateurs, tandis que _Clics totaux_ correspond au nombre de fois où les utilisateurs ont cliqué dans l'e-mail distribué, y compris tout type de clics tels que les clics sur les liens. Vous pouvez voir plus de clics que d'ouvertures pour l'une des raisons suivantes :

- Les utilisateurs effectuent plusieurs clics dans le corps de l'e-mail au cours d'une seule ouverture.
- Les utilisateurs cliquent sur certains liens de l'e-mail dans le volet de prévisualisation de leur téléphone. Dans ce cas, Braze enregistre cet e-mail comme cliqué mais pas ouvert.
- Les utilisateurs rouvrent un e-mail qu'ils avaient prévisualisé précédemment.

### Pourquoi est-ce que je vois zéro ouverture et clic d'e-mails ? {#why-am-i-seeing-zero-email-opens-and-clicks}

Vous pouvez ne voir aucune ouverture ou clic d'e-mail s'il y a une mauvaise configuration de votre domaine de suivi. Cela peut être dû à l'une des raisons suivantes :
- Il y a un problème SSL où les URL de suivi sont en `http` au lieu de `https`.
- Il y a un problème avec votre réseau de diffusion de contenu où la chaîne user agent sur les événements d'ouverture, les événements de clic, ou les deux, ne se renseigne pas.

### Quels sont les risques potentiels de déclenchement de clics par les serveurs ? {#what-are-the-potential-risks-of-triggering-server-clicks}

Certains éléments d'un message e-mail, tels que des messages trop longs ou trop de points d'exclamation, peuvent déclencher des réponses de sécurité des e-mails. Ces réponses peuvent affecter les rapports et la réputation IP et amener les utilisateurs à se désabonner.

Pour les bonnes pratiques sur la gestion de ces réponses, consultez [Gérer les augmentations des taux de clics]({{site.baseurl}}/user_guide/channels/email/reporting/).

### Braze peut-il suivre les liens de désabonnement comptabilisés dans l'indicateur « Désabonnement » ? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

Braze suit les liens de désabonnement si le Liquid suivant est utilisé dans les e-mails : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Pourquoi est-ce que je vois un nombre de désabonnements différent du nombre de clics sur mon lien de désabonnement ? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

S'il y a plus de _Désabonnements_ que d'utilisateurs ayant cliqué sur le lien de désabonnement dans le corps de l'e-mail, le [**List-unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#list-unsubscribe) explique souvent l'écart. Le list-unsubscribe est un chemin de désabonnement supplémentaire dans l'en-tête de l'e-mail (et non le lien dans le corps de votre message). Lorsqu'un utilisateur se désabonne de cette manière, cela est comptabilisé dans les _Désabonnements_ mais ne compte pas comme un clic sur l'URL de désabonnement suivie dans le corps.

Si le nombre total de clics sur le lien de désabonnement dans le corps est supérieur au nombre de _Désabonnements_, les utilisateurs ont peut-être cliqué sur le lien plus d'une fois — par exemple, s'ils se sont désabonnés, réabonnés, puis désabonnés à nouveau, les analyses d'e-mails peuvent enregistrer plusieurs clics dans la ventilation des clics.

Si un utilisateur clique deux fois sur le lien de désabonnement (par exemple, s'il s'est désabonné, réabonné, puis désabonné à nouveau), cela est comptabilisé deux fois dans les analyses d'e-mails.

### Puis-je ajouter un lien « voir cet e-mail dans un navigateur » à mes e-mails ? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Non. Braze ne propose pas cette fonctionnalité. En effet, une majorité croissante des e-mails est ouverte sur des appareils mobiles et dans des clients de messagerie modernes, qui affichent les images et le contenu sans problème.

**Solution de contournement :** Pour obtenir le même résultat, vous pouvez héberger le contenu de votre e-mail sur une page externe (comme votre site web), puis y renvoyer depuis la campagne e-mail que vous créez en utilisant l'outil **Link** lors de la modification du corps de l'e-mail.

### Braze convertit-il automatiquement les URL en texte brut ou le texte « www. » en liens ? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

Non. Braze n'analyse pas votre message et ne convertit pas le texte brut, comme le texte commençant par `www.` ou ressemblant à une URL, en hyperliens. Seuls les liens que vous définissez avec des balises d'ancrage HTML (`<a href="...">`) sont traités par le rendu normal et les fonctionnalités de liens dans Braze.

Si un destinataire voit du texte brut affiché comme un lien cliquable, ce comportement provient généralement de son client de messagerie (par exemple, Gmail, Outlook ou Apple Mail). De nombreux clients détectent les chaînes ressemblant à des URL après la distribution du message et les transforment en liens sur l'appareil du destinataire. Braze ne contrôle pas ce comportement et ne peut pas le désactiver pour le destinataire.

Pour une apparence, un suivi et un style de liens prévisibles, utilisez des balises `<a href>` explicites au lieu d'URL en texte brut.

### Pourquoi mes utilisateurs sont-ils automatiquement désabonnés par un logiciel de sécurité des e-mails ? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

Certains outils de sécurité des e-mails d'entreprise (tels que Barracuda, Proofpoint et services similaires) pré-chargent ou analysent toutes les URL des e-mails entrants, y compris les liens de désabonnement. Cela peut provoquer des désabonnements involontaires lorsque l'outil de sécurité suit le lien de désabonnement en un clic (list-unsubscribe).

Pour atténuer ce problème :

- **Recommandez aux destinataires d'ajouter votre domaine d'envoi à leur liste d'autorisation :** Travaillez avec les équipes informatiques des destinataires concernés pour ajouter votre domaine d'envoi et les domaines de suivi Braze à leur liste d'autorisation de sécurité des e-mails.
- **Utilisez un centre de préférences :** Au lieu d'un lien de désabonnement direct, utilisez un [centre de préférences]({{site.baseurl}}/user_guide/channels/email/subscriptions/) qui nécessite une interaction de l'utilisateur pour confirmer l'action de désabonnement. Les scanners de sécurité ne complètent généralement pas les formulaires à plusieurs étapes.
- **Examinez les journaux de désabonnement :** Vérifiez l'en-tête `User-Agent` et l'adresse IP dans vos données d'événements de désabonnement Currents pour identifier des schémas cohérents avec une analyse automatisée (tels que des en-têtes `User-Agent` identiques sur plusieurs désabonnements).

Pour plus de détails sur la façon dont l'analyse côté serveur peut affecter les indicateurs d'e-mails, consultez [Gérer les augmentations des taux de clics]({{site.baseurl}}/user_guide/channels/email/reporting/#handling-increases-in-click-rates).

### Pourquoi mon taux d'ouvertures automatiques a-t-il changé de manière inattendue ? {#why-has-my-machine-open-rate-changed-unexpectedly}

Les [ouvertures automatiques]({{site.baseurl}}/user_guide/analytics/metrics_glossary/#machine-opens) sont déclenchées par des fonctionnalités de sécurité des e-mails telles que la protection de la confidentialité dans Mail d'Apple (MPP), qui pré-charge le contenu de l'e-mail (y compris le pixel de suivi) sans que l'utilisateur n'ouvre physiquement l'e-mail. Les taux d'ouvertures automatiques peuvent fluctuer en fonction de :

- L'évolution de la proportion de votre audience utilisant Apple Mail ou d'autres clients de messagerie avec protection de la confidentialité.
- Les mises à jour des fonctionnalités de confidentialité des fournisseurs de messagerie ou des comportements de détection de bots.
- Les modifications de votre segmentation ou de votre ciblage d'audience.

Les pourcentages d'ouvertures automatiques ne sont pas une mesure fiable de l'engagement réel. Pour une vision plus précise des performances des e-mails, concentrez-vous sur les *Autres ouvertures* (ouvertures non automatiques) et les *Clics uniques*. Vous pouvez également comparer ces indicateurs dans le temps en utilisant le [tableau de bord des performances des e-mails]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance/).

### Pourquoi mes liens profonds ne fonctionnent-ils pas dans Gmail ? {#why-are-my-deep-links-not-working-in-gmail}

Gmail supprime tous les liens non HTTP/HTTPS des messages e-mail. Si votre lien profond utilise un schéma personnalisé (tel que `myapp://path/to/content`), Gmail le supprimera et le lien ne fonctionnera pas pour les destinataires lisant l'e-mail dans Gmail. Il s'agit d'une limitation de Gmail, pas de Braze.

Pour contourner ce problème :

- **Utilisez les Universal Links (iOS) ou les App Links (Android).** Ceux-ci utilisent des URL `https://` standard qui ouvrent votre application lorsqu'elle est installée et renvoient vers une page web dans le cas contraire. Consultez [Universal Links et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/) pour les instructions de configuration.
- **Utilisez un fournisseur de liens profonds.** Des services comme [Branch](https://www.branch.io/) génèrent des liens profonds au format HTTP compatibles avec les clients de messagerie, y compris Gmail.
- **Configurez un endpoint de redirection.** Hébergez un endpoint `https://` sur votre serveur qui redirige vers l'URL au schéma personnalisé de votre application. Les clients de messagerie conserveront le lien `https://`, et la redirection se chargera d'ouvrir l'application.

### L'indicateur *Ouvertures uniques* inclut-il les *Ouvertures automatiques* ? {#does-the-unique-opens-metric-include-machine-opens}

Oui. Les *Ouvertures uniques* incluent les *Ouvertures automatiques*. Vous pouvez consulter les deux indicateurs dans la vue **Campaign Analytics** et le **Générateur de rapports**.

### Pourquoi mon volume de distribution d'e-mails ne correspond-il pas à mon volume d'envoi ? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

Après l'envoi d'un e-mail, la boîte de réception du destinataire décide du moment de sa distribution. Les messages peuvent être différés pendant des heures ou des jours en raison d'une boîte aux lettres pleine, d'une limitation de débit par l'ESP depuis une IP donnée, et pour des raisons similaires.

Lorsque des messages différés sont distribués un jour calendaire différent du jour d'envoi, les _Distributions_ peuvent dépasser les _Envois_ pour la même plage de dates. Lorsque de nombreux reports se concentrent sur un même jour, les _Envois_ peuvent dépasser les _Distributions_ pour cette plage.

### Pourquoi est-ce que je vois un avertissement m'invitant à inclure un lien de désabonnement alors que mon e-mail en contient déjà un ? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

Cet avertissement peut persister pour les campagnes dupliquées à partir d'une campagne qui ne comportait pas de lien de désabonnement. Pour le supprimer :

- Pour les e-mails HTML, accédez à l'onglet **Plaintext**, puis sélectionnez **Regenerate from HTML**.
- Après la duplication, dupliquez la variante, puis supprimez la variante originale. **Ne sélectionnez pas** la variante originale, sinon l'avertissement peut se propager.

### Quelles sont les raisons pour lesquelles mon utilisateur n'a pas reçu une campagne e-mail ? {#what-are-reasons-why-my-user-hasnt-received-an-email-campaign}

Les raisons pour lesquelles un utilisateur n'a pas reçu une campagne e-mail incluent :

- Il n'était pas éligible pour recevoir l'e-mail.
- Son adresse e-mail est invalide ou n'existe pas.
- Il a peut-être manqué ou supprimé le message.
- Le message se trouve peut-être dans son dossier de courriers indésirables.

### Comment puis-je optimiser les images dans Outlook ? {#how-can-i-optimize-images-in-outlook}

Outlook utilise souvent un rendu de type Microsoft Word, ce qui peut ajouter une bordure autour des images. Vous pouvez encapsuler le contenu pour le masquer dans les clients Office en utilisant des commentaires conditionnels standard, par exemple :

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Puis-je utiliser des images SVG ou WEBP dans mes messages e-mail ? {#can-i-use-svg-or-webp-images-in-my-email-messages}

Les images SVG ne s'affichent pas dans Gmail web ou Gmail iOS. Le format WEBP n'est pas pris en charge de manière cohérente par tous les clients. Utilisez plutôt des formats largement pris en charge tels que PNG ou JPEG pour que les images s'affichent de manière fiable.

### Les variables Liquid assignées dans une partie du compositeur de messages peuvent-elles être utilisées dans une autre ? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

Non. Chaque partie de l'e-mail (objet, corps, en-têtes, boutons, etc.) est générée séparément, de sorte que les variables Liquid assignées dans un champ ne sont pas disponibles dans un autre. Assignez les variables dans chaque champ qui en a besoin.

### Mon modèle d'e-mail est introuvable. Où est-il ? {#my-email-template-is-missing-where-is-it}

Accédez à **Templates** > **Email Templates**. Vous pouvez filtrer par type (HTML ou glisser-déposer).

Confirmez que vous avez l'autorisation de consulter les modèles — voir [Autorisations des utilisateurs]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).

### Dois-je enregistrer des domaines pour les e-mails relais ou masqués ? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

Le [relais d'e-mail privé d'Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO/) nécessite que vous enregistriez vos domaines d'envoi dans le portail développeur Apple pour éviter les rebonds. Google Shielded Email ne nécessite pas de processus d'enregistrement de domaine ou d'ajout à une liste d'autorisation manuel.