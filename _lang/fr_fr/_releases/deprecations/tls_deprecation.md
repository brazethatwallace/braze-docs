---
nav_title: Désactivation de TLS 1.0 et 1.1
page_order: 2

page_type: update
description: "Cet article décrit l'obsolescence de TLS 1.0 et TLS 1.1 chez Braze, achevée en mai 2018."
---
# Désactivation de TLS 1.0 et 1.1 {#tls-10-11-deprecation}

{% alert update %}
Braze a cessé sa prise en charge des chiffrements TLS (Transport Layer Security) dans les versions TLS 1.0 et 1.1, conformément aux recommandations du PCI Security Standards Council. Nous avons effectué cette désactivation en deux phases, achevées en mai 2018.
{% endalert %}

## Contexte {#background}

Braze désactive les chiffrements TLS (Transport Layer Security) réputés faibles dans les versions TLS 1.0 et 1.1, conformément aux recommandations du PCI Security Standards Council, en deux phases qui se sont terminées en mai 2018.

Ce changement n'est pas une réponse à une violation ou à un problème lié à la plateforme de Braze, mais une mesure de précaution visant à maintenir nos normes de sécurité et de données de premier ordre, et à protéger de façon proactive nos clients ainsi que leurs consommateurs.

Ces dernières années, un certain nombre de problèmes de sécurité systématiques associés à la fois à TLS et à son prédécesseur, Secure Sockets Layer (SSL), notamment [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A), [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed), [LOGJAM](https://en.wikipedia.org/wiki/Logjam_(computer_security)) et d'autres, ont menacé le trafic web chiffré et exposé certaines parties d'internet à des failles de sécurité. Comme d'autres entreprises technologiques, Braze a déjà pris des mesures pour désactiver les protocoles et chiffrements faibles au fur et à mesure de la découverte d'attaques — par exemple en supprimant la prise en charge de SSLv3 en 2014.

Plus récemment, le PCI Security Standards Council a publié en avril 2015 des orientations relatives au chiffrement pour la [norme de sécurité des données de l'industrie des cartes de paiement](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (PCI-DSS). Ces directives excluent SSL 3.0, TLS 1.0 et certaines suites de chiffrement prises en charge par TLS 1.1 de leur liste de protocoles de chiffrement cryptographique robuste, et encouragent les entreprises à cesser de prendre en charge ces protocoles ou chiffrements afin de garantir la sécurité des utilisateurs d'internet.

Une suite de chiffrement est une combinaison d'algorithmes qui assurent le chiffrement, l'authentification et l'intégrité des communications lors de la négociation d'une connexion SSL ou TLS sécurisée. Lorsqu'il est découvert qu'un chiffrement donné peut être cassé — qu'il existe ou non des attaques connues à ce jour — ce chiffrement est considéré comme présentant des « faiblesses » susceptibles de permettre de futures attaques. En excluant ces chiffrements TLS des exigences de conformité PCI DSS, le PCI DSS Council exige des fournisseurs de services qu'ils prennent en charge uniquement les normes de chiffrement les plus robustes. Le PCI DSS Council a fixé au 30 juin 2018 la date limite de conformité à l'exigence de chiffrement imposant la désactivation de TLS 1.0 et TLS 1.1.

## Plan d'obsolescence de Braze {#brazes-deprecation-plan}
Afin de se conformer aux recommandations du PCI DSS Council, Braze relèvera les versions minimales de TLS prises en charge sur nos services. Pour vous donner une meilleure idée de notre plan de conformité et de son impact potentiel sur votre marque et vos utilisateurs, notre plan comporte deux phases principales :

### Phase 1 : 1er octobre 2017 {#phase-1-october-1-2017}

Braze supprimera la possibilité d'utiliser les chiffrements suivants sur le tableau de bord web de Braze et les REST API :

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`
- `TLS_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

Ce changement ne devrait pas affecter les clients accédant au tableau de bord de Braze, car tous les navigateurs web modernes prennent en charge des chiffrements plus sécurisés. Cependant, si vous rencontrez une erreur de chiffrement SSL en accédant au tableau de bord web après le 1er octobre, vous pourrez résoudre le problème simplement en installant la dernière version de votre navigateur web.

Votre équipe d'ingénierie doit s'assurer qu'elle n'utilise aucun de ces chiffrements pour les communications serveur à serveur avec les REST API de Braze. Si c'est le cas, elle devra mettre à jour son code pour utiliser des chiffrements plus sécurisés avant le 1er octobre afin de pouvoir continuer à utiliser les API de Braze. Toutefois, pour maintenir la prise en charge des appareils mobiles anciens et obsolètes susceptibles d'utiliser des chiffrements faibles, Braze continuera à prendre en charge ces chiffrements sur les API qui reçoivent des données de nos SDK.

### Phase 2 : 31 mai 2018 {#phase-2-may-31-2018}

Braze désactivera la prise en charge de TLS 1.0 et TLS 1.1 sur l'ensemble des services Braze le 31 mai 2018, y compris le tableau de bord de Braze, les REST API et les API qui communiquent avec nos SDK. Nous supprimerons également la prise en charge des chiffrements répertoriés dans la section précédente pour les API qui reçoivent des données SDK. Cela signifie que toutes les communications TLS 1.0 et 1.1 vers et depuis Braze ne seront plus prises en charge par notre réseau à compter de cette date.

À la suite de ce changement, certains appareils mobiles anciens ou obsolètes — probablement ceux exécutant des versions anciennes d'Android — pourraient perdre la capacité de communiquer avec Braze, les empêchant d'envoyer des données à Braze ou de recevoir des messages in-app de Braze. Cependant, nous prévoyons que ce changement n'affectera qu'un petit nombre d'appareils. Tous les appareils concernés perdront également la capacité de communiquer avec tout site web ou service conforme à la norme PCI un mois plus tard, le 30 juin 2018, date fixée par le PCI DSS Council pour la suppression des chiffrements TLS 1.0 et TLS 1.1.

## Plan d'action {#action-plan}
Si votre marque utilise les REST API de Braze, adressez-vous à votre équipe d'ingénierie pour vous assurer que tous les appels serveur à serveur vers Braze utilisent TLS 1.2 avant la date indiquée, afin d'éviter toute interruption de service. Sachez que certains langages de programmation, comme Java 7, utilisent par défaut des versions plus anciennes de TLS, et votre équipe d'ingénierie devra peut-être apporter des modifications au code pour se conformer aux nouvelles exigences de chiffrement.

Les appareils Apple ne seront pas affectés par l'obsolescence prévue par Braze, car Apple exige TLS 1.2 depuis fin 2016. Il en va de même pour les navigateurs web modernes, et nous ne prévoyons donc pas que ces changements auront un impact sur l'utilisation du SDK Web. Cependant, les appareils Android exécutant Android 4.4 (KitKat) ou une version antérieure peuvent ne pas utiliser TLS 1.2 par défaut. Prenez donc des mesures pour mettre à niveau vos intégrations Android vers au moins la version 2.0.3 du SDK Braze (qui utilise TLS 1.2 par défaut, si l'appareil concerné peut le prendre en charge) avant le 31 mai 2018.

Enfin, en raison des faiblesses connues de TLS 1.0 et de la suite de chiffrement TLS 1.1, il est possible que des attaques surviennent à l'avenir, ce qui obligerait Braze à accélérer son plan d'obsolescence afin de garantir la sécurité de tous nos clients. Braze surveillera l'état de la sécurité et toutes les attaques pertinentes liées aux protocoles TLS 1.0 et 1.1, et vous tiendra informé si des attaques venaient à modifier le calendrier présenté dans les sections précédentes. Mais en raison de cet impact potentiel, nous vous recommandons vivement de travailler avec votre équipe d'ingénierie pour vous assurer que vos appels API vers Braze sont sécurisés avec TLS 1.2, et de prévoir une mise à niveau vers le dernier SDK Android dans les prochains mois.