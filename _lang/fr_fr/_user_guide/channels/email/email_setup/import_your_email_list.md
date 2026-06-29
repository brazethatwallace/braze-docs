---
nav_title: Importez votre liste d'e-mails
article_title: Importez votre liste d'e-mails dans Braze
page_order: 4
page_type: reference
description: "Cet article de référence présente les bonnes pratiques pour importer votre liste d'e-mails dans Braze."
channel: email

---

# Importez votre liste d'e-mails dans Braze {#importing-email-lists}

> Une étape importante pour vous positionner comme un expéditeur d'e-mails performant consiste à vous assurer que vous disposez d'une liste d'e-mails de haute qualité. Une bonne gestion de votre liste d'e-mails peut améliorer votre livrabilité et vous fournir des résultats de campagne plus précis et fiables.

## Points à considérer avant l'importation {#considerations-before-importing}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Validez vos listes d'e-mails {#validate-your-email-lists}

Avant d'importer votre liste d'e-mails dans Braze, vérifiez que votre liste ne contient que des adresses e-mail authentiques. Un taux de rebond élevé peut nuire à votre réputation d'expéditeur d'e-mails.

Des services de nettoyage de listes d'e-mails peuvent effectuer cette vérification pour vous en déterminant si l'adresse e-mail respecte la syntaxe correcte et possède les propriétés physiques d'une adresse e-mail, en vérifiant le domaine de messagerie et en se connectant au serveur de messagerie pour authentifier l'existence de l'adresse e-mail.

### Vérifiez si une adresse e-mail est déjà associée à un utilisateur {#check-if-an-email-address-is-already-associated-with-a-user}

Avant de créer un utilisateur via l'API ou le SDK, appelez l'endpoint [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) et spécifiez l'`email_address` de l'utilisateur. Si un profil utilisateur est renvoyé, cet utilisateur Braze est déjà associé à cette adresse e-mail.

Nous vous recommandons vivement de rechercher des adresses e-mail uniques lors de la création de nouveaux utilisateurs et d'éviter de transmettre ou d'importer des utilisateurs ayant la même adresse e-mail. Dans le cas contraire, vous pourriez rencontrer des conséquences imprévues affectant l'envoi de messages, le ciblage, le reporting et d'autres fonctionnalités.

Par exemple, supposons que vous ayez des profils en double, mais que certains attributs personnalisés ou événements ne résident que sur un seul profil. Lorsque vous essayez de déclencher des Campaigns ou des Canvas avec plusieurs critères, Braze ne peut pas identifier l'utilisateur comme éligible car il existe deux profils utilisateur. Ou encore, si une Campaign cible une adresse e-mail partagée par deux utilisateurs, la page **Rechercher des utilisateurs** affichera les deux profils utilisateur comme ayant reçu la Campaign.

### Identifiez vos utilisateurs engagés {#identify-your-engaged-users}

Afin d'identifier vos utilisateurs les plus engagés, commencez par supprimer les utilisateurs inactifs depuis longtemps. Il est recommandé de ne pas envoyer d'e-mails aux utilisateurs qui n'ont pas interagi avec un e-mail depuis plus de six mois, car cela peut nuire à votre réputation d'expéditeur d'e-mails. Lors de l'importation de votre liste d'e-mails, veillez à n'inclure que les utilisateurs ayant ouvert un e-mail de votre part au cours des six derniers mois.

À long terme, vous devriez également envisager de mettre en place une [politique de temporisation]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies).

### Évitez les listes de suppression {#avoid-suppression-lists}

Si vous effectuez une transition depuis un fournisseur d'e-mails existant, assurez-vous de ne pas importer d'utilisateurs provenant d'une liste de suppression. Les listes de suppression contiennent des adresses e-mail dont les propriétaires se sont désabonnés, ont signalé vos e-mails comme spam ou ont subi un échec d'envoi définitif.

## Méthodes d'importation {#methods-for-importing}

Une fois votre liste d'e-mails préparée, il existe plusieurs façons d'importer des utilisateurs dans Braze, par exemple via la REST API de Braze ou des fichiers CSV. Pour en savoir plus, consultez notre article dédié à l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).