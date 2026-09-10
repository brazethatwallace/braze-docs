---
nav_title: Calculateur de facturation
article_title: Calculateur de facturation
page_order: 5
description: "Cet article de référence explique ce qu'est un segment de message SMS, comment ils sont comptabilisés pour la facturation, ainsi que les points à garder à l'esprit lors de la rédaction de vos messages SMS et RCS."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# Calculateurs de facturation SMS et RCS {#sms-and-rcs-billing-calculators}

> Chez Braze, les messages SMS sont facturés par segment de message, tandis que les messages RCS sont facturés par message. Comprendre ce qui définit un segment SMS et les différents types de facturation RCS vous aidera à mieux appréhender votre facturation et à éviter les dépassements accidentels.

## Texte des messages SMS et calculateur de segments {#sms-message-copy-and-segment-calculator}

Les messages SMS sont facturés par segment de message. Comprendre comment les messages SMS sont découpés est essentiel pour maîtriser votre facturation.

### Qu'est-ce qu'un segment de message SMS ? {#what-is-an-sms-segment}

Le Short Messaging Service (SMS) est un protocole de communication standardisé qui permet aux appareils d'envoyer et de recevoir de courts messages texte. Il a été conçu pour « s'insérer entre » d'autres protocoles de signalisation, ce qui explique pourquoi la longueur des messages SMS est limitée à 160 caractères sur 7 bits, soit 1 120 bits ou 140 octets. Les segments de message SMS sont les lots de caractères que les opérateurs utilisent pour mesurer les messages texte. Les messages étant facturés par segment, les clients qui utilisent les SMS ont tout intérêt à bien comprendre les subtilités du découpage des messages.

Lorsque vous créez une Campaign SMS ou un Canvas avec Braze, les messages que vous composez dans l'éditeur sont représentatifs de ce que vos utilisateurs verront à la réception sur leur téléphone, mais **ne reflètent pas la manière dont votre message sera découpé en segments ni, en fin de compte, la façon dont vous serez facturé**. Comprendre le nombre de segments qui seront envoyés et anticiper les éventuels dépassements relève de votre responsabilité, mais nous mettons à votre disposition des ressources pour vous faciliter la tâche. Consultez notre [calculateur de segments](#segment-calculator) intégré.

![Lorsque vous créez une Campaign SMS ou un Canvas avec Braze, les messages composés dans l'éditeur sont représentatifs de ce que verront vos utilisateurs, mais ne reflètent pas le découpage en segments ni la facturation. Consultez le calculateur de segments intégré.]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Détail du découpage en segments {#segment-breakdown}

La limite de caractères pour **un segment SMS autonome** est de 160 caractères (encodage [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)) ou 70 caractères (encodage [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)) selon le type d'encodage. Cependant, la plupart des téléphones et réseaux prennent en charge la concaténation, ce qui permet des messages SMS plus longs, jusqu'à 1 530 caractères (GSM-7) ou 670 caractères (UCS-2). Ainsi, même si un message peut comporter plusieurs segments, tant qu'il ne dépasse pas ces limites de concaténation, il sera affiché comme un seul message et rapporté en tant que tel.

Il est important de noter que **dès que vous dépassez la limite de caractères de votre premier segment, les caractères supplémentaires entraînent le découpage de l'ensemble de votre message en segments basés sur de nouvelles limites de caractères** :
- **Encodage GSM-7**
    - Les messages dépassant la limite de 160 caractères seront désormais découpés en segments de 153 caractères et envoyés individuellement, puis reconstitués par l'appareil du destinataire. Par exemple, un message de 161 caractères sera envoyé en deux messages : l'un de 153 caractères et le second de 8 caractères.
- **Encodage UCS-2**
    - Si vous incluez des caractères non GSM tels que des emojis, des idéogrammes chinois, coréens ou japonais dans vos messages SMS, ceux-ci doivent être envoyés en encodage UCS-2. Les messages dépassant la limite initiale de 70 caractères seront concaténés en segments de 67 caractères. Par exemple, un message de 71 caractères sera envoyé en deux messages : l'un de 67 caractères et le second de 4 caractères.

Quel que soit le type d'encodage, chaque message SMS envoyé par Braze est limité à 10 segments maximum et est compatible avec les [modèles Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid), le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), les emojis et les liens.

{% tabs %}
{% tab Encodage GSM-7 %}
| Nombre de caractères | Nombre de segments |
| -------------------- | ----------------- |
| 0 - 160 caractères | 1 segment |
| 161 - 306 caractères | 2 segments |
| 307 - 459 caractères | 3 segments |
| 460 - 612 caractères | 4 segments |
| 613 - 765 caractères | 5 segments |
| 766 - 918 caractères | 6 segments |
| 919 - 1071 caractères | 7 segments |
| 1072 - 1224 caractères | 8 segments |
| 1225 - 1377 caractères | 9 segments |
| 1378 - 1530 caractères | 10 segments |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détail du découpage en segments" }
{% endtab %}
{% tab Encodage UCS-2 %}
| Nombre de caractères | Nombre de segments |
| -------------------- | ----------------- |
| 0 - 70 caractères | 1 segment |
| 71 - 134 caractères | 2 segments |
| 135 - 201 caractères | 3 segments |
| 202 - 268 caractères | 4 segments |
| 269 - 335 caractères | 5 segments |
| 336 - 402 caractères | 6 segments |
| 403 - 469 caractères | 7 segments |
| 470 - 536 caractères | 8 segments |
| 537 - 603 caractères | 9 segments |
| 604 - 670 caractères | 10 segments |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détail du découpage en segments" }
{% endtab %}
{% endtabs %}

### Points à garder à l'esprit lors de la rédaction de vos messages {#things-to-keep-in-mind-as-you-create-your-copy}

- **Limite de caractères par segment**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) impose une limite de 160 caractères pour un segment SMS unique. Pour les messages de plus de 160 caractères, tous les messages seront découpés en segments de 153 caractères.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) impose une limite de 70 caractères par segment de message. Pour les messages de plus de 70 caractères, tous les messages seront découpés en segments de 67 caractères.<br><br>
- **Limite de segments par message**
    - Il existe un nombre maximum de segments que vous pouvez envoyer en raison des limitations du protocole. Un seul message SMS Braze ne peut pas dépasser **10 segments**.
    - Ces 10 segments sont limités à 1 530 caractères (encodage GSM-7) ou 670 caractères (encodage UCS-2).<br><br>
- **Compatibilité avec les modèles Liquid, le contenu connecté, les emojis et les liens**
    - Les modèles Liquid et le contenu connecté peuvent faire dépasser la limite de caractères correspondant à votre type d'encodage. Vous pouvez utiliser le [filtre truncatewords](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) pour limiter le nombre de mots que Liquid peut ajouter à votre message.
    - Les emojis n'ont pas un nombre de caractères standard d'un emoji à l'autre : assurez-vous donc de tester que vos messages sont correctement découpés en segments et s'affichent comme prévu.
    - Les liens peuvent consommer de nombreux caractères, entraînant un nombre de segments supérieur à celui attendu. Bien que l'utilisation de raccourcisseurs de liens soit possible, ils fonctionnent mieux avec les codes courts. Consultez notre [FAQ SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs) pour plus d'informations.<br><br>
- **Tests**
    - Testez toujours vos messages SMS avant le lancement, en particulier lorsque vous utilisez Liquid et le contenu connecté, car le dépassement des limites de message ou de texte peut entraîner des frais supplémentaires. Notez que les messages de test sont décomptés de vos limites de messages.<br><br>
- **Messages de réponse automatique**
    - Les messages de réponse automatique envoyés par Braze, tels que les confirmations de double abonnement et les réponses au mot-clé HELP, sont des envois SMS qui comptent comme des segments facturables. Le nombre de segments facturables dépend de la longueur du texte et de l'encodage des caractères.

### Calculateur de segments SMS {#segment-calculator}
---

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

## Facturation des messages RCS {#rcs-message-billing}

Les messages RCS sont facturés en fonction de leur contenu et du pays dans lequel le message est envoyé. Pour estimer précisément les coûts, il est essentiel de comprendre les différents types de messages et leur mode de facturation.

### Types de facturation RCS {#rcs-billing-types}

Notre plateforme prend en charge deux modèles de facturation principaux : un modèle global et un modèle pour les États-Unis.

#### Modèle global (marchés hors États-Unis) {#global-model-non-us-markets}

Les messages sont facturés par message et classés comme Basic ou Single.

{% tabs local %}
{% tab Basic %}

Les messages RCS Basic sont des messages texte uniquement de 160 caractères maximum et sont facturés comme un seul message.

{% alert note %}
L'ajout de boutons ou de tout élément enrichi modifie le type de message en message RCS Single.
{% endalert %}

{% endtab %}
{% tab Single %}

Les messages RCS Single sont des messages de plus de 160 caractères OU incluant des éléments enrichis tels que des boutons ou des médias. Ils sont facturés comme un seul message, quelle que soit la longueur du message.

{% alert note %}
L'envoi d'un message texte et d'un fichier média séparé est toujours facturé comme deux messages distincts.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Modèle États-Unis {#united-states-model}

Les messages sont classés en deux catégories : Rich ou Rich Media.

{% tabs local %}
{% tab Rich messages %}

Les messages Rich sont des messages texte uniquement, avec ou sans boutons. Ils sont facturés par segment de message, chaque segment étant limité à 160 octets UTF-8, ce qui signifie que **le nombre de caractères par segment n'est pas fixe**. Un message contenant uniquement 160 caractères en anglais simple constitue un segment, mais un message avec un texte plus long et des emojis peut correspondre à plusieurs segments.

{% endtab %}
{% tab Rich media messages %}

Les messages Rich media incluent les messages **Media** autonomes et les messages **Card**, et sont facturés comme un seul message. Pour les dispositions de Card et les limites spécifiques aux fournisseurs, consultez [Types de messages RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create#rcs-message-types).

{% endtab %}
{% endtabs %}

### Compositeur de messages et tableau de bord Credits Usage {#message-composer-and-credits-usage-dashboard}

Lorsque vous créez votre message, le compositeur affiche le type de facturation en temps réel via un libellé (Basic RCS, Single RCS, Rich ou Rich Media), ce qui vous aide à suivre les coûts avant l'envoi.

Votre [tableau de bord Credits Usage]({{site.baseurl}}/credits_usage_dashboard) reflète ces types de facturation et indique le nombre de segments utilisés pour les messages envoyés aux États-Unis, vous offrant une vue transparente de votre consommation de crédits de messages.