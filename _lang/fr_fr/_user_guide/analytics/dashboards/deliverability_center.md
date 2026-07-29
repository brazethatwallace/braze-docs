---
nav_title: Centre de livrabilité
article_title: Centre de livrabilité
alias: "/deliverability_center/"
page_order: 4
description: "Cet article de référence explique comment configurer le Centre de livrabilité, une fonctionnalité qui permet aux marketeurs de consulter la réputation de leurs domaines d'envoi d'e-mails et de leurs adresses IP, et de mieux comprendre leur livrabilité d'e-mails."
channel:
  - email

---

# Centre de livrabilité {#deliverability-center}

> Le Centre de livrabilité offre une meilleure visibilité sur les performances de vos e-mails en prenant en charge l'utilisation de [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) pour suivre les données relatives aux e-mails envoyés et recueillir des informations sur votre domaine d'envoi.

La livrabilité des e-mails est au cœur du succès de vos campagnes. Grâce au Centre de livrabilité du tableau de bord de Braze, vous pouvez consulter vos domaines par **IP Reputation** ou **Delivery Errors** afin de détecter et résoudre d'éventuels problèmes de livrabilité.

Pour accéder au Centre de livrabilité, vous devez disposer des [autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) listées dans le menu déroulant ci-dessous pour votre espace de travail.

{% details Autorisations utilisateur pour le Centre de livrabilité %}

- Campaigns : consulter
- Campaigns : modifier
- Campaigns : archiver
- Canvas : consulter
- Canvas : modifier
- Canvas : archiver
- Règles de limite de fréquence : consulter
- Règles de limite de fréquence : modifier
- Priorisation des messages : consulter
- Priorisation des messages : modifier
- Content Blocks : consulter
- Indicateurs de fonctionnalité : consulter
- Indicateurs de fonctionnalité : modifier
- Indicateurs de fonctionnalité : archiver
- Segments : consulter
- Segments : modifier
- Modèles IAM : consulter
- Modèles IAM : modifier
- Modèles IAM : archiver
- Modèles d'e-mail : consulter
- Modèles d'e-mail : modifier
- Modèles d'e-mail : archiver
- Modèles de webhook : consulter
- Modèles de webhook : modifier
- Modèles de webhook : archiver
- Modèles de liens d'e-mail : consulter
- Modèles de liens d'e-mail : modifier
- Ressources de la bibliothèque multimédia : consulter
- Ressources de la bibliothèque multimédia : modifier
- Ressources de la bibliothèque multimédia : supprimer
- Emplacements : consulter
- Emplacements : modifier
- Emplacements : archiver
- Codes de promotion : consulter
- Codes de promotion : modifier
- Codes de promotion : exporter
- Centres de préférences : consulter
- Centres de préférences : modifier
- Rapports : consulter
- Rapports : modifier
- Données d'utilisation : consulter

{% enddetails %}

## Configurer votre compte Google Postmaster {#set-up-your-google-postmaster-account}

Avant de vous connecter au Centre de livrabilité, vous devez configurer un compte Google Postmaster Tools. Vous pouvez utiliser un compte Gmail professionnel ou personnel pour cette configuration.

1. Accédez au [tableau de bord Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. En bas de la page, sélectionnez <i class="fas fa-plus-circle"></i> **Add domain**.
3. Saisissez votre domaine racine (parent) pour authentifier votre e-mail. Assurez-vous que l'enregistrement TXT est lié à ce domaine racine (parent), et **non** au sous-domaine que vous utilisez via Braze. La vérification du domaine racine (parent) vous permet d'ajouter ultérieurement des sous-domaines dans Postmaster Tools sans créer d'enregistrements TXT supplémentaires. Par exemple, en vérifiant `braze.com`, vous pouvez ensuite ajouter `demo.braze.com` comme sous-domaine distinct dans Postmaster Tools pour consulter les indicateurs au niveau du sous-domaine.
4. Google génère un enregistrement TXT qui peut être ajouté directement au DNS de votre domaine. Celui-ci est généralement géré par la personne responsable de votre DNS. Pour obtenir des informations et des instructions sur la mise à jour de votre DNS spécifique, consultez [Vérifier votre domaine (étapes spécifiques à l'hébergeur)](https://support.google.com/a/topic/1409901).
5. Sélectionnez **Next**. <br>![Un exemple de domaine « demo.braze.com » pour authentifier un e-mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Une fois l'enregistrement TXT ajouté au DNS, retournez au tableau de bord Google Postmaster Tools et sélectionnez **Verify**. Cette étape confirme que vous êtes propriétaire du domaine, ce qui vous permet d'accéder aux indicateurs de livrabilité Gmail dans votre compte Postmaster. <br>![Une invite pour vérifier la propriété du domaine « demo.braze.com ».]({% image_buster /assets/img_archive/domain_verification.png %})
7. Après avoir vérifié le domaine racine (parent), ajoutez vos sous-domaines d'envoi à Google Postmaster.

{% alert note %}
Si vos sous-domaines n'apparaissent pas dans le Centre de livrabilité pour Google Postmaster, cela peut être dû au fait que seul le domaine racine (parent) a été ajouté à Google Postmaster. Une fois les domaines racines vérifiés dans Google Postmaster, vous pouvez ajouter vos sous-domaines, qui sont vérifiés automatiquement. Ce processus permet à Google de fournir des indicateurs au niveau du sous-domaine, qui peuvent ensuite être récupérés dans le Centre de livrabilité de Braze.
{% endalert %}

## Intégrer Google Postmaster {#integrating-google-postmaster}

{% alert important %}
**Migration vers Google Postmaster Tools v2**<br>
Google abandonne l'ancienne version de Postmaster Tools (v1) et a publié une nouvelle génération (v2) avec une interface utilisateur modernisée et de nouveaux tableaux de bord, notamment un tableau de bord de conformité pour vous aider à surveiller le respect des directives d'envoi de Gmail. Tous les utilisateurs doivent migrer vers la v2 avant le 31 octobre 2026.<br><br>
Pour réautoriser votre connexion Google Postmaster Tools, accédez à **Intégrations partenaires** > **Partenaires technologiques**, ouvrez **Google Postmaster**, puis sélectionnez **Change Account** pour vous réauthentifier avec les nouvelles autorisations v2. Une fois terminé, vous êtes mis à niveau vers la v2 et accédez aux nouveaux tableaux de bord et données.<br><br>
Pour en savoir plus, consultez l'[annonce de Google concernant les nouveaux Postmaster Tools](https://support.google.com/mail/answer/16594218?hl=en).
{% endalert %}

Avant de configurer votre Centre de livrabilité, vérifiez que vos domaines ont été [ajoutés à Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

Suivez ces étapes pour intégrer Google Postmaster et configurer votre Centre de livrabilité :

1. Accédez à **Analytics** > **Email Performance**.
2. Sélectionnez l'onglet **Deliverability Center**. <br>![Un Centre de livrabilité avec Google Postmaster non connecté.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Sélectionnez **Connect with Google Postmaster**.
4. Sélectionnez votre compte Google, puis sélectionnez **Allow** pour autoriser Braze à consulter les indicateurs de trafic e-mail pour les domaines enregistrés dans Postmaster Tools.

Vos domaines vérifiés s'affichent dans le Centre de livrabilité.

![Deux domaines vérifiés pour Google Postmaster avec une réputation moyenne et faible.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Vous pouvez également accéder à Google Postmaster dans le tableau de bord de Braze en allant dans **Intégrations partenaires** > **Partenaires technologiques** > **Google Postmaster**. Après l'intégration, Braze récupère les données de réputation et d'erreurs des 30 derniers jours. Les données peuvent ne pas être immédiatement disponibles et nécessiter quelques minutes pour se charger.

### Autorisation invalide ou expirée {#invalid-or-expired-authorization}

Si vous recevez une alerte indiquant que les identifiants d'autorisation de Google Postmaster Tools sont invalides, l'envoi d'e-mails depuis Braze n'est **pas** affecté. Seule la connexion entre Braze et Google Postmaster est interrompue, ce qui empêche la synchronisation des données de réputation et d'erreurs Gmail vers le Centre de livrabilité jusqu'à ce que vous vous reconnectiez.

Pour restaurer l'intégration, accédez à **Intégrations partenaires** > **Partenaires technologiques**, ouvrez **Google Postmaster**, sélectionnez **Disconnect**, puis suivez à nouveau le processus de connexion (mêmes étapes que dans [Intégrer Google Postmaster](#integrating-google-postmaster)).

### Indicateurs et définitions {#metrics-and-definitions}

Les indicateurs et définitions suivants s'appliquent à Google Postmaster Tools.

#### Réputation IP {#ip-reputation}

Pour comprendre les évaluations de la réputation IP, consultez ce tableau :

| Évaluation de la réputation | Définition |
| ----- | ---------- |
| Élevée | Présente un bon historique avec un faible taux de plaintes pour spam (par exemple, les utilisateurs qui cliquent sur le bouton « spam »). |
| Moyenne/Correcte | Connue pour générer un engagement positif, mais reçoit occasionnellement des plaintes pour spam. La plupart des e-mails provenant de ce domaine arrivent dans la boîte de réception, sauf lorsque les plaintes pour spam augmentent. |
| Faible | Connue pour recevoir régulièrement un taux élevé de plaintes pour spam. Les e-mails de cet expéditeur sont susceptibles d'être filtrés vers le dossier spam. |
| Mauvaise | Présente un historique de taux élevés de plaintes pour spam. Les e-mails provenant de ce domaine sont presque toujours rejetés à la connexion ou filtrés vers le dossier spam. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Réputation IP" }

{% alert important %}
Les données de plaintes pour spam affichées dans Braze sont basées sur les rapports de boucle de rétroaction (FBL) des fournisseurs de messagerie qui les partagent, tels que Microsoft, Yahoo et Comcast. Lorsque les utilisateurs de ces fournisseurs signalent un e-mail comme spam, ces plaintes sont renvoyées à Braze.<br><br>
Cependant, Gmail et iCloud ne disposent pas de boucles de rétroaction traditionnelles et ne transmettent pas les plaintes pour spam à Braze. Cela signifie :<br>
- Les plaintes pour spam des utilisateurs Gmail ne sont pas incluses dans les indicateurs Braze et ne sont pas disponibles dans les données Snowflake ou Currents.<br>
- Vous pouvez consulter les données de spam Gmail uniquement sous forme de pourcentages agrégés dans [Gmail Postmaster Tools](https://www.gmail.com/postmaster/), et non sous forme d'adresses individuelles.<br>
- Si vous constatez des taux de spam élevés dans Gmail Postmaster Tools, ces chiffres ne correspondent pas à vos indicateurs de plaintes pour spam dans Braze, car Gmail ne partage pas ces données avec les expéditeurs.
{% endalert %}

#### Réputation du domaine {#domain-reputation}

Utilisez le tableau suivant pour surveiller et comprendre les évaluations de la réputation de votre domaine afin d'éviter d'être filtré dans le dossier spam.

| Évaluation de la réputation | Définition |
| ----- | ---------- |
| Élevée | Présente un bon historique avec un très faible taux de plaintes pour spam. Conforme aux directives d'envoi de Gmail. Les e-mails sont rarement filtrés vers le dossier spam. Présente un bon historique avec un très faible taux de spam. Conforme aux [directives d'envoi de Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Moyenne/Correcte | Connue pour générer un engagement positif, mais a occasionnellement reçu un faible volume de plaintes pour spam. La plupart des e-mails provenant de ce domaine arrivent dans la boîte de réception (sauf en cas d'augmentation notable du niveau de spam). |
| Faible | Connue pour recevoir régulièrement des plaintes pour spam. Les e-mails de cet expéditeur sont susceptibles d'être filtrés vers le dossier spam. |
| Mauvaise | Présente un historique de taux élevés de plaintes pour spam. Les e-mails provenant de ce domaine sont presque toujours rejetés à la connexion ou filtrés vers le dossier spam. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Réputation du domaine" }

#### Authentification {#authentication}

Utilisez le tableau de bord d'authentification pour examiner le pourcentage d'e-mails ayant passé les vérifications SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail) et DMARC (Domain-based Message Authentication, Reporting and Conformance).

| Type de graphique | Définition |
| ----- | ---------- |
| SPF | Affiche le pourcentage d'e-mails ayant passé la vérification SPF par rapport à l'ensemble des e-mails du domaine ayant tenté la vérification SPF. Cela exclut les e-mails usurpés. |
| DKIM | Affiche le pourcentage d'e-mails ayant passé la vérification DKIM par rapport à l'ensemble des e-mails du domaine ayant tenté la vérification DKIM. |
| DMARC | Affiche le pourcentage d'e-mails conformes à l'alignement DMARC par rapport à l'ensemble des e-mails reçus du domaine ayant passé la vérification SPF ou DKIM. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Authentification" }

#### Chiffrement {#encryption}

Consultez ce tableau pour comprendre quel pourcentage de votre trafic entrant et sortant est chiffré.

| Terme | Définition |
| ----- | ---------- |
| TLS entrant | Affiche le pourcentage de courrier entrant (vers Gmail) ayant passé la vérification TLS par rapport à l'ensemble du courrier reçu de ce domaine. |
| TLS sortant | Affiche le pourcentage de courrier sortant (depuis Gmail) accepté via TLS par rapport à l'ensemble du courrier envoyé à ce domaine. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chiffrement" }

Pour plus d'idées sur l'amélioration de la livrabilité, consultez [Pièges de livrabilité et pièges à spam]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps). N'oubliez pas de consulter nos [Bonnes pratiques pour les e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices) pour vérifier les points essentiels avant d'envoyer une campagne e-mail.

## Configurer Microsoft Smart Network Data Services (SNDS) {#set-up-microsoft-smart-network-data-services-snds}

Si Microsoft est votre principal fournisseur de messagerie, vous pouvez consulter les données Microsoft SNDS dans le Centre de livrabilité. Cela inclut les adresses IP d'envoi dédiées pour les espaces de travail qui utilisent Amazon SES, SendGrid ou SparkPost. Utilisez ces données pour surveiller la santé de vos adresses IP et comprendre comment les fournisseurs de messagerie Microsoft évaluent vos envois.

Microsoft SNDS fournit des données au niveau de l'adresse IP sur les plaintes pour spam, les occurrences de pièges à spam et le volume d'envoi, tels que rapportés par les fournisseurs de messagerie Microsoft comme Outlook, Hotmail et Live.

{% alert important %}
Si vous ne voyez pas vos données dans le Centre de livrabilité, contactez l'[assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support) en fournissant la liste de vos adresses IP.
{% endalert %}

### Amazon SES

Pour les espaces de travail qui envoient des e-mails via Amazon SES, le Centre de livrabilité affiche les indicateurs Microsoft SNDS pour vos adresses IP d'envoi dédiées. Braze rétrocharge jusqu'à 90 jours de données SNDS historiques lorsque cette fonctionnalité est activée pour votre espace de travail.

{% alert note %}
Amazon SES ne fournit pas les indicateurs **Trap message period start** ni **Trap message period end**. Pour les adresses IP d'envoi SES, ces colonnes sont masquées dans le tableau Microsoft SNDS. Vous pouvez toujours consulter les autres indicateurs SNDS pour ces adresses IP, y compris les occurrences de pièges à spam.
{% endalert %}

![Un exemple de résultats de Microsoft SNDS, incluant des adresses IP d'exemple, des destinataires, des commandes RCPT, des commandes DATA, des résultats de filtrage, un taux de plaintes, les dates de début et de fin de la période de messages piège, et les occurrences de pièges à spam.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Indicateurs et définitions

Les indicateurs suivants s'appliquent à Microsoft SNDS.

#### Destinataires {#recipients}

Cet indicateur correspond au nombre de destinataires des messages transmis par l'adresse IP.

#### Commandes DATA {#data-commands}

Cet indicateur suit le nombre de commandes DATA envoyées par l'adresse IP. Les commandes DATA font partie du protocole SMTP utilisé pour envoyer du courrier.

#### Résultats de filtrage {#filter-results}

Consultez ce tableau pour comprendre les résultats de filtrage.

| Résultat | Définition |
| ----- | ---------- |
| Vert | Considéré comme spam par le filtre anti-spam de Microsoft pour moins de 10 % de la période donnée. |
| Jaune | Considéré comme spam par le filtre anti-spam de Microsoft pour 10 % à 90 % de la période donnée. |
| Rouge | Considéré comme spam par le filtre anti-spam de Microsoft pour plus de 90 % de la période donnée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résultats de filtrage" }

#### Taux de plaintes {#complaint-rate}

Il s'agit de la proportion de fois où un message reçu depuis l'adresse IP fait l'objet d'une plainte de la part d'un utilisateur Hotmail ou Windows Live pendant la période d'activité. Les utilisateurs ont la possibilité de signaler la quasi-totalité des messages comme indésirables via l'interface web.

Pour calculer le taux de plaintes, divisez le nombre de plaintes par le nombre de destinataires des messages.

| Résultat | Définition |
| ----- | ---------- |
| Inférieur à 0,3 % | Le taux de plaintes idéal. |
| Supérieur à 0,3 % | Examinez votre processus d'inscription et assurez-vous que votre lien de désabonnement fonctionne. Demandez-vous également si le contenu pourrait être mieux personnalisé pour votre audience. |
| Supérieur à 100 % | Notez que SNDS affiche les plaintes pour le jour où elles ont été signalées, et non rétroactivement pour le jour où l'e-mail ayant fait l'objet de la plainte a été distribué. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Taux de plaintes" }

#### Occurrences de pièges à spam {#spam-trap-hits}

Les occurrences de pièges à spam correspondent au nombre de messages envoyés à des « comptes piège », c'est-à-dire des comptes gérés par Outlook.com qui ne sollicitent aucun courrier. Il est probable que tout message envoyé à ces comptes piège soit considéré comme spam. Il est donc important de surveiller cet indicateur pour s'assurer qu'il reste faible. Un faible nombre d'occurrences de pièges à spam signifie que les messages ne sont pas envoyés à ces comptes et sont bien distribués à de véritables comptes.

#### Début et fin de la période de messages piège {#trap-message-period-start-and-end}

Ces colonnes indiquent quand les premiers et derniers messages envoyés à des comptes piège ont été reçus depuis l'adresse IP pendant la période d'activité. Amazon SES ne fournit pas ces indicateurs, les colonnes sont donc masquées lorsque vous consultez uniquement les adresses IP d'envoi SES dans le tableau Microsoft SNDS.

{% alert tip %}
Si vous recherchez des enregistrements liés à l'un de vos domaines vérifiés dans Braze, notez que le Centre de livrabilité affiche vos données provenant de Google Postmaster ou de Microsoft SNDS, ce qui signifie qu'il est possible que l'une ou l'autre de ces plateformes n'ait pas de données à partager avec Braze. Vous pouvez également essayer de maintenir un envoi d'e-mails régulier, car cela peut contribuer à améliorer votre réputation.
{% endalert %}

## Plaintes pour spam et boucles de rétroaction {#spam-complaints-and-feedback-loops}

Une boucle de rétroaction (FBL) pour les e-mails permet aux expéditeurs de recevoir des rapports lorsque les destinataires signalent des messages comme spam. Cependant, Gmail et iCloud ne proposent pas de boucles de rétroaction traditionnelles, ce qui signifie que Braze (via SparkPost ou SendGrid) ne reçoit pas de données de plaintes pour spam de ces fournisseurs.

Étant donné que les données de plaintes pour spam ne sont pas disponibles pour Gmail et iCloud, il est important d'utiliser d'autres outils pour surveiller la santé et la réputation de vos e-mails auprès de ces principaux fournisseurs :

- Utilisez [Google Postmaster Tools](https://www.gmail.com/postmaster/) pour surveiller la réputation de votre domaine et de vos adresses IP, les taux de spam et l'engagement des utilisateurs. Vous pouvez intégrer Google Postmaster avec Braze comme décrit dans [Intégrer Google Postmaster](#integrating-google-postmaster).
- Apple ne propose pas d'outil Postmaster public équivalent à celui de Google. Concentrez-vous sur le maintien d'indicateurs d'engagement solides et sur le respect des bonnes pratiques en matière d'e-mails.

Pour maintenir une bonne livrabilité auprès de tous les fournisseurs, mettez en place une [politique de temporisation]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) pour cesser automatiquement d'envoyer des e-mails aux utilisateurs inactifs. Cela permet d'éviter que vos e-mails soient signalés comme spam et protège la réputation de votre expéditeur.