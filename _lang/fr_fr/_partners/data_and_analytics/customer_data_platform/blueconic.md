---
nav_title: BlueConic
article_title: BlueConic
description: "Cet article de référence présente le partenariat entre Braze et BlueConic, une plateforme de données client spécialisée, vous permettant d'unifier les données dans des profils individuels durables, puis de les synchroniser entre les deux systèmes pour des objectifs d'importation via un serveur Amazon Web Services S3."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic](https://www.blueconic.com/), la plateforme spécialisée dans l'exploitation des données clients, extrait les données first-party des entreprises à partir de systèmes disparates et les rend accessibles au moment et à l'endroit où elles sont nécessaires pour transformer les relations client et stimuler la croissance de l'entreprise.

_Cette intégration est maintenue par Blueconic._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et BlueConic permet aux utilisateurs d'unifier les données à travers des profils individuels persistants, puis de les synchroniser entre les deux systèmes pour les objectifs d'importation via un serveur Amazon Web Services S3. Les objectifs potentiels comprennent des initiatives axées sur la croissance, l'orchestration du cycle de vie des clients, la modélisation et l'analyse, les produits et expériences numériques, la monétisation basée sur l'audience, et plus encore. Cette intégration prend en charge l'importation et l'exportation par lots planifiés.

{% alert important %}
Lors de l'utilisation de l'intégration, BlueConic enverra des deltas (données modifiées) à chaque synchronisation. Cela inclut tous les profils qui ont été modifiés depuis le dernier envoi ainsi que tous les attributs de ces profils. Surveillez l'utilisation des points de données en conséquence.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte BlueConic | Un [compte BlueConic](https://www.blueconic.com/) est nécessaire pour profiter de ce partenariat. Vous aurez besoin d'un accès pour [voir et modifier les connexions](https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles) dans votre compte BlueConic afin d'accéder aux plugins. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists` et `segments.details`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance](https://portal.aws.amazon.com/billing/signup#/start). |
| Authentification S3 | Vous devrez avoir accès à un serveur Amazon Web Services (S3) pour exporter et importer les données. |
| ID de la clé d'accès<br>Clé d'accès secrète | L'ID de la clé d'accès et la clé d'accès secrète vous permettront d'authentifier votre serveur S3 pour l'importation et l'exportation. |
| Compartiment AWS | Vous devrez vous connecter à S3 dans le plugin. Après authentification, les compartiments disponibles s'afficheront dans un menu déroulant. C'est là que sont stockés les fichiers à importer ou à exporter. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Création d'une connexion Braze {#step-1-creating-a-braze-connection}

Dans BlueConic, sélectionnez **Connections** dans la barre de navigation, puis **Add Connection**. Dans l'invite qui s'affiche, recherchez **Braze** et sélectionnez **Braze connection**.

Développez ou réduisez les champs de métadonnées disponibles dans la connexion en cliquant sur l'icône grise en forme de chevron. Dans ces champs, vous pouvez mettre cette connexion en favori, la nommer, ajouter des étiquettes, inclure une description et choisir de recevoir des notifications par e-mail si la connexion [s'exécute ou ne s'exécute pas](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ).

Enregistrez vos paramètres.

### Étape 2 : Configuration d'une connexion Braze {#step-2-configuring-a-braze-connection}

Pour configurer la connexion entre BlueConic et Braze, vous devez ajouter les identifiants de votre compte Braze et les informations de votre compte Amazon Web Services (S3) pour authentifier la connexion.

1. Dans BlueConic, sélectionnez **Set up and run** dans la section **Setup**.<br><br>
2. Dans la page d'authentification Braze qui s'ouvre, saisissez votre endpoint API REST Braze et votre clé API Braze.<br>
![Formulaire de paramètres d'authentification BlueConic Braze pour l'endpoint REST et la clé API.]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. Dans la section de configuration et d'authentification S3, entrez ces identifiants : ID de la clé d'accès Amazon Web Services (S3), clé d'accès secrète et compartiment S3. Il doit s'agir des [mêmes identifiants]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) que ceux que vous avez configurés lors de la mise en place de votre intégration Braze et Amazon S3. Enregistrez vos paramètres. <br>![Champs de configuration S3 de BlueConic pour la clé d'accès, la clé secrète et le compartiment.]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### Étape 3 : Création d'objectifs d'importation ou d'exportation (mappage d'importation) {#step-3-creating-import-or-export-goals-import-mapping}

Une fois l'authentification terminée, vous devez créer au moins un objectif d'importation ou d'exportation, activer la connexion et planifier ou exécuter la connexion.

{% tabs %}
{% tab Import %}

1. Sélectionnez **Import data into BlueConic** dans la section **Setup** pour ouvrir la page de configuration des données Braze.<br><br>
2. Sélectionnez l'emplacement des données dans Braze. Ici, vous pouvez indiquer à BlueConic où trouver les données à importer en sélectionnant votre audience Braze.<br>![L'audience BlueConic Braze définie comme « BlueConic Test Users ».]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Ensuite, mappez les identifiants entre Braze et BlueConic. <br>![Le champ « External ID » de Braze mappé sur le champ « Braze external ID » de BlueConic.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Pour relier les données clients entre les deux systèmes, saisissez un ou plusieurs identifiants client.<br>Utilisez la case à cocher **Allow creation...** pour permettre à BlueConic de créer de nouveaux profils pour les données qui ne correspondent pas à un profil BlueConic existant.<br><br>
4. Ensuite, faites correspondre les champs de données BlueConic que vous exportez aux champs Braze. Utilisez le premier menu déroulant pour sélectionner soit l'identifiant de profil BlueConic, soit une propriété de profil, puis sélectionnez l'identifiant de profil Braze correspondant dans le menu déroulant associé. Ensuite, utilisez le menu déroulant pour spécifier comment le contenu importé doit être ajouté aux valeurs existantes : ajouté, additionné, défini uniquement si la propriété de profil est vide, ou défini pour effacer (si le champ Braze est vide).<br>![Tableau de mappage des champs BlueConic faisant correspondre les propriétés BlueConic aux champs Braze.]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Utilisez le bouton **Add Mapping** pour créer des lignes de mappage supplémentaires si nécessaire. Vous pouvez ajouter plusieurs lignes de mappage avec l'option **Add remaining fields**. BlueConic détecte les champs Braze restants et les fait correspondre aux propriétés de profil BlueConic. Vous pouvez définir la stratégie de fusion pour les importations (définir, ajouter, additionner, définir si vide ou effacer) et fournir un préfixe personnalisé aux noms des propriétés de profil BlueConic.<br><br>
5. Enfin, sélectionnez **Run the connection** pour démarrer la connexion. Consultez [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) pour en savoir plus sur la planification et l'exécution des connexions.
{% endtab %}
{% tab Export %}

1. Sélectionnez **Export data to Braze** dans la section **Setup** pour configurer votre exportation de données de BlueConic vers Braze.<br><br>
2. Choisissez un segment BlueConic pour l'exportation. Seuls les profils de ce segment dont les identifiants correspondent dans Braze seront exportés.<br>![Un segment BlueConic de 20 000 profils.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. Ensuite, reliez les identifiants entre les profils BlueConic et les champs Braze. Vous pouvez éventuellement choisir de laisser BlueConic créer de nouveaux enregistrements si aucune correspondance n'est trouvée.<br>![Le champ « External ID » de Braze mappé sur le champ « Braze external ID » de BlueConic.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. Ensuite, faites correspondre les champs de données BlueConic que vous exportez aux champs Braze. Utilisez le menu déroulant de l'icône BlueConic pour choisir le type d'[information](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) que vous souhaitez exporter. Les informations disponibles comprennent les propriétés de profil, les identifiants de profil BlueConic, les segments associés, toutes les interactions consultées, les niveaux d'autorisation et une valeur textuelle statique.<br>![Tableau de mappage des champs BlueConic faisant correspondre les propriétés BlueConic aux champs Braze.]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Enfin, sélectionnez **Run the connection** pour démarrer la connexion. Consultez [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) pour en savoir plus sur la planification et l'exécution des connexions.
{% endtab %}
{% endtabs %}

## Étape 4 : Activer la connexion {#step-4-toggle-connection-on}

Utilisez la bascule située à côté du titre de la connexion Braze pour activer ou désactiver la connexion. Une connexion doit être activée pour s'exécuter pendant les heures planifiées.