---
nav_title: Octolis
article_title: Octolis
description: "Cet article de référence décrit le partenariat entre Braze et Octolis, une plateforme d'activation de données, qui vous permet d'intégrer vos données dans Braze."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis](http://octolis.com) est une puissante plateforme d'activation de données (ou plateforme de données clients headless). En se basant sur l'une de vos bases de données, Octolis permet d'unifier, de préparer, de noter et de synchroniser les données dans vos outils professionnels.

_Cette intégration est maintenue par Octolis._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Octolis agit comme un intergiciel entre vos sources de données brutes et Braze, vous permettant de récupérer et d'unifier des données provenant de différentes sources, en ligne et hors ligne :
1. Unifiez et combinez les données provenant de sources telles que des boutiques en ligne, le CRM, le système POS, etc.
2. Normalisez et attribuez un score
3. Synchronisation en temps réel des champs calculés et des événements avec Braze

![Diagramme d'architecture montrant les sources de données Octolis, le traitement et le flux de synchronisation vers Braze.]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Octolis | Un compte Octolis est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track). <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Clé de l'application Braze | La clé de l'identifiant de votre application. Elle se trouve dans le **tableau de bord de Braze > Gérer les paramètres > Clé API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Avant de commencer l'intégration, consultez les sections suivantes sur les connexions, les sources, les audiences et les synchronisations.

Pour plus d'informations, consultez la section [Getting started](https://help.octolis.com/) d'Octolis.

### Étape 1 : Connecter Octolis à vos sources de données {#step-1-connect-octolis-to-your-data-sources}

Pour envoyer des données à Braze, vous devez vous assurer d'avoir créé au moins une [audience](https://help.octolis.com/audiences/create-a-no-code-audience). Une audience combine plusieurs sources de données, les applique aux étapes de préparation et ajoute des champs calculés.

Ces audiences doivent être établies à partir de plusieurs sources de données. Une source peut être l'une des suivantes :
- Un objet Salesforce (contacts, comptes, etc.)
- Un objet Zendesk (tickets)
- Un fichier à l'intérieur d'un SFTP (fichier CSV contenant certains contacts, fichier JSON contenant des événements…)
- Une table/vue d'une base de données.
- L'un de vos systèmes nous envoie des enregistrements via des webhooks ou des appels d'API.

### Étape 2 : Ajouter Braze comme destination {#step-2-add-braze-as-a-destination}

Ensuite, pour définir Braze comme nouvelle destination, sélectionnez **+ Add more** en haut de votre destination actuelle sur l'écran principal et sélectionnez **Braze** parmi les outils disponibles.

![Sélecteur de destination Octolis avec Braze sélectionné parmi les outils disponibles.]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

Une fois sélectionné, fournissez les informations suivantes :

- Votre clé API Braze : celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**.
- Fenêtre temporelle : Octolis appliquera la limitation du débit pendant la période donnée.
- Volume de requêtes : nombre de requêtes que vous pouvez effectuer au cours de cette période.
- Attributs personnalisés : spécifiez ici les nouveaux champs que vous allez envoyer à Braze, leur format (chaîne de caractères, entier, float), et cochez la case **Required for syncs** si vous souhaitez que l'un d'entre eux soit obligatoire pour une synchronisation.

![Champs de configuration de la destination Braze dans Octolis pour la clé API, les limites de débit et les attributs personnalisés.]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

Une fois configuré, Braze apparaîtra comme une nouvelle destination sur l'écran d'accueil.

### Étape 3 : Créer une nouvelle synchronisation {#step-3-create-a-new-sync}

Dans le menu, cliquez sur **Syncs** et sélectionnez **Add sync** dans la barre d'actions. Sélectionnez l'audience souhaitée parmi celles que vous avez créées précédemment.
Ensuite, sélectionnez **Braze** comme destination et l'entité à laquelle vous allez envoyer des données.

![Écran de création de synchronisation Octolis montrant les sélections d'audience et de destination Braze.]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### Étape 4 : Définir les paramètres de sortie {#step-4-set-output-settings}

Par défaut, Braze crée tous les attributs que vous allez envoyer, mais vous devez documenter la liste des champs à synchroniser.

![Écran des paramètres de sortie Octolis pour le mappage des champs Braze et la planification de la synchronisation.]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

Voici une définition spécifique des champs de paramétrage.

| Champ | Description |
| --- | --- |
| Où souhaitez-vous synchroniser l'audience ? | L'entité de Braze dans laquelle vous allez créer ou mettre à jour des enregistrements. |
| Quel champ est utilisé pour identifier un enregistrement ? | Le champ qu'Octolis utilisera pour identifier un enregistrement s'il existe déjà dans Braze. |
| À quelle fréquence souhaitez-vous envoyer chaque enregistrement ? | Par défaut, la synchronisation sera incrémentielle pour toutes les intégrations (API, base de données, FTP). Cela signifie que seules les nouvelles valeurs enregistrées depuis la dernière mise à jour seront mises à jour. Si nécessaire, vous pouvez également envoyer des tables entières à intervalles réguliers. À l'initialisation, Octolis enverra la table complète. |
| Quels champs doivent être synchronisés ? | Mappage des champs d'Octolis vers Braze. La liste de tous les champs disponibles apparaît dans le menu déroulant. Pour envoyer un champ calculé à Braze, vous devez d'abord vous assurer que vous avez créé la colonne correspondante dans votre entité Braze. |
| Quand souhaitez-vous synchroniser l'audience ? | Comment les données seront envoyées à Braze : manuellement, en temps réel ou de manière programmée. |
| Synchroniser lorsque l'enregistrement est… | Créé : pour les abonnements, il est important que la table Braze reste la table principale. Vous ne voulez pas qu'Octolis déclenche une synchronisation lorsque le champ est mis à jour.<br><br>Mis à jour : en revanche, pour un champ de prénom, par exemple, vous souhaitez pouvoir mettre à jour le champ de votre table Braze chaque fois qu'un client vous fournit une nouvelle entrée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 4 : Définir les paramètres de sortie" }

## Déduplication à clés multiples {#multi-keys-deduplication}

La déduplication constitue un défi majeur lorsqu'il s'agit de réconcilier des données provenant de sources multiples, notamment en ligne et hors ligne. Grâce au module avancé sans code d'Octolis, vous pouvez utiliser plusieurs clés pour la [déduplication](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work). Ce module est disponible pour chaque table principale, ce qui signifie que vous pouvez adapter la logique à chaque entité.