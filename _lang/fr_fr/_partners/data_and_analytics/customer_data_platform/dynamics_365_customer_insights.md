---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "Cet article de référence présente le partenariat entre Braze et Dynamics 365 Customer Insights, une plateforme de données client d'entreprise de premier plan, qui vous permet d'exporter des segments de clients vers Braze pour les utiliser dans des campagnes ou des Canvas."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights

> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) est une plateforme de données client d'entreprise de premier plan qui offre des expériences client personnalisées avec une vue à 360 degrés de vos clients.

_Cette intégration est gérée par Dynamics 365 Customer Insights._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et de Dynamics 365 Customer Insights vous permet d'exporter des segments de clients vers Braze afin de les utiliser dans des campagnes ou des Canvas.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Dynamics 365 Customer Insights | Un compte [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) est nécessaire pour bénéficier de ce partenariat. Vous aurez besoin d'un accès en tant qu'administrateur pour voir et modifier les connexions dans votre compte Dynamics 365 Customer Insights afin d'accéder aux plugins nécessaires. |
| Clé API REST Braze | Une clé API REST Braze est requise avec les autorisations `users.track` et `users.export.segment`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Correspondance des identifiants de profil | Les profils de clients unifiés dans les segments exportés contiennent un champ représentant une adresse e-mail et un `external_id` Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration {#integration}

### Étape 1 : Établir une connexion Braze {#step-1-set-up-braze-connection}

Dans Customer Insights, accédez à **Admin > Connections**. Ensuite, sélectionnez **Add connections** et choisissez **Braze** pour configurer la connexion.

1. Donnez à votre connexion un nom reconnaissable dans le champ **Display name**.
2. Choisissez qui peut utiliser cette connexion. Si vous laissez ce champ vide, la valeur par défaut sera Administrators. Pour plus d'informations, reportez-vous à la section [Autoriser les contributeurs à utiliser une connexion pour les exportations](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Indiquez votre clé API Braze et votre endpoint REST au format `rest.iad-03.braze.com`.
4. Sélectionnez **I agree** pour confirmer la conformité des données et de la confidentialité.
5. Sélectionnez **Connect** pour initialiser la connexion avec Braze.
6. Sélectionnez **Add yourself as export user** et fournissez vos informations d'identification Customer Insights.
7. Sélectionnez **Save** pour terminer la connexion.

### Étape 2 : Créer un segment Braze {#step-2-create-a-braze-segment}

1. Dans Braze, accédez à **Audience** > **Segments**.
2. Créez un segment des utilisateurs que vous souhaitez que Microsoft mette à jour via Dynamics 365 Customer Insights.
3. Récupérez l'**identifiant API** du segment.

### Étape 3 : Configurer une exportation {#step-3-configure-an-export}

Vous pouvez configurer cette exportation si vous avez accès à une connexion de ce type. Pour plus d'informations, reportez-vous à l'[aperçu des exportations](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. Dans Customer Insights, accédez à **Data > Exports**. Pour créer une nouvelle exportation, sélectionnez **Add destination**.
2. Dans le champ **Connection for export**, sélectionnez une connexion pour la section Braze. Si vous ne voyez pas le nom de cette section, c'est qu'aucune connexion de ce type n'est disponible.
3. Indiquez l'identifiant API du segment dans Braze.
4. Dans la section **Data matching**, dans le champ **Email**, sélectionnez le champ qui représente l'adresse e-mail d'un client. Ensuite, dans le champ **Braze Customer ID**, sélectionnez le champ qui représente l'ID Braze du client. Vous pouvez également sélectionner un champ supplémentaire, facultatif, pour la correspondance des données.
  a. Si vous mappez le `external_id` dans Braze au champ ID client de Braze dans Customer Insights, les enregistrements existants seront mis à jour dans Braze lors de l'exportation.
  b. Si vous mappez un champ ID différent qui ne représente pas le `external_id` d'un enregistrement dans Braze, ou un champ vide, de nouveaux enregistrements seront créés dans Braze lors de l'exportation.
5. Enfin, sélectionnez les segments que vous souhaitez exporter et cliquez sur **Save**.

Notez que le fait d'enregistrer une exportation ne l'exécute pas immédiatement. Cette exportation sera exécutée à chaque [actualisation planifiée](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab). Vous pouvez également [exporter des données à la demande](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand).


### Utilisation de cette intégration {#using-this-integration}

Une fois vos segments exportés avec succès vers Braze, vous pouvez les retrouver en tant qu'attributs personnalisés dans les profils utilisateurs. L'attribut personnalisé sera nommé avec l'identifiant API du segment Braze qui a été saisi lors de la configuration de la connexion d'exportation. Par exemple, `"Segment_API_Identifier": "0000-0000-0000"`

Pour créer un segment de ces utilisateurs dans Braze, accédez à **Segments**, créez un nouveau segment et sélectionnez **Custom Attributes** comme filtre. À partir de là, vous pouvez choisir l'attribut personnalisé synchronisé par Dynamics 365. Une fois le segment créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

{% alert note %}
Pour plus d'informations sur cette intégration, consultez l'[article d'intégration de Braze](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) de Microsoft.
{% endalert %}