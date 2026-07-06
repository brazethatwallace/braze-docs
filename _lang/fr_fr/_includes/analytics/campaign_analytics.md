## Visualisation de l'analytique {#viewing-analytics}

Une fois que vous avez lancé votre campagne, vous pouvez revenir à la page des détails de cette campagne pour afficher les indicateurs clés. Accédez à la page **Campaigns** et sélectionnez votre campagne pour ouvrir la page des détails.{% if include.channel != "banner" %} Pour les {% if include.channel == "Content Card" %}Content Cards {% elsif include.channel == "banner" %}bannières {% elsif include.channel == "email" %}e-mails {% elsif include.channel == "in-app message" %}messages in-app {% elsif include.channel == "KakaoTalk" %}messages KakaoTalk {% elsif include.channel == "push" %}messages push {% elsif include.channel == "SMS" %}SMS {% elsif include.channel == "whatsapp" %}messages WhatsApp {% elsif include.channel == "webhook" %}webhooks {% endif %}envoyés dans Canvas, reportez-vous à [Canvas analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).{% endif %}

{% alert tip %}
Vous recherchez des définitions pour les termes et les indicateurs répertoriés dans votre rapport ? Consultez notre
  {% if include.channel == "email" %}[Glossaire analytique pour l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary)
  {% elsif include.channel == "banner" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics) et filtrez par bannières.
  {% elsif include.channel == "Content Card" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics) et filtrez par Content Cards.
  {% elsif include.channel == "in-app message" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics) et filtrez par message in-app.
  {% elsif include.channel == "push" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics) et filtrez par Push.
  {% elsif include.channel == "SMS" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics) et filtrez par SMS/MMS et RCS.
  {% elsif include.channel == "whatsapp" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics) et filtrez par WhatsApp.
  {% elsif include.channel == "webhook" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics) et filtrez par webhook.{% endif %}
{% endalert %}

À partir de l'onglet **Campaign Analytics**, vous pouvez consulter vos rapports dans une série de panneaux. Vous pouvez en voir plus ou moins que ceux énumérés dans les sections ci-dessous, mais chacun a son utilité propre.

### Intervalle de temps {#time-range}

Par défaut, la période prise en compte par **Campaign Analytics** correspond aux 90 derniers jours à compter de la date actuelle. Cela signifie que si la campagne a été lancée il y a plus de 90 jours, les analyses afficheront « 0 » pour la période donnée. Pour consulter toutes les analyses des campagnes antérieures, ajustez la période de référence du rapport.

### Détails de la campagne {#campaign-details}

Le panneau **Campaign Details** présente un aperçu global des performances de votre
  {% if include.channel == "banner" %}bannière.
  {% elsif include.channel == "Content Card" %}carte de contenu.
  {% elsif include.channel == "email" %}e-mail.
  {% elsif include.channel == "in-app message" %}message in-app.
  {% elsif include.channel == "KakaoTalk" %}message KakaoTalk.
  {% elsif include.channel == "push" %}message push.
  {% elsif include.channel == "SMS" %}SMS, MMS et RCS.
  {% elsif include.channel == "whatsapp" %}messages WhatsApp.
  {% elsif include.channel == "webhook" %}webhook.
  {% endif %}

Examinez ce panneau pour voir les indicateurs globaux tels que le nombre de messages envoyés par rapport au nombre de destinataires, le taux de conversion principal et le chiffre d'affaires total généré par ce message. Vous pouvez également consulter les paramètres de réception/distribution, d'audience et de conversion à partir de cette page.

{% alert note %}
Les chiffres analytiques dans le tableau de bord et dans Snowflake peuvent légèrement différer. Braze mesure les chiffres dans le tableau de bord et enregistre les lignes dans Snowflake séparément. Snowflake est la source de données la plus précise. Si vous constatez des écarts entre ces sources, nous vous recommandons de vous référer aux données Snowflake.
{% endalert %}

{% if include.channel == "whatsapp" %}
{% alert note %}
Le canal WhatsApp comprend le taux de lecture. Cet indicateur n'est fourni que pour les utilisateurs ayant activé les accusés de lecture, ce qui peut varier.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Panneau Détails de la campagne présentant un aperçu des indicateurs utilisés pour évaluer la performance de la campagne.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![Panneau Détails de la campagne présentant un aperçu des indicateurs utilisés pour évaluer la performance de la campagne.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![Panneau Détails de la campagne présentant un aperçu des indicateurs utilisés pour évaluer la performance de la campagne.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Panneau Détails de la campagne présentant un aperçu des indicateurs utilisés pour évaluer la performance de la campagne.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Panneau Détails de la campagne présentant un aperçu des indicateurs utilisés pour évaluer la performance de la campagne.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Panneau Détails de la campagne présentant un aperçu des indicateurs utilisés pour évaluer la performance de la campagne.]({% image_buster /assets/img/campaign_details_iam.png %})

Dans Canvas, les performances des messages in-app sont cartographiées sur le Canvas que vous avez créé. Vous pouvez utiliser le panneau de commande en haut de la page pour masquer les autres types de messages (canaux) et afficher uniquement les messages in-app de votre Canvas.

![Option de sélection du canal, avec la case In-App Message cochée.]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "KakaoTalk" %}
![La section Détails de la campagne.]({% image_buster /assets/img/kakaotalk/campaign_details.png %})

{% elsif include.channel == "webhook" %}
![Panneau Détails de la campagne présentant un aperçu des indicateurs utilisés pour évaluer la performance de la campagne.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

#### Audience estimée et audience actuelle {#estimated-audience-and-current-audience}

Selon la taille de votre espace de travail, le panneau **Campaign Details** peut afficher les statistiques d'audience sous le libellé **Estimated Audience** ou **Current Audience**.

Le tableau suivant résume la signification de chaque libellé.

| Libellé | Quand il est utilisé |
| --- | --- |
| **Estimated Audience** | Braze n'effectue pas par défaut un comptage complet de la base de données. La taille de l'audience est estimée à partir d'un échantillon et extrapolée, de manière similaire à la plage **Utilisateurs pouvant être atteints** dans le générateur de segments. Des marges d'erreur sont attendues, en particulier pour les grands espaces de travail ou les petits segments par rapport à l'ensemble de l'espace de travail. |
| **Current Audience** | Braze peut calculer la statistique par défaut avec un balayage complet des profils de l'espace de travail, de sorte que la taille d'audience affichée est un comptage actuel et non échantillonné (toujours soumis à l'accessibilité du canal, aux règles d'abonnement et aux autres options de ciblage). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Audience estimée et audience actuelle" }

Pour en savoir plus sur le comportement d'échantillonnage, le calcul des **statistiques exactes** et la segmentation des **utilisateurs pouvant être atteints**, consultez [Mesurer la taille d'un segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

{% if include.channel == "Content Card" %}

#### Groupes de contrôle {#cc-control-group}

Pour mesurer l'impact d'une carte de contenu individuelle, vous pouvez ajouter un [groupe de contrôle]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) à un test A/B. Le panneau supérieur **Campaign Details** n'inclut pas les indicateurs de la variante Groupe de contrôle.

{% elsif include.channel == "SMS" %}

#### Groupes de contrôle {#sms-control-group}

Pour mesurer l'impact d'un SMS, MMS ou message RCS individuel, vous pouvez ajouter un [groupe de contrôle]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) à un test A/B. Le panneau supérieur **Campaign Details** n'inclut pas les indicateurs de la variante Groupe de contrôle.

{% elsif include.channel == "whatsapp" %}

#### Groupes de contrôle {#whatsapp-control-group}

Pour mesurer l'impact d'un message WhatsApp individuel, vous pouvez ajouter un [groupe de contrôle]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) à un test A/B. Le panneau supérieur **Campaign Details** n'inclut pas les indicateurs de la variante Groupe de contrôle.

{% elsif include.channel == "webhook" %}

#### Groupes de contrôle {#webhook-control-group}

Pour mesurer l'impact d'un message webhook individuel, vous pouvez ajouter un [groupe de contrôle]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) à un test A/B. Le panneau supérieur **Campaign Details** n'inclut pas les indicateurs de la variante Groupe de contrôle.

{% endif %}

#### Modifications depuis la dernière consultation {#changes-since-last-viewed}

Le nombre de mises à jour de la campagne effectuées par d'autres membres de votre équipe est suivi par l'indicateur *Modifications depuis la dernière consultation* sur la page d'aperçu de la campagne. Sélectionnez **Changes Since Last Viewed** pour afficher un journal des modifications apportées au nom de la campagne, à sa planification, à ses étiquettes, à son message, à son audience, à son statut d'approbation ou à la configuration de l'accès de l'équipe. Pour chaque mise à jour, vous pouvez voir qui a effectué la modification et quand. Ce journal des modifications vous permet d'auditer les changements apportés à votre campagne.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Performance des Content Cards {#content-card-performance}

Le panneau **Content Card Performance** indique le niveau de performance de votre message selon différentes dimensions. Les indicateurs de ce panneau varient en fonction du canal de communication choisi et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal.

![Analytique des performances des messages des Content Cards]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### Performances des e-mails {#email-performance}

Le panneau **Email Performance** indique le niveau de performance de votre message selon différentes dimensions. Les indicateurs de ce panneau varient en fonction du canal de communication choisi et selon que vous exécutez ou non un test multivarié. Vous pouvez sélectionner l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal.

![Analytique des performances des messages e-mail]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### Performance des messages in-app {#in-app-message-performance}

Le panneau **In-App Message Performance** présente l'efficacité de votre message selon différentes dimensions. Les indicateurs de ce panneau varient en fonction du canal de communication choisi et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal.

![Analytique des performances des messages in-app]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Performances des notifications push {#push-performance}

Le panneau **Push Performance** donne un aperçu de la performance de votre message selon différentes dimensions. Les indicateurs de ce panneau varient en fonction du canal de communication choisi et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal.

![Analytique des performances des messages push]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### Performances des SMS/MMS/RCS {#smsmmsrcs-performance}

Le panneau **SMS/MMS/RCS Performance** présente les performances de votre message selon différentes dimensions. Les indicateurs de ce panneau varient en fonction du canal de communication choisi et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal.

![Panneau de performances SMS/MMS/RCS comprenant un tableau d'indicateurs pour le groupe de contrôle, la variante 1 et la variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### Performance des bannières {#banner-performance}

Le panneau **Banner Performance** indique le niveau de performance de votre message selon différentes dimensions. Ces indicateurs varient en fonction de votre canal de communication et de l'exécution ou non d'un test multivarié.

![Panneau de performances des bannières comprenant un tableau d'indicateurs pour un groupe de contrôle, la variante 1 et la variante 2.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "KakaoTalk" %}
### Performances KakaoTalk {#kakaotalk-performance}

Le panneau **KakaoTalk Performance** présente les performances de votre message selon différentes dimensions. Les indicateurs de ce panneau varient en fonction du canal de communication choisi et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal.

{% elsif include.channel == "webhook" %}
### Performances des webhooks {#webhook-performance}

Le panneau **Webhook Performance** donne un aperçu de l'efficacité de votre message selon différentes dimensions. Les indicateurs de ce panneau varient en fonction du canal de communication choisi et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal.

![Panneau de performances webhook comprenant un tableau d'indicateurs pour un groupe de contrôle et la variante 1.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### Performances WhatsApp {#whatsapp-performance}

Le panneau **WhatsApp Performance** présente les performances de votre message selon différentes dimensions. Les indicateurs de ce panneau varient en fonction du canal de communication choisi et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal.

![Panneau de performances WhatsApp comprenant un tableau d'indicateurs pour la variante 1.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

Si vous souhaitez simplifier votre vue, cliquez sur <i class="fas fa-plus"></i> **Add/Remove Columns** et décochez les indicateurs souhaités. Par défaut, tous les indicateurs sont affichés.

{% if include.channel == "email" %}

#### Cartes thermiques {#heatmaps}

Grâce aux cartes thermiques, vous pouvez visualiser le succès des différents liens d'une même campagne e-mail. Dans la section **Message Analytics**, accédez au panneau **Email Performance**. Sélectionnez **Preview & Heatmap** pour afficher un aperçu de votre campagne e-mail et de la carte thermique. Vous pouvez également sélectionner le lien hypertexte dans le nom de la variante pour afficher la carte thermique.

{% alert note %}
L'analytique de campagne affiche les données de clics pour un maximum de 100 URL uniques par variante, triées par nombre total de clics. Les URL sont regroupées par leur forme normalisée, qui n'inclut pas les paramètres de requête. Si une variante comporte plus de 100 URL normalisées uniques, seules les 100 premières par nombre de clics sont affichées. Les données de clics pour les URL au-delà de cette limite existent toujours, mais n'apparaîtront pas dans le tableau de bord ni dans la carte thermique. Lorsque l'aliasage de lien est activé, les clics sont suivis par identifiant de lien plutôt que par URL brute, ce qui entraîne généralement moins d'entrées uniques et rend cette limite moins susceptible d'être atteinte.
{% endalert %}

Dans cette vue, vous pouvez utiliser la bascule **Show Heatmap** pour afficher une vue visuelle de votre e-mail qui montre la fréquence globale et l'emplacement des clics au cours de la durée de vie de la campagne. Dans le panneau **Link Table by Total Clicks**, vous pouvez afficher tous les liens de votre campagne e-mail et les trier par nombre total de clics. Cela peut fournir des informations supplémentaires sur les endroits où vos utilisateurs naviguent. Pour enregistrer une copie de la carte thermique à des fins de référence, sélectionnez le bouton de téléchargement.

{% alert note %}
Si les liens utilisent Liquid pour des URL dynamiques, les URL cliquées peuvent ne pas correspondre suffisamment au lien rendu dans le message pour que la carte thermique associe les clics à ce lien, de sorte que ces liens peuvent ne pas apparaître sur la carte thermique. Utilisez les données de clics dans le panneau **Link Table by Total Clicks** pour obtenir une vue complète.
{% endalert %}

![Exemple de la page Aperçu et carte thermique qui inclut une campagne e-mail et un panneau avec des exemples d'alias de liens et leur nombre total de clics.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### Images

Nous vous recommandons d'activer CORS pour vos URL d'images afin d'éviter que les images ne soient cassées dans les aperçus et les exportations de cartes thermiques.

Si des images sont manquantes dans une exportation, travaillez avec vos développeurs pour que les ressources d'images autorisent l'accès cross-origin : le serveur doit renvoyer l'en-tête `Access-Control-Allow-Origin` avec soit `*`, soit le domaine de votre tableau de bord de Braze.

{% endif %}

{% if include.channel == "Content Card" %}

#### Indicateurs des Content Cards {#content-card-metrics}

Voici une description de certains indicateurs clés que vous pouvez voir lors de l'examen des performances de vos messages. Pour obtenir les définitions complètes de tous les indicateurs des Content Cards, reportez-vous au [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) et filtrez par Content Cards.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Indicateurs des Content Cards">
    <caption class="sr-only">Indicateurs de performance des Content Cards</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Messages Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                Le calcul diffère en fonction de ce que vous avez choisi pour la
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">création de cartes</a> :<br><br>
                <ul>
                    <li><b>Au moment du lancement ou de l'entrée d'étape :</b> Le nombre de cartes créées et disponibles pour être vues. Le fait que les utilisateurs aient consulté ou non la carte n'est pas comptabilisé.</li>
                    <li><b>À la première impression :</b> Le nombre de cartes affichées aux utilisateurs.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Ce compteur peut être incrémenté plusieurs fois pour un même utilisateur.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Ce compteur</span> n'augmente pas la deuxième fois qu'un utilisateur consulte une Content Card.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> Étant donné qu'un utilisateur peut avoir une impression quotidienne unique chaque jour, il est normal que ce chiffre soit supérieur au nombre d'<i>impressions uniques</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Cela inclut les clics sur les liens de désabonnement fournis par Braze.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">Unique Dismissals</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
En matière d'enregistrement des impressions, il existe quelques nuances entre le web, Android et iOS. En règle générale, Braze enregistre une impression lorsqu'une carte est vue, c'est-à-dire après qu'un utilisateur a fait défiler son fil jusqu'à la Content Card spécifique.
{% endalert %}

#### Impressions quotidiennes uniques et impressions uniques {#unique-daily-impressions-versus-unique-impressions}

Plusieurs indicateurs sont disponibles pour couvrir la visibilité de votre message, notamment les _impressions quotidiennes uniques_ et les _impressions uniques_. Prenons quelques exemples pour mieux comprendre ces indicateurs.

Supposons que vous visualisiez une Content Card aujourd'hui, puis que vous receviez une nouvelle carte de la même campagne demain, et encore après-demain — vous serez comptabilisé trois fois comme _impression quotidienne unique_. En revanche, vous ne serez comptabilisé que pour une seule _impression unique_. Vous serez également inclus dans le nombre de _messages envoyés_, car la carte était disponible sur votre appareil.

Autre exemple : supposons que vous observiez cinq _impressions uniques_ sur une campagne de Content Cards affichant 150 000 _messages envoyés_. Cela signifie que la carte a été mise à disposition (côté serveur) pour une audience de 150 000 utilisateurs, mais que seuls cinq appareils d'utilisateurs ont effectué toutes les étapes suivantes après l'envoi :

1. Ont démarré une session ou l'application a explicitement demandé une synchronisation des Content Cards (ou les deux)
2. Ont navigué vers la vue des Content Cards
3. Le SDK a enregistré une impression et l'a consignée sur le serveur

Les _messages envoyés_ correspondent aux Content Cards disponibles pour être vues, tandis que les _impressions quotidiennes uniques_ correspondent aux Content Cards qui ont été effectivement vues.

{% elsif include.channel == "banner" %}

### Indicateurs des bannières {#banner-metrics}

Voici les indicateurs clés à suivre lors de l'évaluation des performances de votre campagne de bannières. Les clics et les impressions pour les bannières sont suivis automatiquement par le SDK.

Pour obtenir les définitions complètes de tous les indicateurs relatifs aux bannières, reportez-vous au [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) et filtrez par bannières.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Indicateurs des bannières">
    <caption class="sr-only">Indicateurs de performance des bannières</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Pour les bannières, les impressions sont enregistrées une fois par session utilisateur. Si la même bannière est affichée plusieurs fois au cours d'une même session, une seule impression est enregistrée.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Chaque utilisateur n'est compté qu'une seule fois.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split">Le <i>nombre total de clics</i> est le nombre total (et le pourcentage) d'utilisateurs qui ont cliqué dans le message distribué, indépendamment du fait que le même utilisateur clique plusieurs fois.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-dismissals">Total Dismissals</a></td>
            <td class="no-split">Le <i>nombre total de rejets</i> est le nombre total de fois où les utilisateurs ont fermé la bannière. Disponible uniquement pour les bannières dont le comportement de fermeture est activé.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks No Dispatch ID' %} Chaque utilisateur n'est compté qu'une seule fois.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">Primary Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> Étant donné qu'un spectateur peut avoir une impression quotidienne unique chaque jour, il est normal que ce chiffre soit plus élevé que celui des <i>impressions uniques</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Revenue</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">Confidence</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### Exemples de calcul des indicateurs de bannières {#banner-metrics-calculation-examples}

Plusieurs indicateurs sont disponibles pour couvrir la visibilité de votre message, notamment les _impressions quotidiennes uniques_ et les _impressions uniques_. Prenons quelques exemples pour mieux comprendre ces indicateurs.

Supposons que vous consultiez une bannière aujourd'hui, puis la même bannière demain, et encore après-demain — vous serez comptabilisé trois fois comme _impression quotidienne unique_. En revanche, vous ne serez comptabilisé que pour une seule _impression unique_.

Autre exemple : supposons que vous observiez cinq _impressions uniques_ sur une campagne de bannières. Cela signifie que seuls les appareils de cinq utilisateurs ont effectué toutes les étapes suivantes :

1. Ont démarré une session ou l'application a explicitement demandé une synchronisation des bannières (ou les deux)
2. Ont navigué vers la vue des bannières
3. Le SDK a enregistré une impression et l'a consignée sur le serveur

Les _impressions quotidiennes uniques_ désignent les bannières qui ont été effectivement vues.

{% elsif include.channel == "email" %}

#### Indicateurs des e-mails {#email-metrics}

Voici quelques indicateurs clés spécifiques aux e-mails que vous ne retrouverez pas dans d'autres canaux. Pour voir les définitions complètes de tous les indicateurs e-mail utilisés dans Braze, reportez-vous à notre [Glossaire analytique pour l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Indicateurs des e-mails">
    <caption class="sr-only">Indicateurs de performance des e-mails</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Ceci est suivi sur une période de sept jours pour les e-mails et mesuré par <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a>. Cela inclut les clics sur les liens de désabonnement fournis par Braze. Ce nombre devrait se situer entre 5 et 10 %. Au-delà de 10 %, c'est exceptionnel !
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Unique Opens</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Pour les e-mails, le suivi s'effectue sur une période de 7 jours. Ce chiffre devrait se situer entre 30 et 40 %. Au-delà de 40 %, c'est exceptionnel !
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Click-to-Open Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Spam Rate</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %} Si cet indicateur est supérieur à 0,08, cela pourrait indiquer que le contenu de votre message est trop commercial ou que vous devriez reconsidérer vos méthodes de collecte d'adresses e-mail (afin de vous assurer que vous envoyez des messages à des personnes intéressées par votre correspondance).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Unsubscribers or Unsub</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Other Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Estimated Real Opens</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Consultez la section suivante pour plus de détails.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Machine Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Hard Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Soft Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Deferral</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### Réceptions et rebonds {#deliveries-and-bounces}

Le tableau de bord met en évidence les _échecs d'envoi définitifs_. Certains _rebonds_ peuvent être des échecs provisoires d'envoi et ne correspondront pas à ce seul compteur. Vous pouvez estimer les échecs provisoires d'envoi avec cette formule :

_Envois − (Réceptions + Échecs d'envoi définitifs) ≈ Échecs provisoires d'envoi_

Les _réceptions_ peuvent augmenter pendant la fenêtre de réessai de votre fournisseur de services d'e-mailing (ESP) à mesure que les tentatives réussissent, tandis que les _envois_ et les échecs d'envoi définitifs pour un envoi unique restent fixes une fois l'envoi terminé. SendGrid et SparkPost effectuent des réessais pendant 72 heures maximum ; Amazon SES effectue des réessais pendant 14 heures maximum.

###### Scénarios courants de résolution des problèmes de distribution {#common-delivery-troubleshooting-scenarios}

Lors de l'examen de vos analyses e-mail, gardez ces schémas à l'esprit :

- **Écart entre les _envois_ et (_réceptions_ + _échecs d'envoi définitifs_) :** Pendant la fenêtre de réessai de l'ESP après un envoi unique, cet écart reflète souvent des échecs provisoires d'envoi ou des reports encore en cours de réessai. Une fois les réessais terminés, tout écart restant correspond généralement à des messages qui ont subi un échec provisoire d'envoi et n'ont jamais été distribués — ces envois ne sont pas comptabilisés dans les _réceptions_ ni dans les _rebonds_ de la campagne. Utilisez la formule de la section [Réceptions et rebonds](#deliveries-and-bounces) pour estimer les échecs provisoires d'envoi en cours.
- **_Réceptions_ faibles après la fin des réessais :** Si les taux de distribution restent faibles une fois les réessais terminés, comparez le volume de cet envoi à vos habitudes. Les fournisseurs de boîtes de réception peuvent reporter, limiter ou rejeter provisoirement les e-mails lorsque le volume augmente par rapport à votre réputation d'expéditeur. Vous pouvez voir des messages tels que `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Utilisez la [limitation du débit de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) pour cadencer les envois importants, et consultez la section [IP limitées]({{site.baseurl}}/user_guide/channels/email/reporting#throttled-ips) pour des étapes de résolution supplémentaires.
- **Échecs provisoires d'envoi et reports non affichés dans l'analytique de campagne :** L'analytique de campagne met en évidence les _échecs d'envoi définitifs_ mais n'inclut pas les _échecs provisoires d'envoi_ ni les _reports_ en tant que colonnes distinctes. Surveillez ces événements dans le Journal d'activité des messages, avec le [filtre de segment Échec provisoire d'envoi]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced), ou via les événements de report Currents. Pour comprendre le fonctionnement des réessais, consultez la section [Reports](#deferrals).
- **Les pourcentages de distribution peuvent ne pas totaliser 100 % :** Le _% de réceptions_, le _% de rebonds_ et le _taux de spam_ peuvent ne pas totaliser 100 % des _envois_. Les messages qui subissent un échec provisoire d'envoi et ne sont jamais distribués après la fenêtre de réessai de l'ESP ne sont pas comptabilisés dans les _réceptions_ ni dans les _rebonds_ de la campagne, de sorte qu'une partie des _envois_ peut rester non comptabilisée dans ces taux. Attendez la fin des réessais avant de juger les performances finales de distribution, ou utilisez la formule de la section [Réceptions et rebonds](#deliveries-and-bounces) pour estimer le nombre d'envois encore en cours de réessai.

##### Clics sans événement d'ouverture {#clicks-without-an-open-event}

Un clic peut être enregistré sans ouverture lorsque le pixel d'ouverture ne se charge pas. Par exemple, le message est tronqué dans Gmail, ou l'utilisateur a désactivé les images (le pixel d'ouverture se trouve généralement en bas de page). Certains clients utilisent un proxy pour les images (comme Apple Mail), de sorte que l'ouverture peut être enregistrée lorsque le serveur récupère le pixel pour la première fois, et non lorsque l'utilisateur lit le message. Les domaines d'entreprise bloquent souvent les images par défaut.

Un clic et une ouverture peuvent également se produire à des jours différents : un utilisateur peut cliquer le 16 mai avec les images désactivées (pas d'ouverture), puis ouvrir dans le webmail le 17 mai (ouverture enregistrée à ce moment-là).

##### _Clics uniques_ supérieurs aux _ouvertures uniques_ {#higher-unique-clicks-than-unique-opens}

Il peut arriver que les _clics uniques_ dépassent largement les _ouvertures uniques_ (par exemple, plusieurs clics uniques pour chaque ouverture unique), même lorsque vous attendez un ratio plus faible de la part de votre audience. Ce phénomène signifie généralement que les ouvertures sont sous-comptabilisées, que les clics sont gonflés, ou les deux. Cela ne signifie toutefois pas que Braze comptabilise mal les clics de manière isolée.

Braze enregistre une ouverture d'e-mail lorsque le pixel de suivi d'ouverture se charge. Ce pixel est une petite image transparente (souvent décrite comme 1 x 1&nbsp;px) que Braze ajoute au HTML du message. Si le pixel ne se charge jamais, aucune ouverture n'est enregistrée pour cette consultation, mais les clics sur les liens peuvent tout de même être comptabilisés — de sorte que votre taux de clic par ouverture et l'équilibre entre ces deux indicateurs peuvent sembler faussés.

**La boîte de réception n'a jamais chargé le pixel de suivi d'ouverture**

Le pixel peut ne pas se charger lorsque :

- **Le message est tronqué.** Un HTML long repousse le contenu — y compris le pixel en bas de page — derrière une coupure de type « Afficher le message en entier ». Dans Gmail, les messages de plus d'environ [102 Ko]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size) sont souvent tronqués, ce qui peut empêcher le chargement du pixel jusqu'à ce que le message complet soit ouvert (et parfois même pas, selon le client).
- **Les images sont bloquées ou restreintes.** Une sécurité de boîte de réception plus stricte (courante sur les comptes d'entreprise) peut bloquer les images distantes jusqu'à ce que le destinataire choisisse de les charger, de sorte que le pixel d'ouverture ne se déclenche pas même s'il clique sur les liens suivis.
- **Le message se trouve dans les dossiers spam ou courrier indésirable.** De nombreux fournisseurs ne chargent pas les images distantes (y compris le pixel d'ouverture) dans ces dossiers par défaut.

**Ce que vous pouvez faire**

- **Troncature :** Raccourcissez et simplifiez le HTML, supprimez les styles ou ressources inutilisés et maintenez la taille globale du message dans les limites du client. Pour Gmail, visez moins d'environ 102 Ko comme décrit dans [Taille des e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size).
- **Sécurité de la boîte de réception et chargement des images :** Seul le destinataire (ou sa politique informatique) peut modifier le chargement des images par défaut.
- **Placement en spam :** Concentrez-vous sur l'[amélioration de la livrabilité des e-mails]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) et l'hygiène de vos listes. Si les e-mails atterrissent systématiquement dans le spam et que les indicateurs semblent erronés, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

**Activité de sécurité ou de bots sur les liens**

Certains produits de sécurité des e-mails suivent les liens pour détecter les menaces. Ces requêtes peuvent enregistrer un clic sans charger les images, de sorte que vous pouvez voir une activité de clics sans ouverture correspondante.

##### Reports {#deferrals}

On parle de report ou d'ajournement lorsqu'un e-mail n'a pas été livré immédiatement, mais que Braze relance l'e-mail via votre ESP après cet échec temporaire de distribution afin de maximiser les chances de réussite avant l'arrêt des tentatives pour cette campagne spécifique. SendGrid et SparkPost effectuent des réessais pendant 72 heures maximum ; Amazon SES effectue des réessais pendant 14 heures maximum. Les raisons habituelles de ces reports sont la limitation du débit du volume d'e-mails basée sur la réputation par le fournisseur de la boîte de réception, des problèmes temporaires de connectivité ou des erreurs DNS.

Les _reports_ diffèrent des _échecs provisoires d'envoi_. Si aucun e-mail n'a été délivré avec succès pendant cette période de réessai, Braze enverra un événement d'échec provisoire d'envoi par tentative de campagne envoyée. Avant le 25 février 2025, ces tentatives étaient comptabilisées comme plusieurs échecs provisoires d'envoi pour un même envoi de campagne.

Notez que les _reports_ ne sont actuellement disponibles qu'en utilisant les fonctionnalités Currents ou Braze Snowflake (telles que le Générateur de requêtes, SQL Segment, Snowflake Data Sharing). Si vous souhaitez les inclure dans l'analytique des campagnes ou de Canvas, veuillez [nous faire part de vos commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

##### Taux d'ouverture réel estimé {#estimated-real-open-rate}

Cette statistique utilise un modèle analytique propriétaire créé par Braze pour reconstruire une estimation du taux d'ouverture unique de la campagne comme si les ouvertures automatiques n'existaient pas. Bien que nous recevions des étiquettes *Ouvertures automatiques* pour certains événements d'ouverture provenant d'expéditeurs d'e-mails, ces étiquettes peuvent souvent classer les ouvertures réelles comme des ouvertures automatiques. Autrement dit, les *autres ouvertures* sont probablement une sous-estimation des ouvertures réelles (par des utilisateurs réels). Braze utilise plutôt les données de clics de chaque campagne pour déduire le taux d'ouverture du message par des humains réels. Cela permet de compenser les divers mécanismes d'ouverture automatique, y compris la protection de la confidentialité dans Mail d'Apple.

Le _taux d'ouverture réel estimé_ est calculé 24 heures après le début de l'envoi de l'e-mail et est ensuite recalculé toutes les 72 heures.

Étant donné que cet indicateur est recalculé de manière continue, la valeur du _taux d'ouverture réel estimé_ peut évoluer au fil du temps à mesure que de nouveaux signaux d'engagement (tels que les ouvertures et les clics) sont reçus et intégrés au modèle. En pratique, le _taux d'ouverture réel estimé_ peut continuer à être mis à jour quotidiennement tant qu'une campagne reste active.

En règle générale, il faut environ 10 000 e-mails délivrés pour que la statistique soit calculée avec succès, bien que ce nombre puisse varier en fonction du taux de clics. Si la statistique ne peut pas être calculée, la colonne affiche « -- ».

###### Limitations {#considerations}

Le taux d'ouverture réel estimé n'est disponible que dans les campagnes et n'est pas indiqué dans les événements Currents. Cet indicateur n'est calculé rétroactivement que pour les campagnes actives lancées avant le 14 novembre 2023.

##### Gestion des augmentations des taux de clics {#handling-increases-in-click-rates}

Les taux d'ouverture peuvent être un indicateur pertinent à suivre pour vos campagnes e-mail. Cependant, ils ne sont pas nécessairement des indicateurs précis de l'engagement humain avec les campagnes e-mail. Un événement d'ouverture, par définition, se produit lorsqu'un utilisateur ouvre un e-mail, ce qui signifie qu'un pixel de suivi d'ouverture transparent a été téléchargé avec succès.

De plus, l'utilisation d'outils d'analyse de sécurité peut gonfler les taux d'ouverture. Certains de ces outils protègent leurs utilisateurs en scannant les e-mails entrants à la recherche de contenu malveillant en cliquant sur les liens pour vérifier leur légitimité. Ces clics sont souvent appelés « clics de bot » ou « interaction non humaine » (NHI).

En fin de compte, une fois qu'un e-mail quitte nos serveurs, nous avons une visibilité limitée sur ce qui se passe ensuite. Voici quelques recommandations pour gérer les NHI qui affectent vos résultats :

1. Gardez à l'esprit que cela peut arriver à n'importe quel expéditeur et à presque n'importe quel destinataire. Les clics, comme les ouvertures, ne sont pas des indicateurs entièrement fiables de l'interaction humaine avec vos messages, ce qui signifie que les NHI ne sont pas évitables.
2. Un engagement positif plus élevé tend à être corrélé à un NHI plus faible, il est donc important de respecter les [bonnes pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) en matière d'envoi d'e-mails. Cela inclut l'obtention de la permission explicite de vos utilisateurs pour envoyer des e-mails et la temporisation régulière des abonnés non engagés.
3. Utilisez des liens HTTPS dans vos e-mails lorsque cela est possible. Les NHI sont moins fréquentes pour les expéditeurs utilisant des liens sécurisés.
4. Si vous utilisez un processus de désabonnement en un seul clic, envisagez de créer un [centre de préférences]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview) qui redirige les utilisateurs vers une page leur permettant de modifier et de gérer leurs préférences de notification. Cela peut être utile car les NHI peuvent désabonner des utilisateurs par inadvertance.
5. Envisagez d'utiliser [d'autres indicateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance) pour évaluer le succès de votre marketing par e-mail, tels que les conversions, les sessions d'application ou les visites de site.
6. Ajoutez un lien caché dans vos campagnes e-mail. Ce lien serait quelque chose qu'un humain ne remarquerait pas, comme un texte blanc sur blanc ou un signe de ponctuation. Les bots ont tendance à cliquer sur tous les liens. Vous pouvez donc en conclure que les utilisateurs qui génèrent des événements de clic sur le lien invisible sont en réalité le résultat de NHI, et que l'ouverture ou le clic n'indique donc pas nécessairement un engagement positif.

{% elsif include.channel == "in-app message" %}

#### Indicateurs des messages in-app {#in-app-message-metrics}

Voici quelques indicateurs clés des messages in-app que vous pouvez voir dans vos analyses. Pour consulter les définitions complètes de tous les indicateurs des messages in-app utilisés dans Braze, reportez-vous à notre [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

{% alert note %}
Les rapports pour les _clics sur le bouton 1_ et les _clics sur le bouton 2_ ne fonctionnent que si vous spécifiez l'**Identifier for Reporting** comme étant respectivement « 0 » et « 1 » dans le message in-app.

![Le champ « Identifier for Reporting » avec la valeur « 0 ».]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Indicateurs des messages in-app">
    <caption class="sr-only">Indicateurs de performance des messages in-app</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Body Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Button 1 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Button 2 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Conversions (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Total Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Conversion Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Close Message</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

#### Écarts entre les groupes de contrôle et les variantes {#discrepancies-between-control-groups-and-variants}

Lorsqu'une campagne de messages in-app a une répartition 50-50 entre les variantes, il arrive que le groupe de contrôle ait un pourcentage légèrement supérieur à celui de la variante (par exemple 51 % pour le groupe de contrôle et 49 % pour la variante). Cet écart est dû à une différence dans le temps de rendu — par exemple, lorsque les messages de la variante utilisent des images volumineuses ou du contenu connecté avec modèle et que les utilisateurs quittent avant la fin du rendu, tandis que le groupe de contrôle enregistre les impressions sans afficher de message.

La répartition entre les groupes de contrôle et les variantes est censée être à peu près égale, mais l'affectation à une variante se produit au moment où le message in-app est effectivement envoyé à l'appareil. Certains utilisateurs peuvent ne jamais déclencher le message in-app (par exemple, s'ils n'effectuent jamais l'action qui déclenche l'événement personnalisé requis), ce qui peut entraîner des différences dans la taille des groupes.

{% elsif include.channel == "KakaoTalk" %}

### Indicateurs KakaoTalk {#kakaotalk-metrics}

Voici quelques indicateurs clés de KakaoTalk que vous pouvez voir dans vos analyses. Pour plus de détails, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics).

{% alert note %}
Actuellement, les statistiques d'audience estimées ou exactes ne sont pas disponibles pour les campagnes KakaoTalk.
{% endalert %}

| Terme | Définition |
| --- | --- |
| Audience | L'_audience_ est le pourcentage d'utilisateurs qui ont reçu un message particulier. <br><br>_(Nombre de destinataires dans la variante) / (Destinataires uniques)_ |
| Destinataires uniques | Les _destinataires uniques_ correspondent au nombre de destinataires quotidiens uniques, c'est-à-dire les utilisateurs qui ont reçu un nouveau message au cours d'une journée. Pour que ce compteur s'incrémente plus d'une fois pour un utilisateur, celui-ci doit recevoir un nouveau message un jour différent. Ce nombre est basé sur le `user_id`. Pour plus de détails, consultez [Destinataires uniques dans le Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics#unique-recipients). |
| Envois | Le nombre total de messages envoyés dans une campagne. Cela ne signifie pas que le message a été reçu ou distribué sur un appareil, seulement que le message a été envoyé. |
| Nombre total de clics | Le nombre total de fois où les messages KakaoTalk envoyés ont été cliqués par les utilisateurs. |
| Erreurs | Les _erreurs_ correspondent au nombre d'erreurs renvoyées par le fournisseur KakaoTalk (incrémenté pendant le processus d'envoi). |
| Chiffre d'affaires | Le _chiffre d'affaires_ est le revenu en dollars provenant des destinataires de la campagne dans la fenêtre de conversion principale définie. |
| Conversions principales | Les _conversions principales_ correspondent au nombre de fois qu'un événement défini s'est produit après l'interaction avec ou la consultation d'un message reçu d'une campagne Braze. Cet événement défini est déterminé par vous lors de la création de la campagne. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs KakaoTalk" }

{% elsif include.channel == "push" %}

#### Indicateurs des notifications push {#push-metrics}

Voici une description de certains indicateurs clés que vous pouvez voir lors de l'examen des performances de vos messages. Pour obtenir les définitions complètes de tous les indicateurs push, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) et filtrez par push.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Indicateurs des notifications push">
    <caption class="sr-only">Indicateurs de performance des notifications push</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} Consultez <a href="#bounced-push">Notifications push rejetées</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Direct Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> La distribution des notifications est assurée au mieux par les services de notification push d'Apple (APNs). Elle n'est pas destinée à fournir des données à votre application, mais seulement à informer l'utilisateur que de nouvelles données sont disponibles. La distinction importante est que nous affichons le nombre de messages que nous avons délivrés avec succès aux APNs, et pas nécessairement le nombre de notifications que les APNs ont délivrées avec succès aux appareils.

##### Suivi des désabonnements {#tracking-unsubscribes}

Les désabonnements push ne sont pas inclus dans les indicateurs analytiques des campagnes et dépendent des mises à jour du statut push d'un utilisateur par des fournisseurs tels qu'Apple ou Google. Ces mises à jour peuvent être peu fréquentes et imprévisibles. Par conséquent, les désabonnements push ne sont pas pris en compte en tant qu'indicateur dans l'analytique des campagnes push.

Cependant, le suivi manuel des désabonnements push peut fournir des informations précieuses sur les réponses des utilisateurs à votre fréquence de notification et à la pertinence du contenu. Voici deux options pour suivre les désabonnements push : les filtres de segment ou les filtres personnalisés.

{% tabs local %}
{% tab Filtres de segment %}

Vous pouvez créer un segment pour identifier les utilisateurs qui ne sont pas activés pour les notifications push, c'est-à-dire qui ne sont pas abonnés ou en situation d'abonnement et qui ne disposent pas d'un [jeton push au premier plan]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration#push-tokens). Par exemple, pour visualiser le nombre de désabonnements dans votre application, vous pouvez utiliser une combinaison « OU » des segments suivants :

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![Dans le générateur de segments, le filtre « Background or Foreground Push Enabled for App » pour une application est désactivé et le filtre « Has Uninstalled » est sélectionné.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Notez que les filtres de segmentation sont approximatifs et ne peuvent pas être spécifiquement liés à une date et à une campagne.

{% endtab %}
{% tab Filtres personnalisés %}

{% alert important %}
L'enregistrement d'un événement personnalisé pour un changement d'abonnement consommera des [points de donnée]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Vous pouvez également utiliser des filtres de segmentation pour identifier et cibler les utilisateurs qui ne sont pas activés pour les notifications push.
{% endalert %}

Autre solution possible : nous vous recommandons de créer un événement personnalisé pour les désabonnements push en fonction du statut push activé de l'utilisateur (`true` ou `false`) afin d'assurer le suivi de cet indicateur.

{% endtab %}
{% endtabs %}

##### Comprendre les ouvertures {#understanding-opens}

Bien que les termes _ouvertures directes_ et _ouvertures influencées_ contiennent le mot « ouvertures », il s'agit en fait d'indicateurs différents. Les _ouvertures directes_ font référence à l'ouverture directe d'une notification push. Les _ouvertures influencées_ font référence à l'ouverture d'une application sans ouverture d'une notification push dans un délai spécifique après sa réception. Les _ouvertures influencées_ concernent donc les ouvertures de l'application, et non les ouvertures des notifications push.

##### Boutons d'action push et rapports {#push-action-buttons-and-reporting}

Lorsque vous ajoutez des [boutons d'action push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), le panneau **Push Performance** peut inclure les **Body Clicks**, les **Button 1 Clicks** et les **Button 2 Clicks** aux côtés d'indicateurs tels que les **Direct Opens**. Ces colonnes mesurent des interactions différentes, comparez-les donc lorsque vous interprétez l'engagement.

Les _ouvertures directes_ reflètent les indicateurs du tableau de bord pour les interactions comptabilisées comme une ouverture directe de votre message. Les événements **Push Notification Open** dans [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou Snowflake décrivent les interactions push de manière plus large et peuvent inclure des champs facultatifs tels que `button_action_type` (par exemple, `close`) et `button_string`. Pour les définitions des champs, consultez les [événements Push Notification Open]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#push-notification-open-events).

Pour **iOS**, les catégories de notification par défaut de Braze (telles que **Yes** / **No**, **Accept** / **Decline**, ou **Confirm** / **Cancel**) utilisent un appariement fixe : la première action prend en charge `OPEN_APP`, un URI ou un deep link (aligné avec le **comportement au clic** dans le compositeur). L'action complémentaire utilise `CLOSE` par défaut — elle ferme la notification et n'ouvre pas l'application. Consultez le mappage par défaut dans l'[objet bouton d'action push Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-action-button-object-for-braze-default-buttons).

De ce fait, les appuis sur le bouton prédéfini de rejet (par exemple, **No** ou **Decline**) ne comptent généralement **pas** dans les _ouvertures directes_. Ces appuis peuvent toutefois apparaître dans les exports **Push Notification Open** lorsqu'ils sont enregistrés, avec `button_action_type` défini sur `close` et `button_string` identifiant l'action appuyée. Lorsque vous comparez l'analytique de campagne aux données de l'entrepôt, utilisez ces champs de payload pour ne pas traiter les appuis de rejet de la même manière que les appuis sur le corps de la notification ou l'action principale.

Pour **Android**, vous définissez le **comportement au clic** par bouton (**Ouvrir l'application**, **Rediriger vers une URL web** ou **Deep link**), de sorte que les rapports suivent les actions que vous configurez plutôt que la répartition par défaut `OPEN_APP` / `CLOSE` d'iOS.

##### Pourquoi les envois push peuvent dépasser le nombre de destinataires uniques {#why-push-sends-can-exceed-unique-recipients}

Le nombre d'_envois_ peut dépasser le nombre de _destinataires uniques_ pour les raisons suivantes :

- **La rééligibilité est activée :** Lorsque la rééligibilité est activée dans les paramètres de votre campagne ou de votre Canvas, les utilisateurs qui répondent aux critères de segmentation et de distribution peuvent recevoir la même notification push plusieurs fois. Cela se traduit par un nombre plus élevé d'envois totaux.
- **Les utilisateurs disposent de plusieurs appareils :** Si la rééligibilité n'est pas activée, la différence peut s'expliquer par le fait que les utilisateurs ont plusieurs appareils associés à leur profil. Par exemple, un utilisateur peut avoir à la fois un smartphone et une tablette, et la notification push est envoyée à tous les appareils enregistrés. Chaque distribution compte comme un envoi, mais un seul destinataire unique est enregistré.
- **Les utilisateurs sont affectés à plusieurs applications :** Si les utilisateurs sont associés à plusieurs applications (par exemple lorsqu'ils testent une nouvelle application), ils peuvent recevoir la même notification push sur chaque application. Cela contribue à augmenter le nombre d'envois.

##### Pourquoi les rebonds se produisent {#bounced-push}

{% tabs %}
{% tab Apple Push Notification service %}

Les rebonds se produisent dans les services de notification push d'Apple (APNs) lorsqu'une notification push tente d'être distribuée à un appareil sur lequel l'application prévue n'est pas installée. Les APNs ont également le droit de modifier les jetons pour les appareils de manière arbitraire. Si vous essayez d'envoyer un message à un appareil d'utilisateur sur lequel le jeton de notification push a changé entre le moment où nous avons enregistré son jeton (c'est-à-dire au début de chaque session lorsque nous enregistrons un utilisateur pour un jeton de notification push) et le moment de l'envoi, cela provoquera un rebond.

Si un utilisateur désactive les notifications push dans les paramètres de l'appareil, lors de la prochaine ouverture de l'application, le SDK détecte que le push a été désactivé et informe Braze. À ce stade, nous mettons à jour l'état push de Activé à Désactivé. Lorsqu'un utilisateur désactivé reçoit une campagne push avant d'avoir une nouvelle session, la campagne s'envoie avec succès et apparaît comme livrée. Il n'y aura pas de rebond push pour cet utilisateur. Après une session ultérieure, lorsque vous essayez d'envoyer une notification push à l'utilisateur, Braze sait déjà si nous avons un jeton de premier plan, et donc aucune notification n'est envoyée.

Les notifications push expirant avant la livraison ne sont pas considérées comme ayant échoué et ne seront pas enregistrées comme rebond.

{% endtab %}
{% tab Firebase Cloud Messaging %}

Les rebonds Firebase Cloud Messaging (FCM) peuvent se produire dans trois cas :

| Scénario | Description |
| -- | -- |
| Applications désinstallées | Lorsqu'un message tente une livraison à un appareil et que l'application prévue est désinstallée sur cet appareil, le message est supprimé et l'ID d'enregistrement de l'appareil est invalidé. Toute future tentative d'envoi de message à l'appareil renverra une erreur NotRegistered. |
| Application sauvegardée | Lorsqu'une application est sauvegardée, son ID d'enregistrement peut cesser d'être valide avant la restauration de l'application. Dans ce cas, FCM ne conservera plus l'ID d'enregistrement de l'application et l'application ne recevra plus de messages. Ainsi, les ID d'enregistrement ne doivent **pas** être enregistrés lors de la sauvegarde d'une application. |
| Application mise à jour | Lorsqu'une application est mise à jour, l'ID d'enregistrement de la version précédente peut ne plus fonctionner. Une application mise à jour doit donc remplacer son ID d'enregistrement existant. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pourquoi les rebonds se produisent" }

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### Indicateurs SMS, MMS et RCS {#sms-mms-and-rcs-metrics}

Voici une description de certains indicateurs clés que vous pouvez voir lors de l'examen des performances de vos messages. Pour obtenir les définitions complètes de tous les indicateurs SMS, MMS et RCS, consultez le [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) et filtrez par SMS/MMS et RCS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Indicateurs SMS, MMS et RCS">
    <caption class="sr-only">Indicateurs de performance SMS, MMS et RCS</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Delivery Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Confirmed Delivery</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Rejections</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Opt-Out</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Help</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Indicateurs des webhooks {#webhook-metrics}

Voici quelques indicateurs clés des webhooks qui peuvent apparaître dans vos analyses. Pour voir les définitions complètes de tous les indicateurs webhook utilisés dans Braze, reportez-vous à notre [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Indicateurs des webhooks">
    <caption class="sr-only">Indicateurs de performance des webhooks</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Unique Recipients</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Errors</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### Indicateurs WhatsApp {#whatsapp-metrics}

Voici quelques indicateurs clés de WhatsApp qui peuvent apparaître dans vos analyses. Pour voir les définitions complètes de tous les indicateurs WhatsApp utilisés dans Braze, reportez-vous à notre [Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Indicateurs WhatsApp">
    <caption class="sr-only">Indicateurs de performance WhatsApp</caption>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Deliveries</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Reads</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### Indicateurs de blocage et de signalement par l'utilisateur final {#end-user-blocking-and-reporting-metrics}

D'autres indicateurs peuvent être consultés via le [tableau de bord du gestionnaire WhatsApp](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx), bien qu'une [confirmation de votre accès](https://www.facebook.com/business/help/218116047387456) soit nécessaire pour accéder à toutes les informations disponibles.

{% endif %}

### Performances historiques {#historical-performance}

Le panneau **Historical Performance** vous permet de visualiser les indicateurs du panneau **Message Performance** sous la forme d'un graphique dans le temps. Utilisez les filtres en haut du panneau pour modifier les statistiques et les canaux affichés dans le graphique. La plage temporelle de ce graphique reflète toujours la plage de temps spécifiée en haut de la page.

Pour obtenir une ventilation jour par jour, cliquez sur le menu hamburger <i class="fas fa-bars"></i> et sélectionnez **Download CSV** pour recevoir une exportation CSV du rapport.

![Graphique du panneau Performances historiques avec des exemples de statistiques pour un e-mail envoyé entre février 2021 et mai 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Si vous choisissez d'envoyer uniquement aux utilisateurs qui peuvent voir la dernière version de Braze des messages in-app (Génération 3), votre **audience cible** ne s'ajuste pas pour refléter votre choix.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Réponses aux mots-clés {#keyword-responses}

Le panneau **Keyword Responses** vous montre une chronologie des mots-clés entrants avec lesquels les utilisateurs ont répondu après avoir reçu votre message.

![Panneau Réponses aux mots-clés SMS/MMS/RCS au niveau de la campagne comprenant un graphique linéaire représentant la répartition des mots-clés dans le temps, ainsi qu'une section Catégories de mots-clés avec des cases à cocher pour Opt-In, Opt-Out, Help, Other, More et Coaching.]({% image_buster /assets/img/sms/keyword_responses.png %})

Ici, vous pouvez également consulter la répartition des réponses pour chaque catégorie de mots-clés afin de déterminer les prochaines étapes de [reciblage]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) et de [création de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) de manière pratique.

![Le tableau situé sous le graphique linéaire comporte des colonnes pour la catégorie de mots-clés, la répartition des réponses et le reciblage, où vous avez la possibilité de créer un segment avec la catégorie de mots-clés.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Détails de l'événement de conversion {#conversion-event-details}

Le panneau **Conversion Event Details** vous indique les performances de vos événements de conversion pour votre campagne. Pour plus d'informations, reportez-vous à la section [Événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events#step-3-view-results).

![Le panneau Détails de l'événement de conversion.]({% image_buster /assets/img/cc-conversion.png %})

### Corrélation de conversion {#conversion-correlation}

Le panneau **Conversion Correlation** vous donne des informations sur les attributs et les comportements des utilisateurs qui favorisent ou entravent les résultats que vous avez définis pour les campagnes. Pour plus d'informations, consultez la section [Corrélation de conversion]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).

![Le panneau Corrélation de conversion avec une analyse des attributs et du comportement des utilisateurs à partir de l'événement de conversion principal - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "KakaoTalk" %}

## Générateur de rapports {#report-builder}

Vous pouvez également utiliser le [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder) pour créer des rapports personnalisés pour vos campagnes KakaoTalk. Lors de la création d'un rapport, vous pouvez filtrer pour n'inclure que les campagnes KakaoTalk en sélectionnant **KakaoTalk** sous **Canaux**, ou en filtrant par les étiquettes que vous avez appliquées à vos campagnes KakaoTalk.

{% endif %}

{% if include.channel == "whatsapp" %}

### Analyses Meta {#meta-analytics}

En plus des analyses de Braze, des analyses au niveau des modèles sont accessibles dans le gestionnaire d'entreprise WhatsApp. Pour plus d'informations, consultez la [documentation de Meta](https://www.facebook.com/business/help/218116047387456).

{% endif %}

{% if include.channel == "SMS" %}

### Événements SMS Currents {#sms-currents-events}

Comme pour les e-mails, Braze reçoit des événements au niveau utilisateur liés à un message SMS à mesure qu'il effectue son parcours vers un utilisateur. Tout événement SMS entrant sera également envoyé en tant qu'événement Currents par le biais de l'événement [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events). Cela vous permet d'effectuer des actions supplémentaires ou des rapports sur les messages que vos utilisateurs envoient en dehors de la plateforme Braze.

{% alert note %}
Les messages entrants sont tronqués au-delà de 1 600 caractères.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Rapport de rétention {#retention-report}

Les rapports de rétention vous indiquent les taux auxquels vos utilisateurs ont effectué un événement de rétention sélectionné sur des périodes de temps dans une campagne spécifique{% if include.channel != "banner" %} ou Canvas{% endif %}. Pour plus d'informations, reportez-vous aux [rapports de rétention]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports).

## Rapport d'entonnoir {#funnel-report}

Le rapport d'entonnoir offre un rapport visuel qui vous permet d'analyser les parcours de vos clients après avoir reçu une campagne{% if include.channel != "banner" %} ou Canvas{% endif %}. Si votre campagne {% if include.channel != "banner" %}ou Canvas {% endif %}utilise un groupe de contrôle ou plusieurs variantes, vous pourrez comprendre l'impact des différentes variantes sur le tunnel de conversion à un niveau plus granulaire et optimiser en fonction de ces données.

Pour plus d'informations, reportez-vous aux [rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports).

{% endif %}