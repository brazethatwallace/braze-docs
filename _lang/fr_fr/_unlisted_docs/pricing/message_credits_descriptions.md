---
nav_title: Descriptions des Action Credits Braze
permalink: "/message_credits_descriptions/"
hidden: true
noindex: true
hide_toc: true
---

# Descriptions des Action Credits Braze {#braze-action-credits-descriptions}

> Les Action Credits offrent une structure flexible qui vous permet d'accéder facilement à l'envoi de messages multicanal et aux produits avancés d'intelligence artificielle tout en optimisant votre budget marketing. Commencez par interagir sur un seul canal ou une seule région, puis élargissez de façon fluide votre mix pour inclure des agents IA à mesure que votre modèle commercial, votre base de clients et vos stratégies d'engagement évoluent.

Les Action Credits peuvent être appliqués à l'ensemble des canaux et fonctionnalités présentés sur cette page.

Notez que le « ratio de crédits » référencé sur cette page correspond au nombre exact d'Action Credits nécessaires pour effectuer l'action spécifiée.

## Table des matières {#table-of-contents}

- [Détails du canal e-mail](#email-channel-details)
- [Détails des canaux SMS, MMS et RCS](#sms-mms-and-rcs-channel-details)
  - [Segments de message SMS](#sms-segments)
  - [Messages MMS](#mms-messages)
  - [Types RCS](#rcs-types)
- [Détails du canal WhatsApp](#whatsapp-channel-details)
  - [Répartition par région de facturation](#billing-region-breakdown)
- [Détails de la console d'agents](#agent-console-details)
- [Détails des canaux supplémentaires](#additional-channel-details)
  - [LINE](#line)
  - [KakaoTalk](#kakaotalk)
  - [Content Cards](#content-cards)
  - [Bannières](#banners)
  - [Audience Sync](#audience-sync)
  - [Archivage des messages](#message-archiving)
  - [Webhooks](#webhooks)

## Détails du canal e-mail {#email-channel-details}

Les ratios de crédits e-mail sont exprimés en incréments de mille e-mails envoyés (CPM) depuis la plateforme Braze.

{% alert note %}
Consultez notre [documentation sur les e-mails]({{site.baseurl}}/user_guide/channels/email) pour en savoir plus sur notre canal e-mail.
{% endalert %}

## Détails des canaux SMS, MMS et RCS {#sms-mms-and-rcs-channel-details}

Les ratios de crédits SMS et MMS sont calculés en incréments de segments de message envoyés depuis la plateforme Braze. Les ratios de crédits RCS sont calculés en incréments de types Basic et Rich Media, ou de types Single et Rich Media délivrés depuis la plateforme Braze. Les types entrants et sortants sont tous deux facturés.

{% alert note %}
Le cas échéant pour ces canaux, les frais des opérateurs sont facturés séparément (en différé) et ne sont pas pris en compte dans les Action Credits.
{% endalert %}

### Segments de message SMS {#sms-segments}

L'industrie du SMS comptabilise les messages en segments de message SMS. Un segment de message est un regroupement d'un nombre défini de caractères maximum (160 pour l'encodage GSM-7 ; 67 pour l'encodage UCS-2) qui sera envoyé en un seul envoi SMS. Si vous envoyez un SMS de 161 caractères en utilisant l'encodage GSM-7, deux (2) segments de message seront envoyés. L'envoi de plusieurs segments de message entraîne des frais supplémentaires.

### Messages MMS {#mms-messages}

Pour les MMS, la limite de message est de 5 Mo (cela inclut la ressource multimédia et la taille du corps du message). Par mesure de précaution, Braze recommande de ne pas dépasser 600 Ko pour votre ressource multimédia tout en incluant un corps de message.

### Types RCS {#rcs-types}

Le RCS est la prochaine génération du SMS et du MMS. Il offre les avantages d'un canal direct et à fort engagement comme le SMS, avec des fonctionnalités plus riches auxquelles les consommateurs modernes s'attendent, telles que du contenu enrichi (images, vidéos, documents), des envois vérifiés et brandés, des fonctionnalités interactives comme les réponses et actions suggérées, et bien plus encore.

{% multi_lang_include pricing/rcs_billing_message_types.md %}

{% alert note %}
Consultez notre [documentation SMS et MMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) pour en savoir plus sur nos offres de la famille SMS.
{% endalert %}

## Détails du canal WhatsApp {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## Répartition par région de facturation {#billing-region-breakdown}

### Amérique du Nord {#north-america}

États-Unis, Canada

### Reste de l'Afrique {#rest-of-africa}

Algérie, Angola, Bénin, Botswana, Burkina Faso, Burundi, Cameroun, Tchad, Congo, Érythrée, Éthiopie, Gabon, Gambie, Ghana, Guinée-Bissau, Côte d'Ivoire, Kenya, Lesotho, Liberia, Libye, Madagascar, Malawi, Mali, Mauritanie, Maroc, Mozambique, Namibie, Niger, Rwanda, Sénégal, Sierra Leone, Somalie, Soudan du Sud, Soudan, Eswatini, Tanzanie, Togo, Tunisie, Ouganda, Zambie

### Reste de l'Asie-Pacifique {#rest-of-asia-pacific}

Afghanistan, Australie, Bangladesh, Cambodge, Chine, Japon, Laos, Mongolie, Népal, Nouvelle-Zélande, Papouasie-Nouvelle-Guinée, Philippines, Sri Lanka, Taïwan, Tadjikistan, Thaïlande, Turkménistan, Ouzbékistan, Vietnam

### Reste de l'Europe centrale et orientale {#rest-of-central-eastern-europe}

Albanie, Arménie, Azerbaïdjan, Biélorussie, Bulgarie, Croatie, République tchèque, Géorgie, Grèce, Lettonie, Lituanie, Macédoine, Moldavie, Serbie, Slovaquie, Slovénie, Ukraine

### Reste de l'Amérique latine {#rest-of-latin-america}

Bolivie, Costa Rica, République dominicaine, Équateur, Salvador, Guatemala, Haïti, Honduras, Jamaïque, Nicaragua, Panama, Paraguay, Porto Rico, Uruguay, Venezuela

### Reste du Moyen-Orient {#rest-of-middle-east}

Bahreïn, Irak, Jordanie, Koweït, Liban, Oman, Yémen

### Reste de l'Europe occidentale {#rest-of-western-europe}

Autriche, Belgique, Danemark, Finlande, Irlande, Norvège, Portugal, Suède, Suisse

{% alert note %}
Consultez notre [documentation WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp) pour en savoir plus sur nos offres WhatsApp.
{% endalert %}

## Détails de la console Agent {#agent-console-details}

Les ratios de crédits de la console Agent sont exprimés par tranches de mille (1 000) invocations effectuées depuis la plateforme Braze. Une invocation est enregistrée lorsqu'un agent initie un appel à un LLM. Par défaut, votre contrat inclut une allocation d'invocations telle que spécifiée par votre édition de plateforme pour chaque période de votre durée d'abonnement. Les invocations supplémentaires seront facturées conformément à votre bon de commande.

{% alert note %}
Consultez notre [documentation Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) pour en savoir plus sur la console Agent.
{% endalert %}

## Détails supplémentaires par canal {#additional-channel-details}

### LINE {#line}

Les ratios de crédits LINE sont calculés par incréments de messages LINE envoyés depuis la plateforme Braze.

{% alert note %}
Consultez notre [documentation LINE]({{site.baseurl}}/user_guide/channels/line) pour en savoir plus sur l'utilisation de LINE avec Braze.
{% endalert %}

### KakaoTalk {#kakaotalk}

Les ratios de crédits KakaoTalk sont calculés par incréments de messages KakaoTalk envoyés depuis la plateforme Braze.

{% alert note %}
Consultez notre [documentation KakaoTalk]({{site.baseurl}}/kakaotalk) pour en savoir plus sur l'utilisation de KakaoTalk avec Braze.
{% endalert %}

### Content Cards {#content-cards}

Les ratios de crédits Content Cards sont calculés par incréments de mille impressions uniques quotidiennes.

Braze se réserve le droit de facturer des crédits pour les Content Cards sur la base du nombre de Content Cards envoyées si le Client ne configure pas les Content Cards pour enregistrer les impressions uniques conformément aux recommandations de Braze. Cela sera considéré comme applicable si, dans les six (6) mois suivant le premier envoi de Content Cards, le Client a :
- Envoyé plus de cinq millions (5 000 000) de Content Cards, ET SOIT
    - Zéro (0) impression enregistrée
    - Un ratio envois/impressions uniques quotidiennes supérieur à cent (100)

{% alert note %}
Consultez notre [documentation Content Cards]({{site.baseurl}}/user_guide/channels/content_cards) pour en savoir plus sur les Content Cards de Braze.
{% endalert %}

### Banners {#banners}

Les ratios de crédits Banners sont calculés par incréments de mille impressions uniques quotidiennes.

{% alert note %}
Consultez notre [documentation Banner]({{site.baseurl}}/developer_guide/banners) pour en savoir plus sur les Banners de Braze.
{% endalert %}

### Audience Sync {#audience-sync}

Les ratios de crédits Audience Sync sont calculés par incréments de mille synchronisations totales d'utilisateurs. Par défaut, votre contrat inclut cinq millions de synchronisations d'utilisateurs par période de votre durée d'abonnement. Les synchronisations d'utilisateurs supplémentaires seront facturées conformément à votre bon de commande.

{% alert note %}
Consultez notre [documentation Canvas]({{site.baseurl}}/partners/canvas_audience_sync) pour en savoir plus sur Canvas Audience Sync et les partenaires disponibles.
{% endalert %}

### Archivage des messages {#message-archiving}

Les ratios de crédits d'archivage des messages sont calculés par incréments de mille messages archivés avec succès sur les canaux notifications push, e-mail, SMS/MMS et messages in-app.

{% alert note %}
À compter du 2 septembre 2026, les tentatives d'archivage échouées sont exclues de la facturation de l'utilisation ; seuls les archivages réussis consomment des Action Credits. Ce changement n'affecte pas l'utilisation facturée avant le 2 septembre 2026.
{% endalert %}

{% alert note %}
Consultez notre [documentation sur l'archivage des messages]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving) pour en savoir plus sur l'archivage des messages.
{% endalert %}

### Webhooks {#webhooks}

Les ratios de crédits webhooks sont calculés par incréments de mille webhooks envoyés avec succès depuis la plateforme Braze. Par défaut, votre contrat inclut cent mille webhooks par période de votre durée d'abonnement. Les webhooks supplémentaires seront facturés conformément à votre bon de commande.

{% multi_lang_include pricing/webhook_failed_requests_billing.md credit_name='Action Credits' %}

{% alert note %}
Consultez notre [documentation webhooks]({{site.baseurl}}/user_guide/channels/webhooks) pour en savoir plus sur les webhooks de Braze.
{% endalert %}