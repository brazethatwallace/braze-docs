---
nav_title: Protection de la confidentialité dans Apple Mail
article_title: Protection de la confidentialité dans Apple Mail pour iOS 15
page_order: 1
description: "Le présent article de référence explique la mise à jour de la protection de la confidentialité dans Apple Mail, les personnes concernées et les prochaines étapes pour se préparer à cette fonctionnalité."
channel:
  - email

---

# Protection de la confidentialité dans Apple Mail {#apples-mail-privacy-protection}

> Cet article présente la protection de la confidentialité dans Mail d'Apple (MPP), les personnes concernées et comment se préparer à son impact sur les indicateurs de livrabilité des e-mails.

## Qu'est-ce que la mise à jour de la protection de la confidentialité dans Apple Mail ? {#what-is-apples-mail-privacy-protection-update}

La protection de la confidentialité dans Mail d'Apple (MPP) est une mise à jour de la confidentialité disponible pour les utilisateurs de l'application Apple Mail sur iOS 15, iPadOS 15, macOS Monterey et watchOS 8, publiée mi-septembre 2021. Pour les utilisateurs qui activent la MPP (ce que nous prévoyons que la plupart des utilisateurs feront), les e-mails seront désormais préchargés à l'aide de serveurs proxy, mettant en cache les images et entravant la capacité à utiliser des pixels de suivi pour des indicateurs tels que [le suivi des ouvertures]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#changing-location-of-tracking-pixel).

Les marques doivent s'attendre à ce que la MPP entraîne des problèmes concernant les indicateurs de livrabilité des e-mails et des difficultés avec les Campaigns et Canvas existants qui se déclenchent en fonction de ces indicateurs. Pour comprendre l'impact sur la livrabilité des e-mails, consultez le [rapport sur les e-mails]({{site.baseurl}}/user_guide/channels/email/reporting).

### Qui est impacté ? {#who-will-this-affect}

Tout destinataire utilisant l'application native Apple Mail sur :

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

Cela s'applique à tous les utilisateurs qui ont connecté leur compte de messagerie à l'application Apple Mail et qui ont activé la fonctionnalité de sécurité, quel que soit le service de messagerie (Gmail, Outlook, Yahoo, AOL, etc.). Cet impact ne se limite pas aux utilisateurs abonnés qui reçoivent des e-mails à des adresses Apple/iCloud/me.com.

{% alert important %}
Bien que ces mises à jour concernant la livrabilité des e-mails soient significatives, la MPP ne modifie pas fondamentalement les règles qui régissent les e-mails et la livrabilité. En revanche, elle aura un impact sur la façon dont nous mesurons le succès et sur les outils et fonctionnalités e-mail qui pourront être utilisés à l'avenir.
{% endalert %}

## Comment se préparer à la MPP ? {#how-to-prepare-for-mpp}

Le temps presse pour les marques qui commencent tout juste à réfléchir à la manière de répondre à la MPP et à son impact potentiel sur leur marketing par e-mail et leurs efforts globaux d'engagement client. Nous recommandons aux utilisateurs de procéder comme suit :

- Évaluer le risque que la MPP représente pour leurs efforts marketing
- Élaborer un plan de réponse ciblé qui aborde les ajustements d'automatisation sur la plateforme Braze, renforce les bonnes pratiques de livrabilité et développe un ensemble plus large d'indicateurs pour mesurer les performances.
- Mettre en œuvre ce plan de réponse dès que possible

Pour un aperçu approfondi de la préparation à la protection de la confidentialité dans Apple Mail, consultez notre [article de blog](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare).