---
nav_title: Komo
article_title: Komo
description: "Cet article de référence décrit le partenariat entre Braze et Komo, une plateforme d'engagement client spécialisée dans la gamification, le contenu interactif, les compétitions, les prix et la fidélité. Grâce à cette intégration, les données first-party et zero-party capturées dans Komo peuvent être publiées dans Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) est une plateforme d'engagement client spécialisée dans la gamification, le contenu interactif, les concours, les prix et la fidélisation.

_Cette intégration est maintenue par Komo._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Komo vous permet de recueillir des données first-party et zero-party via les Komo Engagement Hubs. Ces hubs sont des microsites dynamiques qui offrent du contenu interactif et des fonctionnalités de gamification. Les données utilisateur collectées à partir de ces hubs sont ensuite transmises à l'API Braze.

- Intégrez en temps réel dans Braze des données utilisateur first-party et zero-party collectées dans Komo
- Ingérez des données d'études de marché et les préférences des utilisateurs lorsqu'ils répondent à des enquêtes, des sondages et des quiz
- Créez progressivement des profils utilisateurs dans Braze à mesure que l'utilisateur continue de s'engager et de partager plus de données le concernant
- Standardisez l'apparence et la convivialité des e-mails transactionnels envoyés via Braze

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Komo | Vous aurez besoin d'un compte Komo actif pour profiter de ce partenariat. Visitez [Komo](https://komo.tech/) pour commencer un essai dès maintenant. |
| Clé REST API Braze | Une clé REST API Braze avec les autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance.<br><br>Par exemple, cela devrait ressembler à ceci : https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation {#use-cases}

{% tabs local %}
{% tab Data Capture - Form Submission %}

Lorsqu'un utilisateur soumet un formulaire de capture de données personnalisable dans Komo, les champs Komo mappés dans l'intégration Braze seront transmis à Braze via l'appel d'API `/users/track/`.

Les formulaires de capture de données existent soit au début, soit à la fin des cartes.

{% endtab %}
{% tab Market Research - Coming soon %}

Komo permet également de transmettre des données d'études de marché capturées lorsqu'un utilisateur répond à une question de quiz, de sondage, de test de personnalité, de swiper, etc. Ces données vous permettront d'enrichir le profil d'un utilisateur au-delà des données capturées dans les soumissions de formulaires.

{% endtab %}
{% endtabs %}

## Intégration {#integration}

### Étape 1 : Publier un hub d'engagement Komo et une carte {#step-1-publish-a-komo-engagement-hub-and-card}

Vous devrez publier un Hub Komo avec au moins une carte contenant un formulaire de capture de données. Une fois publié, vous pouvez tester l'expérience utilisateur de bout en bout et vérifier que l'intégration fonctionne correctement.

![Hub Komo.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### Étape 2 : Ajouter l'application connectée Braze {#step-2-add-the-braze-connected-app}

Dans Komo, allez dans l'onglet **Company Settings**, puis sélectionnez la section **Connected Apps**.

Ensuite, trouvez l'intégration Braze dans la liste et sélectionnez le bouton **Connect** pour activer l'intégration.

![Connecter l'intégration Braze.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Connecter l'intégration Braze, étape 2b.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### Configurer l'intégration via un flux de travail {#configure-the-integration-via-a-workflow}

Vous devez maintenant configurer un flux de travail, au sein d'un espace de travail, d'un site ou d'une carte, pour synchroniser les données avec Braze.

L'étendue du flux de travail — à l'échelle de l'ensemble de l'espace de travail, d'un site (qui contient de nombreuses cartes) ou d'une seule carte — dépend de si vous souhaitez que le flux de travail se déclenche sur plusieurs cartes ou campagnes.

Après avoir créé un flux de travail, définissez votre déclencheur, recherchez Braze dans le menu des étapes et ajoutez l'étape « Track User ».

![Configuration de l'étape Track User.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

À partir de là, configurez les événements, les attributs et les abonnements que vous souhaitez synchroniser de Komo vers Braze.

![Liste des blocs de contenu.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Utilisation de l'intégration {#using-the-integration}

Votre intégration est désormais opérationnelle et vous pouvez surveiller chaque exécution dans l'onglet Exécutions du flux de travail.