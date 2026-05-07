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

{% multi_lang_include field_level_encryption_pii_description.md %}

{% alert important %}
Le chiffrement au niveau du champ de l'identifiant est disponible en tant que fonctionnalité supplémentaire. Pour commencer à utiliser le chiffrement au niveau du champ de l'identifiant, contactez votre gestionnaire de compte Braze.
{% endalert %}

## Fonctionnement {#how-it-works}

Les adresses e-mail doivent être hachées et chiffrées avant d'être ajoutées à Braze. Lors de l'envoi d'un message, un appel est effectué à AWS KMS pour obtenir l'adresse e-mail déchiffrée. Ensuite, l'adresse e-mail hachée est insérée dans les métadonnées des événements de distribution et d'engagement afin d'être reliée à l'utilisateur d'origine. C'est ainsi que Braze assure le suivi de l'analytique des e-mails. Braze masque toutes les adresses e-mail en clair qui sont incluses et ne stocke pas l'adresse e-mail de l'utilisateur en clair.

## Conditions préalables {#prerequisites}

Pour utiliser le chiffrement au niveau du champ de l'identifiant, vous devez avoir accès à AWS KMS pour [chiffrer](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) et [hacher](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) les adresses e-mail **avant** de les envoyer à Braze.

Procédez comme suit pour configurer votre méthode d'authentification par clé secrète AWS.

1. Pour récupérer votre ID de clé d'accès et votre clé d'accès secrète, [créez un utilisateur IAM et un groupe d'administrateurs](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) dans AWS avec une politique d'autorisations pour AWS Key Management Service. L'utilisateur IAM doit disposer des autorisations [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) et [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html). Pour plus d'informations, consultez la rubrique [Autorisations AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Sélectionnez **Show User Security Credentials** pour afficher votre ID de clé d'accès et votre clé d'accès secrète. Prenez note de ces identifiants ou sélectionnez le bouton **Download Credentials**, car vous devrez les saisir lors de la connexion de vos clés AWS KMS.
3. Vous devez configurer KMS dans les régions AWS suivantes :
    - **Clusters Braze aux États-Unis :** `us-east-1`
    - **Clusters Braze dans l'UE :** `eu-central-1`
    - **Cluster Braze AU :** `ap-southeast-2`
    - **Cluster Braze ID :** `ap-southeast-3`
4. Dans AWS Key Management Service, créez deux clés et assurez-vous que l'utilisateur IAM est ajouté dans les autorisations d'utilisation des clés :
    - **[Chiffrer/déchiffrer](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) :** Sélectionnez le type de clé **Symmetric** et l'utilisation de clé **Encrypt and Decrypt**.
    - **[Hacher](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html) :** Sélectionnez le type de clé **Symmetric** et l'utilisation de clé **Generate and Verify MAC**. La spécification de clé doit être **HMAC_256**. Après avoir créé la clé, prenez note de l'ID de la clé HMAC, car vous devrez le saisir dans Braze.

![]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Étape 1 : Connectez vos clés AWS KMS {#step-1-connect-your-aws-kms-keys}

Dans le tableau de bord de Braze, accédez à **Paramètres des données** > **Field-Level Encryption**. Pour vos paramètres AWS KMS, saisissez les éléments suivants :

- ID de la clé d'accès
- Clé d'accès secrète
- ID de la clé HMAC (elle ne peut pas être mise à jour après enregistrement)

## Étape 2 : Sélectionnez vos champs chiffrés {#step-2-select-your-encrypted-fields}

Ensuite, sélectionnez **Email address** pour chiffrer le champ.

Lorsque le chiffrement est activé pour un champ, il n'est pas possible de revenir à un champ déchiffré. Cela signifie que le chiffrement est un paramètre permanent. Lorsque vous configurez le chiffrement de l'adresse e-mail, assurez-vous qu'aucun utilisateur ne dispose d'une adresse e-mail dans l'espace de travail. Cela garantit qu'aucune adresse e-mail en clair n'est stockée dans Braze lorsque vous activez la fonctionnalité pour l'espace de travail.

![]({% image_buster /assets/img/field_level_encryption.png %})

## Étape 3 : Importation et mise à jour des utilisateurs {#step-3-import-and-update-users}

Lorsque le chiffrement au niveau du champ de l'identifiant est activé, vous devez hacher et chiffrer l'adresse e-mail avant de l'ajouter à Braze. Veillez à mettre l'adresse e-mail en minuscules avant de la hacher. Pour plus de détails, consultez l'[objet attributs de l'utilisateur](#user-attributes-object).

Lorsque vous mettez à jour l'adresse e-mail dans Braze, vous devez utiliser la valeur hachée de l'e-mail partout où `email` est inclus. Cela comprend :

- Les endpoints REST :
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Ajout ou mise à jour d'utilisateurs via CSV

{% alert note %}
Lorsque vous créez un nouvel utilisateur avec une adresse e-mail, vous devez ajouter `email_encrypted` avec la valeur chiffrée de l'e-mail de l'utilisateur. Sinon, l'utilisateur ne sera pas créé. De même, si vous ajoutez une adresse e-mail à un utilisateur existant qui ne dispose pas d'adresse e-mail, vous devez ajouter `email_encrypted`. Dans le cas contraire, l'utilisateur ne sera pas mis à jour.
{% endalert %}

## Considérations {#considerations}

Ces fonctionnalités ne sont pas prises en charge avec le chiffrement au niveau du champ de l'identifiant :

- Identification et capture d'adresse e-mail via le SDK
- Formulaires de capture d'adresse e-mail via les messages in-app
- Rapports sur le domaine du destinataire, y compris les graphiques de fournisseurs de messagerie dans Email Insights
- Filtre d'adresses e-mail par expression régulière
- Synchronisation de l'audience
- Intégration Shopify

### Objet attributs de l'utilisateur {#user-attributes-object}

Lorsque vous utilisez le chiffrement au niveau du champ de l'identifiant avec l'endpoint `/users/track`, notez les détails de ces champs pour l'[objet attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) :

- Le champ `email` doit être la valeur hachée de l'e-mail.
- Le champ `email_encrypted` doit être la valeur chiffrée de l'e-mail.

## Foire aux questions {#frequently-asked-questions}

### Quelle est la différence entre le chiffrement et le hachage ? {#what-is-the-difference-between-encrypting-and-hashing}

Le chiffrement est une fonction bidirectionnelle qui permet de chiffrer et de déchiffrer des données. Si la même valeur en clair est chiffrée plusieurs fois, l'algorithme de chiffrement d'AWS (AES-256-GCM) produira des valeurs chiffrées différentes. Le hachage est une fonction à sens unique dans laquelle le texte en clair est brouillé de manière à ne pas pouvoir être déchiffré. Le hachage produit la même valeur à chaque fois. Cela nous permet de maintenir les états d'abonnement pour plusieurs utilisateurs partageant la même adresse e-mail.

### Quelle adresse e-mail dois-je utiliser pour mon envoi de test ? {#what-email-address-should-i-use-in-my-test-send}

Les adresses e-mail en clair sont prises en charge dans le cadre de l'envoi de tests. Pour voir à quoi ressemble un e-mail pour un utilisateur spécifique, procédez comme suit :

1. Sélectionnez **Preview message as a user**.
2. Dans **Test Send**, sélectionnez **Override recipients attributes with current preview user's attributes**.

{%raw%}
### Que se passe-t-il si j'ajoute cette adresse e-mail Liquid `{{${email_address}}}` dans Braze ? {#what-happens-if-i-add-this-email-address-liquid-emailaddress-in-braze}

Braze affiche l'adresse e-mail en clair lors de l'envoi de l'e-mail. Dans les prévisualisations, la version chiffrée de l'adresse e-mail est affichée. Nous vous recommandons d'utiliser l'ID externe de l'utilisateur si vous faites référence à un utilisateur dans une URL personnalisée en un clic.

`{{${email_address}}}` n'est actuellement pas pris en charge dans le centre de préférences et les pages de désabonnement.
{%endraw%}

### Quelle adresse e-mail dois-je m'attendre à voir dans Currents ? {#what-email-address-should-i-expect-to-see-in-currents}

L'adresse e-mail hachée est incluse dans les événements de distribution et d'engagement des e-mails.

### Quelle adresse e-mail dois-je m'attendre à voir dans l'archivage des messages ? {#what-email-address-should-i-expect-to-see-in-message-archiving}

L'adresse e-mail en clair est incluse dans l'archivage des messages. Ceux-ci sont envoyés directement au fournisseur de stockage cloud du client et d'autres données personnelles peuvent être incluses dans le corps des e-mails.

### Puis-je utiliser mail-to list-unsubscribe pour la gestion des abonnements avec le chiffrement au niveau du champ de l'identifiant ? {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

Non. L'utilisation de mail-to list-unsubscribe enverrait l'adresse e-mail déchiffrée en clair à Braze. Lorsque le chiffrement au niveau du champ de l'identifiant est activé, nous prenons en charge la méthode HTTP basée sur l'URL, y compris le clic unique. Nous vous recommandons également d'inclure un lien de désabonnement en un clic dans le corps de votre e-mail.

### Le chiffrement au niveau du champ de l'identifiant prend-il en charge d'autres identifiants tels que le téléphone ? {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

Non. Actuellement, le chiffrement au niveau du champ de l'identifiant n'est pris en charge que pour les adresses e-mail.