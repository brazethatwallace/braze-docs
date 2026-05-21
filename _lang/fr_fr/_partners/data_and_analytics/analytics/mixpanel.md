---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "Cet article de référence présente le partenariat entre Braze et Mixpanel, une plateforme d'analyse commerciale, vous permettant d'importer des cohortes Mixpanel dans Braze afin de créer des segments Braze qui peuvent être utilisés pour cibler les utilisateurs dans de futures Campaigns ou Canvas Braze."
page_type: partner
search_tag: Partner
tool: Currents

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommixpanel-integration-with-braze339085scorm2u7y2e6qrldh2-stylefloatrightwidth120pxborder0-classnoimgbordermixpanel}

> [Mixpanel](https://mixpanel.com/) est une plateforme d'analyse commerciale qui vous permet d'exporter des événements de Mixpanel vers d'autres plateformes afin d'effectuer des analyses plus approfondies. Les données collectées peuvent ensuite être utilisées pour créer des rapports personnalisés et mesurer l'engagement et la rétention des utilisateurs.

L'intégration de Braze et Mixpanel vous permet d'[importer des cohortes Mixpanel dans Braze]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/) afin de créer des segments Braze qui peuvent cibler les utilisateurs dans de futures Campaigns ou Canvas Braze. La synchronisation des cohortes met à jour l'appartenance aux cohortes dans Braze et n'importe pas les événements ni les propriétés utilisateur de Mixpanel. Pour plus de détails, consultez [Importation de la cohorte Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/#data-import-integration).

Vous pouvez également tirer parti de Braze Currents pour [exporter vos événements Braze vers Mixpanel](#data-export-integration) afin d'obtenir des analyses plus approfondies sur les conversions, la rétention et l'utilisation des produits.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Mixpanel | Un [compte Mixpanel](https://mixpanel.com/) est nécessaire pour profiter de ce partenariat. |
| Currents | Pour pouvoir exporter des données vers Mixpanel, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de l'exportation des données {#data-export-integration}

Vous trouverez ci-dessous une liste complète des événements qui peuvent être exportés de Braze vers Mixpanel. Tous les événements envoyés à Mixpanel comprendront l'`external_user_id` de l'utilisateur comme ID distinct de Mixpanel. À l'heure actuelle, Braze n'envoie pas de données d'événement pour les utilisateurs dont l'`external_user_id` n'est pas défini.

Vous pouvez exporter deux types d'événements vers Mixpanel : les [événements d'engagement lié aux messages](#supported-currents-events), constitués des événements Braze directement liés à l'envoi de messages, et les [événements de comportement des clients](#supported-currents-events), comprenant d'autres activités de l'application ou du site web telles que les sessions, les événements personnalisés et les achats suivis par l'intermédiaire de la plateforme. Tous les événements personnalisés sont précédés du préfixe `[Braze Custom Event]`. Les propriétés d'événements personnalisés et les propriétés d'événements d'achat sont précédées des préfixes `[Custom event property]` et `[Purchase property]`, respectivement.

Contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires.

### Étape 1 : Obtenir les informations d'identification de Mixpanel {#step-1-get-mixpanel-credentials}

Dans votre tableau de bord Mixpanel, cliquez sur **Project Settings** dans un projet nouveau ou existant. Vous y trouverez le secret de l'API Mixpanel et le jeton Mixpanel. Ces informations d'identification seront utilisées à l'étape suivante pour créer votre connexion Currents.

### Étape 2 : Créer un flux Braze Currents {#step-2-create-braze-current}

1. Dans Braze, accédez à **Currents** > **+ Create Current** > **Create Mixpanel Export**.
2. Indiquez le nom de l'intégration, l'e-mail du contact, le secret de l'API Mixpanel et le jeton Mixpanel dans les champs répertoriés.
3. Sélectionnez les événements que vous souhaitez suivre ; une liste des événements disponibles est fournie.
4. Cliquez sur **Launch Current**.

![La page Braze Mixpanel Currents. Cette page comprend des champs pour spécifier le nom de l'intégration, l'e-mail du contact, le secret de l'API et le jeton d'exportation Mixpanel. La moitié inférieure de la page Currents répertorie les événements Currents disponibles que vous pouvez envoyer.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Consultez la [documentation sur l'intégration](https://help.mixpanel.com/hc/en-us/articles/360001243663) de Mixpanel pour en savoir plus.
{% endtab %}

## Événements Currents pris en charge {#supported-currents-events}

Braze prend en charge l'exportation des événements suivants vers Mixpanel :

- [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [Événements de comportement des clients]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

Pour la structure du payload de chaque événement, sélectionnez l'onglet **Mixpanel** dans le [glossaire des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) et le [glossaire des événements de comportement des clients]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).

## Résolution des problèmes {#troubleshooting}

### Vérifier la clé API Mixpanel et l'ID externe Braze {#verify-mixpanel-api-key-and-braze-external-id}

Confirmez que votre clé API Mixpanel et les valeurs `braze_external_id` correspondent à ce que vous attendez dans Braze et Mixpanel. L'API de synchronisation des cohortes partage des groupes d'utilisateurs entre les produits, et la synchronisation ne fonctionnera pas correctement si l'`external_id` dans Braze et l'identifiant envoyé par Mixpanel ne correspondent pas. Les synchronisations de cohortes depuis Mixpanel s'exécutent selon le calendrier de Mixpanel — par exemple, une fois ou environ toutes les deux heures — laissez donc du temps entre les vérifications.

### Vérifier l'état de l'implémentation {#check-implementation-status}

Confirmez que `braze_external_id` est implémenté dans Mixpanel.

### Définir la propriété utilisateur directement {#set-the-user-property-directly}

Pour réduire toute ambiguïté, définissez `braze_external_id` directement dans Mixpanel.

### Définition automatique de la propriété (SDK) {#automatic-property-setting-sdks}

Le SDK Mixpanel peut définir `braze_external_id` automatiquement lorsque le SDK Braze est intégré dans la même application. Si vous implémentez Mixpanel et Braze ensemble, vous n'avez généralement pas besoin de configuration supplémentaire au-delà de l'installation des deux SDK.

{% alert note %}
`braze_external_id` n'est pas défini lorsque `changeUser()` est appelé dans Braze ; il est défini lorsque Mixpanel s'initialise ou démarre une session (lors de l'« init » ou du « start session »).
{% endalert %}