---
nav_title: Cartões de contato
article_title: Cartões de contato
page_order: 3
description: "Este artigo de referência aborda como criar um cartão de contato para incluir nas suas mensagens MMS e SMS."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS

---

# Cartões de contato {#contact-cards}

> Cartões de contato (às vezes conhecidos como vCard ou Virtual Contact Files (VCF)) são um formato de arquivo padronizado para enviar informações comerciais e de contato que podem ser facilmente importadas para catálogos de endereços ou listas de contatos.

{% alert note %}
O envio de um cartão de contato é cobrado como MMS. Revise o volume esperado de MMS e o uso de créditos de mensagem ou de ação ao criar cartões de contato, e confirme os custos na [página de Faturamento]({{site.baseurl}}/user_guide/administer/global/billing) da Braze.
{% endalert %}

Os cartões de contato podem ser criados [programaticamente](https://www.twilio.com/blog/send-vcard-twilio-sms) e enviados para a [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#media-library) da Braze, ou criados por meio do nosso gerador de cartões de contato integrado. Esses cartões podem receber propriedades comuns, como o nome da sua empresa, número de telefone, endereço, e-mail e uma pequena foto. Para começar a criar cartões de contato, primeiro certifique-se de que o MMS está configurado na Braze.

## Gerador de cartões de contato {#contact-card-generator}

### Etapa 1: Atribuir nome {#step-1-assign-name}

Os cartões de contato podem ser criados a partir do criador de SMS e MMS. Selecione a guia **Contact Card Generator** para começar.

Em seguida, você será solicitado a inserir o nome ou apelido da sua empresa. Esse é o nome que seus usuários verão ao salvar o cartão. Um limite de 20 caracteres é aplicado para garantir que o usuário consiga ver o nome completo da empresa ou alias nos contatos e no app de mensagens.

![A guia do gerador de cartão de contato.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### Etapa 2: Atribuir número de telefone {#step-2-assign-phone-number}

Selecione o grupo de inscrições e o número de telefone desejado nas opções disponíveis no menu suspenso. Esse número será listado no seu cartão de contato e ficará disponível no telefone do destinatário para enviar mensagens de texto após ser salvo.

Observe que códigos alfanuméricos não são compatíveis com envio de mensagens bidirecional e não são suportados para cartões de contato.

### Etapa 3: Campos opcionais {#step-3-optional-fields}

![Campos opcionais para o gerador de cartões de contato.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### Fazer upload da foto de contato do cartão {#upload-contact-card-contact-photo}

Você pode fazer upload de uma foto de contato opcional para o seu cartão de contato. Recomendamos uma imagem JPEG ou PNG de 240 x 240&nbsp;px. Qualquer imagem de alta resolução enviada será redimensionada para 240 x 240&nbsp;px para garantir a entregabilidade da mensagem, já que mensagens MMS maiores que 5&nbsp;MB podem falhar.

{% alert note %}
A imagem enviada aparece no cartão de contato quando o destinatário o abre; o [campo **Full Name**](#add-more-information) determina o que aparece na miniatura do chat de mensagens.
{% endalert %}

#### Adicionar mais informações {#add-more-information}

Outros campos permitem inserir seu nome, subtítulo, endereço e outras informações de contato que o usuário pode querer ter disponíveis.

O campo **Full Name** determina as iniciais que aparecem na miniatura do chat de mensagens. Quando o campo é marcado como opcional e deixado em branco, os destinatários veem um círculo branco em vez de iniciais.

### Etapa 4: Salvar seu cartão de contato {#step-4-saving-your-contact-card}

Depois de preencher todos os campos necessários, selecione **Generate Contact Card**, e ele será automaticamente anexado à sua Campaign ou Canvas. A partir daqui, você pode adicionar uma mensagem, testar seu cartão de contato e lançar sua Campaign ou Canvas.

O cartão de contato também será salvo na [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#media-library) para reutilização fácil em futuras Campaigns e Canvas.

## Adicionando um cartão de contato existente {#adding-an-existing-contact-card}

Para adicionar um cartão de contato existente, crie uma Campaign ou Canvas e selecione o grupo de inscrições desejado. Em seguida, uma opção **Add Media** aparecerá na janela do criador de mensagens. Aqui, você pode fazer upload de um arquivo de cartão de contato existente ou localizar um pela Biblioteca de mídia.