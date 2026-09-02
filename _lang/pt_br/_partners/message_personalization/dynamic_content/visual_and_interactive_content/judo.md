---
nav_title: Judo
article_title: Judo
description: "Este artigo de referência descreve a parceria entre a Braze e o Judo, uma plataforma de interface do usuário sem código e orientada por servidor que permite adicionar contexto e rastreamento de localização aos seus apps para iOS e Android."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> O [Judo](https://judo.app) é uma plataforma de interface do usuário orientada por servidor que permite que os editores forneçam com eficiência experiências ricas e envolventes para o usuário no app, sem atualizações do app.

_Essa integração é mantida pelo Judo._

## Sobre a integração {#about-the-integration}

A integração da Braze com o Judo proporciona experiências personalizadas em suas campanhas e Canvas. Em vez de uma experiência de landing page simples e modelada, uma campanha da Braze pode incorporar conteúdo que inclua várias telas, modais, vídeo, fontes personalizadas e configurações de suporte, como modo escuro e acessibilidade, criadas sem código e implantadas sem atualizações de app. Os dados da Braze também podem ser usados para oferecer suporte a conteúdo personalizado em uma experiência do Judo. Eventos do usuário e dados da experiência podem ser retroalimentados na Braze para atribuição e direcionamento.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Judo | É necessário ter uma conta [Judo](https://www.judo.app/) para aproveitar essa parceria. |
| SDK do Judo | O SDK do Judo deve ser integrado aos seus apps para [iOS](https://github.com/judoapp/judo-ios/) e/ou [Android](https://github.com/judoapp/judo-android). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

**Integração**: os editores de apps que usam o Judo criam e implementam experiências de integração ricas e nativas. Essas experiências agora podem ser um elemento em uma jornada de integração personalizada entre canais, coordenada pela Braze. As experiências podem ser personalizadas e atualizadas rapidamente sem nenhuma atualização do app para testar a eficácia de diferentes fluxos no app.

**Conversão**: os editores de apps podem usar os dados da Braze para criar uma experiência rica e personalizada no app para impulsionar compras no app, inscrições pagas ou merchandising contextual usando ganchos de integração no Judo. O acesso a essas experiências pode ser disparado por meio de campanhas de marketing de engajamento criadas na Braze.

**Conteúdo orientado por eventos**: um dos principais usos do Judo em esportes e entretenimento é a criação de experiências ricas para prévia, promoção e recapitulação de eventos. Esse recurso tem amplas aplicações em outros verticais de conteúdo sazonal e voltado para notícias. Vincular o envio de mensagens para promover ou destacar eventos em tempo hábil a experiências ricas no app capacita os editores a impulsionar o engajamento sendo contextualmente relevantes.

## Integração lado a lado de SDK {#side-by-side-sdk-integration}

O Judo oferece bibliotecas adicionais que automatizam parte do esforço necessário para integrar os SDKs do Judo e da Braze lado a lado em seus apps móveis.

### Etapa 1: instale a biblioteca de integração Judo-Braze {#step-1-install-the-judo-braze-integration-library}

Instale e configure a biblioteca de integração Judo-Braze em seus apps. Isso ativará automaticamente o rastreamento de eventos.

- [Instruções de instalação para iOS](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Instruções de instalação para Android](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Etapa 2: configure o envio de mensagens no app {#step-2-configure-in-app-messaging}

Essa etapa envolverá a criação de implementações personalizadas de `ABKInAppMessageControllerDelegate` e `IInAppMessageManagerListener` para iOS e Android.

Consulte a documentação de configuração de mensagens no app incluída em cada uma das bibliotecas de integração:

- [Configuração de mensagens no app para iOS](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Configuração de mensagens no app para Android](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Usando esta integração {#using-this-integration}

Depois de concluir a integração no lado do app, você pode testá-la executando uma campanha de teste de mensagens no app da Braze para uma experiência do Judo, verificando se ela funciona conforme o esperado.

### Etapa 1: crie uma campanha de mensagem no app com código personalizado {#step-1-create-a-custom-code-in-app-message-campaign}

Na plataforma Braze, crie uma campanha de mensagem no app da Braze com o tipo de mensagem **Custom Code**. Em seguida, selecione **HTML Upload** como o tipo personalizado. Certifique-se de preencher o conteúdo da mensagem com os campos básicos de envio de mensagens no app; esse conteúdo não será mostrado ao usuário.

![Uma imagem da aparência do dashboard ao selecionar o tipo de mensagem "Custom Code".]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

Em seguida, use o seguinte snippet de HTML mínimo para satisfazer a validação do formulário:
```
<a href="appboy://close">X</a>
```

Observe que isso não será exibido em produção no seu dispositivo, pois o Judo reescreverá e substituirá o snippet por uma Judo Experience.

![Uma imagem mostrando o código de validação de formulário adicionado à etapa de composição da sua campanha.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### Etapa 2: defina um par chave-valor para o Judo {#step-2-set-a-key-value-pair-for-judo}
![Esta imagem mostra o par chave-valor necessário para essa integração, sendo que a "chave" é "judo-experience" e o "valor" é o seu link do Judo.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Defina um [par chave-valor personalizado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) na campanha com a chave `judo-experience`. Forneça a URL da experiência do Judo que você gostaria de exibir aqui. A biblioteca de integração Judo-Braze detectará esse par chave-valor no manipulador e o usará para injetar sua experiência do Judo no lugar da interface padrão de mensagens no app da Braze.
<br><br>
### Etapa 3: finalize a campanha {#step-3-finishing-the-campaign}

Por fim, conclua a campanha, configurando um gatilho para a campanha e selecionando usuários por meio de Segments nas seções **Delivery** e **Target User**. Acesse nosso [artigo]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) sobre mensagens no app para conhecer os diferentes componentes de uma mensagem no app da Braze.