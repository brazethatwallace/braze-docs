---
nav_title: septembre
page_order: 3
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2021."
---

# Septembre 2021 {#september-2021}

## iOS 15

### Protection de la confidentialité dans Apple Mail {#apple-mail-privacy-protection}

La protection de la confidentialité dans Mail (MPP) d'Apple est une mise à jour de confidentialité qui sera disponible mi-septembre pour les utilisateurs de l'application Apple Mail sur iOS 15, iPadOS 15, macOS Monterey et watchOS 8. Pour les utilisateurs qui s'abonnent à la protection de la confidentialité dans Mail, les e-mails seront désormais préchargés à l'aide de serveurs proxy, ce qui mettra les images en cache et empêchera d'exploiter les pixels de suivi pour des indicateurs tels que le [suivi du nombre d'ouvertures]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#open-tracking-pixel). Pour en savoir plus sur la protection de la confidentialité dans Mail et les problèmes concernant les indicateurs de livrabilité des e-mails ainsi que les problèmes liés aux campagnes préexistantes et aux Canvas qui se déclenchent sur la base de ces indicateurs, consultez notre [documentation]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp).

### Fonctionnalités push {#push-features}

iOS 15 a introduit de nouvelles fonctionnalités de notification pour aider les utilisateurs à rester concentrés et à éviter de fréquentes interruptions tout au long de la journée. Nous sommes ravis de prendre en charge ces nouvelles fonctionnalités, notamment les [niveaux d'interruption et les scores de pertinence]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options).

## Cartes de contact {#contact-cards}

Les cartes de contact sont un format de fichier normalisé pour l'envoi d'informations professionnelles et de contact facilement importables dans les carnets d'adresses ou de contacts. Vous pouvez maintenant télécharger et créer des cartes de contact pour vos messages SMS et MMS. Pour en savoir plus sur la manière de créer des cartes de contact dans notre générateur de cartes de contact intégré, consultez notre [documentation]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card).

## Personnalisation des Content Cards par défaut {#default-content-cards-customization}

Vous pouvez créer votre propre interface de Content Cards en étendant le `ABKContentCardsTableViewController` pour personnaliser tous les éléments de l'interface utilisateur et le comportement des Content Cards. Pour en savoir plus sur la manière de personnaliser le flux des Content Cards, consultez notre [documentation]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style).

## Limites de débit de l'API {#api-rate-limits}

Les [limites de débit]({{site.baseurl}}/api/basics#api-limits) s'appliqueront à tous les clients intégrés après le 16 septembre 2021.

## Mises à jour des guides du développeur pour Android et FireOS {#updates-to-android-and-fireos-developer-guides}

Les guides du développeur pour Android et FireOS ont été fusionnés en un seul endroit. Des articles dédiés à FireOS seront disponibles dans cette [nouvelle section Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Mises à jour des rapports d'entonnoir et de rétention {#updates-to-funnel-and-retention-reports}

Les [rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) et les [rapports de rétention]({{site.baseurl}}/user_guide/analytics/reports/retention_reports) sont désormais disponibles pour les campagnes SMS.