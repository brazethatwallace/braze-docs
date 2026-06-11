---
nav_title: "Vérification de l'expéditeur"
article_title: "Vérification de l'expéditeur"
permalink: /sender_verification/
description: "Cet article explique comment configurer la vérification de l'expéditeur et déléguer vos propres sous-domaines à Braze."
hidden: true
---

# Vérification de l'expéditeur {#sender-verification}

> Cette page explique comment déléguer vos propres sous-domaines à Braze. Utilisez la vérification de l'expéditeur pour configurer et déléguer le contrôle d'un sous-domaine d'envoi dédié à Braze, ce qui permet une meilleure cohérence de marque avec votre domaine d'expédition (From) et vos liens de suivi hébergés sous le même sous-domaine.

{% alert important %}
Cette fonctionnalité est en version bêta et n'est disponible que pour les équipes internes de Braze.
{% endalert %}

## Fonctionnement de la vérification de l'expéditeur {#how-sender-verification-works}

La délégation de domaine est une option de configuration DNS qui vous permet de déléguer le contrôle d'un sous-domaine d'envoi spécifique à Braze. Par exemple, si vous utilisez « marketing.example.com » comme sous-domaine, Braze gère les enregistrements DNS nécessaires aux fonctionnalités d'envoi de messages, comme l'e-mail.

### Avantages {#benefits}

La vérification de l'expéditeur simplifie la configuration et la maintenance. Braze crée et met à jour ce qui est nécessaire, ce qui réduit les risques d'erreur de configuration DNS.

### Points à considérer {#considerations}

- Choisissez un sous-domaine dédié.
- Une fois la délégation de domaine terminée, Braze gère vos enregistrements DNS pour le sous-domaine délégué.
- Si vous avez plusieurs marques ou espaces de travail Braze, vous pouvez sélectionner un sous-domaine délégué par marque.
- La vérification de l'expéditeur est limitée à 50 domaines d'envoi et 50 domaines de suivi. Si vous devez en ajouter davantage, veuillez contacter l'équipe d'assistance Braze.

## Étape 1 : Remplir les conditions préalables {#step-1-complete-prerequisites}

Dans le tableau de bord de Braze, accédez à **Paramètres** > **Vérification de l'expéditeur** sous **Paramètres de l'entreprise** et travaillez avec votre gestionnaire d'onboarding pour remplir les conditions préalables suivantes :

- Ajouter un pool d'adresses IP
- Ajouter des adresses IP
- Ajouter un domaine délégué et vérifier l'enregistrement NS

## Étape 2 : Ajouter votre sous-domaine d'envoi {#step-2-add-your-sending-subdomain}

1. Dans la section **Domaines d'envoi**, sélectionnez **Ajouter un domaine d'envoi**.
2. Renseignez les champs **Mail from** et **Domaine d'envoi** avec votre sous-domaine d'envoi pour le pool d'adresses IP. Par exemple : « marketing.mail.example.com ».
3. Sélectionnez votre domaine délégué dans le menu déroulant.
4. Ensuite, sélectionnez **Envoyer**.

![Formulaire affichant les champs pour l'adresse Mail from et le domaine d'envoi, avec un menu déroulant pour le domaine délégué et un bouton Envoyer.]({% image_buster /assets/unlisted_docs/img/sender_verification/sending_subdomain.png %}){: style="max-width:85%;"}

La propagation des enregistrements DNS prend de 5 à 10 minutes. Une fois terminée, vous recevrez un e-mail de notification indiquant que votre domaine est prêt à être utilisé.

{% alert important %}
Les domaines ne peuvent pas être modifiés après leur envoi. Braze crée des enregistrements DNS pour la vérification et l'authentification, puis les ajoute à vos paramètres DNS.
{% endalert %}

## Étape 3 : Ajouter votre sous-domaine de suivi {#step-3-add-your-tracking-subdomain}

Après avoir créé un sous-domaine et l'avoir fait vérifier :

1. Sélectionnez **Ajouter un domaine de suivi**.
2. Saisissez le sous-domaine de suivi. Par exemple, si votre sous-domaine de suivi est « click », votre sous-domaine serait : « click.marketing.mail.example.com ».
3. Sélectionnez le domaine d'envoi associé dans le menu déroulant.
4. Ensuite, sélectionnez **Envoyer**.

![Exemple de domaine de suivi à ajouter.]({% image_buster /assets/unlisted_docs/img/sender_verification/tracking_domain.png %}){: style="max-width:85%;"}

La propagation de ces enregistrements DNS peut prendre jusqu'à 24 heures, mais elle est généralement plus rapide. Une fois terminée, vous recevrez un e-mail de notification indiquant que votre domaine est prêt à être utilisé.

{% alert important %}
Le domaine de suivi doit être un sous-domaine du domaine d'envoi pour que la délégation DNS fonctionne correctement.
{% endalert %}

## Étape 4 : Sélectionner les espaces de travail {#step-4-select-the-workspaces}

Ensuite, sélectionnez les espaces de travail qui doivent avoir accès au domaine, puis sélectionnez **Confirmer**. Vous pouvez éventuellement ajouter automatiquement un domaine d'envoi aux nouveaux espaces de travail lors de leur création.

![Boîte de dialogue affichant des cases à cocher pour la sélection des espaces de travail, avec une option pour ajouter automatiquement le domaine d'envoi aux nouveaux espaces de travail et un bouton Confirmer.]({% image_buster /assets/unlisted_docs/img/sender_verification/select_workspaces_domain.png %}){: style="max-width:85%;"}

## Étape 5 : Tester l'envoi d'e-mails {#step-5-test-your-email-sending}

Lorsque les domaines d'envoi et de suivi affichent l'état **Prêt à l'emploi**, vous pouvez tester l'envoi d'e-mails en procédant comme suit :

1. Dans votre espace de travail, accédez à **Paramètres** > **Paramètres des e-mails**.
2. Vérifiez que le nouveau domaine d'envoi apparaît dans la section **Adresse du nom d'affichage**.
3. Ajoutez l'adresse e-mail utilisant le nouveau domaine (par exemple « marketing@marketing.mail.example.com »).
4. Sélectionnez **Enregistrer**.
5. Ensuite, créez une campagne de test et envoyez-vous un e-mail pour vérifier les points suivants :
- Votre e-mail a été livré avec succès.
- L'adresse d'expédition (From) est correcte.
- Le lien de suivi des clics utilise le domaine de suivi.
- Les en-têtes de votre e-mail s'affichent correctement.