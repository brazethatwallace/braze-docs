---
nav_title: "Chiffrement au niveau du champ de l'identifiant"
article_title: "Chiffrement au niveau du champ de l'identifiant"
page_order: 2
alias: "/field_level_encryption/"
description: "Cet article de référence explique comment chiffrer les adresses e-mail afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze."
page_type: reference
---

# Chiffrement au niveau du champ de l'identifiant {#identifier-field-level-encryption}

> Chiffrez les adresses e-mail afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze.

{% multi_lang_include data_activation/field_level_encryption_pii_description.md %}

{% alert important %}
Le chiffrement au niveau du champ de l'identifiant est disponible en tant que fonctionnalité supplémentaire. Pour commencer à utiliser le chiffrement au niveau du champ de l'identifiant, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Fonctionnement {#how-it-works}

Les adresses e-mail doivent être hachées et chiffrées avant d'être ajoutées à Braze. Lors de l'envoi d'un message, un appel est effectué vers AWS KMS pour obtenir l'adresse e-mail déchiffrée. Ensuite, l'adresse e-mail hachée est insérée dans les métadonnées afin que les événements de distribution et d'engagement puissent être associés à l'utilisateur d'origine. C'est ainsi que Braze peut suivre les analyses e-mail. Braze supprime toute adresse e-mail en texte clair incluse et ne stocke pas l'adresse e-mail en texte clair de l'utilisateur.

## Prérequis {#prerequisites}

Pour utiliser le chiffrement au niveau des champs d'identification, vous devez avoir accès à AWS KMS pour [chiffrer](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) et [hacher](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) les adresses e-mail **avant** de les envoyer à Braze.

Suivez ces étapes pour configurer votre méthode d'authentification par clé secrète AWS.

1. Pour récupérer votre identifiant de clé d'accès et votre clé d'accès secrète, [créez un utilisateur IAM et un groupe d'administrateurs](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) dans AWS avec une politique d'autorisations pour AWS Key Management Service. L'utilisateur IAM doit disposer des autorisations [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) et [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html). Pour plus de détails, consultez les [autorisations AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Sélectionnez **Show User Security Credentials** pour afficher votre identifiant de clé d'accès et votre clé d'accès secrète. Notez ces identifiants quelque part ou sélectionnez le bouton **Download Credentials**, car vous devrez les saisir lors de la connexion de vos clés AWS KMS.
3. Vous devez configurer KMS dans les régions AWS suivantes :
    - **Clusters Braze US :** `us-east-1`
    - **Clusters Braze EU :** `eu-central-1`
    - **Cluster Braze AU :** `ap-southeast-2`
    - **Cluster Braze ID :** `ap-southeast-3`
    - **Cluster Braze JP :** `ap-northeast-1`
4. Dans AWS Key Management Service, créez deux clés et assurez-vous que l'utilisateur IAM est ajouté dans les autorisations d'utilisation des clés :
    - **[Chiffrement/déchiffrement](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) :** Sélectionnez le type de clé **Symmetric** et l'utilisation de clé **Encrypt and Decrypt**.
    - **[Hachage](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html) :** Sélectionnez le type de clé **Symmetric** et l'utilisation de clé **Generate and Verify MAC**. La spécification de clé doit être **HMAC_256**. Après avoir créé la clé, notez l'identifiant de clé HMAC quelque part, car vous devrez le saisir dans Braze.

![Paramètres de configuration de la clé avec les options Symmetric, Generate and Verify MAC et HMAC_256 sélectionnées.]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Étape 1 : Connecter vos clés AWS KMS {#step-1-connect-your-aws-kms-keys}

Dans le tableau de bord de Braze, allez dans **Data Settings** > **Field-Level Encryption**. Pour vos paramètres AWS KMS, saisissez les informations suivantes :

- Access key ID
- Secret access key
- Identifiant de clé HMAC (key ID ou key ARN ; cette valeur ne peut pas être modifiée après l'enregistrement)

## Étape 2 : Sélectionnez vos champs chiffrés {#step-2-select-your-encrypted-fields}

Ensuite, sélectionnez **Email address** pour chiffrer le champ.

Lorsque le chiffrement est activé pour un champ, il ne peut pas être rétabli en champ déchiffré. Cela signifie que le chiffrement est un paramètre permanent. Lors de la configuration du chiffrement pour l'adresse e-mail, confirmez qu'aucun utilisateur ne possède d'adresse e-mail dans l'espace de travail. Cela garantit qu'aucune adresse e-mail en texte clair n'est stockée dans Braze lors de l'activation de la fonctionnalité pour l'espace de travail.

![Paramètres de chiffrement au niveau des champs.]({% image_buster /assets/img/field_level_encryption.png %})

## Étape 3 : Importer et mettre à jour les utilisateurs {#step-3-import-and-update-users}

Lorsque le chiffrement au niveau du champ d'identification est activé, vous devez hacher et chiffrer l'adresse e-mail avant de l'ajouter à Braze. Veillez à mettre l'adresse e-mail en minuscules avant de la hacher. Consultez [l'objet attributs utilisateur](#user-attributes-object) pour plus de détails.

Lors de la mise à jour d'une adresse e-mail dans Braze, vous devez utiliser la valeur e-mail hachée partout où `email` est inclus. Cela comprend :

- Les endpoints REST :
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- L'ajout ou la mise à jour d'utilisateurs via CSV

{% alert note %}
Lors de la création d'un nouvel utilisateur avec une adresse e-mail, vous devez ajouter `email_encrypted` avec la valeur e-mail chiffrée de l'utilisateur. Sinon, l'utilisateur ne sera pas créé. De même, si vous ajoutez une adresse e-mail à un utilisateur existant qui n'en possède pas, vous devez ajouter `email_encrypted`. Sinon, l'utilisateur ne sera pas mis à jour.
{% endalert %}

## Considérations {#considerations}

Ces fonctionnalités ne sont pas prises en charge avec le chiffrement au niveau du champ d'identifiant :

- Identification et capture de l'adresse e-mail via le SDK
- Formulaires de capture d'e-mail dans les messages in-app
- Rapports sur le domaine du destinataire, y compris les graphiques de fournisseur de messagerie d'Email Insights
- Filtre d'adresse e-mail par expression régulière
- Synchronisation d'audience
- Intégration Shopify

### Objet d'attributs utilisateur {#user-attributes-object}

Lorsque vous utilisez le chiffrement au niveau du champ d'identifiant avec l'endpoint `/users/track`, notez ces détails de champ pour l'[objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object) :

- Le champ `email` doit contenir la valeur hachée de l'e-mail.
- Le champ `email_encrypted` doit contenir la valeur chiffrée de l'e-mail.

## Questions fréquemment posées {#frequently-asked-questions}

### Quelle est la différence entre le chiffrement et le hachage ? {#what-is-the-difference-between-encrypting-and-hashing}

Le chiffrement est une fonction bidirectionnelle qui permet de chiffrer et de déchiffrer des données. Si la même valeur en texte clair est chiffrée plusieurs fois, l'algorithme de chiffrement d'AWS (AES-256-GCM) produira des valeurs chiffrées différentes. Le hachage est une fonction unidirectionnelle où le texte clair est brouillé de manière irréversible. Le hachage produit la même valeur à chaque fois. Cela nous permet de gérer les états d'abonnement de plusieurs utilisateurs partageant la même adresse e-mail.

### Quelle adresse e-mail dois-je utiliser pour mon envoi de test ? {#what-email-address-should-i-use-in-my-test-send}

Les adresses e-mail en texte clair sont prises en charge dans les envois de test. Pour voir à quoi ressemble un e-mail pour un utilisateur spécifique, procédez comme suit :

1. Sélectionnez **Prévisualiser le message en tant qu'utilisateur**.
2. Dans **Envoi de test**, sélectionnez **Remplacer les attributs des destinataires par ceux de l'utilisateur de la prévisualisation actuelle**.

### Puis-je utiliser un ARN pour la clé HMAC ? {#can-i-use-an-arn-for-the-hmac-key}

Oui. Dans **Paramètres des données** > **Chiffrement au niveau des champs**, l'identifiant de la clé HMAC accepte soit un ID de clé, soit un ARN de clé.

### Comment supprimer ou réinitialiser une clé HMAC ? {#how-do-i-remove-or-reset-an-hmac-key}

Vous ne pouvez pas supprimer ou réinitialiser une clé HMAC dans le tableau de bord après l'avoir enregistrée. Pour demander la réinitialisation d'une clé HMAC ou la suppression de la configuration du chiffrement au niveau des champs de l'identifiant, contactez votre gestionnaire de compte Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support).

{%raw%}
### Que se passe-t-il si j'ajoute cette adresse e-mail Liquid `{{${email_address}}}` dans Braze ? {#what-happens-if-i-add-this-email-address-liquid-email_address-in-braze}

Braze affichera l'adresse e-mail en texte clair lors de l'envoi de l'e-mail. Dans les prévisualisations, la version chiffrée de l'e-mail sera affichée. Nous recommandons d'utiliser l'ID externe de l'utilisateur si vous faites référence à un utilisateur dans une URL personnalisée de désinscription en un clic.

`{{${email_address}}}` n'est actuellement pas pris en charge dans le centre de préférences et les pages de désinscription.
{%endraw%}

### Quelle adresse e-mail dois-je m'attendre à voir dans Currents ? {#what-email-address-should-i-expect-to-see-in-currents}

L'adresse e-mail hachée est incluse dans les événements de réception et d'engagement des e-mails.

### Quelle adresse e-mail dois-je m'attendre à voir dans l'archivage des messages ? {#what-email-address-should-i-expect-to-see-in-message-archiving}

L'adresse e-mail en texte clair est incluse dans l'archivage des messages. Ces derniers sont envoyés directement au fournisseur de stockage cloud du client et d'autres données personnelles peuvent être incluses dans le corps des e-mails.

### Puis-je utiliser la désinscription par liste mail-to pour la gestion des abonnements avec le chiffrement au niveau des champs de l'identifiant ? {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

Non. L'utilisation de la désinscription par liste mail-to enverrait l'adresse e-mail déchiffrée en texte clair à Braze. Avec le chiffrement au niveau des champs de l'identifiant activé, nous prenons en charge la méthode HTTP basée sur l'URL, y compris le clic unique. Nous recommandons également d'inclure un lien de désinscription en un clic dans le corps de votre e-mail.

### Le chiffrement au niveau des champs de l'identifiant prend-il en charge d'autres identifiants comme le numéro de téléphone ? {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

Non. Actuellement, le chiffrement au niveau des champs de l'identifiant est pris en charge uniquement pour les adresses e-mail.