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

## Texte des SMS et calculateur de segments {#sms-message-copy-and-segment-calculator}

Les SMS sont facturés par segment de message. Comprendre comment les messages SMS sont découpés est essentiel pour maîtriser votre facturation.

### Qu'est-ce qu'un segment de SMS ? {#what-is-an-sms-segment}

Le Short Messaging Service (SMS) est un protocole de communication standardisé qui permet aux appareils d'envoyer et de recevoir des messages texte courts. Il a été conçu pour « s'intercaler » entre d'autres protocoles de signalisation, c'est pourquoi la longueur d'un SMS est limitée à 160 caractères de 7 bits, soit 1120 bits ou 140 octets. Les segments de message SMS sont les lots de caractères utilisés par les opérateurs téléphoniques pour mesurer les messages texte. Les messages sont facturés par segment de message, de sorte que les clients utilisant les SMS tirent un grand avantage à comprendre les subtilités du découpage des messages.

Lorsque vous créez une Campaign ou un Canvas SMS avec Braze, les messages que vous rédigez dans le compositeur représentent ce que vos utilisateurs pourraient voir lorsque le message est livré sur leur téléphone, mais **cela n'indique pas comment votre message sera découpé en segments, ni comment vous serez finalement facturé**. Comprendre combien de segments seront envoyés et anticiper les éventuels dépassements relève de votre responsabilité, mais nous mettons à votre disposition des ressources pour vous faciliter la tâche. Consultez notre [calculateur de segments](#segment-calculator) intégré.

![Lorsque vous créez une Campaign ou un Canvas SMS avec Braze, les messages rédigés dans le compositeur représentent ce que vos utilisateurs verront, mais pas la façon dont votre message sera découpé en segments ni la facturation associée. Consultez notre calculateur de segments intégré.]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Détail des segments {#segment-breakdown}

La limite de caractères pour **un segment SMS autonome** est de 160 caractères (encodage [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)) ou 70 caractères (encodage [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)) selon le type d'encodage. Cependant, la plupart des téléphones et réseaux prennent en charge la concaténation, permettant l'envoi de SMS plus longs pouvant atteindre 1530 caractères (GSM-7) ou 670 caractères (UCS-2). Ainsi, bien qu'un message puisse contenir plusieurs segments, s'il ne dépasse pas ces limites de concaténation, il sera affiché comme un seul message et signalé comme tel.

Il est important de noter que **lorsque vous dépassez la limite de caractères de votre premier segment, les caractères supplémentaires entraînent le découpage de l'intégralité de votre message en segments basés sur de nouvelles limites de caractères** :
- **Encodage GSM-7**
    - Les messages dépassant la limite de 160 caractères seront découpés en segments de 153 caractères et envoyés individuellement, puis reconstitués par l'appareil du destinataire. Par exemple, un message de 161 caractères sera envoyé sous forme de deux messages, l'un de 153 caractères et le second de 8 caractères.
- **Encodage UCS-2**
    - Si vous incluez des caractères non GSM tels que des emojis, des caractères chinois, coréens ou japonais dans vos SMS, ces messages devront être envoyés via l'encodage UCS-2. Les messages dépassant la limite initiale de 70 caractères seront concaténés en segments de 67 caractères. Par exemple, un message de 71 caractères sera envoyé sous forme de deux messages, l'un de 67 caractères et le second de 4 caractères.

Quel que soit le type d'encodage, chaque SMS envoyé par Braze est limité à 10 segments maximum et est compatible avec le [templating Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid), le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), les emojis et les liens.

{% tabs %}
{% tab Encodage GSM-7 %}
| Nombre de caractères | Combien de segments ? |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détail des segments" }
{% endtab %}
{% tab Encodage UCS-2 %}
| Nombre de caractères | Combien de segments ? |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détail des segments" }
{% endtab %}
{% endtabs %}

### Points à garder à l'esprit lors de la rédaction de vos messages {#things-to-keep-in-mind-as-you-create-your-copy}

- **Limite de caractères par segment**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) impose une limite de 160 caractères pour un segment SMS unique. Pour les messages dépassant 160 caractères, tous les messages seront découpés avec une limite de 153 caractères.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) impose une limite de 70 caractères par segment de message. Pour les messages dépassant 70 caractères, tous les messages seront découpés avec une limite de 67 caractères.<br><br>
- **Limite de segments par message**
    - Il existe un nombre maximum de segments que vous pouvez envoyer en raison des limitations du support. Un seul SMS Braze ne peut pas dépasser **10 segments** de messages.
    - Ces 10 segments sont limités à 1530 caractères (encodage GSM-7) ou 670 caractères (encodage UCS-2).<br><br>
- **Compatibilité avec le templating Liquid, le contenu connecté, les emojis et les liens**
    - Le templating Liquid et le contenu connecté peuvent faire dépasser la limite de caractères de votre type d'encodage. Vous pouvez utiliser le [filtre truncate words](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) pour limiter le nombre de mots que Liquid peut ajouter au message.
    - Les emojis n'ont pas un nombre de caractères standardisé pour l'ensemble des emojis, alors assurez-vous de tester que vos messages sont correctement segmentés et affichés.
    - Les liens peuvent utiliser de nombreux caractères, ce qui entraîne plus de segments de message que prévu. Bien que l'utilisation de raccourcisseurs de liens soit possible, ils sont à privilégier avec les codes courts. Consultez notre [FAQ SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs) pour plus d'informations.<br><br>
- **Tests**
    - Testez toujours vos SMS avant le lancement, en particulier lorsque vous utilisez Liquid et le contenu connecté, car le dépassement des limites de message ou de texte peut entraîner des frais supplémentaires. Notez que les messages de test comptent dans vos limites de messages.<br><br>
- **Messages de réponse automatique**
    - Les messages de réponse automatique envoyés par Braze, tels que les confirmations de double abonnement et les réponses aux mots-clés HELP, sont des envois SMS qui comptent dans les segments facturables. Le nombre de segments facturables dépend de la longueur du texte et de l'encodage des caractères.

### Calculateur de segments SMS {#segment-calculator}
---

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

## Facturation des messages RCS {#rcs-message-billing}

Les messages RCS sont facturés en fonction de leur contenu et du pays dans lequel le message est distribué. Pour estimer les coûts avec précision, il est essentiel de comprendre les différents types de messages et la manière dont ils sont facturés.

### Types de facturation RCS {#rcs-billing-types}

Notre plateforme prend en charge deux modèles de facturation principaux : un modèle mondial et un modèle pour les États-Unis.

#### Modèle mondial (marchés hors États-Unis) {#global-model-non-us-markets}

Les messages sont facturés par message et classés comme Basic ou Single.

{% tabs local %}
{% tab Basic %}

Les messages RCS Basic sont des messages texte uniquement de 160 caractères maximum et sont facturés comme un seul message.

{% alert note %}
L'ajout de boutons ou de tout élément enrichi changera le type de message en message RCS Single.
{% endalert %}

{% endtab %}
{% tab Single %}

Les messages RCS Single sont des messages de plus de 160 caractères OU incluant des éléments enrichis tels que des boutons ou des médias. Ils sont facturés comme un seul message, quelle que soit la longueur du message.

{% alert note %}
L'envoi d'un message texte et d'un fichier multimédia distinct est toujours facturé comme deux messages distincts.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Modèle États-Unis {#united-states-model}

Les messages sont classés comme Rich ou Rich Media.

{% tabs local %}
{% tab Rich messages %}

Les messages Rich sont des messages texte uniquement, avec ou sans boutons. Ils sont facturés par segment de message, chaque segment étant limité à 160 octets UTF-8, ce qui signifie que **le nombre de caractères par segment n'est pas fixe**. Un message contenant uniquement 160 caractères en anglais standard constitue un seul segment, mais un message avec un texte plus long et des émojis peut représenter plusieurs segments.

{% endtab %}
{% tab Rich media messages %}

Les messages Rich media incluent un fichier multimédia (image, vidéo) ou une Rich Card et sont facturés comme un seul message.

{% endtab %}
{% endtabs %}

### Éditeur de message et tableau de bord d'utilisation des crédits {#message-composer-and-credits-usage-dashboard}

Lorsque vous créez votre message, l'éditeur de message affiche le type de facturation en temps réel via un libellé (Basic RCS, Single RCS, Rich ou Rich Media), vous permettant de suivre les coûts avant l'envoi.

Votre [tableau de bord d'utilisation des crédits]({{site.baseurl}}/credits_usage_dashboard) reflète ces types de facturation et fournit le nombre de segments utilisés pour les messages aux États-Unis, vous offrant une vue transparente de votre consommation de crédits de messages.