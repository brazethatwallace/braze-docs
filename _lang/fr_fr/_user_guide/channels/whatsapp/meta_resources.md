---
nav_title: Ressources Meta
article_title: Ressources Meta
page_order: 6
description: "Cet article fournit de la documentation, des informations et des ressources Meta utiles pour améliorer votre compréhension de l'intégration WhatsApp."
alias: /meta_resources/
page_type: reference
channel:
  - WhatsApp

---

# Ressources Meta {#meta-resources}

> Cette page fournit de la documentation Meta utile, des mises à jour produit et des questions fréquemment posées pour améliorer votre compréhension de l'intégration WhatsApp avec Braze.

## Documentation Meta {#meta-documentation}

Consultez la documentation Meta suivante pour obtenir des conseils sur les noms d'affichage, les numéros de téléphone et plus encore.

- [Conseils sur le nom d'affichage](https://www.facebook.com/business/help/757569725593362)
- [Activer Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Exigences relatives aux numéros de téléphone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Limites de messagerie](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Évaluation de la qualité](https://www.facebook.com/business/help/896873687365001)

## Mises à jour produit WhatsApp {#whatsapp-product-updates}

### 2026 : Noms d'utilisateur professionnels {#2026-business-usernames}
*Dernière mise à jour : mai 2026*

Meta introduit les noms d'utilisateur professionnels pour WhatsApp — un nom d'affichage optionnel que les entreprises peuvent adopter pour leur numéro de téléphone WhatsApp. Lorsqu'un nom d'utilisateur est défini, il apparaît dans les fenêtres de discussion de l'application WhatsApp et WhatsApp Business à la place du numéro de téléphone. Notez que l'adoption d'un nom d'utilisateur ne masque pas votre numéro de téléphone ; il reste toujours visible dans votre profil professionnel.

Les noms d'utilisateur sont uniques pour l'ensemble des numéros de téléphone WhatsApp — deux numéros, qu'ils soient personnels ou professionnels, ne peuvent pas partager le même nom d'utilisateur. Ils sont insensibles à la casse pour les besoins de l'unicité, mais les points et les tirets bas sont traités comme des caractères distincts. Par exemple, `myid`, `my.id` et `my_id` sont tous considérés comme des noms d'utilisateur différents, tandis que `myID` et `myid` sont traités comme identiques.

Les noms d'utilisateur professionnels doivent respecter les exigences de format suivantes :

- Contient uniquement des lettres anglaises (a–z), des chiffres (0–9), des points (`.`) ou des tirets bas (`_`)
- Comporte entre 3 et 35 caractères
- Contient au moins une lettre anglaise
- Ne commence ni ne se termine par un point, et ne contient pas deux points consécutifs
- Ne commence pas par `www`
- Ne se termine pas par un suffixe de domaine courant (tel que `.com`, `.org` ou `.net`)

#### Revendiquer un nom d'utilisateur réservé {#claiming-a-reserved-username}

Avant que la fonctionnalité de nom d'utilisateur soit largement disponible, Meta peut avoir pré-réservé un nom d'utilisateur pour votre entreprise — correspondant généralement à un nom de page Facebook ou un nom d'utilisateur Instagram existant. Vous pouvez revendiquer ce nom d'utilisateur réservé ou en choisir un autre via [WhatsApp Manage](https://business.facebook.com/wa/manage/). Les noms d'utilisateur revendiqués ne sont pas activés tant que Meta n'a pas rendu la fonctionnalité disponible.

Si le nom d'utilisateur réservé correspond à un nom déjà associé à votre page Facebook ou votre compte Instagram, vous devez d'abord lier votre numéro de téléphone professionnel à cette page ou ce compte. Vous pouvez le faire lors de la revendication du nom d'utilisateur dans WhatsApp gestionnaire ou Meta Business Suite, ou en ajoutant votre numéro de téléphone directement depuis la page ou le compte concerné. La liaison nécessite soit un contrôle total de la page ou du compte, soit un accès partiel de base avec la permission `manage_phone`.

#### Priorité d'affichage dans les fenêtres de discussion {#display-priority-in-chat-windows}

Lorsque votre profil professionnel apparaît dans une fenêtre de discussion, WhatsApp utilise l'ordre de priorité suivant (du plus élevé au plus bas) :

1. Nom du contact enregistré
2. Nom d'entreprise vérifié ou nom de compte professionnel officiel (OBA)
3. Nom d'utilisateur
4. Numéro de téléphone

Pour plus d'informations, consultez la documentation de Meta sur les [noms d'utilisateur professionnels](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/#business-usernames).

### Avril 2026 : Archivage automatique des modèles inactifs {#april-2026-automatic-archival-of-inactive-templates}
*Dernière mise à jour : avril 2026*

- Meta archive automatiquement les modèles inactifs depuis 12 mois ou plus.
- L'archivage automatique est activé pour tous les comptes WhatsApp Business et ne peut pas être désactivé.
- L'activité d'un modèle inclut la création, la modification, l'envoi, la contestation ou la désarchivation d'un modèle.
- Les modèles archivés ne peuvent pas être envoyés et sont programmés pour une suppression définitive après 28 jours.
- Vous pouvez désarchiver les modèles dans la fenêtre de 28 jours pour les restaurer et annuler la suppression programmée.
- Les notifications sont envoyées via le webhook `message_template_status_update`, par e-mail et par une bannière unique dans WhatsApp gestionnaire.

Pour plus d'informations, consultez la documentation de Meta sur l'[archivage des modèles](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-archival).

### Juin 2026 : Identifiants utilisateur au niveau de l'entreprise {#june-2026-business-scoped-user-ids}
*Dernière mise à jour : mars 2026*

- Meta introduit des identifiants utilisateur pour remplacer le partage de numéros de téléphone pour des raisons de confidentialité
- Braze travaille sur une solution en amont du déploiement
- Déploiement prévu par Meta en juin 2026

### Novembre 2025 : [API de messages marketing pour WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (anciennement API Marketing Messages Lite) {#november-2025-marketing-messages-api-for-whatsapp-formerly-marketing-messages-lite-api}
*Dernière mise à jour : mars 2026*

- Remplace les limites statiques de l'API Cloud par des limites dynamiques basées sur l'engagement
- Non disponible en EMEA, au Japon ou en Corée du Sud pour la distribution optimisée
- Les messages utilitaires et d'authentification continuent automatiquement via l'API Cloud

### Octobre 2025 : Changement du processus d'approbation du compte professionnel officiel (OBA) {#october-2025-official-business-account-oba-approval-process-changed}
*Dernière mise à jour : mars 2026*

- Auparavant ouvert à tous les clients via WhatsApp gestionnaire
- Désormais restreint aux : gouvernements/grands annonceurs Meta, annonceurs directs, ou via un BSP comme Braze (jusqu'à 5 par semaine)
- Nouveaux prérequis : vérification de l'entreprise, vérification en deux étapes, nom d'affichage approuvé, notoriété
- Contactez votre CSM or gestionnaire de la satisfaction client or gestionnaire du succès des clients pour obtenir de l'aide

### Octobre 2025 : Réduction des tarifs régionaux {#october-2025-regional-pricing-rate-cuts}
*Dernière mise à jour : mars 2026*

- Tarifs utilitaires/authentification réduits en Argentine, Égypte, Mexique et Amérique du Nord
- Tarifs marketing réduits au Mexique (en vigueur à partir du 1er octobre 2025)

### Octobre 2025 : Les limites d'envoi passent du niveau par téléphone au niveau par portefeuille d'entreprise {#october-2025-messaging-limits-change-from-per-phone-to-per-business-portfolio}
*Dernière mise à jour : mars 2026*

- Les limites sont désormais partagées entre tous les numéros de téléphone d'un portefeuille
- Les portefeuilles héritent de la limite existante la plus élevée
- Accès plus rapide aux limites supérieures (dans les 6 heures)
- Risque : les entreprises sans numéro « illimité » peuvent voir leurs limites agrégées diminuer

### 1er juillet 2025 : Refonte de la tarification {#july-1-2025-pricing-overhaul}
*Dernière mise à jour : mars 2026*

- La facturation par message a remplacé la facturation par conversation
- Les messages utilitaires envoyés dans une fenêtre de service de 24 heures sont devenus gratuits
- Tarifs utilitaires/authentification mis à jour sur plusieurs marchés, avec de nouveaux paliers de volume
- Nouvelles règles sur la catégorisation incorrecte des modèles utilitaires — les entreprises peuvent faire face à un rejet de modèle et à des restrictions de soumission

### Avril 2025 : Pause des messages marketing vers les numéros de téléphone américains {#april-2025-pause-of-marketing-messages-to-us-phone-numbers}
*Dernière mise à jour : août 2026*

Meta suspend les nouvelles conversations marketing initiées par les entreprises avec les utilisateurs WhatsApp possédant un numéro de téléphone américain (un numéro composé de l'indicatif `+1` et d'un indicatif régional américain). Il n'y a actuellement aucune date prévue pour la levée de cette pause.

Les modèles marketing peuvent toujours être envoyés pendant une fenêtre de conversation ouverte et initiée par l'utilisateur, comme une fenêtre de service client de 24 heures ou une fenêtre de point d'entrée gratuit de 72 heures ouverte par une [publicité qui redirige vers WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/ads_that_click_to_whatsapp#considerations). En dehors de ces fenêtres, les tentatives d'envoi de modèles marketing vers des numéros de téléphone américains génèrent l'erreur `131049`. Les messages utilitaires, d'authentification, de service et les réponses restent disponibles.

### Mars 2025 : Restrictions pour mauvaise catégorisation des modèles {#march-2025-template-category-misuse-restrictions}
*Dernière mise à jour : mars 2026*

- Meta a mis en place des mesures d'application pour les entreprises qui utilisent de manière abusive la catégorisation utilitaire/marketing
- Cela peut entraîner des restrictions de 7 à 30 jours sur la création de modèles et les révisions de catégories

### Mars 2025 : Limites de messages marketing par modèle et par utilisateur {#march-2025-per-user-marketing-template-message-limits}
*Dernière mise à jour : août 2025*

Meta limitera le nombre de messages marketing par modèle qu'un utilisateur peut recevoir de l'ensemble des entreprises au cours d'une période donnée, en commençant par les messages les moins susceptibles d'être lus.

Une exception existe : si une personne répond à un message marketing, cela ouvre une fenêtre de service client de 24 heures. Les messages marketing envoyés dans cette fenêtre ne seront pas comptabilisés dans la limite de cette personne.

La limite spécifique varie selon l'utilisateur, en fonction de son niveau d'engagement. En savoir plus sur les limites de messages marketing par modèle et par utilisateur de WhatsApp dans la [documentation sur les limites de messages marketing par modèle et par utilisateur de WhatsApp](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Janvier 2025 : WhatsApp suspend l'envoi de messages marketing aux utilisateurs américains à partir du 1er avril {#january-2025-whatsapp-pausing-marketing-message-sending-to-us-users-starting-april-1}
*Dernière mise à jour : janvier 2025*

WhatsApp suspendra l'envoi de messages marketing aux utilisateurs américains (personnes possédant des numéros de téléphone américains) à partir du 1er avril 2025. Les [messages utilitaires, de service et d'authentification](https://developers.facebook.com/docs/whatsapp/pricing/) ainsi que les [messages de réponse]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) resteront autorisés aux États-Unis.

L'envoi de messages marketing (ainsi que tous les autres types de messages) vers tous les autres pays ou régions reste autorisé et ne sera pas affecté.

Meta nous a informés qu'ils effectuent cette mise à jour pour maintenir la santé de l'écosystème WhatsApp aux États-Unis, où WhatsApp connaît une croissance rapide mais en est encore à un stade plus précoce (par exemple, les messages marketing affichent un engagement plus faible que dans d'autres régions). Ils continueront d'évaluer quand le marché américain sera prêt à reprendre les messages marketing.

La distribution des messages marketing vers les numéros de téléphone avec des indicatifs régionaux américains sera rejetée par WhatsApp et renverra un code d'erreur 131049.

### Novembre 2024 : Changements de la politique d'abonnement WhatsApp {#november-2024-changes-to-whatsapp-opt-in-policy}
*Dernière mise à jour : janvier 2025*

Meta a récemment mis à jour sa [politique d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Au lieu d'exiger un consentement spécifique au canal, les entreprises peuvent désormais envoyer des messages aux utilisateurs sur la plateforme si :

1. La personne a fourni son numéro de téléphone.
2. La personne a donné son consentement pour recevoir des communications générales, et pas uniquement via WhatsApp.

Les entreprises doivent toujours se conformer à toutes les lois locales et respecter les exigences suivantes lors de l'obtention du consentement :

- Les entreprises doivent indiquer clairement que la personne accepte de recevoir des communications de l'entreprise
- Les entreprises doivent indiquer clairement le nom de l'entreprise de laquelle la personne accepte de recevoir des messages
- Les entreprises doivent se conformer aux lois applicables

Bien que WhatsApp ait assoupli sa politique, Braze recommande toujours de recueillir un consentement spécifique au canal WhatsApp afin de favoriser la meilleure expérience client et les meilleurs taux d'engagement. Comme toujours, consultez votre équipe juridique pour déterminer ce qui convient le mieux à votre marque.

### Novembre 2024 : Mises à jour de la limite de messages marketing par modèle et par utilisateur pour les personnes aux États-Unis, avant la période des fêtes {#november-2024-updates-to-the-per-user-marketing-template-limit-for-people-in-the-us-ahead-of-the-holiday-season}
*Dernière mise à jour : décembre 2024*

Depuis que Meta a déployé la limite de messages marketing par modèle et par utilisateur, Meta a constaté des améliorations significatives des taux de lecture et du sentiment des utilisateurs.

À compter de maintenant, avant la période des fêtes, les personnes aux États-Unis recevront moins de nouvelles conversations marketing. Meta s'attend à ce que ce changement crée des audiences plus engagées, ce qui conduit in fine à de meilleurs résultats pour les entreprises. Cela peut entraîner des taux de distribution plus faibles pour votre entreprise si vous envoyez des messages marketing vers des numéros de téléphone américains, ce qui peut être surveillé avec le code d'erreur `131049` via Braze Currents et le journal d'activité des messages.

Les entreprises aux États-Unis peuvent toujours envoyer des messages marketing dans d'autres zones géographiques, et il n'y a aucun impact sur les messages utilitaires, d'authentification ou de service, ni sur les messages marketing par modèle envoyés dans une fenêtre de conversation initiée par l'utilisateur (par exemple, une publicité avec clic vers WhatsApp ou un carrousel de produits ou un modèle de coupon envoyé dans le cadre d'une conversation).

### Novembre 2024 : WhatsApp étend les mesures de qualité au niveau du compte pour inclure les taux de lecture {#november-2024-whatsapp-expanding-quality-based-account-enforcements-to-include-read-rates}
*Dernière mise à jour : décembre 2024*

WhatsApp investit continuellement dans de nouvelles approches pour aider les entreprises à créer des expériences de qualité pour leurs clients, notamment en réduisant les comportements de type spam sur leur plateforme.

Le 22 novembre, WhatsApp a commencé à étendre ses mesures de qualité existantes au niveau des comptes WhatsApp Business (WABA) avec des taux de lecture extrêmement bas. Ce changement sera déployé à l'échelle mondiale.

Lorsque le taux de lecture d'un compte baisse de manière significative (par exemple, la majorité des messages envoyés par le compte ne sont pas lus), des blocages d'envoi seront appliqués au compte. La sévérité du blocage augmentera si les taux de lecture restent constamment bas à grande échelle.

Si le taux de lecture du compte est extrêmement bas, les actions suivantes seront entreprises :

- Le compte sera bloqué pour l'envoi de messages initiés par l'entreprise. Il pourra toujours répondre aux messages initiés par les clients. Ce blocage initial est un « verrouillage souple » et peut être levé en sélectionnant le bouton de confirmation dans la section Qualité du compte pour reprendre l'envoi de messages.
- Si le taux de lecture continue de baisser ou reste bas après le verrouillage souple, les entreprises peuvent faire face à une augmentation progressive des mesures d'application (par exemple, quelques jours de restrictions d'envoi).
- Les entreprises devront attendre la fin de la limite appliquée pour reprendre l'envoi de messages. Si le taux de lecture continue de rester bas après des verrouillages souples répétés, le compte sera finalement désactivé.

#### Comment rester informé de ces avertissements et mesures d'application {#how-to-stay-updated-on-these-warnings-and-enforcements}

Comme pour les mesures d'application existantes de la plateforme, les entreprises seront notifiées de ces actions et pourront les confirmer via la page Qualité du compte dans WhatsApp Business gestionnaire. Vérifiez que vous avez les coordonnées correctes indiquées dans WhatsApp Business gestionnaire pour tous les administrateurs nécessaires, car les e-mails de notification d'application seront envoyés en fonction de ces informations.

Les notifications concernant les violations graves de spam seront :

- Affichées dans le Centre de notifications de WhatsApp Business gestionnaire
- Affichées dans une bannière dans WhatsApp gestionnaire
- Envoyées par e-mail à tous les administrateurs définis dans WhatsApp Business gestionnaire

### Mai 2024 : L'API Cloud devient disponible en Türkiye {#may-2024-cloud-api-going-live-in-trkiye}
*Dernière mise à jour : mai 2024*

Meta fournit désormais aux entreprises utilisant l'API Cloud un accès à la Türkiye pour la messagerie professionnelle. Auparavant, l'API Cloud de WhatsApp était disponible pour les entreprises en Turquie, mais les utilisateurs WhatsApp avec des numéros turcs ne pouvaient pas envoyer ou recevoir de messages envoyés via l'API Cloud.

Meta indique toujours clairement aux utilisateurs lorsqu'ils discutent avec une entreprise hébergée par Meta, et tous les utilisateurs doivent accepter les conditions d'utilisation et la politique de confidentialité WhatsApp pertinentes pour poursuivre la messagerie professionnelle. La mise à jour des conditions d'utilisation et de la politique de confidentialité de 2021 en Turquie avait été suspendue, mais est maintenant en cours de déploiement. Elle ne modifie pas l'engagement de Meta en matière de confidentialité — les conversations personnelles continuent d'être protégées par le chiffrement de bout en bout, ce qui signifie que seuls vous et le destinataire prévu pouvez les voir. La mise à jour permet aux utilisateurs turcs d'accéder à des fonctionnalités professionnelles optionnelles s'ils choisissent de le faire et offre plus de transparence sur le fonctionnement de WhatsApp.

Les entreprises utilisant l'API Cloud peuvent désormais initier des conversations avec les utilisateurs WhatsApp ayant des numéros turcs, qui renverront maintenant un webhook en tant que conversation « envoyée », au lieu du code d'erreur 131026 actuel.

Pour qu'un message professionnel soit « distribué » ou « lu », l'utilisateur doit accepter les conditions de WhatsApp. Une entreprise ne sera pas facturée tant que le message n'est pas distribué.

Les utilisateurs qui reçoivent ou essaient d'envoyer un message à une entreprise utilisant l'API Cloud verront une notification dans l'application concernant la mise à jour des conditions, indiquant clairement qu'ils ne peuvent pas envoyer de messages à une entreprise utilisant l'API Cloud tant qu'ils n'ont pas accepté la mise à jour de WhatsApp. De plus, les utilisateurs qui enregistrent ou réenregistrent l'application sur leur téléphone seront invités à accepter la mise à jour de WhatsApp.

Lorsqu'un utilisateur accepte la mise à jour, il verra le message système existant de l'API Cloud lorsqu'il discutera avec une entreprise utilisant l'API Cloud.

### Mai 2024 : Limites de messages marketing par modèle et par utilisateur {#may-2024-per-user-marketing-template-message-limits}
*Dernière mise à jour : mai 2024*

Meta déploie de nouvelles approches pour maintenir des expériences utilisateur de haute qualité et maximiser l'engagement des messages marketing par modèle sur la plateforme WhatsApp. À partir du 23 mai 2024, ils limiteront le nombre de messages marketing par modèle que chaque utilisateur individuel peut recevoir de toutes les entreprises avec lesquelles il interagit pendant une période donnée, en commençant par un petit nombre de conversations qui sont moins susceptibles d'être lues. Notez que la limite est déterminée en fonction du nombre de messages marketing par modèle que cette personne a déjà reçus de n'importe quelle entreprise, et n'est pas liée spécifiquement à votre marque. Cependant, cela peut affecter la livrabilité de vos messages marketing par modèle.

La limite s'applique uniquement aux messages marketing par modèle qui ouvriraient normalement une nouvelle conversation marketing. Si une conversation marketing est déjà ouverte entre votre marque et un utilisateur WhatsApp, les messages marketing par modèle envoyés à l'utilisateur ne seront pas affectés.

Si un message marketing par modèle n'est pas distribué à un utilisateur donné en raison de la limite, l'API Cloud renverra le code d'erreur 131026. Notez cependant que ces codes d'erreur couvrent un large éventail de problèmes pouvant entraîner la non-distribution d'un message et, pour des raisons de confidentialité, Meta ne divulguera pas si le message n'a effectivement pas été distribué en raison de la limite. Reportez-vous au [document de résolution des problèmes](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) de l'API Cloud pour les descriptions des raisons de non-distribution et ce que vous pouvez faire pour en déterminer la cause sous-jacente.

Si vous recevez l'un de ces codes d'erreur et suspectez qu'il est dû à la limite, évitez de renvoyer immédiatement le message par modèle, car cela ne fera que générer une autre réponse d'erreur.

Pour plus d'informations sur cette mise à jour de livrabilité, y compris des détails sur la surveillance de votre livrabilité et d'autres bonnes pratiques pour la communication marketing sur WhatsApp, consultez notre récent [article de blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Avril 2024 : Régulation du rythme d'envoi pour les modèles utilitaires {#april-2024-template-pacing-for-utility-templates}
*Dernière mise à jour : avril 2024*

L'année dernière, WhatsApp a introduit la régulation du rythme d'envoi (template pacing) pour les messages marketing comme nouvelle façon d'aider les entreprises à améliorer l'engagement de leurs modèles et à créer des expériences utilisateur de qualité. À partir du 30 avril, ils étendent la régulation du rythme d'envoi aux messages utilitaires. Si un modèle utilitaire d'un compte est mis en pause en raison des retours des utilisateurs, les nouveaux modèles utilitaires créés seront soumis à la régulation du rythme d'envoi pendant les sept jours suivants.

### Avril 2024 : Les taux de lecture affecteront la note de qualité des modèles marketing {#april-2024-read-rates-will-affect-quality-rating-for-marketing-templates}
*Dernière mise à jour : mars 2024*

WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus enrichissantes et maximiser l'engagement avec les conversations marketing des entreprises. Cela peut inclure la limitation du nombre de conversations marketing qu'une personne reçoit de n'importe quelle entreprise au cours d'une période donnée, en commençant par un petit nombre de conversations qui sont moins susceptibles d'être lues. Braze recevra un code d'erreur si un message n'est pas distribué.

WhatsApp commencera à prendre en compte les taux de lecture dans la note de qualité des modèles marketing, en plus des indicateurs traditionnels comme les blocages et les signalements. WhatsApp pourra temporairement mettre en pause les Campaigns de messages marketing avec de faibles taux de lecture, donnant aux entreprises le temps d'itérer sur les modèles avec le plus faible engagement avant d'augmenter le volume, à partir du 1er avril 2024.

### Février 2024 : Expérimentation sur les conversations marketing {#february-2024-marketing-conversations-experimentation}
*Dernière mise à jour : février 2024*

À partir du 6 février 2024, WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus enrichissantes et maximiser l'engagement des clients avec les conversations marketing de votre marque. Cela peut inclure la limitation du nombre de conversations marketing qu'un utilisateur reçoit de votre marque au cours d'une période donnée, en commençant par un petit nombre de conversations qui sont moins susceptibles d'être lues.

### Octobre 2023 : Régulation du rythme d'envoi des modèles {#october-2023-template-pacing}
*Dernière mise à jour : octobre 2023*

À partir du 12 octobre 2023, WhatsApp introduit un concept appelé « régulation du rythme d'envoi » (template pacing) pour les messages marketing. Au lieu d'envoyer votre message à l'ensemble de l'audience de votre Campaign simultanément, la « régulation du rythme d'envoi » distribue initialement le message à un sous-ensemble plus restreint d'utilisateurs pour recueillir des retours en temps réel de la part des destinataires avant d'envoyer les messages restants.

La « limite de rythme » (le sous-ensemble initial de messages envoyés) est variable en fonction du modèle. Après l'envoi initial, WhatsApp retient les messages restants pendant un maximum de 30 minutes. Pendant cette période de rétention, ils évaluent la qualité du modèle en fonction des retours des clients. Si les retours sont positifs, indiquant un modèle de haute qualité, ils distribuent les messages restants. Si les retours sont négatifs, ils suppriment les messages restants non distribués, évitant ainsi d'autres retours négatifs d'une plus grande partie de vos clients et vous aidant à éviter d'éventuels problèmes de mesures de qualité (comme les impacts sur la note de qualité du numéro de téléphone).

Notez que WhatsApp utilise le même système d'évaluation de la qualité des modèles pour la régulation du rythme d'envoi que pour la mise en pause des modèles. Ainsi, les messages non distribués pendant la régulation du rythme d'envoi (en raison de modèles de faible qualité) sont les mêmes que ceux qui auraient été mis en pause à plus grande échelle.

En fin de compte, cette mise à jour vous offre une boucle de rétroaction plus rapide (30 minutes contre des heures ou des jours avec la mise en pause des modèles), vous permettant d'ajuster vos modèles et d'offrir une meilleure expérience client.

**Si vous avez d'autres questions concernant cette mise à jour, contactez votre représentant partenaire Meta.**

### Juin 2023 : Expérimentation sur la messagerie {#june-2023-messaging-experimentation}
*Dernière mise à jour : juin 2023*

À partir du 14 juin 2023, Meta introduit de nouvelles pratiques d'expérimentation sur la plateforme WhatsApp afin d'évaluer l'impact des messages marketing sur l'expérience et l'engagement des consommateurs. Cette expérimentation peut affecter vos messages marketing envoyés via l'API WhatsApp Business avec Braze.

Meta a l'intention de poursuivre de telles expérimentations sur la plateforme WhatsApp. Veuillez consulter la [documentation de Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl) pour plus d'informations.

**L'expérimentation de WhatsApp affecte uniquement les messages marketing.** Cette expérimentation a le potentiel d'impacter la distribution des messages marketing par modèle. Les modèles utilitaires et d'authentification continueront d'être distribués sans aucun impact de l'expérimentation.

Dans le cadre de l'expérimentation, Meta sélectionne aléatoirement environ 1 % des consommateurs WhatsApp comme participants. S'ils sont sélectionnés, Meta ne distribuera pas de messages marketing par modèle à ces consommateurs, sauf si l'une des conditions suivantes est remplie :

- Si un consommateur vous a répondu dans les dernières 24 heures ;
- Si une conversation marketing existante est ouverte ; ou
- Si le consommateur a cliqué sur une publicité WhatsApp dans les dernières 72 heures.

## Questions fréquemment posées {#faq}

### Comment saurai-je si mon message marketing a été impacté par l'expérimentation de Meta ? {#how-will-i-know-if-my-marketing-message-was-impacted-by-metas-experiment}

Si un message n'est pas livré en raison de l'expérimentation, un code d'erreur spécifique sera affiché dans le journal d'activité et dans Currents. Le message sera également comptabilisé comme un échec et intégré dans vos indicateurs d'échecs WhatsApp dans tous les rapports du tableau de bord de Braze. Vous ne serez pas facturé pour ces messages.

Ce code d'erreur 130472 indiquera « User's number is part of an experiment. » Veuillez consulter la [documentation de Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) pour plus d'informations sur les codes d'erreur de l'API Cloud WhatsApp.

### Puis-je me retirer de l'expérimentation de Meta ? {#can-i-opt-out-of-metas-experiment}

Non, Meta ne permet aucun retrait de l'expérimentation. Tous les fournisseurs et utilisateurs de l'API WhatsApp Business sont soumis à cette expérimentation de Meta.

### Puis-je essayer de renvoyer un modèle plus tard ? {#can-i-try-to-resend-a-template-later}

Il n'y a pas de durée fixe pour cette expérimentation. En tant que tel, un consommateur peut continuer à être soumis à l'expérimentation.

### Que puis-je faire si mes messages marketing ne sont pas livrés en raison de l'expérimentation de Meta ? {#what-can-i-do-if-my-marketing-messages-are-not-delivered-due-to-metas-experiment}

Nous recommandons d'utiliser d'autres canaux Braze, tels que l'e-mail, le SMS, les notifications push ou les messages in-app pour envoyer un message au contenu similaire à vos utilisateurs ciblés.