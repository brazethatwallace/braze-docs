---
nav_title: Groupes internes
article_title: Groupes internes
page_order: 4
page_type: reference
description: "Cet article de référence décrit les groupes internes, un excellent moyen d'obtenir des informations sur les journaux SDK ou API de votre appareil de test lors du test de l'intégration SDK."

---

# Groupes internes {#internal-groups}

> Les groupes internes sont un excellent moyen de créer et d'organiser des groupes de test internes ou tiers. Ils fournissent des informations sur vos journaux SDK ou API et sont utiles lors du test de votre intégration SDK. Vous pouvez créer un nombre illimité de groupes internes personnalisés pouvant contenir jusqu'à 1 000 utilisateurs.

{% alert tip %}
Nous vous recommandons également de consulter notre cours d'apprentissage Braze [Tests et résolution des problèmes](https://learning.braze.com/path/developer/testing-and-troubleshooting), qui explique comment utiliser les groupes internes pour effectuer vos propres opérations de résolution des problèmes et de débogage.
{% endalert %}

## Prérequis {#prerequisites}

Pour créer et gérer des groupes internes, vous avez besoin des [autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) suivantes :

- View API Keys
- Edit API Keys
- View Internal Groups
- Edit Internal Groups
- View Message Activity Log
- View Event User Log
- View API identifiers
- View API Usage Dashboard
- View API Limits
- View API Usage Alerts
- Edit API Usage Alerts
- Edit SDK Debugger
- View SDK Debugger

## Créer un groupe interne {#creating-an-internal-group}

Pour créer un groupe interne :

1. Accédez à **Paramètres** > **Groupes internes**.
2. Sélectionnez **Créer un groupe interne**.
3. Donnez un nom à votre groupe, par exemple « Groupe de test e-mail ».
4. Choisissez un ou plusieurs types de groupes, comme indiqué dans le tableau suivant.

| Type de groupe         | Description                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Groupe d'événements utilisateurs**   | Utilisez-le pour vérifier les événements ou les journaux depuis votre appareil de test.<br><br>Pour capturer les journaux du SDK et de la REST API pour les membres du groupe, cochez la case **Événements utilisateurs**. Sans ce paramètre, les utilisateurs ajoutés au groupe n'afficheront pas de journaux dans le [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log). |
| **Groupe de test de contenu** | Utilisez-le pour les notifications push, les e-mails et les messages in-app afin d'envoyer une copie rendue du message. |
| **Groupe initiateur**         | Envoie automatiquement une copie de l'e-mail à tous les membres du groupe initiateur lors de l'envoi.               |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Créer un groupe interne" }

{:start="5"}
5. Sélectionnez à nouveau **Créer un groupe interne**.

### Ajouter des utilisateurs test {#adding-test-users}

Après avoir créé votre groupe interne, ajoutez des utilisateurs test en tant que membres de ce groupe.

1. Depuis la page de gestion de votre groupe interne, sélectionnez **Ajouter des utilisateurs test**.
2. Choisissez parmi les méthodes suivantes pour rechercher et sélectionner vos utilisateurs test.

| Méthode                  | Description                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ajouter un utilisateur identifié** | Recherchez l'utilisateur par son ID externe, son adresse e-mail, son numéro de téléphone ou son jeton push.                                                                                                                                                           |
| **Ajouter un utilisateur anonyme**  | Recherchez par adresse IP. Ensuite, attribuez un nom à chaque utilisateur test que vous ajoutez. Ce nom est celui auquel tous les journaux d'événements sont associés sur la page du [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log). |
| **Ajouter des utilisateurs en masse**      | Copiez et collez une liste d'adresses e-mail ou d'ID externes. Vous ne pouvez ajouter que des utilisateurs déjà connus dans le tableau de bord. Pour plus d'informations, consultez [Importation d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ajouter des utilisateurs test" }

### Groupes de test de contenu {#content-test-groups}

Tout comme l'envoi d'un aperçu test d'un message, le groupe de test de contenu vous fait gagner du temps et vous permet de lancer des tests vers une liste prédéfinie d'utilisateurs Braze simultanément. Cette fonctionnalité est disponible pour les notifications push, les messages in-app, les SMS, les e-mails et les Content Cards dans Braze. Seuls les groupes étiquetés comme groupes de test de contenu sont disponibles dans la section d'aperçu d'un message.

{% alert note %}
Les messages test [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) ne peuvent être envoyés qu'à des numéros de téléphone valides présents dans la base de données.
{% endalert %}

Sélectionnez des utilisateurs Braze individuels ou un nombre quelconque de groupes internes auxquels envoyer le message. Si votre message contient du Liquid ou toute autre personnalisation dynamique, Braze utilise les attributs disponibles pour chaque utilisateur afin de personnaliser le contenu du message. Pour les utilisateurs qui n'ont pas d'attributs, Braze utilise la valeur par défaut définie.

De plus, si vous prévisualisez le message en tant qu'utilisateur aléatoire, utilisateur personnalisé ou utilisateur existant, vous pouvez envoyer cette version prévisualisée à la place. Décocher la case vous permet d'envoyer en fonction des attributs de chaque utilisateur plutôt que de la version prévisualisée.

Si vous utilisez un pool d'IP pour envoyer un e-mail, sélectionnez le pool d'IP à partir duquel envoyer l'e-mail en le choisissant dans le menu déroulant disponible.

![La section Test de l'éditeur de messages in-app pour sélectionner le groupe de test de contenu.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Groupes initiateurs {#seed-groups}

Les groupes initiateurs ne sont pris en charge que pour le canal e-mail. Ajoutez des utilisateurs à un groupe initiateur pour envoyer des copies de chaque variante d'e-mail à tous les membres du groupe.

Les groupes initiateurs ne sont pas disponibles pour les Campaigns via API, mais vous pouvez inclure des groupes initiateurs en utilisant une entrée déclenchée par API dans la Campaign. Utilisez cette fonctionnalité pour mesurer les indicateurs de livrabilité et pour conserver un historique du contenu de vos e-mails à des fins d'archivage.

Après avoir créé un groupe interne et l'avoir étiqueté pour être utilisé comme groupe initiateur, sélectionnez-le à l'étape **Audiences cibles** de l'éditeur de Campaign, ou à l'étape **Paramètres d'envoi** dans un Canvas.

Les e-mails initiateurs sont précédés de `[SEED]` dans la ligne d'objet. Notez que les e-mails initiateurs **ne font pas** ce qui suit :

- Incrémenter les envois dans l'analyse du tableau de bord.
- Impacter l'analyse des e-mails ou le reciblage.
- Mettre à jour la liste **Campaigns reçues** du profil utilisateur.
- Impacter la limite de fréquence.
- Prendre en compte ou impacter les limites de débit de vitesse de distribution.

#### Comportement d'abonnement {#subscription-behavior}

Les envois initiateurs sont conçus pour l'assurance qualité interne et la révision. Ils contournent donc intentionnellement les vérifications d'abonnement pour les utilisateurs de l'entreprise inclus dans le groupe initiateur. Cela signifie que les utilisateurs disposant d'adresses e-mail valides et faisant partie d'un groupe initiateur reçoivent le message même s'ils ne sont pas abonnés. Cependant, le message doit être configuré pour envoyer des copies initiateurs à ce groupe.

{% alert tip %}
Si les membres du groupe initiateur ne voient pas le message, confirmez qu'ils font bien partie du groupe interne, utilisez des lignes d'objet distinctes pour que Gmail ne regroupe pas les messages, et demandez-leur de vérifier les courriers indésirables.

Si l'e-mail utilise le [Liquid `abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), les membres du groupe initiateur doivent tout de même satisfaire la condition d'abandon pour recevoir l'envoi.
{% endalert %}

#### Pour les Campaigns {#for-campaigns}

Lors de la composition d'une Campaign par e-mail, modifiez vos groupes initiateurs dans la section **Audiences cibles** de l'éditeur.

{% alert important %}
Si vous configurez un groupe initiateur pour qu'il s'attache automatiquement à toutes les Campaigns, cela ne s'applique qu'aux nouvelles Campaigns. Cela ne s'applique pas lorsque vous copiez des Campaigns existantes. Vous devez appliquer manuellement les groupes initiateurs souhaités à la Campaign copiée dans la section **Audiences cibles**.
{% endalert %}

Les groupes initiateurs envoient à chaque variante d'e-mail une seule fois et sont distribués la première fois que votre utilisateur reçoit cette variante particulière. Pour les messages planifiés, il s'agit généralement du premier lancement de la Campaign. Pour les Campaigns déclenchées par une action ou par API, il s'agit du moment où le premier utilisateur reçoit un message.

Si votre Campaign est multivariée et que votre variante a un pourcentage d'envoi de 0 %, elle n'est pas envoyée aux groupes initiateurs. De plus, si la variante a déjà été envoyée et n'a pas été mise à jour pour un renvoi dans **Modifier les groupes initiateurs** à l'étape **Cible**, elle n'est pas renvoyée par défaut.

{% alert note %}
Si vous avez une Campaign récurrente et que l'une des variantes est mise à jour, vous pouvez choisir de renvoyer uniquement aux variantes mises à jour ou à toutes les variantes, ou de désactiver l'envoi du groupe initiateur lors de la mise à jour.
{% endalert %}

![Le groupe initiateur « Email seed test » sélectionné pour recevoir la Campaign par e-mail de la variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Pour Canvas {#for-canvas}

Les groupes initiateurs dans Canvas fonctionnent de manière similaire à toute Campaign déclenchée. Braze détecte automatiquement toutes les étapes contenant un message e-mail et les envoie lorsque votre utilisateur atteint pour la première fois cette étape e-mail particulière.

Si une étape e-mail a été mise à jour après l'envoi au groupe initiateur, Braze propose l'option de n'envoyer qu'aux étapes mises à jour, à toutes les étapes, ou de désactiver les envois initiateurs.