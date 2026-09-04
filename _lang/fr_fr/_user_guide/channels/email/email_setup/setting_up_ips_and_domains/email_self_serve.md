---
nav_title: E-mail en libre-service
article_title: E-mail en libre-service
page_order: 0
page_type: tutorial
channel: email
description: "Cet article pratique explique comment configurer les domaines d'envoi et de suivi avec la configuration e-mail en libre-service dans Braze."
toc_headers: h2
---

# E-mail en libre-service {#email-self-serve}

> Cette page explique comment configurer les domaines d'envoi et de suivi dans Braze afin que votre domaine d'expéditeur et vos liens de suivi partagent le même sous-domaine.

## Prérequis {#prerequisites}

Pour utiliser la configuration e-mail en libre-service, vous devez remplir les prérequis suivants :

- Être un nouveau client en phase d'onboarding
- Disposer de la permission au niveau de l'entreprise « Edit Domain Settings »
- Disposer d'un pool d'IP, d'adresses IP et d'un domaine vérifié

## Considérations {#considerations}

- Prévoyez un sous-domaine d'envoi d'au moins trois niveaux. Étant donné que Braze crée un sous-domaine sous votre domaine délégué (tel que « marketing.example.com »), votre domaine d'envoi doit comporter au moins trois niveaux (tel que « e.marketing.example.com »).
- Le domaine d'envoi doit être subordonné à un domaine que vous possédez. Par exemple, si vous possédez « example.com », un sous-domaine pourrait être « mail.example.com », ce qui vous permet d'utiliser l'adresse d'envoi « @mail.example.com ».
- Des limites de domaines s'appliquent. Le nombre total de domaines de suivi est limité à 2 multiplié par le nombre de domaines vérifiés dans votre contrat. Si vous en avez besoin de davantage, contactez votre gestionnaire de compte.

## Configuration {#setup}

### Étape 1 : Ajouter un domaine d'envoi {#step-1-add-a-sending-domain}

Votre sous-domaine d'envoi est l'adresse à partir de laquelle vos e-mails sont envoyés. Il détermine l'adresse « de » que vos destinataires voient.

1. Dans la section **Domains**, sélectionnez **Add domain**.
2. Ajoutez votre domaine d'envoi dans les champs **Mail from** et **Sending domain** pour le pool d'adresses IP.
    - L'adresse **Mail from** (expéditeur d'enveloppe ou chemin de retour) est celle qui gère les rebonds en coulisses. Vos destinataires ne la voient pas dans un e-mail. Par exemple, vous pourriez utiliser « bounce » comme sous-domaine, de sorte que l'adresse mail from personnalisée soit « bounce.mail.example.com ». L'utilisation de ce sous-domaine est une bonne pratique pour l'alignement DMARC SPF.
    - Le **Sending domain** est le domaine dans l'adresse De que les destinataires voient dans leur boîte de réception. Par exemple, si l'adresse De est « hello@e.mail.example.com », alors « e.mail.example.com » est le domaine d'envoi.
{: start="3"}
3. Sélectionnez votre domaine vérifié dans le menu déroulant.

Les domaines d'envoi ne peuvent pas être modifiés une fois soumis. Braze crée des enregistrements DNS pour la vérification et l'authentification, et les ajoute à vos paramètres DNS. Si vous devez supprimer un domaine d'envoi, contactez le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) pour obtenir de l'aide.

### Étape 2 : Ajouter un domaine de suivi {#step-2-add-a-tracking-domain}

Un domaine de suivi est utilisé pour encapsuler les liens dans vos e-mails à des fins de suivi des clics et de branding. Les destinataires le voient lorsqu'ils survolent ou cliquent sur les liens dans vos e-mails. Il doit être un sous-domaine de votre domaine d'envoi ou vérifié pour une délégation DNS correcte.

1. Sélectionnez si vous utilisez un **Verified domain** ou un **Sending domain** comme sous-domaine pour votre domaine de suivi :
    - Si vous souhaitez que l'URL de suivi corresponde au domaine d'envoi pour la cohérence de marque, sélectionnez **Sending domain**.
    - Si vous souhaitez une URL de suivi plus courte, sélectionnez le **Verified domain**.

{: start="2"}
2. Saisissez votre sous-domaine de suivi. Celui-ci est ajouté devant le sous-domaine sélectionné précédemment.

L'exemple suivant montre comment le domaine de suivi s'affiche dans l'e-mail en fonction de votre sélection :

|  | Sélection | Domaine de suivi |
| --- | --- | ---|
| Domaine vérifié | mail.example.com | links.mail.example.com |
| Domaine d'envoi | marketing.mail.example.com | links.marketing.mail.example.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Domaine de suivi par sélection" }

{: start="3"}
3. Sélectionnez le sous-domaine vérifié ou d'envoi associé à utiliser dans le menu déroulant.
4. Sélectionnez **Submit**. Vous pouvez voir les domaines d'envoi et de suivi avec un statut **Pending**.

La propagation des enregistrements DNS pour les domaines d'envoi peut prendre de 5 à 10 minutes. Lorsque votre domaine est prêt à être utilisé, vous recevez un e-mail de notification. Les enregistrements DNS pour les domaines de suivi peuvent prendre jusqu'à 24 heures pour se propager, bien que cela prenne généralement moins de temps. Il est possible que le sous-domaine d'envoi devienne prêt avant le domaine de suivi.

### Étape 3 : Sélectionner les espaces de travail {#step-3-select-workspaces}

Sélectionnez les espaces de travail qui doivent avoir accès au domaine, puis sélectionnez **Confirm**. Vous pouvez également choisir d'ajouter automatiquement le domaine d'envoi aux nouveaux espaces de travail lors de leur création.

### Étape 4 : Configurer les liens universels (facultatif) {#step-4-set-up-universal-links-optional}

Les liens universels permettent aux liens de vos messages de s'ouvrir directement dans votre application mobile au lieu d'un navigateur mobile. Braze peut héberger les fichiers d'association sur vos domaines de suivi en votre nom.

{% alert note %}
Les liens universels sont appliqués par domaine de suivi. Le même contenu de fichier peut être partagé entre les domaines, mais chaque domaine héberge sa propre copie.
{% endalert %}

1. Accédez à **Settings** > **Company Settings** > **Verified Domains** > **Universal Links**.
2. Sélectionnez **Set up universal links**.
3. Saisissez un nom d'ensemble de liens universels.
4. Activez la configuration iOS et ajoutez votre fichier AASA. JSON est le seul type de fichier accepté. Braze lit le fichier et affiche le nombre d'identifiants d'application et de composants trouvés, ainsi qu'un aperçu du fichier généré.
5. Activez la configuration Android et ajoutez votre fichier Digital Asset Links de la même manière. Braze affiche les noms de packages, l'empreinte du certificat SHA-256 et le nombre de déclarations, ainsi qu'un aperçu.
6. Vérifiez chaque aperçu pour confirmer que le contenu semble correct, puis sélectionnez **Next: Select tracking domains**. Seuls les domaines de suivi vérifiés apparaissent. Un ensemble peut s'appliquer à plusieurs domaines de suivi.
7. Votre ensemble apparaît sur la page Universal Links avec ses domaines de suivi, ses canaux, le statut iOS, le statut Android et la date de création. Braze vérifie que le fichier AASA est correctement hébergé pour chaque domaine et rapporte le résultat dans la colonne de statut.

### Étape 5 : Tester l'envoi de vos e-mails {#step-5-test-your-email-sending}

Une fois que les domaines d'envoi et de suivi affichent un statut **Ready for use**, testez votre configuration :

1. Dans votre espace de travail, accédez à **Settings** > **Email Settings**.
2. Vérifiez que le nouveau domaine d'envoi est répertorié dans la section **Display Name Address**.
3. Ajoutez une adresse De utilisant le nouveau domaine (par exemple, « hello@e.mail.example.com »).
4. Sélectionnez **Save**.
5. Créez une Campaign d'e-mail de test et envoyez-la à vous-même. Ensuite, confirmez que :
    - Votre e-mail a été livré avec succès.
    - L'adresse De est correcte.
    - Les liens de suivi des clics utilisent le domaine de suivi.
    - Les liens universels ouvrent l'application ou le site web comme prévu en fonction de l'appareil du destinataire.
    - Les en-têtes d'e-mail s'affichent correctement.

## Étapes suivantes {#next-steps}

Une fois la vérification de votre expéditeur terminée, Braze recommande l'[IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) afin que vos messages atteignent leurs boîtes de réception de destination à un taux élevé et constant.

Après avoir terminé cette configuration, consultez l'équipe d'onboarding de Braze pour confirmer que vos domaines et votre IP warming fonctionnent correctement.

## Résolution des problèmes {#troubleshooting}

### La propagation DNS prend plus de temps que prévu {#dns-propagation-is-taking-longer-than-expected}

Les enregistrements de domaine d'envoi se propagent généralement en 5 à 10 minutes. Les enregistrements de domaine de suivi peuvent prendre jusqu'à 24 heures selon les paramètres de TTL de votre fournisseur DNS. Si la propagation prend plus de temps, vérifiez d'abord que les enregistrements NS ont été ajoutés correctement, puis contactez le support Braze.

### Je ne parviens pas à supprimer un domaine vérifié {#im-not-able-to-remove-a-verified-domain}

Les domaines vérifiés ne peuvent pas être supprimés directement dans le tableau de bord, car cela pourrait potentiellement interrompre vos envois si la modification n'est pas correctement vérifiée. Contactez le support Braze pour vous aider à supprimer le domaine de votre compte.

### Mes liens universels n'ouvrent pas l'application {#my-universal-links-arent-opening-the-app}

Vérifiez d'abord les statuts iOS et Android sur la page des liens universels. Si un domaine n'héberge pas un fichier valide, ouvrez l'ensemble, corrigez la configuration et enregistrez à nouveau. Si les statuts semblent corrects, assurez-vous de tester à partir d'un lien dans un e-mail sur un appareil réel plutôt que de coller l'URL dans la barre d'adresse du navigateur.

## Questions fréquentes {#frequently-asked-questions}

### Braze peut-il gérer mon certificat SSL sans délégation NS ? {#can-braze-manage-my-ssl-certificate-without-ns-delegation}

Verified Domains nécessite des enregistrements NS (Name Server) pour la délégation de propriété DNS à Braze. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="Braze-hosted SSL certificates without NS delegation" %}

### Puis-je déléguer un domaine racine à la place ? {#can-i-delegate-a-root-domain-instead}

Verified Domains est principalement conçu et recommandé pour une utilisation avec des sous-domaines. Nous ne recommandons pas de déléguer le domaine parent principal de votre marque pour des raisons de sécurité, car vous perdez la visibilité et le contrôle sur celui-ci. Si vous souhaitez déléguer un domaine parent, utilisez un domaine parent qui n'est utilisé nulle part ailleurs que dans Braze.

### Pourquoi mon domaine vérifié ne peut-il pas également être le domaine d'envoi ? {#why-cant-my-verified-domain-also-be-the-sending-domain}

Braze ne peut créer qu'un sous-domaine d'envoi sous votre domaine vérifié, qui est généralement un sous-domaine du domaine parent (`mail.example.com`). Par conséquent, la profondeur minimale du domaine d'envoi dans ce cas est de trois niveaux (`e.mail.example.com`), au lieu des deux niveaux habituels.

### Que se passe-t-il si je modifie l'un de mes enregistrements NS après la configuration ? {#what-happens-if-i-modify-any-of-my-ns-records-after-setup}

Les domaines vérifiés dépendent entièrement de l'intégrité des enregistrements NS. Si vous apportez des modifications à l'un de vos enregistrements NS, cela peut interrompre l'envoi et le suivi de vos e-mails.

### Puis-je n'ajouter qu'une seule des quatre lignes d'enregistrement NS, puisque ma commande dig affiche les quatre enregistrements ? {#can-i-add-only-one-of-four-ns-record-lines-since-my-dig-command-shows-all-four-records}

Confirmez que les quatre enregistrements NS sont explicitement présents à l'aide de la commande `dig` et que le domaine est validé dans le tableau de bord avant de considérer la configuration comme terminée.