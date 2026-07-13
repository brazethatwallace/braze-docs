# Tableau de bord de l'utilisation des crédits {#credits-usage-dashboard}

> Le tableau de bord de l'utilisation des crédits fournit des informations en libre-service sur votre consommation de crédits, offrant une vue complète de l'utilisation historique et actuelle par rapport aux allocations contractuelles. Ces informations peuvent réduire les incertitudes et vous aider à effectuer des ajustements pour prévenir les risques de dépassement.

Le tableau de bord **Credits Usage** est divisé en deux sections :
- [Aperçu de l'utilisation des crédits](#credits-usage-overview)
- [Onglets par canal](#credits-features)

Accédez au tableau de bord en allant dans **Paramètres** > **Facturation** > **Credits Usage**.

## Aperçu de l'utilisation des crédits {#credits-usage-overview}

**Message credit usage overview** fournit un aperçu de l'utilisation sur tous les canaux qui consomment des crédits. Vous pouvez voir comment vous progressez par rapport à votre allocation globale de crédits, et trouver des détails sur votre contrat actif et votre période contractuelle.

Cette page s'affiche si vous êtes sous un contrat de crédits. Les canaux qui consomment des crédits sont affichés dans **Credits usage**.

{% alert note %}
Si vous avez acheté WhatsApp mais que vous n'êtes pas sous un contrat de crédits, vous verrez tout de même la consommation de crédits pour WhatsApp, car c'est ainsi que les anciens contrats WhatsApp sont facturés. Cela diffère de l'ancien SMS, qui ne consomme des crédits que lorsque vous êtes sous un contrat de crédits.
{% endalert %}

Les données d'aperçu de l'utilisation des crédits sont limitées à la période contractuelle, qui est affichée dans **Credits contract overview**. Vous ne pouvez pas filtrer sur une plage de dates en dehors de la **Credits period**.


### Utilisation des crédits sur la durée du contrat {#credits-usage-over-contract}

Le graphique **Message credits usage over contract** affiche votre utilisation sur la période sélectionnée. La granularité de ce graphique dépend de la période choisie. Consultez les options d'exportation en sélectionnant le menu dans le menu du graphique.

![Graphique de l'utilisation des crédits sur la durée du contrat.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %})

## Onglet Aperçu {#overview-tab}

L'onglet **Overview Usage** affiche l'utilisation des crédits sur les canaux applicables à votre société. Par exemple, si vous n'avez pas WhatsApp, son onglet n'apparaîtra pas.

### Fonctionnalités de crédits {#credits-features}

Consultez les onglets suivants pour obtenir des détails sur ce qui est affiché pour chaque fonctionnalité qui consomme des crédits.

{% tabs %}
{% tab Bannières %}

### Bannières {#banners}

**Banners Credits Usage** affiche l'utilisation des crédits des bannières sur tous les comptes. Les tuiles montrent le total des crédits consommés et le total des impressions uniques quotidiennes. Le tableau **Usage by account** inclut **Braze workspace**, **Daily unique impressions**, **Credit ratio** et **Credits**. Lorsque des données sont disponibles, **Last updated** indique quand le tableau a été actualisé.

#### Filtres {#filters}

Vous pouvez filtrer vos données par :
- Plage de dates (par défaut les 30 derniers jours)
- Espace de travail Braze

Utilisez **Export** pour télécharger les données du tableau.

![Utilisation des crédits des bannières avec des tuiles pour les crédits et les impressions uniques et un tableau d'utilisation par compte.]({% image_buster /assets/img/app_settings/credits_usage_banners.png %})

{% endtab %}
{% tab Content Cards %}

### Content Cards

**Content Cards Credits Usage** affiche l'utilisation des crédits Content Cards sur tous les comptes. Les tuiles montrent le total des crédits consommés et le total des impressions uniques quotidiennes. Le tableau **Usage by account** inclut **Braze workspace**, **Card type**, **Daily Unique Impressions**, **Credit ratio** et **Credits**. Lorsque des données sont disponibles, **Last updated** indique quand le tableau a été actualisé.

#### Filtres

Vous pouvez filtrer vos données par :
- Plage de dates (par défaut les 30 derniers jours)
- Espace de travail Braze
- Type de carte

Utilisez **Export** pour télécharger les données du tableau.

![Utilisation des crédits Content Cards avec des tuiles pour les crédits et les impressions uniques et un tableau d'utilisation par compte.]({% image_buster /assets/img/app_settings/credits_usage_content_cards.png %})

{% endtab %}
{% tab E-mail %}

### E-mail {#email}

**Email Credits Usage** affiche l'utilisation des crédits e-mail sur tous les comptes. Les tuiles montrent le total des crédits consommés et le total des e-mails envoyés. Le tableau **Usage by account** inclut **Braze workspace**, **Email sent**, **Credit ratio** et **Credits**. Lorsque des données sont disponibles, **Last updated** indique quand le tableau a été actualisé.

#### Filtres

Vous pouvez filtrer vos données par :
- Plage de dates (par défaut les 30 derniers jours)
- Espace de travail Braze

Utilisez **Export** pour télécharger les données du tableau.

![Utilisation des crédits e-mail avec des tuiles pour les crédits et les e-mails envoyés et un tableau d'utilisation par compte.]({% image_buster /assets/img/app_settings/credits_usage_email.png %})

{% endtab %}
{% tab KakaoTalk %}

### KakaoTalk

**KakaoTalk Credits Usage** affiche l'utilisation des crédits KakaoTalk sur tous les comptes. Les tuiles montrent le total des crédits consommés et le total des envois KakaoTalk. Le tableau de la section **KakaoTalk** inclut **Braze workspace**, **Month**, **Year**, **Company**, **Sends**, **Credit Ratio** et **Credits**. Lorsque des données sont disponibles, **Last updated** indique quand le tableau a été actualisé.

#### Filtres

Vous pouvez filtrer vos données par :
- Plage de dates (par défaut les 30 derniers jours)
- Espace de travail Braze
- Mois
- Année
- Société

Utilisez **Export** pour télécharger les données du tableau.

![Utilisation des crédits KakaoTalk avec des tuiles pour les crédits et les envois KakaoTalk et un tableau d'utilisation.]({% image_buster /assets/img/app_settings/credits_usage_kakaotalk.png %})

{% endtab %}
{% tab LINE %}

### LINE

**LINE Credits Usage** affiche l'utilisation des crédits LINE sur tous les comptes. Les tuiles montrent le total des crédits consommés et le total des envois facturables. Le tableau de la section **Line** inclut **Braze workspace**, **Month**, **Year**, **Company**, **Destination**, **Billable sends**, **Credit ratio** et **Credits**. Lorsque des données sont disponibles, **Last updated** indique quand le tableau a été actualisé.

#### Filtres

Vous pouvez filtrer vos données par :
- Plage de dates (par défaut les 30 derniers jours)
- Espace de travail Braze
- Mois
- Année
- Société
- Destination

Utilisez **Export** pour télécharger les données du tableau.

![Utilisation des crédits LINE avec des tuiles pour les crédits et les envois facturables et un tableau d'utilisation détaillé.]({% image_buster /assets/img/app_settings/credits_usage_line.png %})

{% endtab %}
{% tab SMS, MMS et RCS %}

### SMS, MMS et RCS {#sms-mms-and-rcs}

**SMS/MMS/RCS Credits Usage** affiche la répartition de l'utilisation pour les canaux SMS, MMS et RCS. Les colonnes **Credit ratio** et **Credits** indiquent respectivement le taux par pays et les crédits consommés. De plus, des tuiles de haut niveau indiquent la consommation totale de SMS et, le cas échéant, de MMS sur la plage de dates sélectionnée.

Des filtres sont disponibles pour filtrer par **Country** ou par type SMS et RCS.

![Utilisation des crédits SMS/MMS/RCS avec des tuiles pour les données de haut niveau et une section pour la consommation par compte.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %})

Contrairement à l'**aperçu de l'utilisation des crédits**, cette section contient des données historiques provenant de périodes contractuelles antérieures.

{% alert note %}
Il est possible de sélectionner une plage de dates qui contient à la fois une utilisation avec et sans crédits. Dans ce cas, la consommation qui s'est produite en dehors des crédits affichera `—` (nul) dans les colonnes **Credit ratio** et **Credits**.
{% endalert %}

![Tableau d'utilisation des crédits SMS/MMS/RCS avec des valeurs nulles.]({% image_buster /assets/img/app_settings/sms_table_null3.png %})

{% endtab %}
{% tab Webhooks %}

### Webhooks

**Webhooks Credits Usage** affiche l'utilisation des crédits webhooks sur tous les comptes. Les tuiles montrent le total des crédits consommés et le total des envois de webhooks. Le tableau **Usage by account** inclut **Braze workspace**, **Sends**, **Credit ratio** et **Credits**. Lorsque des données sont disponibles, **Last updated** indique quand le tableau a été actualisé.

#### Filtres

Vous pouvez filtrer vos données par :
- Plage de dates (par défaut les 30 derniers jours)
- Espace de travail Braze

Utilisez **Export** pour télécharger les données du tableau.

![Utilisation des crédits webhooks avec des tuiles pour les crédits et les envois de webhooks et un tableau d'utilisation par compte.]({% image_buster /assets/img/app_settings/credits_usage_webhooks.png %})

{% endtab %}
{% tab WhatsApp %}

### WhatsApp

**WhatsApp Credits Usage** affiche la répartition de l'utilisation pour le canal WhatsApp. Les tuiles affichent le total de l'utilisation des crédits WhatsApp, qui peut être détaillé dans la section **Usage by account** en appliquant des filtres pour limiter les résultats du tableau de données à un espace de travail spécifique.

#### Filtres

Vous pouvez filtrer vos données par :
- Pays
- Compte WhatsApp Business
- Espace de travail Braze
- Type de catégorie de conversation
- Région

![Utilisation des crédits WhatsApp avec une tuile pour le total des crédits consommés et un tableau d'utilisation par compte.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %})

{% endtab %}
{% tab Ratios de crédits %}

### Ratios de crédits {#credit-ratios}

**Credit Ratios** affiche les ratios de crédits sur différents canaux et destinations. Il n'y a pas de tuiles récapitulatives ni de contrôle **Date range** sur cette page. Le tableau **Credit ratios** inclut **Channel grouping**, **Destination** et **Credit ratio**.

#### Filtres

Vous pouvez filtrer vos données par :
- Regroupement de canaux
- Destination

Utilisez **Export** pour télécharger les données du tableau.

![Page des ratios de crédits avec un tableau de ratios de crédits et des filtres par canal et destination.]({% image_buster /assets/img/app_settings/credits_usage_credit_ratios.png %})

{% endtab %}
{% tab Console des agents %}

### Console des agents {#agent-console}

**Agent Console Credits Usage** affiche l'utilisation des crédits de la console des agents sur tous les comptes. Les tuiles montrent le total des crédits consommés et le total des invocations. Le tableau **Usage by account** inclut **Braze workspace**, **Agent name**, **Model owner**, **Total invocations**, **Credit ratio** et **Credits**. Lorsque des données sont disponibles, **Last updated** indique quand le tableau a été actualisé.

#### Filtres

Vous pouvez filtrer vos données par :
- Plage de dates (par défaut les 30 derniers jours)
- Espace de travail Braze
- Nom de l'agent
- Propriétaire du modèle

Utilisez **Export** pour télécharger les données du tableau.

![Utilisation des crédits de la console des agents avec des tuiles pour les crédits et les invocations et un tableau d'utilisation par compte.]({% image_buster /assets/img/app_settings/credits_usage_agent_console.png %})

{% endtab %}
{% tab Audience Sync %}

### Audience Sync

**Audience Sync Credits Usage** affiche l'utilisation des crédits Audience Sync sur tous les comptes. Les tuiles montrent le total des crédits consommés et le total des synchronisations d'audience. Le tableau **Usage by account** inclut **Braze workspace**, **Provider**, **Total syncs**, **Credit ratio** et **Credits**. Lorsque des données sont disponibles, **Last updated** indique quand le tableau a été actualisé.

#### Filtres

Vous pouvez filtrer vos données par :
- Plage de dates (par défaut les 30 derniers jours)
- Espace de travail Braze
- Fournisseur

Utilisez **Export** pour télécharger les données du tableau.

![Utilisation des crédits Audience Sync avec des tuiles pour les crédits et les synchronisations d'audience et un tableau d'utilisation par compte.]({% image_buster /assets/img/app_settings/credits_usage_audience_sync.png %})

{% endtab %}
{% tab Archivage des messages %}

### Archivage des messages {#message-archiving}

**Message Archiving Credits Usage** affiche l'utilisation des crédits d'archivage des messages sur tous les comptes. Les tuiles montrent le total des crédits consommés et le total des messages archivés. Le tableau **Usage by account** inclut **Braze workspace**, **Channel**, **Messages archived**, **Credit ratio** et **Credits**. Lorsque des données sont disponibles, **Last updated** indique quand le tableau a été actualisé.

#### Filtres

Vous pouvez filtrer vos données par :
- Plage de dates (par défaut les 30 derniers jours)
- Espace de travail Braze
- Canal

Utilisez **Export** pour télécharger les données du tableau.

![Utilisation des crédits d'archivage des messages avec des tuiles pour les crédits et les messages archivés et un tableau d'utilisation par compte.]({% image_buster /assets/img/app_settings/credits_usage_message_archiving.png %})

{% endtab %}
{% endtabs %}

## Informations utiles {#things-to-know}

{% alert important %}
Les données affichées dans le tableau de bord **Credits Usage** sont au niveau du contrat et ne sont pas limitées à une société ou un espace de travail individuel du tableau de bord. Ces données reflètent l'utilisation de tous les espaces de travail au sein de votre tableau de bord, et potentiellement de tous les tableaux de bord (si vous en avez plusieurs).
{% endalert %}

- Les données sous-jacentes sont fournies quotidiennement, les tableaux de données étant actualisés à 3 h, 9 h, 12 h et 18 h EST. Le tableau de bord **Credits Usage** peut mettre plus de 24 heures à se mettre à jour.
- Braze suit la méthodologie d'arrondi standard : les nombres sont arrondis au dixième le plus proche.

### Sélection de la plage de dates {#date-range-selection}

Le tableau de bord **Credits Usage** exclut la date de fin de la plage sélectionnée des résultats. Par exemple, si vous sélectionnez du 1er au 31 octobre, les statistiques d'utilisation du 31 octobre sont exclues. Pour inclure le dernier jour de la période souhaitée, étendez la plage d'un jour. Par exemple, pour inclure tout le mois d'octobre, sélectionnez du 1er octobre au 1er novembre.

### Comparaison avec des fournisseurs tiers {#comparing-with-third-party-providers}

Lorsque vous comparez les données d'utilisation des crédits Braze avec des fournisseurs tiers (tels qu'Infobip), gardez à l'esprit :

- **Segments de message versus messages** : Braze compte les messages SMS par segments. Un seul message SMS divisé en plusieurs segments (par exemple, en raison de sa longueur) est compté comme plusieurs segments dans Braze. Pour en savoir plus, consultez [Calculateurs de facturation SMS et RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments).
- **Messages basés sur les crédits versus messages hors crédits** : le tableau de bord inclut à la fois les messages basés sur les crédits et ceux qui ne le sont pas. Les fournisseurs tiers peuvent ne compter que les messages basés sur les crédits, ce qui peut entraîner des écarts dans les totaux.
- **Entrant versus sortant** : assurez-vous de comparer les mêmes types de messages. Certains tableaux de bord tiers incluent à la fois les messages entrants et sortants dans leurs totaux, tandis que Braze vous permet de filtrer par direction.
- **Alignement des plages de dates** : étant donné que le tableau de bord exclut la date de fin, les comparaisons jour par jour peuvent être plus précises que les comparaisons sur des plages de dates plus longues. Si vous comparez des données pour une période spécifique, étendez votre plage de dates Braze d'un jour pour inclure le dernier jour de votre période de comparaison.