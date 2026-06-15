---
nav_title: Wyng
article_title: Wyng
description: "Cet article de référence présente le partenariat entre Braze et Wyng, une plateforme de données zero-party utilisée pour collecter, utiliser et intégrer les préférences et attributs des clients via des micro-expériences, des portails de préférences clients et une plateforme API."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng](https://wyng.com/) fournit des outils pour créer des expériences numériques interactives (quiz, centres de préférences, promotions) qui engagent les consommateurs à des moments clés, collectent des préférences et d'autres données zero-party, et personnalisent en temps réel.

_Cette intégration est maintenue par Wyng._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et Wyng vous permet d'exploiter les données zero-party issues des expériences Wyng pour personnaliser les interactions dans les Campaigns et Canvas Braze. Wyng peut également alimenter un centre de préférences, afin que les consommateurs puissent contrôler les données et les préférences (y compris les préférences de communication) qu'ils partagent avec votre marque.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Wyng | Un compte Wyng est nécessaire pour bénéficier de ce partenariat. |
| Clé REST API Braze | Une clé REST API Braze avec les autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Connecter l'intégration Braze {#step-1-connect-the-braze-integration}

Dans Wyng, accédez à [**Integrations**](https://wyng.com/dashboard/integrations/) et sélectionnez l'onglet **Add**. Ensuite, survolez **Braze** et cliquez sur **Connect** pour l'intégration.

![La tuile partenaire Braze dans la plateforme Wyng.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### Étape 2 : Configurer le connecteur Braze {#step-2-configure-the-braze-connector}

1. Dans la fenêtre de configuration qui s'ouvre, indiquez votre clé REST API Braze.
![Une image montrant l'invite de saisie des identifiants.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. Ensuite, utilisez le menu déroulant pour sélectionner la campagne Wyng que vous souhaitez partager avec Braze.![Une image du connecteur Braze vous invitant à sélectionner une campagne Wyng existante que vous souhaitez partager avec Braze.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. Ensuite, vous devez configurer les abonnements, les objets d'attributs et d'événements, ainsi que les événements personnalisés.<br><br>
- **Configuration des abonnements (obligatoire)**<br>
Pour abonner des utilisateurs à des groupes d'abonnement, cliquez sur **Add Subscription** et ajoutez le nom et l'ID de votre groupe d'abonnement. Pour ajouter plusieurs noms et ID de groupes, cliquez à nouveau sur le bouton **Add Subscription**.<br>![Une image vous invitant à indiquer le nom et l'ID d'un groupe d'abonnement.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **Configuration du suivi des utilisateurs**<br>
Cliquez sur **Add custom property** pour ajouter des paires d'objets d'attributs et d'événements à envoyer à l'endpoint `/users/track`. Utilisez cette option pour ajouter des valeurs d'attribut codées en dur pour chaque transaction de données envoyée pour l'intégration. Pour ajouter plusieurs propriétés, cliquez à nouveau sur le bouton **Add custom property**.<br>![Une image vous invitant à ajouter des propriétés personnalisées d'attributs.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **Envoyer un événement personnalisé**<br>
Vous pouvez éventuellement activer l'option **Sending custom event**. Si elle est activée, vous devez inclure le nom de l'événement et l'ID de l'application correspondante.<br>![Une image vous invitant à envoyer des événements personnalisés, le cas échéant.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. Enfin, vous devez mapper les champs Wyng aux champs de l'API Braze en fonction de votre cas d'utilisation. Cliquez sur **Select a field** pour choisir les champs à mapper, puis cliquez sur **Save** pour enregistrer votre intégration. Une fois enregistrés, ces champs mappés se trouvent sous **Integrations > Manage**.
![Un exemple des différents champs Wyng que vous pouvez mapper à certains champs Braze.]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![Une liste des champs de synchronisation disponibles.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### Étape 3 : Tester votre intégration {#step-3-test-your-integration}

Dans Wyng, testez la soumission du formulaire dans votre campagne Wyng. Vous pouvez également le soumettre dans la campagne de prévisualisation si vous ne souhaitez pas ajouter un enregistrement à la campagne de production principale. Vous devriez voir une transaction réussie dans le tableau de bord **Integration**.

## Utiliser cette intégration {#using-this-integration}

Une fois le connecteur de données en place, tous les champs créés dans Wyng et ajoutés à Braze peuvent être utilisés comme n'importe quel autre champ de données pour déclencher des Campaigns, segmenter des audiences ou alimenter des contenus personnalisés.

Les applications sont vastes et les questions spécifiques peuvent être adressées à [contact@wyng.com](mailto:contact@wyng.com) ou à votre gestionnaire de compte.

## Résolution des problèmes {#troubleshooting}

### Échec de la soumission {#failed-submission}

En cas d'échec de l'envoi des données à Braze, cliquez sur le lien **View Log** pour consulter la soumission échouée et le message d'erreur associé.

![Le lien « View Log » situé sous l'en-tête des actions.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

La page du journal affiche la soumission échouée, le nombre de tentatives, les données de la soumission, l'erreur et un lien pour renvoyer la soumission.

![Un exemple de ce qu'affiche une soumission échouée.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

La section **View Error** affiche le code d'erreur et quelques informations supplémentaires sur la cause de l'erreur. Vous pouvez ensuite comparer le code d'erreur avec Braze pour en déterminer la cause.

![Un exemple de journal d'erreurs affiché dans la plateforme Wyng.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

Si vous avez d'autres questions, contactez le service d'assistance de Wyng ([support@wyng.com](mailto:contact@wyng.com)) pour obtenir de l'aide.