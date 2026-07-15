---
nav_title: Solicitação de avaliação no app para iOS
article_title: Solicitação de avaliação no app para iOS
page_order: 6
description: "Este artigo descreve abordagens e implicações do uso da Braze para pedir aos usuários que avaliem seu app."
channel:
  - in-app messages

---

# Solicitação de avaliação no app para iOS {#in-app-rating-prompt-for-ios}

> Este artigo descreve abordagens e implicações do uso da Braze para pedir aos usuários que avaliem seu app. Para dicas sobre como criar uma campanha de avaliação de app eficaz, confira [O que fazer e o que não fazer nas avaliações de apps por clientes](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

A Apple oferece uma solicitação nativa, introduzida com o iOS 10.3, que permite aos usuários avaliar apps de dentro do próprio app. Se você deseja solicitar avaliações de app aos usuários usando uma mensagem no app no iOS, é necessário usar a solicitação nativa, pois a Apple não permite solicitações de avaliação personalizadas (consulte as [Diretrizes de Revisão da App Store](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), seção 5.6.1).

De acordo com as diretrizes da Apple, as solicitações de avaliação de app podem ser exibidas a um usuário até três vezes por ano, então qualquer campanha de avaliação de app deve aproveitar o [limite de taxa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping). Os usuários também podem optar por não ver solicitações de avaliação de app nas configurações do app. Para mais informações sobre avaliações na App Store, consulte o artigo da Apple sobre [Avaliações, Resenhas e Respostas](https://developer.apple.com/app-store/ratings-and-reviews/).

## Usando a Braze para pedir avaliações de app aos usuários {#using-braze-to-ask-users-for-app-reviews}

Embora a Apple exija o uso da solicitação nativa, você ainda pode aproveitar as Campaigns da Braze para pedir aos usuários que avaliem e escrevam uma resenha do seu app no momento certo. Existem duas abordagens principais que você pode adotar.

### Abordagem 1: Deep linking para a App Store {#approach-1-deep-linking-to-the-app-store}

Com essa abordagem, você quer incentivar os usuários a visitar a App Store para adicionar uma avaliação. Para isso, crie uma campanha de mensagem no app que faça [deep link]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) para a App Store.

![Duas telas de celular lado a lado. A primeira é uma mensagem no app que pede ao usuário para avaliar o app na App Store. A segunda é a página da App Store do iOS para esse app.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### Abordagem 2: Preparação prévia (soft priming) {#approach-2-soft-priming}

Se você não quer que os usuários saiam do seu app, pode primeiro prepará-los com uma mensagem no app separada. A preparação prévia é uma forma de pedir permissão aos usuários antes de enviar a solicitação nativa de avaliação da App Store. Para isso, crie uma campanha de mensagem no app e adicione um deep link personalizado que chame o método `requestReview` quando clicado.

Para etapas detalhadas, consulte [Solicitação personalizada de avaliação da App Store]({{site.baseurl}}/developer_guide/in_app_messages/customization#swift_customizing-the-app-store-review-prompt).

![Duas mensagens no app lado a lado. A primeira prepara o usuário para avaliar o app, perguntando se ele tem um momento para avaliá-lo. A segunda é a mensagem nativa de avaliação da App Store do iOS, exibindo uma escala de cinco estrelas que o usuário pode selecionar para avaliar o app.]({% image_buster /assets/img_archive/prime_app_review.png %})

Os usuários enviarão uma avaliação por meio da solicitação nativa de avaliação da App Store e poderão escrever e enviar uma resenha sem sair do app.

### Considerações {#considerations}

Como alternativa à preparação prévia, você também pode exibir a solicitação de avaliação do iOS diretamente, sem nenhuma mensagem de preparação da Braze exibida antes. A vantagem disso é que, se o usuário tiver optado por não receber solicitações de avaliação de app, não haverá a experiência negativa de tentar avaliar o aplicativo sem que nenhuma solicitação apareça.

{% alert important %}
Não crie mensagens no app em HTML personalizado que imitem a solicitação nativa de avaliação de app do iOS, pois isso viola as diretrizes da Apple.
{% endalert %}