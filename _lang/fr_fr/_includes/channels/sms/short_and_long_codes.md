# Expéditeurs de SMS et de RCS {#sms-and-rcs-senders}

> Cet article fournit un aperçu des codes et des expéditeurs disponibles pour l'envoi de SMS et de messages RCS.

## Types d'expéditeurs de SMS et de RCS {#types-of-sms-and-rcs-senders}

{% tabs %}
{% tab RCS-Verified Sender %}

### Expéditeur vérifié RCS {#rcs-verified-sender}

RCS est un système d'envoi de messages moderne qui offre davantage de fonctionnalités que les SMS traditionnels, en introduisant des capacités telles que les ID d'expéditeur de marque, les médias enrichis et les contenus interactifs, comme les carrousels défilants, les réponses rapides, les boutons CTA, etc. Il est conçu pour offrir une expérience utilisateur plus élégante et plus engageante.

#### Détails {#details}

| Composants visuels | Accès | Débit | MMS activé | Unidirectionnel ou bidirectionnel |
| --- | --- | --- | --- | --- |
| - Nom de marque<br>- logo<br>- légende facultative<br> - badge vérifié | 4 à 6 semaines pour l'approbation de l'opérateur | Le débit et la distribution dépendent de la connexion de données active du destinataire (données mobiles ou Wi-Fi). Le RCS ne dépend pas des limites imposées par les réseaux fixes comme le font les SMS ; les messages RCS sont envoyés via des réseaux de données plutôt que via les canaux de signalisation cellulaire traditionnels utilisés par les SMS. | S.O. | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

#### Avantages et inconvénients {#pros-and-cons}

| Avantages |
| ---- |
| **Confiance et image de marque vérifiées**<br> Contrairement aux SMS traditionnels, où votre marque apparaît sous la forme d'un code court aléatoire à 5 chiffres ou d'un code long, le RCS permet de vérifier les profils des expéditeurs. Ces profils comprennent le logo et le nom de votre marque, ainsi qu'une coche « vérifié ». |
| **Fonctionnalités d'envoi de messages enrichis**<br> RCS prend en charge les carrousels, les vidéos haute résolution et les boutons d'action suggérés (tels que « Réserver maintenant », « Suivre un colis » ou « Payer une facture »). Les utilisateurs peuvent accomplir des tâches complexes sans quitter leur application de messagerie, ce qui peut entraîner des taux de conversion plus élevés qu'un simple lien texte. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

| Inconvénients |
| ---- |
| **Prise en charge fragmentée**<br> Bien que Google ait fortement encouragé l'adoption du RCS pour Android et qu'Apple ait récemment introduit la prise en charge du RCS pour iOS, la mise en œuvre peut encore être inégale selon les opérateurs et les régions. Si le téléphone ou l'opérateur d'un utilisateur ne prend pas en charge le RCS, le message est généralement envoyé sous forme de SMS standard, perdant ainsi toutes les fonctionnalités avancées du RCS. |
| **Incohérences entre plateformes**<br> L'expérience utilisateur RCS varie en fonction de l'opérateur du destinataire, du modèle d'appareil et de l'application de messagerie utilisée (par exemple, Google Messages ou iMessage). |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

{% endtab %}
{% tab SMS Short Codes %}

#### Codes courts SMS {#sms-short-codes}

Un code court est un numéro à 5 ou 6 chiffres qui permet d'envoyer et de recevoir des SMS vers et depuis des téléphones mobiles à des débits plus élevés que les codes longs. Les codes courts sont recommandés pour les envois volumineux et urgents.

Certains pays vous permettent de choisir un numéro spécifique moyennant des frais supplémentaires. Ces codes courts sont appelés codes courts personnalisés. Si vous êtes intéressé par les codes courts personnalisés, contactez votre conseiller Braze pour plus de détails.

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel ou bidirectionnel |
| --- | --- | --- | --- | --- |
| 5-6 chiffres | Demande de 4 à 12 semaines | 100 messages par seconde ou plus | Oui | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Vitesse et évolutivité**<br> Les codes courts sont spécialement conçus pour les volumes de trafic élevés. Ils permettent d'envoyer des messages plus rapidement que les codes longs et, comme ils sont pré-vérifiés directement par les opérateurs, ils présentent le risque le plus faible d'être signalés par les filtres anti-spam automatisés. |
| **Facilité de mémorisation pour les appels à l'action**<br> Pour les campagnes marketing (par exemple, « Envoyez WIN au 55555 »), un code court est beaucoup plus facile à mémoriser et à saisir pour les utilisateurs qu'un numéro à 10 chiffres. Cela fait des codes courts la référence absolue pour les publicités à la radio, à la télévision et sur les panneaux d'affichage, où l'utilisateur ne dispose que de quelques secondes pour voir ou entendre le numéro. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

| Inconvénients |
| ---- |
| **Les codes courts sont disponibles dans moins de pays**<br> Les codes courts ne sont pas disponibles dans tous les pays. Contactez votre équipe de compte Braze pour obtenir des informations sur les pays dans lesquels vous envisagez d'envoyer des messages. |
| **Processus de demande plus long**<br> Contrairement aux codes longs et aux ID alphanumériques, qui peuvent parfois être provisionnés en 1 à 2 semaines, un code court peut nécessiter 4 à 12 semaines, voire plus, pour être mis à disposition. Chaque opérateur majeur doit approuver manuellement votre demande spécifique avant que le code ne soit activé sur son réseau. Si vous avez un lancement marketing prévu la semaine prochaine, un code court n'est pas une option envisageable. |
| **Coût plus élevé**<br> Les codes courts sont généralement le type d'expéditeur le plus coûteux en raison des frais de configuration et de location annuels. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

{% endtab %}
{% tab SMS Long Codes %}

#### Codes longs SMS {#sms-long-codes}

Un code long est un numéro de téléphone standard utilisé pour envoyer et recevoir des messages SMS. Ces numéros de téléphone sont généralement appelés « codes longs » (numéros à 10 chiffres dans de nombreux pays) par opposition aux codes courts SMS (numéros à 5 ou 6 chiffres).

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel ou bidirectionnel |
| --- | --- | --- | --- | --- |
| 10 chiffres | Demande de 4 à 6 semaines (peut être plus courte ou plus longue selon les pays) | Aux États-Unis, le débit des codes longs dépend de votre score de confiance 10DLC ; sur les marchés internationaux, le débit peut varier ou augmenter dans certaines circonstances, mais il commence généralement autour de 10 segments de message par seconde (MPS). | Oui | Bidirectionnel (en fonction de l'endroit où vous envoyez) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Familiarité et confiance**<br> Les codes longs ressemblent à des numéros de téléphone personnels et comprennent souvent un indicatif régional. Pour les marques, cela représente un équilibre entre une présence professionnelle et une image personnelle et accessible. |
| **Une plus grande disponibilité dans le monde entier**<br>Les codes longs sont disponibles dans plus de 100 grands pays à travers le monde. Contactez votre gestionnaire de la satisfaction client ou l'[assistance Braze]({{site.baseurl}}/braze_support) pour obtenir la liste des pays disponibles.|
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

| Inconvénients |
| --- |
| **Vitesses d'envoi réduites et limites quotidiennes d'envoi de messages**<br> Les codes longs ne sont pas conçus pour le marketing de masse comme le sont les codes courts. Si vous essayez d'envoyer une offre promotionnelle limitée dans le temps à 100 000 personnes à la fois à partir d'un code long, la distribution de tous les messages pourrait prendre plusieurs heures. Aux États-Unis, des opérateurs tels que T-Mobile peuvent également imposer des limites quotidiennes d'envoi pour les numéros 10DLC en fonction du score de confiance associé à votre marque. |
| **Risque de filtrage plus strict**<br> Étant donné que les codes longs ressemblent à des numéros de téléphone personnels, les opérateurs les surveillent de près afin d'empêcher que les numéros « de personne à personne » ne soient utilisés à des fins de spam. Même avec une campagne 10DLC enregistrée, si le contenu de votre message est trop « spammeur » ou ne respecte pas un formatage strict, vous courez un risque beaucoup plus élevé d'être bloqué par les opérateurs qu'avec un code court préapprouvé. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

{% endtab %}
{% tab SMS Alphanumeric Sender ID %}

#### ID alphanumérique de l'expéditeur SMS {#sms-alphanumeric-sender-id}

Un ID alphanumérique de l'expéditeur (souvent appelé « alpha ») est une chaîne de caractères reconnaissable composée d'une combinaison de lettres et de chiffres (généralement le nom de votre entreprise ou votre marque) qui s'affiche comme ID de l'expéditeur pour les SMS unidirectionnels.

Ils peuvent comporter jusqu'à 11 caractères et contenir des lettres majuscules (A-Z) et minuscules (a-z), des espaces et des chiffres (0-9). Ils **ne peuvent pas** contenir uniquement des chiffres.

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel ou bidirectionnel |
| --- | --- | --- | --- | --- |
| Jusqu'à 11 caractères | Disponible immédiatement si aucune préinscription n'est requise. Dans la plupart des pays où l'enregistrement est obligatoire, le délai est généralement de 1 à 4 semaines. | Varie selon le pays | Non | Unidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

##### Avantages et inconvénients

| Avantages | Inconvénients |
| ---- | ---- |
| {::nomarkdown} <ul><li> Reconnaissance accrue de la marque </li><li> Sur de nombreux marchés internationaux, les opérateurs locaux préenregistrent et vérifient les expéditeurs alphanumériques afin que vos messages soient moins susceptibles d'être interceptés par les filtres anti-spam agressifs des opérateurs, qui pourraient autrement bloquer les codes longs aléatoires. </li><li> Disponible sous une semaine si aucune préinscription n'est requise. </li></ul> {:/} | {::nomarkdown} <ul><li> L'<a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>envoi de messages bidirectionnel</a> n'est pas pris en charge. </li><li> Cette fonctionnalité n'est pas disponible dans tous les pays. Par exemple, elle est prise en charge au Royaume-Uni, mais bloquée aux États-Unis. </li><li> Certains pays ont mis en place un processus de préinscription complexe qui nécessite la soumission de documents juridiques et des délais plus longs. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Avantages et inconvénients" }

Pour plus d'informations sur les ID alphanumériques de l'expéditeur, contactez votre gestionnaire de la satisfaction client.
{% endtab %}
{% tab SMS toll-free numbers %}

#### Numéros gratuits compatibles SMS {#sms-enabled-toll-free-numbers}

Les numéros gratuits ont des indicatifs régionaux distincts à trois chiffres (par exemple, 800, 888, 877 et 866), ce qui permet aux utilisateurs de joindre les entreprises sans frais. Largement utilisés pour le service client, ils peuvent également traiter tous les types d'envoi de messages A2P (application-to-person), y compris le marketing.

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel ou bidirectionnel |
| --- | --- | --- | --- | --- |
| 10 chiffres	 | Demande de 2 à 4 semaines | Commence à 3 MPS (segments par seconde), possibilité d'augmentation moyennant des frais supplémentaires | Oui | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Image professionnelle**<br> Les numéros gratuits sont largement reconnus et appréciés en Amérique du Nord pour les communications professionnelles, conférant une image professionnelle et sérieuse. |
| **Débit flexible ; aucune limite d'envoi par opérateur**<br> Contrairement aux codes longs standard, qui peuvent être soumis à des limites de débit ou d'envoi par opérateur selon le pays, les numéros gratuits peuvent bénéficier d'un débit accru pour prendre en charge des volumes plus importants et ne sont soumis à aucune limite quotidienne d'envoi par opérateur aux États-Unis.|
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

| Inconvénients |
| --- |
| **Caractère impersonnel et neutralité géographique**<br> Étant donné que les numéros gratuits ne comportent pas d'indicatif régional, ils peuvent paraître trop « corporate » ou anonymes. Pour une entreprise de services locale, un numéro gratuit peut être moins performant qu'un code long standard, car il manque de lien avec la communauté et peut parfois être confondu avec une ligne de télémarketing aléatoire. |
| **Couche supplémentaire de filtrage STOP**<br> Les numéros gratuits comportent une couche de gestion des désabonnements en dehors de Braze qui ne peut être ni supprimée ni personnalisée. Lorsqu'un utilisateur envoie « STOP » par SMS à votre numéro gratuit, il est désabonné de tout envoi de messages ultérieur depuis votre numéro et reçoit une réponse automatique générée par le réseau. Il ne recevra plus de messages de votre numéro gratuit tant qu'il n'aura pas envoyé « START » pour être retiré de la liste de blocage du numéro gratuit. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

{% endtab %}
{% endtabs %}

## Configuration {#setup}

Les exigences de configuration et les délais varient selon le type d'expéditeur et le pays dans lequel celui-ci est provisionné.

{% tabs local %}
{% tab RCS-verified sender %}

### Expéditeur vérifié RCS

Les expéditeurs vérifiés RCS sont provisionnés pays par pays. Le processus de vérification et de configuration se concentre sur votre agent ou expéditeur, c'est-à-dire le personnage numérique qui interagit avec les utilisateurs. Vous fournirez les ressources de marque et les détails de vérification.

#### Ressources de marque {#brand-assets}

- **Nom vérifié :** Le nom que les utilisateurs voient en haut du fil de messages. Il doit s'agir d'un nom commercial reconnaissable, pas nécessairement de la dénomination sociale de votre entreprise.
- **Logo :** Une image haute résolution de 224x224 px. Elle est affichée dans un cadre circulaire, veillez donc à centrer les éléments essentiels.
- **Bannière (image principale) :** Une image d'arrière-plan pour votre carte de profil professionnel (similaire à une photo de couverture Facebook ou LinkedIn).
- **Couleur de la marque :** Une valeur hexadécimale pour les boutons et les éléments d'interface afin de correspondre au style de votre entreprise.

#### Détails de la vérification {#verification-details}

- **Personne de contact :** C'est un point essentiel. Vous devez fournir l'adresse e-mail d'un employé direct de la marque (et non celle d'une agence). Google ou l'opérateur enverra un e-mail à cette personne pour confirmer qu'elle a autorisé Braze à agir en votre nom.
- **Site web et politique de confidentialité :** Un site web fonctionnel et une politique de confidentialité expliquant comment vous traitez les données des utilisateurs et l'envoi de messages.
- **Description du cas d'utilisation :** Une explication claire de ce que vous envoyez (par exemple, « Mises à jour de livraison de commandes et assistance client pour les achats au détail »).

Les délais de mise en œuvre du RCS varient selon les pays et à mesure que de nouveaux opérateurs adoptent ce canal. Actuellement, vous pouvez vous attendre à ce qu'un expéditeur RCS soit approuvé par les opérateurs dans un délai de 3 à 6 semaines à compter de la demande de lancement.

{% endtab %}
{% tab SMS short codes %}

### Codes courts SMS

Les codes courts sont provisionnés pays par pays. Selon le pays, le processus de demande de code court est réputé pour son caractère imprévisible. Braze est là pour vous accompagner à chaque étape. Si vous souhaitez obtenir un code court, contactez votre gestionnaire d'onboarding ou un autre conseiller Braze.

Braze vous aidera à rassembler tous les documents et informations nécessaires pour soumettre une demande et configurer un nouveau code court. Les exigences varient selon les pays, mais la plupart exigent au minimum les éléments suivants :

| Documents de candidature    | Description    | Conditions    |
|----------------------|----------------|-----------------|
| Appel à l'action (abonnement) | L'objectif principal de ces informations est de confirmer que l'utilisateur consent à recevoir des messages texte et comprend la nature du programme. | {::nomarkdown}<ul><li>Description du produit</li><li>Mention de la fréquence des messages</li><li>Conditions générales complètes OU lien vers les conditions générales complètes</li><li>Politique de confidentialité OU lien vers la politique de confidentialité</li><li>Mot-clé STOP</li><li>Mention « Des frais de messages et de données peuvent s'appliquer ».</li></ul>{:/} |
| Conditions générales | Les conditions générales complètes peuvent être présentées intégralement sous l'appel à l'action ou accessibles via un lien situé à proximité de l'appel à l'action. | {::nomarkdown}<ul><li>Nom du programme (marque)</li><li>Mention de la fréquence des messages</li><li>Description du produit</li><li>Coordonnées du service client</li><li>Informations relatives à la désinscription</li><li>Mention « Des frais de messages et de données peuvent s'appliquer ».</li></ul>{:/} |
| Flux des messages | Les programmes d'envoi de messages récurrents doivent confirmer l'abonnement par un seul SMS indiquant explicitement le programme auquel l'utilisateur s'est inscrit et fournir des instructions claires pour se désabonner.<br><br> Braze traite les messages d'abonnement, de désinscription et d'aide, mettant automatiquement à jour le statut du groupe d'abonnement pour l'utilisateur et son numéro de téléphone associé sur toutes les demandes entrantes.<br><br> Notez que ces mots-clés et réponses par défaut sont également personnalisables. | {::nomarkdown}<ul><li>Confirmation d'abonnement :<ul><li>Nom du programme (marque) OU description du produit</li><li>Informations relatives à la désinscription</li><li>Coordonnées du service client</li><li>Mention de la fréquence des messages</li><li>Mention « Des frais de messages et de données peuvent s'appliquer ».</li></ul></li><li>Réponse HELP :<ul><li>Nom du programme (marque) OU description du produit</li><li>Coordonnées du service client (adresse e-mail ou numéro de téléphone).</li></ul></li><li>Réponse de désinscription (STOP) :<ul><li>Nom du programme (marque) OU description du produit</li><li>Confirmation qu'aucun autre message ne sera envoyé.</li></ul></li></ul>{:/} |
| Messages du programme | Les messages du programme sont envoyés dans le cadre normal du programme de code court, après que l'utilisateur a reçu une confirmation d'abonnement. | {::nomarkdown}<ul><li>Les instructions relatives à la désinscription doivent être fournies à intervalles réguliers et au moins une fois par mois.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Codes courts SMS" }

Une fois tous vos documents de candidature prêts, Braze soumet la demande à nos fournisseurs en votre nom. La demande est ensuite examinée et approuvée par les opérateurs locaux, qui peuvent fournir des commentaires supplémentaires ou demander des informations complémentaires. Une fois que tous les opérateurs ont donné leur accord, vous pouvez immédiatement configurer le code court pour l'utiliser dans Braze.

Le délai d'examen et d'approbation des codes courts varie, mais prend généralement entre 4 et 12 semaines selon le pays et la nature du programme.

{% alert important %}
Si vous disposez déjà de votre propre code court, contactez votre gestionnaire de la satisfaction client pendant le processus d'onboarding afin de discuter de la migration ou du transfert de votre code court.
{% endalert %}

{% endtab %}
{% tab SMS long codes and toll-free numbers %}

### Codes longs SMS (10DLC) et numéros gratuits {#sms-long-codes-10dlc-and-toll-free-numbers}

Dans de nombreux pays, la configuration de codes longs (également appelés « 10DLC » ou « codes longs à 10 chiffres ») et de numéros gratuits pour l'envoi de SMS est passée d'un processus « plug and play » à un système de vérification réglementé. Les opérateurs veulent savoir exactement qui vous êtes et ce que vous comptez envoyer avant de vous autoriser à le faire.

Au cours du processus de configuration du code long, vous serez invité à fournir des informations détaillées sur l'identité de votre marque et l'intention de votre campagne.

#### Identité de marque {#brand-identity}

- **Nom de l'entité juridique :** Doit correspondre exactement à vos documents fiscaux (par exemple, « Acme Corp LLC » et non « Acme »).
- **Numéro d'identification fiscale :** Aux États-Unis, il s'agit de votre numéro d'identification d'employeur (EIN). À l'international, vous aurez besoin d'un numéro de taxe sur la valeur ajoutée (TVA) ou d'un numéro d'enregistrement commercial local (BRN).
- **Présence numérique :** Un site web fonctionnel et en ligne. Les opérateurs peuvent le vérifier pour s'assurer que vous n'êtes pas une société fictive.
- **Personne de contact autorisée :** Nom, adresse e-mail et numéro de téléphone de la personne responsable du compte.

#### Intention de la campagne {#campaign-intent}

- **Cas d'utilisation :** Indiquez si vous envoyez des codes 2FA, des rappels de rendez-vous, des promotions marketing ou autre.
- **Exemples de messages :** Fournissez 2 à 5 exemples de ce que vous enverrez.
- **Preuve d'abonnement :** Décrivez (et montrez souvent une capture d'écran de) la manière dont un utilisateur s'inscrit. Par exemple, un formulaire web avec une case à cocher ou le mot-clé « Text START » sur une affiche.

Braze collaborera avec vous pour rassembler toutes les informations nécessaires au provisionnement de votre code long ou numéro gratuit, puis soumettra ces informations à notre fournisseur pour examen et approbation. Une fois que notre fournisseur a approuvé le programme, nous configurons immédiatement le code long ou le numéro gratuit dans Braze.

Le délai de configuration dépend du pays de provisionnement. En règle générale, l'approbation des codes longs et des numéros gratuits prend entre 1 et 4 semaines.

{% alert important %}
Tous les clients qui possèdent et/ou utilisent actuellement des codes longs américains pour envoyer des messages à des clients américains sont tenus d'enregistrer leurs codes longs. Pour en savoir plus sur les spécificités de l'enregistrement A2P 10DLC aux États-Unis et sur les raisons pour lesquelles il est obligatoire, consultez notre [article dédié au 10DLC]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc).
{% endalert %}

{% endtab %}
{% tab SMS alphanumeric sender ID %}

### ID alphanumérique de l'expéditeur SMS

Les ID alphanumériques des expéditeurs sont soumis à une réglementation stricte, car ils peuvent être facilement usurpés à des fins d'hameçonnage. Bien que certains pays autorisent toute personne à créer et à envoyer des messages à partir d'un nom, dans de nombreux pays, vous devez d'abord prouver que vous êtes propriétaire de la marque.

Les informations suivantes peuvent vous être demandées pour configurer un ID alphanumérique d'expéditeur.

- **ID préféré :** Une chaîne de caractères pouvant contenir jusqu'à 11 caractères. Elle doit contenir au moins une lettre et ne peut pas être un mot générique tel que « BANK » ou « INFO ».
- **Preuve de propriété de la marque :** Votre certificat de marque déposée ou un document d'enregistrement de votre entreprise (par exemple, un certificat de constitution délivré au cours des 12 derniers mois).
- **Lettre d'autorisation :** Une lettre signée sur le papier à en-tête de votre entreprise autorisant Braze et notre fournisseur à envoyer des messages en votre nom à l'aide de cet ID spécifique.
- **Exemples de modèles de messages :** Dans plusieurs régions, vous devez enregistrer les modèles exacts des messages que vous avez l'intention d'envoyer. Toute divergence dans les messages réels peut entraîner des échecs de distribution dans ces pays.

Le délai de configuration d'un ID alphanumérique d'expéditeur dépend fortement du fait que le pays autorise une configuration « dynamique » (immédiate, sans inscription requise) ou exige une « préinscription ». Dans les pays où une préinscription est requise, le délai de configuration varie, mais il est généralement compris entre 1 et 4 semaines.

{% endtab %}
{% endtabs %}

## Foire aux questions {#frequently-asked-questions}

Pour obtenir des réponses aux questions fréquentes concernant les expéditeurs de SMS et de RCS, consultez notre page de [questions fréquentes sur les SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/faqs#frequently-asked-questions).