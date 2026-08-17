# Expéditeurs de SMS et de RCS {#sms-and-rcs-senders}

> Cet article fournit un aperçu des codes et des expéditeurs disponibles pour l'envoi de SMS et de messages RCS.

## Types d'expéditeurs SMS et RCS {#types-of-sms-and-rcs-senders}

{% tabs %}
{% tab Expéditeur vérifié RCS %}

### Expéditeur vérifié RCS {#rcs-verified-sender}

Le RCS est un système de messagerie moderne qui offre davantage de fonctionnalités que le SMS traditionnel, en introduisant des capacités telles que les identifiants d'expéditeur de marque, les médias enrichis et le contenu interactif, comme les carrousels défilants, les réponses rapides, les boutons d'appel à l'action, et bien plus encore. Il est conçu pour offrir une expérience utilisateur plus élégante et plus engageante.

{% alert important %}
Les messages RCS ne peuvent pas être envoyés via les services de messagerie Twilio. Les groupes d'abonnement qui utilisent Twilio pour le SMS doivent utiliser un expéditeur RCS compatible avec Infobip (ou un autre fournisseur RCS pris en charge) pour le trafic RCS. Sinon, les envois RCS sont annulés au moment de l'envoi.
{% endalert %}

#### Détails {#details}

| Composants visuels | Accès | Débit | MMS activé | Unidirectionnel vs. bidirectionnel |
| --- | --- | --- | --- | --- |
| - Nom de marque<br>- logo<br>- légende optionnelle<br> - badge vérifié | 4 à 6 semaines pour l'approbation de l'opérateur | Le débit et la distribution dépendent de la connexion de données active du destinataire (données mobiles ou Wi-Fi). Le RCS ne repose pas sur des limites fixes imposées par le réseau comme le SMS ; les messages RCS sont envoyés via des réseaux de données plutôt que par les canaux de signalisation cellulaire traditionnels utilisés par le SMS. | N/A | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

#### Avantages et inconvénients {#pros-and-cons}

| Avantages |
| ---- |
| **Confiance vérifiée et image de marque**<br> Contrairement au SMS traditionnel, où votre marque apparaît sous la forme d'un code court aléatoire à 5 chiffres ou d'un code long, le RCS permet des profils d'expéditeur vérifiés. Ces profils incluent le logo de votre marque, son nom et une coche « vérifié ». |
| **Fonctionnalités de messagerie enrichie**<br> Le RCS prend en charge les carrousels, les vidéos haute résolution et les boutons d'action suggérés (tels que « Réserver maintenant », « Suivre le colis » ou « Payer la facture »). Les utilisateurs peuvent accomplir des tâches complexes sans quitter leur application de messagerie, ce qui peut entraîner des taux de conversion plus élevés qu'un simple lien en texte brut. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

| Inconvénients |
| ---- |
| **Prise en charge fragmentée**<br> Bien que Google ait fortement promu le RCS pour Android et qu'Apple ait récemment introduit la prise en charge du RCS pour iOS, l'implémentation peut encore être inégale selon les opérateurs et les régions. Si le téléphone ou l'opérateur d'un utilisateur ne prend pas en charge le RCS, le message est généralement envoyé en SMS classique, perdant ainsi toutes les fonctionnalités « enrichies » du RCS. |
| **Incohérences entre plateformes**<br> L'expérience utilisateur RCS varie en fonction de l'opérateur du destinataire, du modèle d'appareil et de l'application de messagerie utilisée (par exemple, Google Messages ou iMessage). |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

{% endtab %}
{% tab Codes courts SMS %}

#### Codes courts SMS {#sms-short-codes}

Un code court est un numéro de 5 à 6 chiffres qui peut envoyer et recevoir des SMS vers et depuis des téléphones mobiles à des débits plus élevés que les codes longs. Les codes courts sont recommandés pour les envois à fort volume et sensibles au temps.

Certains pays vous permettent de choisir un numéro spécifique moyennant des frais supplémentaires. Ces codes courts sont appelés codes courts personnalisés (vanity). Si les codes courts personnalisés vous intéressent, contactez votre conseiller Braze pour plus de détails.

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel vs. bidirectionnel |
| --- | --- | --- | --- | --- |
| 5-6 chiffres | Demande de 4 à 12 semaines | 100 messages par seconde ou plus | Oui | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Vitesse et évolutivité**<br> Les codes courts sont spécifiquement conçus pour le trafic à fort volume. Ils peuvent envoyer des messages à des débits plus élevés que les codes longs et, parce qu'ils sont pré-vérifiés directement par les opérateurs, ils présentent le risque le plus faible d'être signalés par les filtres anti-spam automatisés. |
| **Facile à mémoriser pour les « appels à l'action »**<br> Pour les Campaigns marketing (par exemple, « Envoyez GAGNER au 55555 »), un code court est beaucoup plus facile à retenir et à saisir qu'un numéro à 10 chiffres. Cela fait des codes courts la référence pour les publicités à la radio, à la télévision et sur les panneaux d'affichage, où l'utilisateur n'a que quelques secondes pour voir ou entendre le numéro. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

| Inconvénients |
| ---- |
| **Les codes courts sont disponibles dans moins de pays**<br> Les codes courts ne sont pas disponibles dans tous les pays. Contactez votre équipe Braze pour vous renseigner sur les pays dans lesquels vous prévoyez d'envoyer des messages. |
| **Processus de demande plus long**<br> Contrairement aux codes longs et aux identifiants d'expéditeur alphanumériques, qui peuvent parfois être provisionnés en 1 à 2 semaines, un code court peut prendre de 4 à 12 semaines ou plus pour être provisionné. Chaque opérateur majeur doit approuver manuellement votre demande spécifique avant que le code ne soit actif sur son réseau. Si vous avez un lancement marketing la semaine prochaine, un code court n'est pas une option. |
| **Coût plus élevé**<br> Les codes courts tendent à être le type d'expéditeur le plus coûteux en raison des frais de configuration et de location annuelle. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

{% endtab %}
{% tab Codes longs SMS %}

#### Codes longs SMS {#sms-long-codes}

Un code long est un numéro de téléphone standard utilisé pour envoyer et recevoir des SMS. Ces numéros de téléphone sont généralement appelés « codes longs » (numéros à 10 chiffres dans de nombreux pays) par comparaison avec les codes courts SMS (numéros à 5-6 chiffres).

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel vs. bidirectionnel |
| --- | --- | --- | --- | --- |
| 10 chiffres | Demande de 4 à 6 semaines (peut être plus courte ou plus longue selon les pays) | Aux États-Unis, le débit des codes longs dépend de votre score de confiance 10DLC ; sur les marchés internationaux, le débit peut varier ou augmenter dans certaines circonstances, mais commence généralement autour de 10 segments de message par seconde (MPS). | Oui | Bidirectionnel (selon la destination de l'envoi) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Familiarité et confiance**<br> Les codes longs ressemblent à des numéros de téléphone personnels, incluant souvent un indicatif régional local. Pour les marques, cela représente un équilibre entre présence professionnelle et une approche personnelle et accessible. |
| **Plus grande disponibilité mondiale**<br> Les codes longs sont disponibles dans plus de 100 pays majeurs à travers le monde. Contactez votre CSM ou le [support Braze]({{site.baseurl}}/braze_support) pour obtenir la liste des pays disponibles. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

| Inconvénients |
| --- |
| **Vitesses d'envoi plus lentes et limites quotidiennes de messages**<br> Les codes longs ne sont pas conçus pour le marketing de masse comme le sont les codes courts. Si vous essayez d'envoyer une vente flash urgente à 100 000 personnes en même temps depuis un code long, la distribution de tous les messages pourrait prendre des heures. Aux États-Unis, des opérateurs comme T-Mobile peuvent également imposer des limites d'envoi quotidiennes pour le 10DLC en fonction du score de confiance de votre marque. |
| **Risque de filtrage plus strict**<br> Parce que les codes longs ressemblent à des numéros de téléphone personnels, les opérateurs les surveillent de près pour empêcher que des numéros « de personne à personne » soient utilisés pour du spam. Même avec une Campaign 10DLC enregistrée, si le contenu de votre message est trop « spammy » ou ne respecte pas un formatage strict, vous avez un risque beaucoup plus élevé d'être bloqué par les opérateurs par rapport à un code court pré-approuvé. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

{% endtab %}
{% tab Identifiant d'expéditeur alphanumérique SMS %}

#### Identifiant d'expéditeur alphanumérique SMS {#sms-alphanumeric-sender-id}

Un identifiant d'expéditeur alphanumérique (souvent appelé « alpha ») est une chaîne reconnaissable composée de toute combinaison de lettres et de chiffres (souvent le nom de votre entreprise ou de votre marque) affichée comme identifiant d'expéditeur pour la messagerie texte unidirectionnelle.

Ils peuvent contenir jusqu'à 11 caractères et inclure des lettres majuscules (A-Z) et minuscules (a-z), des espaces et des chiffres (0-9). Ils **ne peuvent pas** contenir uniquement des chiffres.

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel vs. bidirectionnel |
| --- | --- | --- | --- | --- |
| Jusqu'à 11 caractères | Disponible immédiatement si le pré-enregistrement n'est pas requis. Sinon, 1 à 4 semaines dans la plupart des pays où l'enregistrement est requis. | Varie selon le pays | Non | Unidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

##### Avantages et inconvénients

| Avantages | Inconvénients |
| ---- | ---- |
| {::nomarkdown} <ul><li> Meilleure reconnaissance de la marque </li><li> Sur de nombreux marchés internationaux, les opérateurs locaux pré-enregistrent et vérifient les expéditeurs alphanumériques, de sorte que vos messages ont moins de chances d'être interceptés par les filtres anti-spam agressifs des opérateurs qui pourraient autrement bloquer des codes longs aléatoires </li><li> Disponible sous 1 semaine si le pré-enregistrement n'est pas requis </li></ul> {:/} | {::nomarkdown} <ul><li> La <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>messagerie bidirectionnelle</a> n'est pas prise en charge </li><li> Tous les pays ne prennent pas en charge cette fonctionnalité. Par exemple, elle est prise en charge au Royaume-Uni mais bloquée aux États-Unis. </li><li> Certains pays ont un processus de pré-enregistrement étendu qui nécessite la soumission de documents juridiques et des délais plus longs. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Avantages et inconvénients" }

Pour plus d'informations sur les identifiants d'expéditeur alphanumériques, contactez votre CSM.
{% endtab %}
{% tab Numéros gratuits SMS %}

#### Numéros gratuits compatibles SMS {#sms-enabled-toll-free-numbers}

Les numéros gratuits ont des indicatifs régionaux distincts à trois chiffres (par exemple, 800, 888, 877 et 866), permettant aux utilisateurs de contacter les entreprises sans être facturés. Largement utilisés pour le service client, ils peuvent également gérer tous les types de messagerie A2P (application vers personne), y compris le marketing.

##### Détails

| Longueur | Accès | Débit | MMS activé | Unidirectionnel vs. bidirectionnel |
| --- | --- | --- | --- | --- |
| 10 chiffres | Demande de 2 à 4 semaines | Commence à 3 MPS (segments par seconde), peut être augmenté moyennant des frais supplémentaires | Oui | Bidirectionnel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails" }

##### Avantages et inconvénients

| Avantages |
| ---- |
| **Image professionnelle**<br> Les numéros gratuits sont largement reconnus et fiables en Amérique du Nord pour la communication d'entreprise, apportant une touche professionnelle et faisant autorité. |
| **Débit flexible ; pas de limites d'envoi imposées par les opérateurs**<br> Contrairement aux codes longs standard, qui peuvent fixer des limites de débit ou d'envoi par opérateur selon le pays, les numéros gratuits peuvent voir leur débit augmenté pour prendre en charge des volumes plus élevés et n'ont pas de limites d'envoi quotidiennes imposées par les opérateurs aux États-Unis. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

| Inconvénients |
| --- |
| **Impersonnel et neutralité géographique**<br> Parce que les numéros gratuits n'ont pas d'indicatif régional local, ils peuvent sembler trop « corporate » ou anonymes. Pour une entreprise de services locale, un numéro gratuit peut être moins performant qu'un code long standard car il manque de connexion avec la communauté et peut parfois être confondu avec une ligne de télémarketing aléatoire. |
| **Couche supplémentaire de filtrage STOP**<br> Les numéros gratuits disposent d'une couche de gestion de désinscription en dehors de Braze qui ne peut être ni supprimée ni personnalisée. Lorsqu'un utilisateur envoie « STOP » à votre numéro gratuit, il est désinscrit de tout message ultérieur provenant de votre numéro et reçoit une réponse automatique générée par le réseau. Il ne recevra plus de messages de votre numéro gratuit tant qu'il n'aura pas envoyé « START » pour être retiré de la liste de blocage du numéro gratuit. |
{: .reset-td-br-1 aria-label="Avantages et inconvénients" }

{% endtab %}
{% endtabs %}

## Utiliser des codes courts et des codes longs ensemble {#using-short-codes-and-long-codes-together}

Si votre groupe d'abonnement comprend à la fois des codes courts et des codes longs, les codes courts sont généralement prioritaires pour les messages sortants. Cependant, certains fournisseurs proposent une fonctionnalité de sticky sender, qui peut entraîner l'utilisation continue d'un code long pour certains utilisateurs même après l'ajout d'un code court au pool d'expéditeurs.

Le sticky sender maintient la continuité des messages en acheminant tous les messages destinés à un utilisateur spécifique depuis le même numéro de téléphone. Si un utilisateur a reçu un message depuis un code long avant qu'un code court ne soit ajouté à votre groupe d'abonnement, votre fournisseur peut continuer à utiliser ce code long pour les futurs messages destinés à cet utilisateur, même si le code court serait normalement prioritaire.

Ce comportement est contrôlé par les fournisseurs et ne peut pas être modifié dans Braze.

## Configuration {#setup}

Les exigences et les délais de configuration varient selon le type d'expéditeur et le pays dans lequel l'expéditeur est provisionné.

{% tabs local %}
{% tab RCS-verified sender %}

### Expéditeur vérifié RCS

Les expéditeurs vérifiés RCS sont provisionnés pays par pays. Le processus de vérification et de configuration se concentre sur votre agent ou expéditeur — le personnage numérique qui interagit avec les utilisateurs. Vous fournirez des ressources de marque et des informations de vérification.

#### Ressources de marque {#brand-assets}

- **Nom vérifié :** le nom que les utilisateurs voient en haut du fil de messages. Il doit s'agir d'un nom commercial reconnaissable, pas nécessairement de votre raison sociale.
- **Logo :** une image haute résolution de 224x224 px. Elle est affichée dans un cadre circulaire, veillez donc à centrer les éléments importants.
- **Bannière (image principale) :** une image d'arrière-plan pour la carte de profil de votre entreprise (similaire à une photo de couverture Facebook ou LinkedIn).
- **Couleur de marque :** une valeur hexadécimale pour les boutons et les éléments d'interface afin de correspondre au style de votre entreprise.

#### Informations de vérification {#verification-details}

- **Point de contact (POC) :** cet élément est essentiel. Vous devez fournir une adresse e-mail d'un employé direct de la marque (pas une adresse d'agence). Google ou l'opérateur enverra un e-mail à cette personne pour confirmer qu'elle a autorisé Braze à agir en votre nom.
- **Site web et politique de confidentialité :** un site web actif et une politique de confidentialité expliquant comment vous gérez les données utilisateur et les communications.
- **Description du cas d'usage :** une explication claire de ce que vous envoyez (par exemple, « Mises à jour de livraison de commandes et support client pour les achats en magasin »).

Les délais RCS fluctuent selon le pays, et à mesure que davantage d'opérateurs adoptent le canal. Actuellement, vous pouvez vous attendre à ce qu'un expéditeur RCS soit approuvé par les opérateurs dans un délai de 3 à 6 semaines après la demande de lancement.

{% endtab %}
{% tab SMS short codes %}

### Codes courts SMS

Les codes courts sont provisionnés pays par pays. Selon le pays, le processus de demande de code court est réputé pour être imprévisible. Braze est là pour vous accompagner à chaque étape, donc si vous souhaitez un code court, contactez votre gestionnaire d'onboarding ou un autre conseiller Braze.

Braze vous aidera à rassembler tous les documents et informations nécessaires pour soumettre une demande et configurer un nouveau code court. Les exigences varient selon le pays, mais beaucoup requièrent au minimum les éléments suivants :

| Document de demande | Description | Exigences |
|----------------------|-------------|-----------|
| Appel à l'action (abonnement) | L'objectif principal des mentions est de confirmer que l'utilisateur consent à recevoir des messages texte et comprend la nature du programme. | {::nomarkdown}<ul><li>Description du produit</li><li>Mention de la fréquence des messages</li><li>Conditions générales complètes OU lien vers les conditions générales complètes</li><li>Politique de confidentialité OU lien vers la politique de confidentialité</li><li>Mot-clé STOP</li><li>Mention « Des frais de messages et de données peuvent s'appliquer ».</li></ul>{:/} |
| Conditions générales | Des conditions générales complètes peuvent être entièrement présentées sous l'appel à l'action ou accessibles via un lien à proximité de l'appel à l'action. | {::nomarkdown}<ul><li>Nom du programme (marque)</li><li>Mention de la fréquence des messages</li><li>Description du produit</li><li>Coordonnées du service client</li><li>Informations de désinscription</li><li>Mention « Des frais de messages et de données peuvent s'appliquer ».</li></ul>{:/} |
| Flux de messages | Les programmes de messages récurrents doivent confirmer l'abonnement par un seul message texte indiquant explicitement à quel programme l'utilisateur s'est inscrit, et fournir des instructions claires de désinscription.<br><br> Braze traite les messages d'abonnement, de désinscription et d'aide, en mettant automatiquement à jour l'état du groupe d'abonnement pour l'utilisateur et son numéro de téléphone associé sur toutes les demandes entrantes.<br><br> Notez que ces mots-clés et réponses par défaut peuvent également être personnalisés. | {::nomarkdown}<ul><li>Confirmation d'abonnement :<ul><li>Nom du programme (marque) OU description du produit</li><li>Informations de désinscription</li><li>Coordonnées du service client</li><li>Mention de la fréquence des messages</li><li>Mention « Des frais de messages et de données peuvent s'appliquer ».</li></ul></li><li>Réponse HELP :<ul><li>Nom du programme (marque) OU description du produit</li><li>Coordonnées du service client (e-mail ou numéro de téléphone du support).</li></ul></li><li>Réponse de désinscription (STOP) :<ul><li>Nom du programme (marque) OU description du produit</li><li>Confirmation qu'aucun autre message ne sera envoyé.</li></ul></li></ul>{:/} |
| Messages du programme | Les messages du programme sont envoyés dans le cadre normal du programme de code court, après que l'utilisateur a reçu une confirmation d'abonnement. | {::nomarkdown}<ul><li>Les instructions de désinscription doivent être fournies à intervalles réguliers et au moins une fois par mois.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Codes courts SMS" }

Lorsque tous vos documents de demande sont prêts, Braze soumet la demande à nos fournisseurs en votre nom. La demande est ensuite examinée et approuvée par les opérateurs locaux qui peuvent fournir des commentaires supplémentaires ou demander des informations complémentaires. Une fois que tous les opérateurs ont donné leur approbation, vous pouvez immédiatement configurer le code court pour l'utiliser dans Braze.

Le délai d'examen et d'approbation des codes courts varie, mais prend généralement de 4 à 12 semaines selon le pays et la nature du programme.

{% alert important %}
Si vous possédez déjà votre propre code court, contactez votre gestionnaire du succès des clients pendant le processus d'onboarding pour discuter de la migration ou du transfert de votre code court.
{% endalert %}

{% endtab %}
{% tab SMS long codes and toll-free numbers %}

### Codes longs SMS (10DLC) et numéros gratuits {#sms-long-codes-10dlc-and-toll-free-numbers}

Dans de nombreux pays, la configuration des codes longs (également appelés « 10DLC » ou « codes longs à 10 chiffres ») et des numéros gratuits pour l'envoi de SMS est passée d'un processus « plug and play » à un système de vérification réglementé. Les opérateurs veulent savoir exactement qui vous êtes et ce que vous prévoyez d'envoyer avant que vous ne commenciez.

Pendant le processus de configuration du code long, vous pouvez vous attendre à partager des informations sur l'identité de votre marque et l'intention de votre campagne.

#### Identité de marque {#brand-identity}

- **Raison sociale :** doit correspondre exactement à vos documents fiscaux (par exemple, « Acme Corp LLC » et non « Acme »).
- **Numéro d'identification fiscale :** aux États-Unis, il s'agit de votre Employer Identification Number (EIN). À l'international, vous aurez besoin d'un numéro de taxe sur la valeur ajoutée (TVA) ou d'un numéro d'immatriculation d'entreprise local (BRN).
- **Présence numérique :** un site web actif et fonctionnel. Les opérateurs peuvent le vérifier pour confirmer que vous n'êtes pas une société « écran ».
- **Contact autorisé :** nom, adresse e-mail et numéro de téléphone d'une personne responsable du compte.

#### Intention de la campagne {#campaign-intent}

- **Cas d'usage :** indiquez si vous envoyez des codes 2FA, des rappels de rendez-vous, des promotions marketing ou autre.
- **Exemples de messages :** fournissez 2 à 5 exemples de ce que vous enverrez.
- **Preuve d'abonnement :** décrivez (et montrez souvent une capture d'écran de) la manière dont un utilisateur s'inscrit. Les exemples incluent un formulaire web avec une case à cocher ou un mot-clé « Envoyez START » sur une affiche.

Braze travaillera avec vous pour collecter toutes les informations nécessaires au provisionnement de votre code long ou numéro gratuit, puis soumettra les détails à notre fournisseur pour examen et approbation. Une fois que notre fournisseur a approuvé le programme, nous configurons immédiatement le code long ou le numéro gratuit dans Braze.

Le délai de configuration dépend du pays de provisionnement. En général, les codes longs et les numéros gratuits prennent entre 1 et 4 semaines pour être approuvés.

{% alert important %}
Tous les clients qui possèdent et/ou utilisent actuellement des codes longs américains pour envoyer des messages à des clients américains sont tenus d'enregistrer leurs codes longs. Pour en savoir plus sur les spécificités de l'enregistrement 10DLC A2P aux États-Unis et pourquoi il est requis, consultez notre [article dédié au 10DLC]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc).
{% endalert %}

{% endtab %}
{% tab SMS alphanumeric sender ID %}

### Identifiant d'expéditeur alphanumérique SMS

Les identifiants d'expéditeur alphanumériques sont fortement réglementés car ils peuvent être facilement usurpés à des fins de phishing. Alors que certains pays permettent à quiconque de configurer et d'envoyer depuis un nom, dans de nombreux pays, vous devez d'abord prouver que vous êtes propriétaire de la marque.

Les informations suivantes peuvent vous être demandées pour configurer un identifiant d'expéditeur alphanumérique.

- **Identifiant souhaité :** une chaîne de caractères de 11 caractères maximum. Elle contient au moins une lettre et ne peut pas être un mot générique comme « BANK » ou « INFO ».
- **Preuve de propriété de la marque :** votre certificat de marque déposée ou un document d'immatriculation d'entreprise (par exemple, un certificat de constitution délivré au cours des 12 derniers mois).
- **Lettre d'autorisation :** une lettre signée sur le papier à en-tête de votre entreprise autorisant Braze et notre fournisseur à envoyer des messages en votre nom en utilisant cet identifiant spécifique.
- **Modèles de messages exemples :** dans plusieurs régions, vous devez enregistrer les « modèles » exacts des messages que vous prévoyez d'envoyer. Tout écart dans les messages réels peut entraîner des échecs de livraison dans ces pays.

Le délai de configuration d'un identifiant d'expéditeur alphanumérique dépend fortement du fait que le pays autorise une configuration « dynamique » (immédiate, sans enregistrement requis) ou exige un « pré-enregistrement ». Dans les pays qui exigent un pré-enregistrement, le délai de configuration varie, mais il faut généralement entre 1 et 4 semaines.

{% endtab %}
{% endtabs %}

## Questions fréquemment posées {#frequently-asked-questions}

Pour obtenir des réponses aux questions fréquemment posées sur les expéditeurs SMS et RCS, consultez notre page de [questions fréquemment posées sur les SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/faqs#frequently-asked-questions).