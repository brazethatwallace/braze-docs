---
nav_title: "Recurso de ícone de app personalizado (iOS 10.3)"
article_title: "Recurso de ícone de app personalizado (iOS 10.3)"
page_order: 3
page_type: reference
description: "Este artigo de referência aborda a atualização do iOS 10.3 sobre ícone de app personalizável."
platform: iOS
channel:
  - push

---

# Recurso de ícone de app personalizado (iOS 10.3) {#custom-app-icon-feature-ios-103}

> Com o iOS 10.3, a Apple introduziu a possibilidade de alterar o ícone de um app na tela inicial sem precisar atualizar o aplicativo pela Apple App Store. O desenvolvedor agora pode permitir que o usuário altere o ícone da tela inicial dentro do próprio app. A Apple exige que todas as imagens de ícone do app que o desenvolvedor deseja disponibilizar para o usuário estejam incluídas no binário enviado à Apple para revisão durante a publicação do app na Apple App Store.

Para notificar seus usuários sobre esse recurso, é possível enviar uma mensagem no app ou notificação por push pela Braze ao usuário, explicando essa funcionalidade ou perguntando se ele gostaria de alterar o ícone. O desenvolvedor precisaria apenas criar um deep link para dentro do aplicativo, onde o prompt nativo do iOS pode ser exibido para realizar a troca de ícone. Isso é semelhante à mesma orientação que fornecemos atualmente sobre como configurar um primer de notificação por push para APNs.

Além disso, esse envio de mensagens pode aproveitar ao máximo a segmentação para tornar o texto da mensagem altamente contextual para o usuário. Você também pode utilizar testes A/B de mensagens para verificar qual abordagem gera mais impacto no resultado desejado.