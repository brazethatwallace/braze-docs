---
nav_title: Suivi de localisation
article_title: Suivi de la localisation pour Windows Universal
platform: Windows Universal
page_order: 6
description: "Cet article de référence explique comment ajouter le suivi de la localisation à votre application Windows Universal."
tool: Location
hidden: true
---

# Suivi de la localisation {#location-tracking}
{% multi_lang_include archive/windows_deprecation.md %}

1. Assurez-vous que dans votre fichier `Package.appxmanifest`, l'option `location` est cochée.
2. Si vous souhaitez désactiver le suivi automatique de la localisation, définissez `<DisableLocationCollection>false</DisableLocationCollection>` sur `true` dans votre fichier `AppboyConfiguration.xml`.