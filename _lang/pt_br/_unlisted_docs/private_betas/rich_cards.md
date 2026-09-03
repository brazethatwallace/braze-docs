---
nav_title: "Criando uma mensagem RCS"
article_title: "Criando uma mensagem RCS"
permalink: /create_rcs_message/
description: "Este artigo aborda como criar uma mensagem RCS."
hidden: true
---

# Criando uma mensagem RCS {#creating-an-rcs-message}

> As campanhas de RCS são ótimas para alcançar diretamente seus clientes e conversar com eles de forma programática. Você pode usar Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e construir um ambiente que promova e aprimore uma experiência de usuário discreta com sua marca.

## Criando uma mensagem RCS

### Etapa 1: Escolha onde criar sua mensagem {#step-1-choose-where-to-build-your-message}

Não tem certeza se a mensagem deve ser enviada usando uma Campaign ou um Canvas? Campaigns são melhores para campanhas de mensagens simples e únicas, enquanto Canvas é melhor para jornadas de usuários com várias etapas.

{% tabs %}
{% tab Campaign %}
1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **SMS/MMS/RCS** ou, para Campaigns direcionadas a vários canais, selecione **Multichannel**.
3. Dê à sua Campaign um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * Tags facilitam a localização das suas Campaigns e a criação de relatórios. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder), você pode filtrar por tags específicas.

{: start="5"}
5. Adicione e nomeie quantas variantes forem necessárias para sua Campaign. Você pode escolher diferentes plataformas, tipos de mensagem e layouts para cada uma das variantes adicionadas. Para saber mais sobre o assunto, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).
- **Testes de variantes SMS e RCS**: a Braze permite incluir variantes de SMS e RCS em uma única Campaign, possibilitando a comparação do desempenho de cada uma. Você pode adicionar variantes de SMS e RCS durante a primeira etapa da composição da mensagem.

{: start="6"}
6. Selecione um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups) habilitado para RCS. Ao selecionar um grupo de inscrições, a Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas os usuários inscritos recebam a Campaign. Somente códigos longos e códigos curtos pertencentes a esse grupo de inscrições serão usados para enviar SMS aos usuários-alvo.
- **Fallback de SMS**: a Braze recomenda fortemente que cada grupo de inscrições que contenha um remetente RCS também inclua pelo menos um código SMS para fallback. Isso é importante para a entregabilidade nos casos em que as mensagens RCS não são entregues. Alguns motivos podem incluir incompatibilidade do dispositivo do usuário e cobertura incompleta de operadoras em um determinado país ou região. Ao ativar o fallback de SMS, sua mensagem ainda será entregue ao usuário e você nunca perderá a oportunidade de se conectar com ele.

{: start="7"}
7. Escolha entre SMS e RCS. Antes de compor mensagens RCS, escolha o canal de envio. Geralmente, recomendamos usar RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS. No entanto, sempre oferecemos a opção de envio por SMS para que você tenha máxima flexibilidade e controle.

![Opções para selecionar um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Se todas as mensagens da sua Campaign forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar variantes adicionais. Em seguida, escolha **Copy from Variant** no menu suspenso **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando o criador de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa de mensagem **SMS/MMS/RCS** no criador de Canvas.
3. Dê à sua etapa um nome claro e significativo.
4. Selecione um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups) habilitado para RCS. Ao selecionar um grupo de inscrições, a Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas os usuários inscritos recebam a Campaign. Somente códigos longos e códigos curtos pertencentes a esse grupo de inscrições serão usados para direcionar os usuários.
- **Fallback de SMS**: a Braze recomenda fortemente que cada grupo de inscrições que contenha um remetente RCS também inclua pelo menos um código SMS para fallback. Isso é importante para a entregabilidade nos casos em que as mensagens RCS não são entregues. Alguns motivos podem incluir incompatibilidade do dispositivo do usuário e cobertura incompleta de operadoras em um determinado país ou região. Ao ativar o fallback de SMS, sua mensagem ainda será entregue ao usuário e você nunca perderá a oportunidade de se conectar com ele.

{: start="5"}
5. Escolha entre SMS e RCS. Antes de compor mensagens RCS, escolha o canal de envio. Geralmente, recomendamos usar RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS. No entanto, sempre oferecemos a opção de envio por SMS para que você tenha máxima flexibilidade e controle.

![Opções para selecionar um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Etapa 2: Selecione o tipo de mensagem RCS {#step-2-select-your-rcs-message-type}

Durante a criação de Campaigns e Canvas, escolha entre três tipos de mensagem RCS (Texto, Mídia, Rich Card) para configurar mensagens que melhor atendam aos seus objetivos.

![Opções para selecionar um tipo de mensagem Texto, Mídia ou Cartão.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs local %}
{% tab Texto %}
Como o nome indica, as mensagens RCS de texto focam no texto como mídia. Se você digitar até 160 caracteres, a mensagem RCS é cobrada como uma mensagem somente de texto (ou "básica"). Se você exceder 160 caracteres ou usar um elemento rico, a mensagem é cobrada como uma mensagem RCS rica (ou "única") (e o limite de caracteres aumenta para 3072 caracteres).

#### Recursos {#features}

- Os tipos de mensagem de texto incluem todos os recursos de SMS. Somente o rastreamento avançado é possível para rastreamento de cliques de URL, oferecendo granularidade de relatórios em nível de usuário.
- Além disso, agora você tem a opção de incluir botões de **Respostas sugeridas** e **Ações sugeridas** que impulsionam ações de alto engajamento do usuário, como visitar uma landing page ou fazer um pedido.
    - **Respostas sugeridas** são botões contendo respostas sugeridas para os usuários clicarem e preencher automaticamente na entrada de texto, eliminando o atrito de pensar em uma resposta ao fornecer um conjunto restrito de opções.
    - **Ações sugeridas** são botões que iniciam uma ação no dispositivo do usuário. Geralmente consistem em uma ou duas palavras descritivas e um ícone visual para ajudar o usuário a entender o que o botão faz. Atualmente, a Braze suporta ações sugeridas do tipo OpenURL. Isso funciona de forma semelhante a uma URL, em que os usuários que selecionam o botão são redirecionados para uma página web ou outro local identificado por URL.

![GIF mostrando três ações sugeridas para uma mensagem RCS promovendo estilos de moda em tendência: "Fairytale royalty", "Edgy academia" e "Show me your other styles".]({% image_buster /assets/unlisted_docs/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Considerações {#considerations}

- Para limites de caracteres em texto, você pode escrever até 160 caracteres para uma mensagem RCS somente de texto (básica) ou até 3072 para uma mensagem RCS rica (única).
- Para limites de botões, você pode adicionar até cinco botões por mensagem. Esses botões podem ser ações sugeridas ou respostas sugeridas.
- Blocos de texto longos e muitos botões podem frustrar os usuários, então, sempre que possível, recomendamos optar pela simplicidade.
- Em alguns casos, pode ser mais econômico enviar mensagens de texto mais longas por RCS do que por SMS. Isso porque mensagens SMS mais longas são divididas em vários segmentos, cada um deles cobrado separadamente, enquanto as mensagens RCS são cobradas por mensagem. Entre em contato com o gerente de conta da Braze para mais detalhes e orientações.
{% endtab %}

{% tab Mídia %}
As mensagens RCS de mídia permitem o uso de formatos de mídia envolventes que não são possíveis com SMS. Incluem arquivos de imagem, vídeo e documentos. Essas opções de mídia existem para ajudar você a engajar seu público de forma ainda mais profunda e viabilizar casos de uso totalmente novos. No momento, apenas o upload de imagens é suportado pela [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications).

#### Recursos

- Os tipos de mensagem de mídia suportam tudo disponível nos tipos de mensagem de texto, incluindo texto, respostas sugeridas e ações sugeridas.
- Suporta arquivos de imagem, incluindo os formatos JPEG e PNG. Arquivos de imagem estão disponíveis por upload da Biblioteca de mídia.
- Suporta arquivos de vídeo, incluindo os formatos MP4, MPEG e MV4. Arquivos de vídeo podem ser adicionados por URL diretamente no criador de mensagem.
- Suporta arquivos de documentos em formato PDF. Arquivos de documentos podem ser adicionados pela URL diretamente no criador de mensagem.

![Criador de RCS com opção para fazer upload de um arquivo de mídia.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_type.png %})

#### Especificações de arquivo {#file-specifications}

| Tipo de arquivo | Especificações |
| --- | --- |
| Todos | - O tamanho do arquivo é limitado a 100 MB <br><br>- A URL do arquivo pode ter até 2048 caracteres |
| Arquivos de imagem | Os formatos suportados incluem JPG, JPEG e GIF |
| Arquivos de vídeo | Os formatos suportados incluem H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Arquivos de documentos | Formato suportado: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Considerações

A experiência do usuário ao receber mensagens RCS pode variar ligeiramente com base em diversos fatores, incluindo a cobertura de operadoras no país de destino, o hardware do dispositivo móvel e o sistema operacional do dispositivo móvel.

De modo geral, o RCS se integra de forma mais natural com dispositivos Android (esse método foi amplamente implementado pelo Google, e o envio de mensagens RCS peer-to-peer é amplamente adotado na comunidade Android). Diferentes dispositivos podem renderizar a experiência em velocidades e qualidades diferentes.
{% endtab %}

{% tab Rich Card %}

{% alert important %}
Rich Cards estão em acesso antecipado. Entre em contato com o gerente de sucesso do cliente da Braze se você estiver interessado em participar deste acesso antecipado.
{% endalert %}

Um Rich Card combina mídia, texto e botões em uma única mensagem, criando uma experiência mais intuitiva e envolvente para seus clientes. Você pode criar dois subtipos de Rich Cards: Texto e Mídia.

{% subtabs %}
{% subtab Texto %}
Um Rich Card de texto é uma mensagem concisa focada em texto. Ele deve incluir os seguintes elementos:

- **Título:** Até 200 caracteres. Pode ser personalizado com Liquid.
- **Descrição:** Até 2.000 caracteres. Pode ser personalizada com Liquid.
- **Botões:** Pelo menos um botão é obrigatório. Você pode adicionar até quatro botões com ações de **Resposta sugerida** ou **Abrir URL da web**.

{% endsubtab %}
{% subtab Mídia %}

Um Rich Card de mídia é uma mensagem visual contendo uma imagem ou vídeo. Ele deve incluir os seguintes elementos:

- **Mídia:** Uma imagem, GIF ou vídeo.
    - Thumbnails de vídeo personalizados não são suportados no acesso antecipado. O acesso antecipado suporta apenas um layout vertical com altura de mídia grande para arquivos de imagem e vídeo.
- **Botões:** Pelo menos um botão é obrigatório. Você pode adicionar até quatro botões com ações de **Resposta sugerida** ou **Abrir URL da web**.

{% endsubtab %}
{% endsubtabs %}

### Recursos
- **Botões do cartão** e **Sugestões:** Você pode adicionar até quatro botões e cinco sugestões (até 25 caracteres cada) na parte inferior do Rich Card (botões) ou na parte inferior da tela da mensagem (sugestões). O usuário pode selecionar essas opções de clique-toque para enviar uma resposta específica ou realizar uma ação específica.
- **Personalização:** Você pode usar Liquid para personalizar todos os elementos do Rich Card, incluindo título, descrição, mídia e botões.
- **Cobrança:** Rich Cards são cobrados como uma única mensagem RCS rica (ou "única").
- **Orientação de URL:** URLs inseridas como texto simples no título ou na descrição não serão clicáveis. Você deve usar um **botão OpenURL** para direcionar os usuários a um site.

![Painel com opções para selecionar um Rich Card de Mídia ou Texto.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_text.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Etapa 3: Componha sua mensagem RCS {#step-3-compose-your-rcs-message}

Escreva sua mensagem usando idiomas e personalização ([Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) e emojis) conforme necessário. Certifique-se de seguir nossos limites de texto da mensagem para reduzir suas chances de cobranças excedentes.

{% alert important %}
Antes de prosseguir, leia nossas [diretrizes para limites de mensagens RCS](#step-2-select-your-rcs-message-type). As mensagens RCS são [cobradas por mensagem]({{site.baseurl}}/sms_rcs_billing_calculators), então é importante entender as nuances do que pode ser incluído em cada tipo de mensagem RCS.
{% endalert %}

### Etapa 4: Pré-visualize e teste sua mensagem {#step-4-preview-and-test-your-message}

A Braze sempre recomenda pré-visualizar e testar sua mensagem antes de enviá-la. Acesse a guia **Test** para enviar um RCS de teste para grupos de teste de conteúdo ou usuários individuais, ou pré-visualize a mensagem como um usuário diretamente na Braze.

### Etapa 5: Construa o restante da sua Campaign ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

Em seguida, construa o restante da sua Campaign ou Canvas. Consulte as seções a seguir para mais detalhes sobre como usar nossas ferramentas da melhor forma para criar mensagens RCS.

#### Etapa 5.1: Escolha o cronograma de entrega ou disparo {#step-51-choose-delivery-schedule-or-trigger}

As mensagens RCS podem ser entregues com base em um horário agendado, uma ação ou um disparo de API. Para mais informações, consulte [Agendar sua Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para entrega baseada em ação, você também pode definir a duração da Campaign e o horário de silêncio.

Especifique seus controles de entrega, como permitir que os usuários se tornem novamente elegíveis para receber a Campaign ou ativar regras de limite de frequência.

#### Etapa 5.2: Escolha os usuários a serem direcionados {#step-52-choose-users-to-target}

Direcione os usuários escolhendo Segments ou filtros para restringir seu público. Você já deve ter selecionado o grupo de inscrições, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você.

{% multi_lang_include audience/target_audiences.md %}

Em seguida, selecione o público maior de seus Segments e restrinja ainda mais esse Segment com [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) opcionais. Você receberá automaticamente uma prévia de como está a população aproximada desse Segment neste momento. Tenha em mente que a associação exata ao Segment é sempre calculada imediatamente antes do envio da mensagem.

{% alert tip %}
Interessado em usar o redirecionamento RCS para direcionar usuários com base em suas interações de SMS e RCS? Consulte [Redirecionamento]({{site.baseurl}}/sms_mms_rcs_user_retargeting).
{% endalert %}

#### Etapa 5.3: Escolha os eventos de conversão {#step-53-choose-conversion-events}

A Braze permite que você rastreie com que frequência os usuários realizam ações específicas, ou eventos de conversão, após receber uma Campaign. Você pode permitir uma janela de até 30 dias durante a qual uma conversão será contabilizada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso da sua Campaign. Por exemplo:
- Se você estiver usando geotargeting para disparar uma mensagem RCS com o objetivo final de o usuário realizar uma compra, defina o evento de conversão como **Purchase**.
- Se você estiver tentando levar o usuário ao seu app, defina o evento de conversão como **Starts Session**.

Você também pode definir eventos de conversão personalizados com base no seu caso de uso específico. Seja criativo em como você realmente deseja medir o sucesso da sua Campaign.

### Etapa 6: Revise e implante {#step-6-review-and-deploy}

Depois de terminar de criar sua Campaign ou Canvas, revise os detalhes, teste e envie!

Em seguida, consulte [Relatórios para SMS, MMS e RCS]({{site.baseurl}}/sms_mms_rcs_reporting) para saber como acessar os resultados das suas Campaigns de RCS.

## Análise de dados e relatórios {#analytics-and-reporting}

As análises da sua Campaign ou Canvas incluem:

- Estatísticas de _Total de cliques_ que incluem todas as interações com o Rich Card, como cliques em botões e Respostas sugeridas ou ações.
- Uma tabela detalhada que fornece uma visão mais aprofundada dessas interações.

{% alert note %}
O acesso antecipado não inclui rastreamento de cliques no nível do usuário. O _Total de cliques_ será incrementado cada vez que um botão for clicado. Por exemplo, se um usuário clicar no mesmo botão três vezes, a contagem de cliques aumentará em três.
{% endalert %}

## Dicas {#tips}

### Usando Liquid para personalização de mensagens {#using-liquid-for-message-personalization}

Se você planeja usar Liquid, inclua um valor padrão para a personalização escolhida. Dessa forma, se o perfil de usuário do destinatário estiver incompleto, ele não receberá um espaço em branco `Hi, !` em vez do nome ou de uma frase coerente.

### Gerando textos com IA {#generating-ai-copy}

Precisa de ajuda para criar textos envolventes? Experimente usar o [Assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Insira o nome ou a descrição de um produto, e a IA gerará textos de marketing semelhantes aos escritos por humanos para uso no seu envio de mensagens.

![Criador de mensagens com um ícone para abrir o Assistente de Copywriting com IA.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Perguntas frequentes {#frequently-asked-questions}

### Posso enviar mensagens de voz pré-gravadas com RCS? {#can-i-send-pre-recorded-voicemails-with-rcs}

Sim, você pode usar mensagens de mídia para suportar arquivos de áudio.