---
nav_title: Lemnisk
article_title: Intégrer Lemnisk à Braze
description: "Cet article de référence détaille le partenariat entre Braze et Lemnisk, une plateforme d'automatisation du marketing pilotée par une plateforme de données client alimentée par l'intelligence artificielle, vous permettant de transmettre en continu à Braze les données utilisateur collectées chez Lemnisk à partir de diverses sources, afin de les activer sur différents canaux et destinations à l'aide des outils de Braze."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/) est une plateforme de données client (CDP) alimentée par l'intelligence artificielle et une solution d'automatisation du marketing qui permet de capturer, d'unifier et d'activer en temps réel les données client provenant de sources diverses et cloisonnées. Elle transmet de façon fluide ces données unifiées sur diverses plateformes MarTech et commerciales, tout en offrant des analyses robustes en temps réel pour suivre chaque étape du cycle de vie des données client.

_Cette intégration est maintenue par Lemnisk._

## À propos de l'intégration {#about-the-integration}

L'intégration de Lemnisk et de Braze permet aux marques et aux entreprises de libérer tout le potentiel de Braze en agissant comme une couche d'intelligence pilotée par CDP qui unifie les données utilisateur à travers les plateformes en temps réel, et en envoyant les informations et les comportements collectés à Braze en temps réel. Lemnisk fournit des profils client enrichis directement dans Braze en combinant des signaux comportementaux et des attributs personnels qui vous permettent de personnaliser vos messages avec un contexte plus approfondi.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Comptes Lemnisk | Un compte [Lemnisk](https://www.lemnisk.co/) est nécessaire pour bénéficier de ce partenariat. |
| API externe dans Lemnisk | Contactez votre CSM Lemnisk pour faire activer l'**API externe** pour votre compte. |
| Clé API REST Braze | Une clé API REST Braze avec l'autorisation `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre compte]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de Lemnisk {#integrating-lemnisk}

### Étape 1 : Créer une API externe Braze {#create-a-braze-external-api}

Dans Lemnisk, accédez au canal API externe. Sélectionnez **Add New External API**. Nous allons maintenant configurer l'endpoint [Track Users]({{site.baseurl}}/api/endpoints/user_data/post_user_track) en tant qu'API externe.

![Démarrage du processus de création d'une API externe dans Lemnisk]({% image_buster /assets/img/lemnisk/open_external_api.png %})

Sous **Basic Details**, entrez un nom, une description, un canal et un identifiant de canal.

![Saisie des détails de configuration de base pour une nouvelle API externe dans Lemnisk]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

Sous **External API details**, entrez les détails pertinents pour votre endpoint `users.track`. Vous pouvez définir plusieurs champs au niveau de l'engagement à l'aide de {% raw %}`{{}}`{% endraw %}, ce qui vous permet de définir des valeurs différentes pour différentes campagnes.

![Remplissage des détails de l'endpoint et du payload de l'API externe]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

Pour terminer la configuration du suivi des utilisateurs, sélectionnez **Save**. Vous serez automatiquement redirigé vers la page **Test API**.

### Étape 2 : Tester la configuration {#step-2-test-the-configuration}

Sur la page **Test API**, saisissez quelques valeurs de test pour les paramètres API dans votre arborescence JSON, puis sélectionnez **Test Configuration**.

Si vos identifiants et les définitions de l'API sont corrects, Braze renvoie une réponse positive.

![Test d'une configuration d'API externe avec un exemple de payload et une réponse positive]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

Ensuite, vérifiez que vos événements sont bien envoyés à Braze. Dans le tableau de bord de Braze, accédez à **Audience** > **Search Users**, puis saisissez l'un des identifiants de votre configuration API externe (par exemple, l'adresse e-mail d'un utilisateur). Si tout fonctionne correctement, le profil qui a reçu votre déclencheur API de test sera répertorié.

![Consultation du profil d'un utilisateur et de l'aperçu de ses activités dans Braze]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### Étape 3 : Déclencher des événements utilisateur dans Braze {#step-3-trigger-user-events-in-braze}

1. Sur Lemnisk, créez un nouveau segment. Par exemple, vous pouvez créer un segment qui envoie des informations à Braze dès que les utilisateurs soumettent un formulaire de prospect.
2. Dans votre nouveau segment, accédez à **External API** > **Add Engagement**.
3. Sous **Engagement Creation**, entrez les détails de base et sélectionnez la configuration [que vous avez créée précédemment](#create-a-braze-external-api).
4. Sous **Configure Parameters**, vous trouverez les entrées pour les paramètres de Braze que vous avez choisi d'exposer au niveau de l'engagement. Dans l'exemple suivant, on retrouve _Name of the User_, _Product ID_ et _Event Time_.
    ![Création d'un engagement pour envoyer les données utilisateur à Braze]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. Saisissez les variables de personnalisation pertinentes pour les paramètres choisis, puis sélectionnez **Save**.
6. Lorsque vous avez terminé, activez l'engagement.