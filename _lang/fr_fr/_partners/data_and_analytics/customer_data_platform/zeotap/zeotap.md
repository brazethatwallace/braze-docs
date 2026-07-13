---
nav_title: Zeotap
description: "Cet article de référence décrit le partenariat entre Braze et Zeotap, une plateforme de données clients de nouvelle génération qui fournit des solutions d'identité, des informations exploitables et des outils d'enrichissement des données."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) est une plateforme de données clients de nouvelle génération qui vous aide à découvrir et à comprendre votre audience mobile grâce à des outils de résolution d'identité, des informations exploitables et un enrichissement des données.

Grâce à l'intégration de Zeotap et Braze, vous pouvez étendre l'échelle et la portée de vos campagnes en synchronisant les segments clients de Zeotap pour associer les données des utilisateurs aux comptes utilisateurs de Braze. Vous pouvez ensuite agir sur la base de ces données, en proposant des expériences ciblées personnalisées à vos utilisateurs.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Zeotap | Un [compte Zeotap](https://zeotap.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST Braze avec les autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL Braze de votre instance]({% image_buster /assets/img/zeotap/zeotap1.png %}). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer une destination Zeotap {#step-1-create-a-zeotap-destination}

1. Depuis la plateforme Zeotap Unity, accédez à l'application **DESTINATIONS**.
2. Sous **All Channels**, sélectionnez **Braze**.
3. Dans l'invite qui apparaît, nommez votre destination et indiquez le nom de votre client ainsi que la clé API REST Braze associée à votre compte Braze.
4. Enfin, sélectionnez votre instance d'endpoint REST Braze dans la liste déroulante et enregistrez la destination. <br><br>![Configuration de la destination Braze dans Zeotap avec la liste déroulante d'instance d'endpoint.]({% image_buster /assets/img/zeotap/zeotap1.png %})

### Étape 2 : Créer et lier un segment Zeotap à votre destination {#step-2-create-and-link-a-zeotap-segment-to-your-destination}

1. Depuis la plateforme Zeotap Unity, accédez à l'application **CONNECT**.
2. Créez un segment et sélectionnez la destination Braze créée à l'étape 1.
3. Sélectionnez un identifiant de sortie compatible : MAIDs, adresse e-mail hachée en SHA256 ou tout identifiant client 1P reconnu par Braze (si vous souhaitez utiliser un identifiant personnalisé pour votre compte Braze, contactez Zeotap afin qu'il puisse être activé pour votre compte). Un seul identifiant de sortie peut être utilisé pour l'intégration Braze. Ces identifiants doivent être identiques à l'ID externe défini lors de la collecte des données du SDK Braze.
4. Enregistrez le segment.

![Configuration d'un segment Zeotap CONNECT lié à la destination Braze.]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
Les identifiants qui apparaissent sont à la fois disponibles dans le segment et pris en charge par Braze.
{% endalert %}

### Étape 3 : Créer un segment Braze {#step-3-create-braze-segment}

Après avoir créé, envoyé et traité avec succès un segment dans Zeotap, les utilisateurs de Zeotap apparaîtront dans le tableau de bord de Braze. Vous pouvez rechercher des utilisateurs par ID utilisateur dans le tableau de bord de Braze.

![Un profil utilisateur Braze montrant les segments un à quatre répertoriés comme « true » sous « Attributs personnalisés ».]({% image_buster /assets/img/zeotap/zeotap4.png %})

Si un utilisateur fait partie du segment Zeotap, le nom du segment apparaît en tant qu'attribut personnalisé sur son profil utilisateur avec la valeur booléenne `true`. Prenez note du nom de l'attribut personnalisé, car vous en aurez besoin lors de la création d'un segment Braze.

Ensuite, vous devez créer et définir ce segment dans Braze :
1. Dans le tableau de bord de Braze, sélectionnez **Segments**, puis **Créer un segment**.
2. Nommez votre segment et sélectionnez le segment d'attribut personnalisé créé dans Zeotap.
3. Enregistrez vos modifications.

![Dans le générateur de segments Braze, vous pouvez trouver les segments importés définis en tant qu'attributs personnalisés.]({% image_buster /assets/img/zeotap/zeotap3.png %})

Vous pouvez désormais ajouter ce segment nouvellement créé aux futures Campaigns et Canvas Braze pour cibler ces utilisateurs finaux.