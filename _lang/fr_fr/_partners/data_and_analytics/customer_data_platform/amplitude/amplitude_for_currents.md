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

L'intégration bidirectionnelle entre Braze et Amplitude vous permet de [synchroniser vos cohortes Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/), traits d'utilisateurs et événements dans Braze, ainsi que d'exploiter Braze Currents pour [exporter vos événements Braze vers Amplitude](#data-export-integration) afin de réaliser des analyses plus approfondies de vos données produit et marketing.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Amplitude | Un [compte Amplitude](https://amplitude.com/) est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour pouvoir exporter des données dans Amplitude, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration de l'exportation des données {#data-export-integration}

Vous trouverez une liste complète des événements et propriétés d'événement pouvant être exportés de Braze vers Amplitude dans les sections suivantes. Tous les événements envoyés à Amplitude contiendront le paramètre `external_user_id` de l'utilisateur comme ID d'utilisateur Amplitude. Les propriétés d'événement propres à Braze seront envoyées sous la clé `event_properties` dans les données transmises à Amplitude.

{% alert important %}
Pour utiliser cette fonctionnalité, votre ID d'utilisateur Amplitude doit correspondre à l'ID externe de Braze.
{% endalert %}

Braze n'enverra des données d'événement que pour les utilisateurs dont l'`external_user_id` est défini ou pour les utilisateurs anonymes dont le `device_id` est défini. Pour les utilisateurs anonymes, vous devez synchroniser votre ID d'appareil Amplitude avec l'ID d'appareil Braze dans le SDK. Par exemple :

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Vous pouvez exporter deux types d'événements vers Amplitude : les [événements d'engagement des messages](#supported-currents-events), constitués des événements Braze directement liés à l'envoi de messages, et les [événements de comportement des clients](#supported-currents-events), incluant d'autres activités de l'application ou du site web telles que les sessions, les événements personnalisés et les achats suivis via la plateforme. Tous les événements réguliers sont précédés du préfixe `[Appboy]`, et tous les événements personnalisés sont précédés du préfixe `[Appboy] [Custom Event]`. Les propriétés d'événements personnalisés et d'achats sont précédées des préfixes `[Custom event property]` et `[Purchase property]`, respectivement.

Toutes les cohortes nommées et importées dans Braze seront préfixées par `[Amplitude]` et suffixées par leur `cohort_id`. Cela signifie qu'une cohorte nommée « TEST_COHORT » avec le `cohort_id` « abcd1234 » sera intitulée `[Amplitude] TEST_COHORT: abcd1234` dans les filtres de Braze.

Contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires.

### Étape 1 : Configurer l'intégration Amplitude dans Braze {#step-1-configure-amplitude-integration-in-braze}

Dans Amplitude, recherchez votre clé API d'exportation Amplitude.

{% alert warning %}
Maintenez votre clé API Amplitude à jour. Si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

### Étape 2 : Créer un flux Currents Braze {#step-2-create-braze-current}

Dans Braze, naviguez vers **Currents > + Create Current > Create Amplitude Export**. Fournissez un nom d'intégration, un e-mail de contact, une clé API d'exportation Amplitude et une région Amplitude dans les champs répertoriés. Ensuite, sélectionnez les événements que vous souhaitez suivre ; une liste des événements disponibles est fournie. Enfin, cliquez sur **Launch Current**.

{% alert note %}
Les événements envoyés de Braze Currents vers Amplitude sont comptabilisés dans votre quota de volume d'événements Amplitude.
{% endalert %}

![La page Braze Amplitude Currents. Cette page contient des champs permettant de définir le nom de l'intégration, l'e-mail du contact, la clé API et la région des États-Unis. La moitié inférieure de la page Currents répertorie les événements Currents que vous pouvez envoyer.]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
Consultez la [documentation sur l'intégration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) d'Amplitude pour en savoir plus.
{% endtab %}

## Limites de débit {#rate-limits}

Currents se connecte à l'API HTTP d'Amplitude, qui a une [limite de débit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) de 30 événements/seconde par appareil et une limite non documentée de 500 000 événements/jour par appareil. Si ces seuils sont dépassés, Amplitude limitera le nombre d'événements enregistrés via Currents. Si un appareil de votre intégration dépasse cette limite de débit, il se peut que les événements de tous les appareils apparaissent avec un certain retard dans Amplitude.

Les appareils ne devraient pas signaler plus de 30 événements par seconde ou 500 000 événements par jour dans des circonstances normales, et ce schéma ne devrait se produire qu'en raison d'une intégration mal configurée. Pour éviter ce type de retard, veillez à ce que votre intégration SDK signale les événements à un rythme normal, comme indiqué dans nos instructions d'intégration SDK, et évitez d'exécuter des tests automatisés qui génèrent de nombreux événements pour un seul appareil.

## Événements Currents pris en charge {#supported-currents-events}

Braze prend en charge l'exportation des événements suivants vers Amplitude :

- [Événements d'engagement des messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [Événements de comportement des clients]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

Pour la structure du payload de chaque événement, sélectionnez l'onglet **Amplitude** dans le [glossaire des événements d'engagement des messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) et le [glossaire des événements de comportement des clients]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).