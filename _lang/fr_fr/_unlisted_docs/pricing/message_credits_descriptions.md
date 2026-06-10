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

- [Descriptions des Action Credits Braze](#braze-action-credits-descriptions)
  - [Détails du canal e-mail](#email-channel-details)
  - [Détails des canaux SMS, MMS et RCS](#sms-mms-and-rcs-channel-details)
    - [Segments SMS](#sms-segments)
    - [Messages MMS](#mms-messages)
    - [Types RCS](#rcs-types)
  - [Détails du canal WhatsApp](#whatsapp-channel-details)
    - [Répartition par région de facturation](#billing-region-breakdown)
  - [Détails de la Console des agents](#agent-console-details)
  - [Détails des canaux supplémentaires](#additional-channel-details)
    - [LINE](#line)
    - [KakaoTalk](#kakaotalk)
    - [Content Cards](#content-cards)
    - [Bannières](#banners)
    - [Audience Sync](#audience-sync)
    - [Archivage des messages](#message-archiving)
    - [Webhooks](#webhooks)

## Détails du canal e-mail {#email-channel-details}

Les ratios de crédits pour les e-mails sont exprimés par tranches de mille e-mails envoyés (CPM) depuis la plateforme Braze.

{% alert note %}
Consultez notre [documentation sur les e-mails](https://www.braze.com/docs/user_guide/message_building_by_channel/email) pour en savoir plus sur notre canal e-mail.
{% endalert %}

## Détails des canaux SMS, MMS et RCS {#sms-mms-and-rcs-channel-details}

Les ratios de crédits SMS et MMS sont exprimés par tranches de segments entrants ou sortants envoyés depuis la plateforme Braze. Les ratios de crédits RCS sont exprimés par tranches de types Basic ou Single envoyés depuis la plateforme Braze.

{% alert note %}
Le cas échéant pour ces canaux, les frais d'opérateur sont facturés séparément (à terme échu) et ne sont pas pris en compte dans les Action Credits.
{% endalert %}

### Segments SMS {#sms-segments}

L'industrie du SMS comptabilise les messages en segments de message SMS. Un segment de message est un regroupement pouvant contenir jusqu'à un nombre défini de caractères (160 pour l'encodage GSM-7 ; 67 pour l'encodage UCS-2) qui sera envoyé en un seul envoi SMS. Si vous envoyez un SMS de 161 caractères en utilisant l'encodage GSM-7, deux (2) segments de message seront envoyés. L'envoi de plusieurs segments de message entraînera des frais supplémentaires.

### Messages MMS {#mms-messages}

Pour les MMS, la limite de taille du message est de 5 Mo (cela inclut la ressource multimédia et la taille du corps du message). Par mesure de précaution, Braze recommande de ne pas dépasser 600 Ko pour votre ressource multimédia tout en incluant un corps de message.

### Types RCS {#rcs-types}

Le RCS est la prochaine génération du SMS et du MMS. Il offre les avantages d'un canal direct à fort engagement comme le SMS, avec des fonctionnalités plus riches auxquelles les consommateurs modernes s'attendent, telles que du contenu enrichi (images, vidéos, documents), un envoi vérifié et brandé, des fonctionnalités interactives comme les réponses et actions suggérées, et bien plus encore.

- La facturation RCS repose sur deux types de messages différents (avec des distinctions pour les États-Unis) :
    - **RCS Basic :** Texte uniquement, jusqu'à 160 caractères
    - **RCS Single :** Messages contenant du contenu enrichi, ou messages texte uniquement de plus de 160 caractères
    - **RCS Rich (États-Unis uniquement) :** Texte uniquement, peut inclure des suggestions/boutons limités (quickReply, dialPhone, openURL sans webview), segmenté par tranches de 160 octets UTF-8
    - **RCS Rich Media (États-Unis uniquement) :** Tout média OU texte avec des suggestions/boutons plus riches (webview, localisation, calendrier, etc.), comptabilisé comme un seul message

{% alert note %}
Consultez notre [documentation SMS et MMS](https://www.braze.com/docs/user_guide/message_building_by_channel/sms) pour en savoir plus sur nos offres de la famille SMS.
{% endalert %}

## Détails du canal WhatsApp {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

### Répartition par région de facturation {#billing-region-breakdown}

#### Amérique du Nord {#north-america}

États-Unis, Canada

#### Reste de l'Afrique {#rest-of-africa}

Algérie, Angola, Bénin, Botswana, Burkina Faso, Burundi, Cameroun, Tchad, Congo, Érythrée, Éthiopie, Gabon, Gambie, Ghana, Guinée-Bissau, Côte d'Ivoire, Kenya, Lesotho, Liberia, Libye, Madagascar, Malawi, Mali, Mauritanie, Maroc, Mozambique, Namibie, Niger, Rwanda, Sénégal, Sierra Leone, Somalie, Soudan du Sud, Soudan, Eswatini, Tanzanie, Togo, Tunisie, Ouganda, Zambie

#### Reste de l'Asie-Pacifique {#rest-of-asia-pacific}

Afghanistan, Australie, Bangladesh, Cambodge, Chine, Hong Kong, Japon, Laos, Mongolie, Népal, Nouvelle-Zélande, Papouasie-Nouvelle-Guinée, Philippines, Singapour, Sri Lanka, Taïwan, Tadjikistan, Thaïlande, Turkménistan, Ouzbékistan, Vietnam

#### Reste de l'Europe centrale et orientale {#rest-of-central-eastern-europe}

Albanie, Arménie, Azerbaïdjan, Biélorussie, Bulgarie, Croatie, République tchèque, Géorgie, Grèce, Hongrie, Lettonie, Lituanie, Macédoine, Moldavie, Pologne, Roumanie, Serbie, Slovaquie, Slovénie, Ukraine

#### Reste de l'Amérique latine {#rest-of-latin-america}

Bolivie, Costa Rica, République dominicaine, Équateur, El Salvador, Guatemala, Haïti, Honduras, Jamaïque, Nicaragua, Panama, Paraguay, Porto Rico, Uruguay, Venezuela

#### Reste du Moyen-Orient {#rest-of-middle-east}

Bahreïn, Irak, Jordanie, Koweït, Liban, Oman, Qatar, Yémen

#### Reste de l'Europe occidentale {#rest-of-western-europe}

Autriche, Belgique, Danemark, Finlande, Irlande, Norvège, Portugal, Suède, Suisse

{% alert note %}
Consultez notre [documentation WhatsApp](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp) pour en savoir plus sur nos offres WhatsApp.
{% endalert %}

## Détails de la Console des agents {#agent-console-details}

Les ratios de crédits de la Console des agents sont exprimés par tranches de mille (1 000) invocations effectuées depuis la plateforme Braze. Une invocation est enregistrée lorsqu'un agent initie un appel vers un LLM. Par défaut, votre contrat inclut une allocation d'invocations telle que spécifiée par votre édition de plateforme pour chaque période de votre durée d'abonnement. Les invocations supplémentaires seront facturées conformément à votre bon de commande.

{% alert note %}
Consultez notre [documentation Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents) pour en savoir plus sur la Console des agents.
{% endalert %}

## Détails des canaux supplémentaires {#additional-channel-details}

### LINE {#line}

Les ratios de crédits LINE sont exprimés par tranches de messages LINE envoyés depuis la plateforme Braze.

{% alert note %}
Consultez notre [documentation LINE](https://www.braze.com/docs/user_guide/message_building_by_channel/line) pour en savoir plus sur l'utilisation de LINE avec Braze.
{% endalert %}

### KakaoTalk {#kakaotalk}

Les ratios de crédits KakaoTalk sont exprimés par tranches de messages KakaoTalk envoyés depuis la plateforme Braze.

{% alert note %}
Consultez notre [documentation KakaoTalk](https://braze.com/docs/kakaotalk/) pour en savoir plus sur l'utilisation de KakaoTalk avec Braze.
{% endalert %}

### Content Cards {#content-cards}

Les ratios de crédits Content Cards sont exprimés par tranches de mille impressions uniques quotidiennes.

Braze se réserve le droit de facturer des crédits pour les Content Cards en fonction du nombre de Content Cards envoyées si le client ne configure pas les Content Cards pour enregistrer les impressions uniques conformément aux recommandations de Braze. Cela sera considéré comme applicable si, dans les six (6) mois suivant le premier envoi de Content Cards, le client a :
- Envoyé plus de cinq millions (5 000 000) de Content Cards, ET SOIT
    - Zéro (0) impression enregistrée
    - Un ratio envois/impressions uniques quotidiennes supérieur à cent (100)

{% alert note %}
Consultez notre [documentation Content Cards](https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards) pour en savoir plus sur les Content Cards de Braze.
{% endalert %}

### Bannières {#banners}

Les ratios de crédits des bannières sont exprimés par tranches de mille impressions uniques quotidiennes.

{% alert note %}
Consultez notre [documentation sur les bannières](https://braze.com/docs/developer_guide/banner_cards) pour en savoir plus sur les bannières Braze.
{% endalert %}

### Audience Sync {#audience-sync}

Les ratios de crédits Audience Sync sont exprimés par tranches de mille synchronisations totales d'utilisateurs. Par défaut, votre contrat inclut cinq millions de synchronisations d'utilisateurs pour chaque période de votre durée d'abonnement. Les synchronisations d'utilisateurs supplémentaires seront facturées conformément à votre bon de commande.

{% alert note %}
Consultez notre [documentation Canvas](https://www.braze.com/docs/partners/canvas_steps) pour en savoir plus sur Canvas Audience Sync et les partenaires disponibles.
{% endalert %}

### Archivage des messages {#message-archiving}

Les ratios de crédits de l'archivage des messages sont exprimés par tranches de mille messages archivés sur les canaux push, e-mail et SMS/MMS.

{% alert note %}
Consultez notre [documentation sur l'archivage des messages](https://www.braze.com/docs/user_guide/data/export_braze_data/message_archiving#message-archiving) pour en savoir plus sur l'archivage des messages.
{% endalert %}

### Webhooks {#webhooks}

Les ratios de crédits des webhooks sont exprimés par tranches de mille webhooks envoyés depuis la plateforme Braze. Par défaut, votre contrat inclut cent mille webhooks pour chaque période de votre durée d'abonnement. Les webhooks supplémentaires seront facturés conformément à votre bon de commande.

{% alert note %}
Consultez notre [documentation sur les webhooks](https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks) pour en savoir plus sur les webhooks Braze.
{% endalert %}