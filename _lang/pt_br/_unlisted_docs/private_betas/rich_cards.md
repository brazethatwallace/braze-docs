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

Não tem certeza se sua mensagem deve ser enviada usando uma campanha ou um Canvas? Campaigns são melhores para campanhas de mensagens simples e únicas, enquanto Canvas é melhor para jornadas de usuário com várias etapas.

{% tabs %}
{% tab Campaign %}
1. Acesse **Envio de mensagens** > **Campaigns** e selecione **Criar campanha**.
2. Selecione **SMS/MMS/RCS** ou, para campanhas direcionadas a múltiplos canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags) conforme necessário.
   * Tags facilitam encontrar suas campanhas e criar relatórios a partir delas. Por exemplo, ao usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reporting/report_builder), você pode filtrar por tags específicas.

{: start="5"}
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagem e layouts para cada uma das variantes adicionadas. Para saber mais sobre este tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).
- **Teste de variantes SMS e RCS**: a Braze permite incluir variantes de SMS e RCS em uma única campanha, possibilitando comparar o desempenho de cada uma. Você pode adicionar variantes de SMS e RCS durante a primeira etapa da composição da mensagem.

{: start="6"}
6. Selecione um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups) habilitado para RCS. Ao selecionar um grupo de inscrições, a Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas usuários inscritos recebam a campanha. Somente códigos longos e curtos pertencentes a esse grupo de inscrições serão usados para enviar SMS aos usuários-alvo.
- **Fallback para SMS**: a Braze recomenda fortemente que todo grupo de inscrições que contenha um remetente RCS também inclua pelo menos um código SMS para fallback. Isso é importante para a entregabilidade nos casos em que as mensagens RCS não conseguem ser entregues. Alguns motivos para isso podem incluir incompatibilidade do dispositivo do usuário e cobertura incompleta da operadora em um determinado país ou região. Ao ativar o fallback para SMS, sua mensagem ainda será entregue ao usuário e você nunca perderá essa oportunidade de se conectar com ele.

{: start="7"}
7. Escolha entre SMS e RCS. Antes de compor mensagens RCS, escolha o canal pelo qual você enviará. Geralmente recomendamos usar RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS; no entanto, sempre oferecemos a opção de enviar por SMS para que você tenha máxima flexibilidade e controle.

![Opções para selecionar entre um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar variantes adicionais. Depois, você pode escolher **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas) usando o criador de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa de mensagem **SMS/MMS/RCS** no construtor de Canvas.
3. Dê à sua etapa um nome claro e significativo.
4. Selecione um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups) habilitado para RCS. Ao selecionar um grupo de inscrições, a Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas usuários inscritos recebam a campanha. Somente códigos longos e curtos pertencentes a esse grupo de inscrições serão usados para direcionar os usuários.
- **Fallback para SMS**: a Braze recomenda fortemente que todo grupo de inscrições que contenha um remetente RCS também inclua pelo menos um código SMS para fallback. Isso é importante para a entregabilidade nos casos em que as mensagens RCS não conseguem ser entregues. Alguns motivos para isso podem incluir incompatibilidade do dispositivo do usuário e cobertura incompleta da operadora em um determinado país ou região. Ao ativar o fallback para SMS, sua mensagem ainda será entregue ao usuário e você nunca perderá essa oportunidade de se conectar com ele.

{: start="5"}
5. Escolha entre SMS e RCS. Antes de compor mensagens RCS, escolha o canal pelo qual você enviará. Geralmente recomendamos usar RCS sempre que possível, pois há benefícios significativos de engajamento do usuário em relação ao SMS; no entanto, sempre oferecemos a opção de enviar por SMS para que você tenha máxima flexibilidade e controle.

![Opções para selecionar entre um tipo de mensagem RCS ou SMS/MMS.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Etapa 2: Selecione o tipo de mensagem RCS {#step-2-select-your-rcs-message-type}

Durante a criação de Campaigns e Canvas, escolha entre três tipos de mensagem RCS (Texto, Mídia, Rich Card) para configurar mensagens que melhor atendam aos seus objetivos.

![Opções para selecionar entre um tipo de mensagem Texto, Mídia ou Cartão.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs local %}
{% tab Texto %}
Como o nome indica, as mensagens RCS de texto focam no texto como meio. Se você digitar até 160 caracteres, a mensagem RCS será cobrada como uma mensagem somente de texto (ou "básica"). Se você exceder 160 caracteres ou usar um elemento rico, a mensagem será cobrada como uma mensagem RCS rica (ou "single") e o limite de caracteres aumenta para 3072.

#### Recursos {#features}

- Os tipos de mensagem de texto incluem todos os recursos de SMS. Apenas o rastreamento avançado é possível para rastreamento de cliques em URL, oferecendo granularidade de relatórios em nível de usuário.
- Além disso, agora você tem a opção de incluir botões de **Respostas sugeridas** e **Ações sugeridas** que impulsionam ações de alto engajamento do usuário, como visitar uma landing page ou fazer um pedido.
    - **Respostas sugeridas** são botões contendo respostas sugeridas para os usuários clicarem e pré-preencherem em sua entrada de texto, removendo o atrito de ter que pensar em uma resposta ao fornecer um conjunto limitado de opções.
    - **Ações sugeridas** são botões que iniciam uma ação no dispositivo do usuário. Eles geralmente consistem em uma ou duas palavras descritivas e um ícone visual para ajudar o usuário a entender o que o botão faz. Atualmente, a Braze suporta ações sugeridas do tipo OpenURL. Isso funciona de forma semelhante a uma URL, onde os usuários que selecionam o botão são redirecionados para uma página da web ou outro local identificado por URL.

![Um GIF de três ações sugeridas para uma mensagem RCS promovendo estilos de moda em tendência: "Fairytale royalty", "Edgy academia" e "Show me your other styles".]({% image_buster /assets/unlisted_docs/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Considerações {#considerations}

- Para limites de caracteres em texto, você pode escrever até 160 caracteres para uma mensagem RCS somente de texto (básica) ou até 3072 para uma mensagem RCS rica (single).
- Para limites de botões, você pode adicionar até cinco botões por mensagem. Esses botões podem ser ações sugeridas ou respostas sugeridas.
- Blocos de texto longos e muitos botões podem frustrar os usuários, então, sempre que possível, recomendamos optar pela simplicidade.
- Em alguns casos, pode ser mais econômico enviar mensagens de texto mais longas por RCS do que por SMS. Isso porque mensagens SMS mais longas são divididas em múltiplos segmentos, cada um sendo cobrado separadamente, enquanto as mensagens RCS são cobradas por mensagem. Entre em contato com o gerente de conta da Braze para mais detalhes e orientações.
{% endtab %}

{% tab Mídia %}
As mensagens RCS de mídia permitem usar formatos de mídia envolventes que não são possíveis com SMS. Isso inclui arquivos de imagem, vídeo e documento. Essas opções de mídia existem para ajudar você a engajar seu público de forma ainda mais profunda e possibilitar casos de uso totalmente novos. No momento, apenas o upload de imagens é suportado pela [Biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library).

#### Recursos

- Os tipos de mensagem de mídia suportam tudo o que está disponível nos tipos de mensagem de texto, incluindo texto, respostas sugeridas e ações sugeridas.
- Suporta arquivos de imagem, incluindo os formatos JPEG e PNG. Os arquivos de imagem estão disponíveis por upload da Biblioteca de mídia.
- Suporta arquivos de vídeo, incluindo os formatos MP4, MPEG e MV4. Os arquivos de vídeo podem ser adicionados por URL diretamente no criador de mensagens.
- Suporta arquivos de documento no formato PDF. Os arquivos de documento podem ser adicionados por URL diretamente no criador de mensagens.

![Criador de RCS com opção para fazer upload de um arquivo de mídia.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_type.png %})

#### Especificações de arquivo {#file-specifications}

| Tipo de arquivo | Especificações |
| --- | --- |
| Todos | - O tamanho do arquivo é limitado a 100 MB <br><br>- A URL do arquivo pode ter até 2048 caracteres |
| Arquivos de imagem | Formatos de arquivo suportados incluem JPG, JPEG e GIF |
| Arquivos de vídeo | Formatos de arquivo suportados incluem H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Arquivos de documento | Formatos de arquivo suportados: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Considerações

A experiência do usuário ao receber mensagens RCS pode variar ligeiramente com base em diversos fatores, incluindo cobertura da operadora no país de destino, hardware do dispositivo móvel e sistema operacional do dispositivo móvel.

De modo geral, o RCS se integra mais naturalmente com dispositivos Android (esse método foi amplamente implementado pelo Google, e o envio de mensagens RCS ponto a ponto é amplamente adotado na comunidade Android). Diferentes dispositivos podem renderizar a experiência em diferentes velocidades e qualidades.
{% endtab %}

{% tab Rich Card %}

{% alert important %}
Os Rich Cards estão em acesso antecipado. Entre em contato com o gerente de sucesso do cliente da Braze se tiver interesse em participar deste acesso antecipado.
{% endalert %}

Um Rich Card combina mídia, texto e botões em uma única mensagem, criando uma experiência mais intuitiva e envolvente para seus clientes. Você pode criar dois subtipos de Rich Cards: Texto e Mídia.

{% subtabs %}
{% subtab Texto %}
Um Rich Card de texto é uma mensagem concisa focada em texto. Ele deve incluir os seguintes elementos:

- **Título:** Até 200 caracteres. Pode ser personalizado com Liquid.
- **Descrição:** Até 2.000 caracteres. Pode ser personalizado com Liquid.
- **Botões:** Pelo menos um botão é obrigatório. Você pode adicionar até quatro botões com ações de **Resposta sugerida** ou **Abrir URL da web**.

{% endsubtab %}
{% subtab Mídia %}

Um Rich Card de mídia é uma mensagem visual contendo uma imagem ou vídeo. Ele deve incluir os seguintes elementos:

- **Mídia:** Uma imagem, GIF ou vídeo.
    - Miniaturas de vídeo personalizadas não são suportadas no acesso antecipado. O acesso antecipado suporta apenas um layout vertical com altura de mídia alta para arquivos de imagem e vídeo.
- **Botões:** Pelo menos um botão é obrigatório. Você pode adicionar até quatro botões com ações de **Resposta sugerida** ou **Abrir URL da web**.

{% endsubtab %}
{% endsubtabs %}

### Recursos
- **Botões do cartão** e **Sugestões:** Você pode adicionar até quatro botões e cinco sugestões (até 25 caracteres cada) na parte inferior do Rich Card (botões) ou na parte inferior da tela da mensagem (sugestões). O usuário pode selecionar essas opções de clique/toque para enviar uma resposta específica ou realizar uma ação específica.
- **Personalização:** Você pode usar Liquid para personalizar todos os elementos do Rich Card, incluindo título, descrição, mídia e botões.
- **Cobrança:** Os Rich Cards são cobrados como uma única mensagem RCS rica (ou "single").
- **Orientação sobre URLs:** URLs inseridas como texto simples no título ou na descrição não serão clicáveis. Você deve usar um **botão OpenURL** para direcionar os usuários a um site.

![Painel com opções para selecionar um Rich Card de Mídia ou Texto.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_text.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Etapa 3: Componha sua mensagem RCS {#step-3-compose-your-rcs-message}

Escreva sua mensagem usando idiomas e personalização ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid), [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) e emojis) conforme necessário. Certifique-se de seguir nossos limites de texto de mensagem para reduzir suas chances de cobranças excedentes.

{% alert important %}
Antes de prosseguir, leia nossas [diretrizes para limites de mensagens RCS](#step-2-select-your-rcs-message-type). As mensagens RCS são [cobradas por mensagem]({{site.baseurl}}/sms_rcs_billing_calculators), então é uma boa ideia entender as nuances do que pode ser incluído em cada tipo de mensagem RCS.
{% endalert %}

### Etapa 4: Pré-visualize e teste sua mensagem {#step-4-preview-and-test-your-message}

A Braze sempre recomenda pré-visualizar e testar sua mensagem antes de enviá-la. Acesse a guia **Teste** para enviar um RCS de teste para grupos de teste de conteúdo ou usuários individuais, ou pré-visualize a mensagem como um usuário diretamente na Braze.

### Etapa 5: Construa o restante da sua campanha ou Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

Em seguida, construa o restante da sua campanha ou Canvas. Consulte as seções a seguir para mais detalhes sobre como usar melhor nossas ferramentas para criar mensagens RCS.

#### Etapa 5.1: Escolha o cronograma de entrega ou gatilho {#step-51-choose-delivery-schedule-or-trigger}

As mensagens RCS podem ser entregues com base em um horário programado, uma ação ou um gatilho de API. Para saber mais, consulte [Programando sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types).

Para entrega baseada em ação, você também pode definir a duração da campanha e o horário de silêncio.

Especifique seus controles de entrega, como permitir que os usuários se tornem reelegíveis para receber a campanha ou ativar regras do limite de frequência.

#### Etapa 5.2: Escolha os usuários-alvo {#step-52-choose-users-to-target}

Direcione os usuários escolhendo segmentos ou filtros para restringir seu público. Você já deve ter selecionado o grupo de inscrições, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você.

{% multi_lang_include audience/target_audiences.md %}

Em seguida, você selecionará o público maior dos seus segmentos e restringirá ainda mais esse segmento com [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) opcionais. Você receberá automaticamente uma pré-visualização de como é a população aproximada desse segmento no momento. Tenha em mente que a composição exata do segmento é sempre calculada imediatamente antes do envio da mensagem.

{% alert tip %}
Tem interesse em usar o redirecionamento RCS para direcionar usuários com base em suas interações de SMS e RCS? Consulte [Redirecionamento]({{site.baseurl}}/sms_mms_rcs_user_retargeting).
{% endalert %}

#### Etapa 5.3: Escolha os eventos de conversão {#step-53-choose-conversion-events}

A Braze permite rastrear com que frequência os usuários realizam ações específicas, ou eventos de conversão, após receberem uma campanha. Você pode permitir um período de até 30 dias durante o qual uma conversão será contabilizada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso da sua campanha. Por exemplo:
- Se você está usando geotargeting para acionar uma mensagem RCS com o objetivo final de o usuário fazer uma compra, defina o evento de conversão como **Compra**.
- Se você está tentando direcionar o usuário para o seu app, defina o evento de conversão como **Inicia sessão**.

Você também pode definir eventos de conversão personalizados com base no seu caso de uso específico. Seja criativo em como você realmente deseja medir o sucesso da sua campanha.

### Etapa 6: Revise e implante {#step-6-review-and-deploy}

Depois de terminar de construir sua campanha ou Canvas, revise os detalhes, teste e envie!

Em seguida, consulte [Relatórios para SMS, MMS e RCS]({{site.baseurl}}/sms_mms_rcs_reporting) para saber como acessar os resultados das suas campanhas de RCS.

## Análise de dados e relatórios {#analytics-and-reporting}

A análise de dados da sua campanha ou Canvas inclui:

- Estatísticas de _Total de cliques_ que incluem todas as interações com o Rich Card, como cliques em botões e respostas ou ações sugeridas.
- Uma tabela detalhada que fornece uma visão mais detalhada dessas interações.

{% alert note %}
O acesso antecipado não inclui rastreamento de cliques em nível de usuário. O _Total de cliques_ será incrementado cada vez que um botão for clicado. Por exemplo, se um usuário clicar no mesmo botão três vezes, a contagem de cliques aumentará em três.
{% endalert %}

## Dicas {#tips}

### Usando Liquid para personalização de mensagens {#using-liquid-for-message-personalization}

Se você planeja usar Liquid, certifique-se de incluir um valor padrão para a personalização escolhida para que, se o perfil do destinatário estiver incompleto, ele não receba um espaço reservado em branco `Hi, !` em vez do nome ou de uma frase coerente.

### Gerando texto com IA {#generating-ai-copy}

Precisa de ajuda para criar textos envolventes? Experimente usar o [Assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Insira o nome ou a descrição de um produto, e a IA gerará textos de marketing semelhantes aos escritos por humanos para uso no seu envio de mensagens.

![Criador de mensagens com um ícone para abrir o assistente de copywriting com IA.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Perguntas frequentes {#frequently-asked-questions}

### Posso enviar mensagens de voz pré-gravadas com RCS? {#can-i-send-pre-recorded-voicemails-with-rcs}

Sim, você pode usar mensagens de mídia para suportar arquivos de áudio.