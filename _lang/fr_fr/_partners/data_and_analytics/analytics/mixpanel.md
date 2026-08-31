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

L'intégration de Braze et Mixpanel vous permet d'[importer des cohortes Mixpanel dans Braze]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import) afin de créer des segments Braze qui peuvent cibler les utilisateurs dans de futures Campaigns ou Canvas Braze. La synchronisation des cohortes met à jour l'appartenance aux cohortes dans Braze et n'importe pas les événements ni les propriétés utilisateur de Mixpanel. Pour plus de détails, consultez [Importation de la cohorte Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import#data-import-integration).

Vous pouvez également tirer parti de Braze Currents pour [exporter vos événements Braze vers Mixpanel](#data-export-integration) afin d'obtenir des analyses plus approfondies sur les conversions, la rétention et l'utilisation des produits.

## Prérequis {#prerequisites}

| Condition | Description |
|---|---|
| Compte Mixpanel | Un [compte Mixpanel](https://mixpanel.com/) est requis pour tirer parti de ce partenariat. |
| Currents | Pour exporter des données vers Mixpanel, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration de l'exportation de données {#data-export-integration}

Une liste complète des événements pouvant être exportés de Braze vers Mixpanel se trouve dans cette section. Tous les événements envoyés à Mixpanel incluront l'`external_user_id` de l'utilisateur en tant qu'identifiant distinct Mixpanel (Distinct ID). Actuellement, Braze n'envoie pas de données d'événements pour les utilisateurs dont l'`external_user_id` n'est pas défini.

Vous pouvez exporter deux types d'événements vers Mixpanel : les [événements d'engagement liés aux messages](#supported-currents-events), qui comprennent les événements Braze directement liés à l'envoi de messages, et les [événements de comportement client](#supported-currents-events), qui incluent d'autres activités de l'application ou du site web telles que les sessions, les custom events et les achats suivis via la plateforme. Tous les custom events sont préfixés par `[Braze Custom Event]`. Les propriétés des custom events et les propriétés des événements d'achat sont préfixées respectivement par `[Custom event property]` et `[Purchase property]`.

Contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support) si vous avez besoin d'accéder à des droits d'événements supplémentaires.

### Étape 1 : Obtenir les identifiants Mixpanel {#step-1-get-mixpanel-credentials}

Dans votre tableau de bord Mixpanel, cliquez sur **Project Settings** dans un projet nouveau ou existant. Vous y trouverez le secret API Mixpanel et le jeton Mixpanel. Ces identifiants seront utilisés à l'étape suivante pour créer votre connexion Currents.

### Étape 2 : Créer un Braze Current {#step-2-create-braze-current}

1. Dans Braze, accédez à **Currents** > **+ Create Current** > **Create Mixpanel Export**.
2. Indiquez un nom d'intégration, une adresse e-mail de contact, le secret API Mixpanel et le jeton Mixpanel dans les champs prévus.
3. Sélectionnez les événements que vous souhaitez suivre ; une liste des événements disponibles est fournie.
4. Sélectionnez **Launch Current**.

![La page Braze Mixpanel Currents. Cette page comprend des champs pour le nom de l'intégration, l'adresse e-mail de contact, le secret API et le jeton d'exportation Mixpanel. La partie inférieure de la page Currents liste les événements Currents disponibles que vous pouvez envoyer.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Consultez la [documentation d'intégration](https://help.mixpanel.com/hc/en-us/articles/360001243663) de Mixpanel pour en savoir plus.
{% endtab %}

## Événements Currents pris en charge {#supported-currents-events}

Braze prend en charge l'exportation des événements suivants vers Mixpanel :

- [Événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Pour la structure du payload de chaque événement, sélectionnez l'onglet **Mixpanel** dans le [glossaire des événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) et le [glossaire des événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

## Résolution des problèmes {#troubleshooting}

### Vérifier la clé API Mixpanel et l'ID externe Braze {#verify-mixpanel-api-key-and-braze-external-id}

Confirmez que votre clé API Mixpanel et les valeurs de `braze_external_id` correspondent à ce que vous attendez dans Braze et Mixpanel. L'API de synchronisation des cohortes partage des groupes d'utilisateurs entre les produits, et la synchronisation ne fonctionnera pas correctement si l'`external_id` dans Braze et l'identifiant envoyé par Mixpanel ne correspondent pas. Les synchronisations de cohortes depuis Mixpanel s'exécutent selon le calendrier de Mixpanel — par exemple, une fois ou environ toutes les deux heures — accordez donc du temps entre les vérifications.

### Vérifier le statut du déploiement {#check-implementation-status}

Confirmez que `braze_external_id` est déployé dans Mixpanel.

### Définir la propriété utilisateur directement {#set-the-user-property-directly}

Pour réduire toute ambiguïté, définissez `braze_external_id` directement dans Mixpanel.

### Définition automatique de la propriété (SDK) {#automatic-property-setting-sdks}

Le SDK Mixpanel peut définir `braze_external_id` automatiquement lorsque le SDK Braze est intégré dans la même application. Si vous déployez Mixpanel et Braze ensemble, vous n'avez généralement pas besoin de configuration supplémentaire au-delà de l'installation des deux SDK.

{% alert note %}
`braze_external_id` n'est pas défini lorsque `changeUser()` est appelé dans Braze ; il est défini lorsque Mixpanel s'initialise ou démarre une session (lors de l'« init » ou du « start session »).
{% endalert %}