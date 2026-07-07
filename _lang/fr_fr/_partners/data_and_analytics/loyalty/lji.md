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
| Clé REST API de Braze | Une clé REST API avec les autorisations `campaigns.trigger.send`, `canvas.trigger.send` et `users.track`.<br><br> Créez cette clé dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
| Endpoint API de Braze | Votre endpoint REST de Braze (par exemple, `https://rest.fra-01.braze.eu`). Pour plus d'informations, consultez [Instances et endpoints Braze]({{site.baseurl}}/api/basics/#endpoints). |
| ID de Campaign ou de Canvas | Les ID des workflows **Campaigns** ou **Canvas** que vous déclenchez depuis GRAVTY®. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Cas d'utilisation {#use-cases}

Cette intégration prend en charge les fonctionnalités Braze suivantes :

- **Synchronisation des données utilisateur (`/users/track`) :** Synchronisez les attributs des membres, les événements et les achats vers Braze pour la segmentation et la personnalisation.
- **Déclenchement de Campaigns (`/campaigns/trigger/send`) :** Déclenchez des messages ponctuels ou transactionnels à l'aide de Campaigns Braze.
- **Déclenchement de Canvas (`/canvas/trigger/send`) :** Lancez des parcours en plusieurs étapes et des messages de cycle de vie à l'aide de **Canvas** Braze.
- **Segmentation et personnalisation :** Créez des audiences ciblées et délivrez des communications personnalisées à partir des données synchronisées.

## Intégration {#integration}

L'intégration entre GRAVTY® et Braze est basée sur les API, permettant la synchronisation des données en temps réel et le déclenchement des communications entre GRAVTY® et Braze.

### Étape 1 : Connecter Braze avec GRAVTY® {#step-1-connect-braze-with-gravty}

1. Accédez à **Subscriber Setup** dans GRAVTY® pour gérer les intégrations externes.
2. Sélectionnez **Add New Subscriber**.
3. Sélectionnez **Braze** comme fournisseur d'intégration.
4. Saisissez les informations suivantes :
   * **API URL** (votre endpoint REST de Braze)
   * **API Key** (votre clé REST API de Braze)
5. Enregistrez la configuration et confirmez que la connexion est active.

![Formulaire GRAVTY® Add Subscriber avec Braze sélectionné, les champs API URL et API key, et un bouton d'activation de l'abonné.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### Étape 2 : Configurer le déclencheur d'événement {#step-2-configure-event-trigger}

Créez un événement dans GRAVTY® qui s'exécute lorsque l'activité d'un membre remplit les conditions que vous définissez (par exemple, une transaction, des points accumulés, un changement de niveau ou une inscription au programme).

1. Accédez à la section **Events** dans GRAVTY®.
2. Cliquez sur **Create Event**.
3. Définissez les conditions de l'événement (par exemple, transaction créée, points accumulés ou montée de niveau).
4. Configurez les règles qui déterminent quand l'événement doit être déclenché.
5. Associez l'abonné Braze à l'événement pour activer les déclencheurs de communication.
6. Enregistrez la configuration de l'événement.

Voici un exemple d'événement configuré pour se déclencher lorsqu'un membre est inscrit au programme :

![Configuration d'événement GRAVTY® pour l'inscription d'un membre au programme, avec Braze associé en tant qu'abonné.]({% image_buster /assets/img/lji/event-configuration.png %})

### Étape 3 : Configurer le mappage des attributs de modèle {#step-3-configure-template-attribute-mapping}

Après avoir configuré l'événement, complétez la configuration de l'abonné pour activer la synchronisation des données et les déclencheurs de communication :

1. Sélectionnez l'**abonné Braze** créé à l'étape 1 dans le menu déroulant des abonnés.
2. Choisissez le **canal** approprié (**Campaign** ou **Canvas**) en fonction de votre cas d'utilisation. Pour les scénarios de synchronisation de données uniquement, le canal peut rester non sélectionné.
3. Saisissez l'**ID de Campaign** ou l'**ID de Canvas** correspondant dans le champ **Template Name**, le cas échéant.
4. Configurez le type de communication pour prendre en charge la synchronisation et/ou l'envoi de messages basé sur des déclencheurs.

Pour configurer le mappage des champs dans GRAVTY® :

1. Cliquez sur **Add New Field**.
2. Sélectionnez l'**attribut GRAVTY®** dans le menu déroulant.
3. Saisissez le **nom de l'attribut Braze** correspondant où les données doivent être mappées.

{% alert important %}
Vous n'avez pas besoin de mapper `external_id`. GRAVTY® le génère en interne en hachant l'identifiant du membre (l'identifiant unique du membre dans GRAVTY®), et Braze reçoit cette valeur hachée comme `external_id` sur le profil utilisateur.<br><br> Avant d'activer l'intégration, confirmez que cela correspond à la façon dont vous définissez `external_id` dans Braze aujourd'hui. Si Braze utilise déjà un `external_id` différent pour les mêmes personnes, travaillez avec LJI pour aligner les identifiants avant de synchroniser les données.
{% endalert %}

{: start="4"}
4. Répétez les étapes **1 à 3** pour ajouter d'autres mappages si nécessaire.
5. Cliquez sur **Save** pour appliquer la configuration.

![Configuration du mappage des attributs pour la synchronisation des membres Braze.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
L'intégration prend en charge tous les types de données d'attributs personnalisés de Braze, y compris les nombres (entier, float), les chaînes de caractères, les tableaux, les valeurs booléennes, les objets, les tableaux d'objets et les dates.
{% endalert %}

### Étape 4 : Tester l'intégration {#step-4-test-the-integration}

Déclenchez un événement de test dans GRAVTY® pour vérifier que la synchronisation, les déclencheurs de communication et l'intégration globale fonctionnent comme prévu.

* Les données du membre sont synchronisées vers Braze et reflétées dans le profil du membre.

![Les champs de données sont renseignés en fonction du mappage de champs configuré.]({% image_buster /assets/img/lji/braze-member-profile.png %})

* La communication est déclenchée en fonction de la Campaign ou du Canvas configuré.

![Exemple d'e-mail déclenché depuis Braze.]({% image_buster /assets/img/lji/braze-email-example.png %})

## Assistance {#support}

Pour obtenir de l'aide sur l'intégration ou la résolution des problèmes, contactez LJI à l'adresse [support@lji.io](mailto:support@lji.io).