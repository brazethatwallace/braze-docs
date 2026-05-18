# Tableau de bord de l'utilisation des messages {#message-usage-dashboard}

> Le tableau de bord de l'utilisation des messages fournit des informations en libre-service sur l'utilisation de vos crédits SMS, RCS et WhatsApp, offrant une vue d'ensemble de l'utilisation historique et actuelle par rapport aux allocations contractuelles. Ces informations vous permettent d'y voir plus clair et de procéder aux ajustements nécessaires pour prévenir les risques de dépassement.

Le tableau de bord de l'**utilisation des messages** est divisé en trois sections :
- [Aperçu de l'utilisation des crédits](#credit-usage-overview)
- [SMS/MMS](#smsmms)
- [WhatsApp](#whatsapp)

Accédez au tableau de bord en sélectionnant **Paramètres** > **Facturation** > **Utilisation des messages**.

## Aperçu de l'utilisation des crédits {#credits-usage-overview}

L'**aperçu de l'utilisation des crédits** donne une vue d'ensemble de l'utilisation de tous les canaux qui consomment des crédits. Vous pouvez voir où vous en êtes par rapport à votre allocation globale de crédits, et consulter les détails de votre contrat actif et de votre période contractuelle.

Cette page s'affiche si vous bénéficiez d'un contrat de crédits. Les canaux qui utilisent des crédits sont indiqués dans l'**aperçu du contrat de crédits**.

{% alert note %}
Si vous avez acheté WhatsApp mais que vous n'avez pas de contrat de crédits, vous verrez toujours la consommation de crédits pour WhatsApp, car c'est ainsi que les anciens contrats WhatsApp sont facturés. Cela diffère des anciens SMS, qui ne consomment des crédits que lorsque vous avez souscrit un contrat de crédits.
{% endalert %}

Les données de l'**aperçu de l'utilisation des crédits** sont limitées à la période du contrat, affichée dans l'**aperçu du contrat de crédits**. Vous ne pouvez pas filtrer sur une plage de dates en dehors de la **période des crédits**.

### Utilisation des crédits sur le contrat {#credits-usage-over-contract}

Le graphique **Utilisation des crédits sur le contrat** montre votre consommation sur la période sélectionnée. La granularité de ce graphique dépend de l'horizon temporel que vous avez choisi. Accédez aux options d'exportation en sélectionnant le menu dans le coin supérieur droit du graphique.

![Tableau de bord présentant un aperçu de l'utilisation des crédits, avec des sections consacrées à l'utilisation des crédits, à la présentation du contrat de crédits et à la consommation de crédits par rapport au contrat.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}){: style="max-width:70%;"}

## SMS, MMS et RCS {#sms-mms-and-rcs}

L'**utilisation des crédits SMS/MMS/RCS** présente la répartition de l'utilisation pour les canaux SMS, MMS et RCS. Les colonnes du tableau de données exigent généralement que vous ayez acheté des crédits (bien que Braze prenne encore temporairement en charge les anciens modèles de facturation), et les colonnes **Credit ratio** et **Credits** indiquent respectivement le taux par pays et les crédits consommés. De plus, les vignettes de synthèse indiquent la consommation totale de SMS et, le cas échéant, de MMS pour la période sélectionnée.

Des filtres sont disponibles, vous permettant de filtrer par **pays** ou par type de SMS et RCS.

![Utilisation des crédits SMS/MMS/RCS avec des vignettes pour les données de synthèse et une section pour la consommation par compte.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}){: style="max-width:70%;"}

Contrairement à l'**aperçu de l'utilisation des crédits**, cette section contient les données historiques des périodes contractuelles précédentes.

{% alert note %}
Il est possible de sélectionner une plage de dates contenant à la fois des utilisations sans crédits et des utilisations avec crédits. Dans ce cas, la consommation survenue en dehors du contrat de crédits affichera `—` (null) dans les colonnes **Credit ratio** et **Credits**.
{% endalert %}

![Tableau d'utilisation des crédits SMS/MMS/RCS avec des valeurs nulles.]({% image_buster /assets/img/app_settings/sms_table_null3.png %}){: style="max-width:70%;"}

## WhatsApp {#whatsapp}

L'**utilisation des crédits WhatsApp** montre la répartition de l'utilisation du canal WhatsApp. Les vignettes affichent l'utilisation totale des crédits WhatsApp, qui peut être détaillée dans la section **Usage by account** en appliquant des filtres pour limiter les résultats du tableau de données à un espace de travail spécifique.

### Filtres {#filters}

Vous pouvez filtrer vos données par :
- Pays
- Compte WhatsApp Business
- Espace de travail Braze
- Type de catégorie de conversation
- Région

![Utilisation des crédits WhatsApp avec une vignette indiquant le total des crédits consommés et un tableau récapitulatif par compte.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}){: style="max-width:70%;"}

## Bon à savoir {#things-to-know}

{% alert important %}
Les données présentées dans le tableau de bord de l'**utilisation des messages** se situent au niveau du contrat et ne se rapportent pas à une entreprise ou à un espace de travail particulier du tableau de bord. Ces données reflètent l'utilisation de tous les espaces de travail de votre tableau de bord, et potentiellement de tous les tableaux de bord (si vous en avez plusieurs).
{% endalert %}

- Les données sous-jacentes sont fournies quotidiennement, les tableaux de données étant actualisés à 3 h, 9 h, 12 h et 18 h (heure de l'Est). Le tableau de bord **Utilisation des messages** peut nécessiter plus de 24 heures pour se mettre à jour.
- Braze suit la méthode d'arrondi standard : les nombres sont arrondis au dixième le plus proche.

### Sélection de la plage de dates {#date-range-selection}

Le tableau de bord **Utilisation des messages** exclut la date de fin de la période sélectionnée des résultats. Par exemple, si vous sélectionnez la période du 1er au 31 octobre, les statistiques d'utilisation du 31 octobre ne seront pas incluses. Pour inclure le dernier jour de la période souhaitée, prolongez la plage d'un jour. Par exemple, pour inclure tout le mois d'octobre, sélectionnez du 1er octobre au 1er novembre.

### Comparaison avec des fournisseurs tiers {#comparing-with-third-party-providers}

Lorsque vous comparez les données d'utilisation des messages de Braze avec celles de fournisseurs tiers (tels qu'Infobip), tenez compte des éléments suivants :

- **Segments de message et messages** : Braze comptabilise les messages SMS par segments de message. Un seul SMS divisé en plusieurs segments (par exemple, en raison de sa longueur) est comptabilisé comme plusieurs segments dans Braze. Pour plus d'informations, consultez [les calculateurs de facturation SMS et RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- **Messages basés sur les crédits ou non** : Le tableau de bord comprend à la fois des messages liés aux crédits et des messages non liés aux crédits. Les fournisseurs tiers peuvent ne compter que les messages basés sur les crédits, ce qui peut entraîner des écarts dans les totaux.
- **Entrant et sortant** : Assurez-vous que vous comparez les mêmes types de messages. Certains tableaux de bord tiers incluent à la fois les messages entrants et sortants dans leurs totaux, tandis que Braze vous permet de filtrer par direction.
- **Alignement de la plage de dates** : Étant donné que le tableau de bord exclut la date de fin, les comparaisons journalières peuvent être plus pertinentes que celles portant sur des périodes plus longues. Si vous comparez des données pour une période spécifique, prolongez votre plage de dates Braze d'un jour afin d'inclure le dernier jour de votre période de comparaison.