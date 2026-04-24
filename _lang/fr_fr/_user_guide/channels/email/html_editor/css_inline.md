---
nav_title: Insertion CSS
article_title: Insertion CSS
page_order: 5.1
description: "Cet article de référence explique comment activer l'insertion CSS et présente quelques bonnes pratiques."
channel:
  - email

---

# Insertion CSS

> L'insertion CSS est une forme de prétraitement des e-mails qui déplace les styles d'une feuille de style CSS dans le corps d'un e-mail HTML. Le terme « insertion » (inlining) fait référence au fait que les styles sont appliqués « en ligne » aux éléments HTML individuels.

Pour certains clients de messagerie, l'insertion CSS peut améliorer le rendu des e-mails et vous aider à confirmer que vos e-mails s'affichent comme prévu. Si la majorité de votre CSS est déjà insérée en ligne ou si vous êtes sûr que votre HTML et votre CSS sont compatibles avec les exigences de la plupart des clients de messagerie, il n'est peut-être pas nécessaire d'activer cette fonctionnalité. Elle peut provoquer des conflits entre les styles intégrés dynamiquement et vos styles en ligne existants, et modifier le rendu attendu de la prévisualisation et de l'e-mail.

## Utiliser l'insertion CSS

Vous pouvez activer ou désactiver l'insertion CSS pour n'importe quel e-mail à l'aide du bouton **Activer l'insertion CSS** dans l'onglet **Envoi en cours** de l'éditeur HTML.

![Case à cocher pour gérer l'insertion CSS dans le compositeur HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### État d'insertion par défaut

Vous pouvez définir un état par défaut (activé ou désactivé) de manière globale depuis **Paramètres** > **Préférences des e-mails**. Recherchez le paramètre **Insertion CSS**. Ce paramètre détermine la valeur par défaut avec laquelle tous les nouveaux e-mails sont créés. Notez que la modification de ce paramètre n'affectera aucun de vos e-mails existants. Vous pouvez également remplacer cette valeur par défaut à tout moment lors de la rédaction de vos e-mails.

![Option d'insertion CSS par défaut pour les nouveaux e-mails, située dans les paramètres des e-mails.]({% image_buster /assets/img_archive/css-inline1.png %})