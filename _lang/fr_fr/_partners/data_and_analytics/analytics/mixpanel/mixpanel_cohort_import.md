---
nav_title: Mixpanel
article_title: Importation de la cohorte Mixpanel
description: "Cet article de référence présente la fonctionnalité d'importation de cohortes de Mixpanel, une plateforme d'analyse commerciale, vous permettant d'importer des cohortes Mixpanel dans Braze afin de créer des segments Braze qui peuvent être utilisés pour cibler les utilisateurs dans de futures Campaigns ou Canvas Braze."
page_type: partner
search_tag: Partner
---

# Importation de la cohorte Mixpanel {#mixpanel-cohort-import}

> Cet article décrit comment importer des cohortes d'utilisateurs de [Mixpanel](https://mixpanel.com/) vers Braze. Pour plus d'informations sur l'intégration de Mixpanel et de ses autres fonctionnalités, consultez l'[article principal sur Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

## Intégration de l'importation de données {#data-import-integration}

Lorsque vous synchronisez une cohorte de Mixpanel vers Braze, Braze reçoit les mises à jour d'appartenance à la cohorte pour les utilisateurs que Mixpanel peut associer à des profils Braze existants. Après une synchronisation, vous pouvez cibler ces utilisateurs avec le filtre de segment **Mixpanel cohorts**.

La synchronisation de cohorte n'importe pas les événements Mixpanel, les propriétés utilisateur Mixpanel ni les attributs personnalisés dans Braze. Le comportement du connecteur, y compris la cadence de synchronisation, est contrôlé dans Mixpanel. Pour les détails de configuration, consultez la [documentation de synchronisation des cohortes Braze de Mixpanel](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze). Pour les exigences de correspondance des utilisateurs, consultez [Correspondance des utilisateurs](#user-matching).

Toute intégration que vous mettez en place enregistrera des points de données. Si vous avez des questions sur les nuances des points de données de Braze, votre gestionnaire de compte Braze peut y répondre.

{% alert important %}
Conformément à la politique de conservation des données de Mixpanel, les événements envoyés avant le 1er janvier 2010 seront supprimés lors de l'importation.
{% endalert %}

### Étape 1 : Obtenir la clé d'importation des données Braze {#step-1-get-the-braze-data-import-key}

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Mixpanel**. Vous y trouverez l'endpoint REST et pourrez générer votre clé d'importation des données Braze.

Une fois générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Mixpanel.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Étape 2 : Configurer l'intégration de Braze dans Mixpanel {#step-2-set-up-the-braze-integration-in-mixpanel}

1. Dans Mixpanel, accédez à **Data Management > Integrations.**
2. Sélectionnez l'onglet de l'intégration Braze et cliquez sur **Connect**.
3. Dans l'invite qui s'affiche, indiquez la clé d'importation des données Braze et l'endpoint REST.
4. Sélectionnez **Continue**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Étape 3 : Exporter une cohorte Mixpanel vers Braze {#step-3-export-a-mixpanel-cohort-to-braze}

Dans Mixpanel, accédez à **Data Management > Cohorts**. Sélectionnez la cohorte à envoyer à Braze, puis sélectionnez **Export to Braze**. Enfin, sélectionnez une synchronisation unique ou une synchronisation dynamique. En sélectionnant la synchronisation dynamique, la cohorte sera mise à jour de manière récurrente selon un calendrier contrôlé par Mixpanel. Pour connaître la cadence de synchronisation la plus récente, consultez la [documentation de synchronisation des cohortes Braze de Mixpanel](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation d'une cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

### Étape 4 : Segmenter les utilisateurs dans Braze {#step-4-segment-users-in-braze}

Dans Braze, pour créer un segment de ces utilisateurs, accédez à **Audience** > **Segments**, nommez votre segment et sélectionnez **Mixpanel_Cohorts** comme filtre. Ensuite, utilisez l'option « inclut » et choisissez la cohorte que vous avez créée dans Mixpanel.

![Dans le générateur de segments de Braze, le filtre d'attributs utilisateur « Mixpanel cohorts » est défini sur « includes » et « Braze cohort ».]({% image_buster /assets/img_archive/mixpanel1.png %})

Après l'avoir enregistré, vous pouvez faire référence à ce segment lors de la création d'un Canvas ou d'une Campaign à l'étape du ciblage des utilisateurs.

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs identifiés peuvent être associés par leur `external_id` ou leur `alias`. Les utilisateurs anonymes peuvent être associés par leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id` et doivent être identifiés par leur `external_id` ou leur `alias`.

## Résolution des problèmes {#troubleshooting}

Si une synchronisation de cohorte Mixpanel semble incomplète ou ne se met pas à jour pour certains utilisateurs, consultez la section [Résolution des problèmes]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/#troubleshooting) de l'article principal sur Mixpanel.

Pour les étapes spécifiques au connecteur et la cadence de synchronisation, consultez la [documentation de synchronisation des cohortes Braze de Mixpanel](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).