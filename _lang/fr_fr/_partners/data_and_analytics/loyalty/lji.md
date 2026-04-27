---
nav_title: GRAVTY®
article_title: Plateforme de fidélité GRAVTY®
description: "Cet article présente le partenariat entre Braze et GRAVTY®, une plateforme de fidélité de niveau entreprise qui permet aux marques de concevoir, gérer et faire évoluer des programmes de fidélité basés sur les données pour améliorer l'engagement client et la rétention."
alias: /partners/lji/
page_type: partner
search_tag: Partner
---

# Plateforme de fidélité GRAVTY® {#gravty-loyalty-platform}

> [GRAVTY®](https://www.lji.io/) est une plateforme de fidélité de niveau entreprise développée par Loyalty Juggernaut Inc. (LJI) qui permet aux marques du commerce de détail, du voyage, de la restauration (y compris la restauration rapide) et des services financiers de concevoir, gérer et faire évoluer des programmes de nouvelle génération — favorisant une croissance mesurable de l'engagement, de la rétention et de la valeur vie client grâce à des expériences personnalisées et basées sur les données.

Construite sur une architecture flexible et orientée API, GRAVTY® prend en charge l'accumulation et l'utilisation de points en temps réel, la gestion d'écosystèmes partenaires et l'intégration multicanale. Les équipes peuvent lancer plus rapidement, itérer sur les programmes et offrir des expériences de fidélité à grande échelle.

_Cette intégration est maintenue par LJI._

## À propos de l'intégration {#about-the-integration}

L'intégration entre Braze et GRAVTY® connecte les données de fidélité et les déclencheurs de messages entre les deux plateformes. GRAVTY® envoie les données utilisateur à Braze sous forme d'attributs, d'événements et d'achats. Braze stocke ces données et délivre des messages sur différents canaux tels que les SMS, les e-mails et les notifications push. Vous utilisez les données synchronisées pour la segmentation, la personnalisation et les déclencheurs.

## Conditions préalables {#prerequisites}

Avant de commencer, vous avez besoin des éléments suivants :

| Condition | Description |
| :--- | :--- |
| Compte GRAVTY® | Un compte GRAVTY® avec les autorisations nécessaires pour configurer les intégrations et gérer les abonnements aux événements. |
| Compte Braze | Un compte Braze actif avec l'accès API activé. |
| Clé API REST de Braze | Une clé API REST avec les autorisations `campaigns.trigger.send`, `canvas.trigger.send` et `users.track`.<br><br> Créez cette clé dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
| Endpoint API de Braze | Votre endpoint REST de Braze (par exemple, `https://rest.fra-01.braze.eu`). Pour plus d'informations, consultez [Instances et endpoints Braze]({{site.baseurl}}/api/basics/#endpoints). |
| ID de Campaign ou de Canvas | Les ID des workflows **Campaigns** ou **Canvas** que vous déclenchez depuis GRAVTY®. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Cas d'utilisation {#use-cases}

Cette intégration prend en charge les fonctionnalités Braze suivantes :

- **Synchronisation des données utilisateur (`/users/track`) :** Synchronisez les attributs des membres, les événements et les achats vers Braze pour la segmentation et la personnalisation.
- **Déclenchement de Campaigns (`/campaigns/trigger/send`) :** Déclenchez des messages ponctuels ou transactionnels à l'aide de Campaigns Braze.
- **Déclenchement de Canvas (`/canvas/trigger/send`) :** Lancez des parcours en plusieurs étapes et des messages de cycle de vie à l'aide de **Canvas** Braze.
- **Segmentation et personnalisation :** Créez des audiences ciblées et délivrez des communications personnalisées à partir des données synchronisées.

## Intégration {#integration}

L'intégration entre GRAVTY® et Braze est basée sur les API. Elle prend en charge la synchronisation des données en temps réel et le déclenchement des communications.

![Diagramme de flux montrant GRAVTY® envoyant des données et des déclencheurs aux API Braze, puis des messages vers SMS, e-mail, push et WhatsApp.]({% image_buster /assets/img/lji/braze-gravty-integration.png %})

### Étape 1 : Connecter Braze avec GRAVTY® {#step-1-connect-braze-with-gravty}

1. Accédez à **Subscriber Setup** dans GRAVTY® pour gérer les intégrations externes.
2. Sélectionnez **Add New Subscriber**.
3. Sélectionnez **Braze** comme fournisseur d'intégration.
4. Saisissez les informations suivantes :
   * **API URL** (votre endpoint REST de Braze)
   * **API Key** (votre clé API REST de Braze)
5. Enregistrez la configuration et confirmez que la connexion est active.

![Formulaire GRAVTY® Add Subscriber avec Braze sélectionné, les champs API URL et API key, et un bouton d'activation de l'abonné.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### Étape 2 : Configurer le mappage des attributs de modèle {#step-2-configure-template-attribute-mapping}

Après avoir enregistré l'abonné Braze, GRAVTY® ouvre la page **Template Attribute Mapping**. Utilisez-la pour mapper les champs vers Braze.

1. Sélectionnez **Add New Field**.
2. Sélectionnez un **attribut GRAVTY®** dans la liste.
3. Saisissez le **nom de l'attribut Braze** (attribut personnalisé) où la valeur doit apparaître dans Braze.

{% alert important %}
Vous n'avez pas besoin de mapper `external_id`. GRAVTY® le génère en interne en hachant l'identifiant du membre, et Braze reçoit cette valeur hachée comme `external_id` sur le profil utilisateur.<br><br> Avant d'activer l'intégration, confirmez que cela correspond à la façon dont vous définissez `external_id` dans Braze aujourd'hui. Si Braze utilise déjà un `external_id` différent pour les mêmes personnes, travaillez avec LJI pour aligner les identifiants avant de synchroniser les données.
{% endalert %}

{: start="4"}
4. Répétez les étapes 1 à 3 pour ajouter d'autres mappages.
5. Sélectionnez **Save**.

![Page GRAVTY® Subscription Setup avec la configuration du modèle, la configuration de la synchronisation et un tableau mappant l'entité, l'attribut GRAVTY® et les champs d'attribut de modèle pour Braze.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
L'intégration prend en charge les types de données d'attributs personnalisés de Braze, y compris les nombres (entier, float), les chaînes de caractères, les tableaux, les valeurs booléennes, les objets, les tableaux d'objets et les dates.
{% endalert %}

### Étape 3 : Tester l'intégration {#step-3-test-the-integration}

Déclenchez un événement de test dans GRAVTY® pour confirmer la synchronisation, les déclencheurs de communication et le flux de bout en bout.

![Aperçu du profil utilisateur Braze montrant le profil, les attributs personnalisés (niveau, dates, pays, ville) et les événements personnalisés renseignés à partir du mappage GRAVTY®.]({% image_buster /assets/img/lji/braze-member-profile.png %})

## Assistance {#support}

Pour obtenir de l'aide sur l'intégration ou la résolution des problèmes, contactez LJI à l'adresse [support@lji.io](mailto:support@lji.io).