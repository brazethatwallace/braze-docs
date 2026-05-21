---
nav_title: Adikteev
article_title: Prédiction de l'attrition Adikteev
description: "Cet article de référence présente le partenariat entre Braze et Adikteev, un moteur de fidélisation des utilisateurs qui combine la prédiction de l'attrition avec un service complet de reciblage applicatif."
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Prédiction de l'attrition Adikteev {#adikteev-churn-prediction}

> [Adikteev](https://www.adikteev.com/churn-prediction) est un moteur de rétention des utilisateurs qui combine la prédiction de l'attrition avec un service complet de reciblage d'applications.

_Cette intégration est maintenue par Adikteev._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et d'Adikteev vous permet de stimuler la rétention des utilisateurs en exploitant la technologie de prédiction de l'attrition d'Adikteev au sein des campagnes CRM de Braze afin de cibler en priorité les segments d'utilisateurs à haut risque.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Adikteev | Un compte Adikteev est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec la permission `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Settings** > **APIs and Identifiers**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation {#use-cases}

{% tabs %}
{% tab Filtrage d'audience %}
Affinement de vos segments d'audience en fonction du risque d'attrition.<br> Les noms et valeurs des attributs personnalisés envoyés par Adikteev sont configurables.

![Capture d'écran montrant un exemple d'utilisation d'un attribut personnalisé envoyé par Adikteev comme filtre d'un segment d'audience.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Ciblage des messages %}
Personnalisation de vos campagnes de messages Braze en fonction du risque d'attrition des destinataires.

![Capture d'écran montrant un exemple d'utilisation d'un attribut personnalisé envoyé par Adikteev comme filtre de ciblage de campagne.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## Intégration {#integration}

### Étape 1 : Partagez le flux d'événements de votre application {#step-1-share-the-event-stream-of-your-app}

Pour commencer à exécuter la prédiction de l'attrition sur l'audience de votre application, Adikteev aura besoin que vous activiez les postbacks d'événements depuis votre plateforme de mesure mobile. Suivez les instructions du [site d'assistance d'Adikteev](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation) pour effectuer cette configuration.

### Étape 2 : Créez votre clé API REST Braze {#step-2-create-your-braze-rest-api-key}

Dans Braze, accédez à **Settings** > **APIs and Identifiers**. Sélectionnez **Create New API Key**, saisissez le nom de la clé API de votre choix et assurez-vous que la permission suivante est ajoutée :

- `users.track`

### Étape 3 : Fournir des informations à l'équipe d'Adikteev {#step-3-provide-information-to-the-adikteev-team}

Pour terminer l'intégration, vous devez fournir votre clé API REST et l'URL de votre endpoint REST à votre gestionnaire de compte Adikteev. Adikteev établira la connexion et vous contactera une fois la configuration terminée pour valider l'intégration.

## Mise en lots et limites de débit {#batching-and-rate-limits}

L'endpoint `user.track` est utilisé pour mettre à jour les informations concernant vos utilisateurs. Consultez la [documentation de l'API]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour obtenir tous les détails concernant les limites de débit, les requêtes groupées et les détails des requêtes.

{% alert tip %}
N'oubliez pas que les appels à l'API ne doivent être effectués que pour mettre à jour des données qui ont changé, afin de réduire le nombre total d'appels à l'API. En d'autres termes, ne mettez à jour que les utilisateurs dont le segment d'attrition a changé.
{% endalert %}

## Identifiants des utilisateurs et des appareils {#user-and-device-identifiers}

Les profils utilisateurs dans Braze peuvent être associés à n'importe quel type d'identifiant d'utilisateur ou d'appareil ; la liste des options disponibles dépend de la manière dont vous avez intégré la collecte de données à Braze. Pour Adikteev, vous devrez trouver un identifiant commun entre votre MMP et vos profils utilisateurs dans Braze afin d'envoyer correctement les informations relatives au segment d'attrition.

## Conservation et suppression des données {#data-retention-and-deletion}

Si aucune mise à jour n'est effectuée, l'attribut et sa valeur sont conservés indéfiniment dans les profils utilisateurs de Braze.

Pour supprimer un attribut de profil, définissez-le sur `null`.

## Payloads des requêtes {#request-payloads}

Le payload envoyé par Adikteev à Braze est personnalisable et peut être configuré en fonction des besoins du client. Il s'agit notamment de configurer les identifiants utilisés, le nom de l'attribut personnalisé et de déterminer si Adikteev peut créer de nouveaux utilisateurs dans Braze ou seulement mettre à jour les utilisateurs existants.


## Assistance et résolution des problèmes {#support-and-troubleshooting}

Contactez votre gestionnaire de compte Adikteev pour toute question relative à l'intégration ou pour toute assistance concernant vos cas d'utilisation.