---
nav_title: Amplitude pour Currents
article_title: Amplitude pour Currents
page_order: 0
description: "Cet article de référence présente le partenariat entre Braze Currents et Amplitude, une plateforme d'analyse de produits et d'aide à la décision."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude pour Currents {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude-for-currents}

> [Amplitude](https://amplitude.com/) est une plateforme d'analyse de produits et d'aide à la décision.

L'intégration bidirectionnelle entre Braze et Amplitude vous permet de [synchroniser vos cohortes Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences), traits d'utilisateurs et événements dans Braze, ainsi que d'exploiter Braze Currents pour [exporter vos événements Braze vers Amplitude](#data-export-integration) afin de réaliser des analyses plus approfondies de vos données produit et marketing.

## Prérequis {#prerequisites}

| Condition | Description |
|---|---|
| Compte Amplitude | Un [compte Amplitude](https://amplitude.com/) est nécessaire pour tirer parti de ce partenariat. |
| Currents | Pour exporter des données vers Amplitude, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration d'exportation de données {#data-export-integration}

Une liste complète des événements et des propriétés d'événement pouvant être exportés de Braze vers Amplitude se trouve dans les sections suivantes. Tous les événements envoyés à Amplitude incluront l'`external_user_id` de l'utilisateur comme identifiant utilisateur Amplitude. Les propriétés d'événement spécifiques à Braze seront envoyées sous la clé `event_properties` dans les données transmises à Amplitude.

{% alert important %}
Pour utiliser cette fonctionnalité, votre identifiant utilisateur Amplitude doit correspondre à l'ID externe Braze.
{% endalert %}

Braze n'enverra des données d'événement que pour les utilisateurs dont l'`external_user_id` est défini ou les utilisateurs anonymes dont le `device_id` est défini. Pour les utilisateurs anonymes, vous devrez synchroniser votre identifiant d'appareil Amplitude avec l'identifiant d'appareil Braze dans le SDK. Par exemple :

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Vous pouvez exporter deux types d'événements vers Amplitude : les [événements d'engagement liés aux messages](#supported-currents-events), qui comprennent les événements Braze directement liés à l'envoi de messages, et les [événements de comportement client](#supported-currents-events), qui incluent d'autres activités de l'application ou du site web telles que les sessions, les custom events et les achats suivis via la plateforme. Tous les événements standard sont préfixés par `[Appboy]`, et tous les custom events sont préfixés par `[Appboy] [Custom Event]`. Les propriétés des custom events et des événements d'achat sont préfixées respectivement par `[Custom event property]` et `[Purchase property]`.

Toutes les cohortes nommées et importées dans Braze seront préfixées par `[Amplitude]` et suffixées par leur `cohort_id`. Cela signifie qu'une cohorte nommée « TEST_COHORT » avec le `cohort_id` « abcd1234 » sera intitulée `[Amplitude] TEST_COHORT: abcd1234` dans les filtres Braze.

Contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support) si vous avez besoin d'accéder à des droits d'événement supplémentaires.

### Étape 1 : Configurer l'intégration Amplitude dans Braze {#step-1-configure-amplitude-integration-in-braze}

Dans Amplitude, localisez votre clé API d'exportation Amplitude.

{% alert warning %}
Maintenez votre clé API Amplitude à jour. Si les identifiants de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cela persiste pendant plus de **48 heures**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

### Étape 2 : Créer un Current Braze {#step-2-create-braze-current}

Dans Braze, accédez à **Currents > + Create Current > Create Amplitude Export**. Fournissez un nom d'intégration, une adresse e-mail de contact, une clé API d'exportation Amplitude et une région Amplitude dans les champs indiqués. Ensuite, sélectionnez les événements que vous souhaitez suivre ; une liste des événements disponibles est fournie. Enfin, cliquez sur **Launch Current**.

{% alert note %}
Les événements envoyés de Braze Currents vers Amplitude seront comptabilisés dans votre quota de volume d'événements Amplitude.
{% endalert %}

![La page Braze Amplitude Currents. Cette page comprend des champs pour le nom de l'intégration, l'adresse e-mail de contact, la clé API et la région US. La moitié inférieure de la page Currents liste les événements Currents disponibles que vous pouvez envoyer.]({% image_buster /assets/img/amplitude4.png %})

{% alert tip %}
Si vous recevez une erreur « Clé API invalide » lors du collage de votre clé API Amplitude, essayez de saisir la clé manuellement. Certains navigateurs peuvent ajouter des caractères masqués lors du copier-coller, ce qui peut provoquer des erreurs de validation.
{% endalert %}

{% tab note %}
Pour plus d'informations, consultez la documentation d'Amplitude sur l'[intégration Appboy Amplitude](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration).
{% endtab %}

## Limites de débit {#rate-limits}

Currents se connecte à l'API HTTP d'Amplitude, qui impose une [limite de débit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 événements/seconde par appareil et une limite non documentée de 500 000 événements/jour par appareil. Si ces seuils sont dépassés, Amplitude limitera les événements enregistrés via Currents. Si un appareil de votre intégration dépasse cette limite de débit, vous pourriez constater un délai avant que les événements de tous les appareils n'apparaissent dans Amplitude.

Les appareils ne devraient pas signaler plus de 30 événements/seconde ou 500 000 événements/jour dans des circonstances normales, et ce type de comportement ne devrait se produire qu'en raison d'une intégration mal configurée. Pour éviter ce type de délai, assurez-vous que votre intégration SDK signale les événements à un rythme normal, tel que spécifié dans nos instructions d'intégration SDK, et évitez d'exécuter des tests automatisés qui génèrent un grand nombre d'événements pour un seul appareil.

## Événements Currents pris en charge {#supported-currents-events}

Braze prend en charge l'exportation des événements suivants vers Amplitude :

- [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Pour la structure du payload de chaque événement, sélectionnez l'onglet **Amplitude** dans le [glossaire des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) et le [glossaire des événements de comportement client]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).