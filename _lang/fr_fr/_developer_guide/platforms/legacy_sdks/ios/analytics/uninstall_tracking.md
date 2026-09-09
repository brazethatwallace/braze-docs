---
nav_title: Suivi des désinstallations
article_title: Suivi des désinstallations pour iOS
platform: iOS
page_order: 7
description: "Cet article explique comment configurer le suivi des désinstallations pour votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Suivi des désinstallations pour iOS {#uninstall-tracking-for-ios}

> Cet article explique comment configurer le suivi des désinstallations pour votre application iOS, et comment effectuer des tests pour que votre application ne prenne pas d'actions automatiques indésirables à la réception d'une notification push de suivi des désinstallations de Braze.

Le suivi des désinstallations utilise des notifications push en arrière-plan avec un indicateur Braze dans le payload. Pour plus d'informations, consultez le [suivi des désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking) dans notre guide de l'utilisateur.

## Étape 1 : Activer les notifications push en arrière-plan {#step-1-enabling-background-push}

Assurez-vous d'avoir activé l'option **Remote notifications** dans la section **Background Modes** de l'onglet **Capabilities** de votre projet Xcode. Consultez notre documentation sur les [notifications push silencieuses]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications) pour plus de détails.

## Étape 2 : Vérification des notifications push silencieuses de Braze {#step-2-checking-for-braze-background-push}

Braze utilise les notifications push silencieuses pour collecter les données d'analyse du suivi des désinstallations. Assurez-vous que votre application [n'effectue aucune action non souhaitée]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push) lors de la réception de nos notifications de suivi des désinstallations.

## Étape 3 : Tester depuis le tableau de bord {#step-3-test-from-the-dashboard}

Ensuite, envoyez-vous une notification push de test depuis le tableau de bord. Cette notification push de test ne mettra pas à jour votre profil utilisateur.

1. Sur la page **Campaigns**, créez une Campaign de notification push et sélectionnez **iOS push** comme plateforme.<br><br>
2. Sur la page **Settings**, ajoutez la clé `appboy_uninstall_tracking` avec la valeur correspondante `true` et cochez **Add Content-Available Flag**.<br><br>
3. Utilisez la page **Preview** pour vous envoyer une notification push de test de suivi des désinstallations.<br><br>
4. Vérifiez que votre application n'effectue aucune action automatique indésirable à la réception de la notification push.

{% alert important %}
Ces étapes de test servent de simulation pour l'envoi d'une notification push de suivi des désinstallations depuis Braze. Si vous avez activé le compteur de badges, un numéro de badge sera envoyé avec la notification push de test, mais les notifications push de suivi des désinstallations de Braze ne définiront pas de numéro de badge sur votre application.
{% endalert %}

## Étape 4 : Activer le suivi des désinstallations {#step-4-enable-uninstall-tracking}

Suivez les instructions pour [activer le suivi des désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).