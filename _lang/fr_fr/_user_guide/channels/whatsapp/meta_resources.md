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

- [Conseils sur les noms d'affichage](https://www.facebook.com/business/help/757569725593362)
- [Activer Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Exigences relatives aux numéros de téléphone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Limites d'envoi de messages](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Évaluation de la qualité](https://www.facebook.com/business/help/896873687365001)

## Mises à jour du produit WhatsApp {#whatsapp-product-updates}

### 2026 : noms d'utilisateur professionnels {#2026-business-usernames}
*Dernière mise à jour : mai 2026*

Meta introduit les noms d'utilisateur professionnels pour WhatsApp — un nom d'affichage optionnel que les entreprises peuvent adopter pour leur numéro de téléphone WhatsApp. Lorsqu'un nom d'utilisateur est défini, il apparaît dans les fenêtres de discussion des applications WhatsApp et WhatsApp Business à la place du numéro de téléphone. Notez que l'adoption d'un nom d'utilisateur ne masque pas votre numéro de téléphone ; il reste toujours visible dans votre profil professionnel.

Les noms d'utilisateur sont uniques pour tous les numéros de téléphone WhatsApp — deux numéros, qu'ils soient personnels ou professionnels, ne peuvent pas partager le même nom d'utilisateur. Ils ne sont pas sensibles à la casse pour les besoins de l'unicité, mais les points et les tirets bas sont traités comme des caractères distincts. Par exemple, `myid`, `my.id` et `my_id` sont tous considérés comme des noms d'utilisateur différents, tandis que `myID` et `myid` sont traités comme identiques.

Les noms d'utilisateur professionnels doivent respecter les exigences de format suivantes :

- Contient uniquement des lettres anglaises (a–z), des chiffres (0–9), des points (`.`) ou des tirets bas (`_`)
- Comporte entre 3 et 35 caractères
- Contient au moins une lettre anglaise
- Ne commence ni ne se termine par un point, et ne contient pas deux points consécutifs
- Ne commence pas par `www`
- Ne se termine pas par un suffixe de domaine courant (tel que `.com`, `.org` ou `.net`)

#### Revendiquer un nom d'utilisateur réservé {#claiming-a-reserved-username}

Avant que la fonctionnalité de nom d'utilisateur ne soit largement disponible, Meta peut avoir pré-réservé un nom d'utilisateur pour votre entreprise — correspondant généralement à un nom de page Facebook ou de compte Instagram existant. Vous pouvez revendiquer ce nom d'utilisateur réservé ou en choisir un autre via [WhatsApp Manage](https://business.facebook.com/wa/manage/). Les noms d'utilisateur revendiqués ne sont pas activés tant que Meta ne rend pas la fonctionnalité disponible.

Si le nom d'utilisateur réservé correspond à un nom déjà associé à votre page Facebook ou à votre compte Instagram, vous devez d'abord lier votre numéro de téléphone professionnel à cette page ou à ce compte. Vous pouvez le faire lors de la revendication du nom d'utilisateur dans WhatsApp Manager ou Meta Business Suite, ou en ajoutant votre numéro de téléphone directement depuis la page ou le compte concerné. La liaison nécessite soit un contrôle total de la page ou du compte, soit un accès partiel de base avec la permission `manage_phone`.

#### Priorité d'affichage dans les fenêtres de discussion {#display-priority-in-chat-windows}

Lorsque votre profil professionnel apparaît dans une fenêtre de discussion, WhatsApp utilise l'ordre de priorité suivant (du plus élevé au plus faible) :

1. Nom du contact enregistré
2. Nom d'entreprise vérifié ou nom de compte professionnel officiel (OBA)
3. Nom d'utilisateur
4. Numéro de téléphone

Pour plus d'informations, consultez la documentation de Meta sur les [noms d'utilisateur professionnels](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/#business-usernames).

### Avril 2026 : archivage automatique des modèles inactifs {#april-2026-automatic-archival-of-inactive-templates}
*Dernière mise à jour : avril 2026*

- Meta archive automatiquement les modèles inactifs depuis 12 mois ou plus.
- L'archivage automatique est activé pour tous les comptes WhatsApp Business et ne peut pas être désactivé.
- L'activité d'un modèle inclut la création, la modification, l'envoi, la contestation ou le désarchivage d'un modèle.
- Les modèles archivés ne peuvent pas être envoyés et sont programmés pour une suppression définitive après 28 jours.
- Vous pouvez désarchiver les modèles dans la fenêtre de 28 jours pour les restaurer et annuler la suppression programmée.
- Les notifications sont envoyées via le webhook `message_template_status_update`, par e-mail et via une bannière unique dans WhatsApp Manager.

Pour plus d'informations, consultez la documentation de Meta sur l'[archivage des modèles](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-archival).

### Juin 2026 : identifiants utilisateur au niveau de l'entreprise {#june-2026-business-scoped-user-ids}
*Dernière mise à jour : mars 2026*

- Meta introduit des identifiants utilisateur pour remplacer le partage de numéros de téléphone à des fins de confidentialité
- Braze travaille sur une solution en amont du déploiement
- Déploiement prévu par Meta en juin 2026

### Novembre 2025 : [API Marketing Messages pour WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (anciennement Marketing Messages Lite API) {#november-2025-marketing-messages-api-for-whatsapphttpsdevelopersfacebookcomdocumentationbusiness-messagingwhatsappmarketing-messagesoverview-formerly-marketing-messages-lite-api}
*Dernière mise à jour : mars 2026*

- Remplace les limites statiques de l'API Cloud par des limites dynamiques basées sur l'engagement
- Non disponible dans la zone EMEA, au Japon ou en Corée du Sud pour la livraison optimisée
- Les messages utilitaires et d'authentification continuent automatiquement via l'API Cloud

### Octobre 2025 : modification du processus d'approbation des comptes professionnels officiels (OBA) {#october-2025-official-business-account-oba-approval-process-changed}
*Dernière mise à jour : mars 2026*

- Auparavant ouvert à tous les clients via WhatsApp Manager
- Désormais limité aux : gouvernements/grands annonceurs Meta, annonceurs directs, ou via un BSP comme Braze (jusqu'à 5 par semaine)
- Nouvelles conditions préalables : vérification de l'entreprise, vérification en deux étapes, nom d'affichage approuvé, notoriété
- Contactez votre gestionnaire du succès des clients pour obtenir de l'aide

### Octobre 2025 : réductions tarifaires régionales {#october-2025-regional-pricing-rate-cuts}
*Dernière mise à jour : mars 2026*

- Tarifs utilitaires/d'authentification réduits en Argentine, en Égypte, au Mexique et en Amérique du Nord
- Tarifs marketing réduits au Mexique (à compter du 1er octobre 2025)

### Octobre 2025 : les limites d'envoi de messages passent du niveau par téléphone au niveau par portefeuille d'entreprise {#october-2025-messaging-limits-change-from-per-phone-to-per-business-portfolio}
*Dernière mise à jour : mars 2026*

- Les limites sont désormais partagées entre tous les numéros de téléphone d'un portefeuille
- Les portefeuilles héritent de la limite existante la plus élevée
- Accès plus rapide aux limites supérieures (dans les 6 heures)
- Risque : les entreprises sans numéro « illimité » peuvent voir leurs limites agrégées diminuer

### 1er juillet 2025 : refonte de la tarification {#july-1-2025-pricing-overhaul}
*Dernière mise à jour : mars 2026*

- La facturation par message a remplacé la facturation par conversation
- Les messages utilitaires envoyés dans une fenêtre de service de 24 heures sont devenus gratuits
- Tarifs utilitaires/d'authentification mis à jour sur plusieurs marchés, avec de nouveaux paliers de volume
- Nouvelles règles sur la mauvaise catégorisation des modèles utilitaires — les entreprises peuvent faire face à un rejet de modèle et à des restrictions de soumission

### Avril 2025 : suspension des messages marketing vers les numéros de téléphone américains {#april-2025-pause-of-marketing-messages-to-us-phone-numbers}
*Dernière mise à jour : août 2025*

Meta suspendra la livraison de tous les messages de modèles marketing aux utilisateurs WhatsApp disposant d'un numéro de téléphone américain (un numéro composé d'un indicatif `+1` et d'un indicatif régional américain). Il n'y a actuellement aucune date prévue pour la levée de cette suspension.

Toute tentative d'envoi d'un modèle à un utilisateur WhatsApp avec un numéro de téléphone américain entraînera l'erreur `131049`.

### Mars 2025 : restrictions liées à l'utilisation abusive des catégories de modèles {#march-2025-template-category-misuse-restrictions}
*Dernière mise à jour : mars 2026*

- Meta a introduit des mesures d'application pour les entreprises utilisant abusivement la catégorisation utilitaire/marketing
- Cela peut entraîner des restrictions de 7 à 30 jours sur la création de modèles et les examens de catégories

### Mars 2025 : limites de messages de modèles marketing par utilisateur {#march-2025-per-user-marketing-template-message-limits}
*Dernière mise à jour : août 2025*

Meta limitera le nombre de messages de modèles marketing qu'un utilisateur peut recevoir de l'ensemble des entreprises sur une période donnée, en commençant par les messages les moins susceptibles d'être lus.

Une exception : si une personne répond à un message marketing, cela ouvrira une fenêtre de service client de 24 heures. Les messages marketing envoyés dans cette fenêtre ne seront pas comptabilisés dans la limite de la personne.

La limite spécifique varie selon l'utilisateur, en fonction de son niveau d'engagement. Pour en savoir plus sur les limites de messages de modèles marketing par utilisateur de WhatsApp, consultez la [documentation de WhatsApp sur les limites de messages de modèles marketing par utilisateur](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Janvier 2025 : WhatsApp suspend l'envoi de messages marketing aux utilisateurs américains à partir du 1er avril {#january-2025-whatsapp-pausing-marketing-message-sending-to-us-users-starting-april-1}
*Dernière mise à jour : janvier 2025*

WhatsApp suspendra l'envoi de messages marketing aux utilisateurs américains (personnes disposant de numéros de téléphone américains) à partir du 1er avril 2025. Les [messages utilitaires, de service et d'authentification](https://developers.facebook.com/docs/whatsapp/pricing/) ainsi que les [messages de réponse]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) resteront autorisés aux États-Unis.

L'envoi de messages marketing (ainsi que tous les autres types de messages) vers tous les autres pays ou régions reste autorisé et ne sera pas affecté.

Meta nous a informés qu'ils effectuent cette mise à jour pour maintenir la santé de l'écosystème WhatsApp aux États-Unis, où WhatsApp connaît une croissance rapide mais en est encore à un stade précoce (par exemple, les messages marketing ont un engagement plus faible que dans d'autres régions). Ils continueront d'évaluer quand le marché américain sera prêt à reprendre les messages marketing.

La livraison de messages marketing vers les numéros de téléphone avec des indicatifs régionaux américains sera rejetée par WhatsApp et renverra un code d'erreur 131049.

### Novembre 2024 : modifications de la politique d'abonnement WhatsApp {#november-2024-changes-to-whatsapp-opt-in-policy}
*Dernière mise à jour : janvier 2025*

Meta a récemment mis à jour sa [politique d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Au lieu d'exiger un consentement spécifique au canal, les entreprises peuvent désormais envoyer des messages aux utilisateurs sur la plateforme si :

1. La personne a fourni son numéro de téléphone.
2. La personne a donné son consentement pour recevoir des messages de manière générale, pas uniquement sur WhatsApp.

Les entreprises doivent toujours se conformer à toutes les lois locales et respecter les exigences suivantes lors de l'obtention du consentement :

- Les entreprises doivent clairement indiquer qu'une personne consent à recevoir des communications de l'entreprise
- Les entreprises doivent clairement indiquer le nom de l'entreprise dont la personne consent à recevoir des messages
- Les entreprises doivent se conformer à la législation applicable

Bien que WhatsApp ait assoupli sa politique, Braze recommande toujours de recueillir un consentement spécifique au canal WhatsApp afin de favoriser la meilleure expérience client et les meilleurs taux d'engagement. Comme toujours, consultez votre équipe juridique pour déterminer ce qui convient le mieux à votre marque.

### Novembre 2024 : mises à jour de la limite de modèles marketing par utilisateur pour les personnes aux États-Unis, avant la période des fêtes {#november-2024-updates-to-the-per-user-marketing-template-limit-for-people-in-the-us-ahead-of-the-holiday-season}
*Dernière mise à jour : décembre 2024*

Depuis que Meta a déployé la limite de modèles marketing par utilisateur, Meta a constaté des améliorations significatives des taux de lecture et du sentiment des utilisateurs.

À partir de maintenant, avant la période des fêtes, les personnes aux États-Unis recevront moins de nouvelles conversations marketing. Meta s'attend à ce que ce changement crée des audiences plus engagées, ce qui conduit finalement à de meilleurs résultats pour les entreprises. Cela peut entraîner des taux de livraison plus faibles pour votre entreprise si vous envoyez des messages marketing vers des numéros de téléphone américains, ce qui peut être surveillé avec le code d'erreur `131049` via Braze Currents et le journal d'activité des messages.

Les entreprises aux États-Unis peuvent toujours envoyer des messages marketing dans d'autres zones géographiques, et il n'y a aucun impact sur les messages utilitaires, d'authentification ou de service, ni sur les messages de modèles marketing envoyés dans une fenêtre de conversation initiée par l'utilisateur (par exemple, une publicité click-to-WhatsApp, un carrousel de produits ou un modèle de coupon envoyé dans le cadre d'une conversation).

### Novembre 2024 : WhatsApp étend les mesures de qualité au niveau du compte pour inclure les taux de lecture {#november-2024-whatsapp-expanding-quality-based-account-enforcements-to-include-read-rates}
*Dernière mise à jour : décembre 2024*

WhatsApp investit continuellement dans de nouvelles façons d'aider les entreprises à créer des expériences de qualité pour leurs clients, comme la réduction des comportements de type spam sur leur plateforme.

Le 22 novembre, WhatsApp a commencé à étendre ses mesures de qualité existantes au niveau du compte sur les comptes professionnels WhatsApp (WABA) avec des taux de lecture extrêmement faibles. Ce changement sera déployé à l'échelle mondiale.

Lorsque le taux de lecture d'un compte chute de manière significative (par exemple, la majorité des messages envoyés par le compte ne sont pas lus), des blocages d'envoi de messages seront appliqués au compte. La sévérité du blocage augmentera en cas de taux de lecture constamment faibles à grande échelle.

Si le taux de lecture du compte est extrêmement faible, les actions suivantes seront prises :

- Le compte sera bloqué pour l'envoi de messages initiés par l'entreprise. Il pourra toujours répondre aux messages initiés par les clients. Ce blocage initial est un « verrouillage souple » et peut être levé en sélectionnant le bouton d'accusé de réception dans la page Qualité du compte pour recommencer à envoyer des messages.
- Si le taux de lecture continue de baisser ou reste faible après le verrouillage souple, les entreprises peuvent faire face à une augmentation progressive des mesures d'application (par exemple, quelques jours de restrictions d'envoi de messages).
- Les entreprises devront attendre la fin de la limite imposée pour recommencer à envoyer des messages. Si le taux de lecture continue de rester faible après des verrouillages souples répétés, le compte sera finalement désactivé.

#### Comment rester informé de ces avertissements et mesures d'application {#how-to-stay-updated-on-these-warnings-and-enforcements}

Comme pour les mesures d'application existantes de la plateforme, les entreprises seront notifiées de ces actions et pourront en accuser réception en utilisant la page Qualité du compte dans le WhatsApp Business Manager. Confirmez que vous avez les coordonnées correctes répertoriées dans le WhatsApp Business Manager pour tous les administrateurs nécessaires, car les e-mails de notification d'application seront envoyés en fonction de ces informations.

Les notifications concernant les violations graves de spam seront :

- Affichées dans le centre de notifications du WhatsApp Business Manager
- Affichées dans une bannière dans le WhatsApp Manager
- Envoyées par e-mail à tous les administrateurs définis dans le WhatsApp Business Manager

### Mai 2024 : l'API Cloud devient disponible en Türkiye {#may-2024-cloud-api-going-live-in-trkiye}
*Dernière mise à jour : mai 2024*

Meta offre désormais aux entreprises utilisant l'API Cloud l'accès à la Türkiye pour l'envoi de messages professionnels. Auparavant, l'API Cloud WhatsApp était disponible pour les entreprises en Turquie, mais les utilisateurs WhatsApp avec des numéros turcs ne pouvaient pas envoyer ni recevoir de messages envoyés via l'API Cloud.

Meta indique toujours clairement aux utilisateurs lorsqu'ils discutent avec une entreprise hébergée par Meta, et tous les utilisateurs doivent accepter les conditions d'utilisation et la politique de confidentialité WhatsApp pertinentes pour procéder à l'envoi de messages professionnels. La mise à jour des conditions d'utilisation et de la politique de confidentialité de 2021 en Turquie avait été suspendue, mais est maintenant en cours de déploiement. Elle ne modifie pas l'engagement de Meta en matière de confidentialité — les conversations personnelles continuent d'être protégées par le chiffrement de bout en bout, ce qui signifie que seuls vous et le destinataire prévu pouvez les voir. La mise à jour permet aux utilisateurs turcs d'accéder à des fonctionnalités professionnelles optionnelles s'ils le souhaitent et offre plus de transparence sur le fonctionnement de WhatsApp.

Les entreprises utilisant l'API Cloud peuvent désormais initier des conversations avec les utilisateurs WhatsApp disposant de numéros turcs, ce qui renverra désormais un webhook en tant que conversation « envoyée », au lieu du code d'erreur 131026 actuel.

Pour qu'un message professionnel soit « livré » ou « lu », l'utilisateur doit accepter les conditions WhatsApp. Une entreprise ne sera pas facturée tant que le message n'est pas livré.

Les utilisateurs qui reçoivent ou tentent d'envoyer un message à une entreprise utilisant l'API Cloud verront une notification in-app concernant la mise à jour des conditions, indiquant clairement qu'ils ne peuvent pas envoyer de messages à une entreprise utilisant l'API Cloud tant qu'ils n'ont pas accepté la mise à jour WhatsApp. De plus, les utilisateurs qui s'inscrivent ou se réinscrivent sur l'application sur leur téléphone seront invités à accepter la mise à jour WhatsApp.

Lorsqu'un utilisateur accepte la mise à jour, il verra la notification système existante de l'API Cloud lorsqu'il discutera avec une entreprise utilisant l'API Cloud.

### Mai 2024 : limites de messages de modèles marketing par utilisateur {#may-2024-per-user-marketing-template-message-limits}
*Dernière mise à jour : mai 2024*

Meta déploie de nouvelles approches pour maintenir des expériences utilisateur de haute qualité et maximiser l'engagement des messages de modèles marketing sur la plateforme WhatsApp. À partir du 23 mai 2024, ils limiteront le nombre de messages de modèles marketing que chaque utilisateur individuel peut recevoir de toutes les entreprises avec lesquelles il interagit pendant une période donnée, en commençant par un petit nombre de conversations les moins susceptibles d'être lues. Notez que la limite est déterminée en fonction du nombre de messages de modèles marketing que cette personne a déjà reçus de n'importe quelle entreprise, et n'est pas liée spécifiquement à votre marque. Cependant, cela peut affecter la livrabilité de vos messages de modèles marketing.

La limite s'applique uniquement aux messages de modèles marketing qui ouvriraient normalement une nouvelle conversation marketing. Si une conversation marketing est déjà ouverte entre votre marque et un utilisateur WhatsApp, les messages de modèles marketing envoyés à l'utilisateur ne seront pas affectés.

Si un message de modèle marketing n'est pas livré à un utilisateur donné en raison de la limite, l'API Cloud renverra le code d'erreur 131026. Notez cependant que ces codes d'erreur couvrent un large éventail de problèmes pouvant entraîner la non-livraison d'un message, et pour des raisons de confidentialité, Meta ne divulguera pas si le message n'a effectivement pas été livré en raison de la limite. Consultez le [document de résolution des problèmes](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) de l'API Cloud pour les descriptions des raisons de non-livraison et ce que vous pouvez faire pour déterminer leur cause sous-jacente.

Si vous recevez l'un de ces codes d'erreur et suspectez qu'il est dû à la limite, évitez de renvoyer immédiatement le message de modèle, car cela ne fera que générer une autre réponse d'erreur.

Pour plus d'informations sur cette mise à jour de livrabilité, y compris des détails sur la surveillance de votre livrabilité et d'autres bonnes pratiques pour l'envoi de messages marketing sur WhatsApp, consultez notre récent [article de blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Avril 2024 : régulation du rythme des modèles utilitaires {#april-2024-template-pacing-for-utility-templates}
*Dernière mise à jour : avril 2024*

L'année dernière, WhatsApp a introduit la régulation du rythme des modèles pour les messages marketing comme une nouvelle façon d'aider les entreprises à améliorer l'engagement de leurs modèles et à créer des expériences utilisateur de qualité. À partir du 30 avril, ils étendent la régulation du rythme aux messages utilitaires. Si un modèle utilitaire d'un compte est mis en pause en raison des retours utilisateurs, ils réguleront le rythme des nouveaux modèles utilitaires créés pendant les sept jours suivants.

### Avril 2024 : les taux de lecture affecteront l'évaluation de la qualité des modèles marketing {#april-2024-read-rates-will-affect-quality-rating-for-marketing-templates}
*Dernière mise à jour : mars 2024*

WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus enrichissantes et maximiser l'engagement avec les conversations marketing des entreprises. Cela peut inclure la limitation du nombre de conversations marketing qu'une personne reçoit de n'importe quelle entreprise sur une période donnée, en commençant par un petit nombre de conversations les moins susceptibles d'être lues. Braze recevra un code d'erreur si un message n'est pas livré.

WhatsApp commencera à prendre en compte les taux de lecture dans l'évaluation de la qualité des modèles marketing, en plus des indicateurs traditionnels comme les blocages et les signalements. WhatsApp pourra temporairement suspendre les campagnes de messages marketing avec de faibles taux de lecture, donnant aux entreprises le temps d'itérer sur les modèles ayant le plus faible engagement avant d'augmenter le volume à partir du 1er avril 2024.

### Février 2024 : expérimentation sur les conversations marketing {#february-2024-marketing-conversations-experimentation}
*Dernière mise à jour : février 2024*

À partir du 6 février 2024, WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus enrichissantes et maximiser l'engagement client avec les conversations marketing de votre marque. Cela peut inclure la limitation du nombre de conversations marketing qu'un utilisateur reçoit de votre marque sur une période donnée, en commençant par un petit nombre de conversations les moins susceptibles d'être lues.

### Octobre 2023 : régulation du rythme des modèles {#october-2023-template-pacing}
*Dernière mise à jour : octobre 2023*

À partir du 12 octobre 2023, WhatsApp introduit un concept appelé « régulation du rythme des modèles » pour les messages marketing. Au lieu d'envoyer votre message à l'ensemble de l'audience de votre campagne simultanément, la « régulation du rythme des modèles » livre initialement le message à un sous-ensemble plus petit d'utilisateurs pour recueillir des retours en temps réel des destinataires de la campagne avant d'envoyer les messages restants.

La « limite de rythme » (le sous-ensemble initial de messages envoyés) est variable selon le modèle. Après l'envoi initial, WhatsApp retient les messages restants pendant un maximum de 30 minutes. Pendant cette période de rétention, ils évaluent la qualité du modèle en fonction des retours clients. Si les retours sont positifs, indiquant un modèle de haute qualité, ils livrent les messages restants. Si les retours sont négatifs, ils abandonnent les messages restants non livrés, évitant ainsi des retours négatifs supplémentaires d'une plus grande partie de vos clients et vous aidant à éviter d'éventuels problèmes de mesures de qualité (tels que les impacts sur l'évaluation de la qualité du numéro de téléphone).

Notez que WhatsApp utilise le même système d'évaluation de la qualité des modèles pour la régulation du rythme que pour la mise en pause des modèles. Ainsi, les messages non livrés lors de la régulation du rythme (en raison de modèles de faible qualité) sont les mêmes qui auraient été mis en pause à plus grande échelle.

En fin de compte, cette mise à jour vous offre une boucle de rétroaction plus rapide (30 minutes contre des heures ou des jours avec la mise en pause des modèles), vous permettant d'ajuster vos modèles et d'offrir une meilleure expérience client.

**Si vous avez d'autres questions concernant cette mise à jour, contactez votre conseiller partenaire Meta.**

### Juin 2023 : expérimentation sur l'envoi de messages {#june-2023-messaging-experimentation}
*Dernière mise à jour : juin 2023*

À partir du 14 juin 2023, Meta introduit de nouvelles pratiques d'expérimentation sur la plateforme WhatsApp afin d'évaluer l'impact des messages marketing sur l'expérience et l'engagement des consommateurs. Cette expérimentation peut affecter vos messages marketing envoyés via l'API WhatsApp Business avec Braze.

Meta a l'intention de poursuivre ce type d'expérimentation sur la plateforme WhatsApp. Veuillez consulter la [documentation de Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl) pour plus d'informations.

**L'expérimentation WhatsApp n'affecte que les messages marketing.** Cette expérimentation a le potentiel d'impacter la livraison des messages de modèles marketing. Les modèles utilitaires et d'authentification continueront d'être livrés sans aucun impact de l'expérimentation.

Dans le cadre de l'expérimentation, Meta sélectionne aléatoirement environ 1 % des consommateurs WhatsApp comme participants. S'ils sont sélectionnés, Meta ne livrera pas les messages de modèles marketing à ces consommateurs, sauf si l'une des conditions suivantes est remplie :

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