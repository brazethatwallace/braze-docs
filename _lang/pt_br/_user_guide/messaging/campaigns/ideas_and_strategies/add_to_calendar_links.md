---
nav_title: Links de adicionar ao calendário
article_title: Links de adicionar ao calendário
page_order: 1
page_type: tutorial
description: "Este artigo descreve como incluir um link de adicionar ao calendário nas suas campanhas de e-mail."
channel: email

---

# Links de adicionar ao calendário {#add-to-calendar-links}

> Ao promover um evento, promoção ou compromisso, você pode ajudar os usuários a salvar facilmente o evento no calendário adicionando um link "adicionar ao calendário" nos seus e-mails.

Crie o rascunho do seu e-mail e escolha onde as duas opções de calendário aparecerão: um link para o Google Calendar e outro para outros calendários (como iCal ou Outlook). Use textos de link como "Adicionar ao Google Calendar" e "Adicionar ao iCal ou Outlook".

A forma de anexar as URLs depende do editor de e-mail que você usa:

- **Editor de arrastar e soltar:** Em um bloco **Paragraph**, selecione as palavras que deseja vincular, abra o controle **Link** na barra de ferramentas e cole a URL do [formato de URL](#url-format). Ou use um bloco **Button**, defina **Link type** como **Open web page** e cole a URL em **URL**.
- **Editor de HTML:** Use os controles de link de rich text para texto vinculado, ou adicione tags `<a href="...">` no seu HTML para cada URL de calendário.

## Formato da URL {#url-format}

Adicione a URL a seguir aos seus links, substituindo os espaços reservados. A única diferença entre essas duas URLs é que o Google Calendar precisa de um parâmetro adicional: `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal ou Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Substitua os seguintes valores:

- `EVENT_SUBJECT`: Título do evento
- `EVENT_LOCATION`: Local do evento
- `START_TIME`: Horário de início do evento no formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) em UTC
- `END_TIME`: Horário de término do evento no formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) em UTC
- `EVENT_DESCRIPTION`: Descrição do evento

Substitua quaisquer espaços pelo código de escape HTML `%20`. Por exemplo, um assunto "Meet Braze" ficaria como "Meet%20Braze".

Veja um exemplo de URL "Adicionar ao Google Calendar":

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Parâmetros adicionais {#additional-parameters}

Os parâmetros a seguir são opcionais e podem ser usados para definir aspectos adicionais de um evento.

- **Nome do organizador:** `&organizer=name`
- **Anexar URL relacionada ao evento:** `&attach=http://www.example.com/`
- **Duração:** `duration=30M`, como alternativa ao horário de término do evento (dtend), especifique uma duração como 1H ou 30M
- **Horário do lembrete, em minutos:** `&reminder=15`
- **Evento de dia inteiro:** `&allday=1`
- **UID:** parâmetro opcional para definir manualmente o identificador único do evento, permitindo que alguns apps de calendário atualizem o evento ao longo do tempo. A string @ics.agical.io é automaticamente adicionada ao valor.

Você também pode adicionar parâmetros adicionais para eventos recorrentes:
- **Eventos semanais:** `&recur=weekly`
- **Eventos mensais:** `&recur=monthly`
- **Fim da recorrência:** `&recuruntil=END_DATE`, em que `END_DATE` é a data e hora em que a recorrência termina no formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) em UTC

## Comportamento do link {#link-behavior}

Quando um usuário clica no link, os calendários transformam automaticamente os timestamps UTC nas URLs para refletir o fuso horário do usuário definido no calendário.

Por exemplo, se você abrir o link de exemplo "Adicionar ao Google Agenda" e seu calendário estiver definido como CST, o horário do evento será preenchido automaticamente de acordo com o que 15h UTC é em CST (10h).

### Google Agenda {#google-calendar}

Ao clicar, o Google Agenda abre em uma nova guia ou janela com os detalhes do evento pré-preenchidos no convite e prontos para o usuário salvar. Isso acontece tanto em dispositivos móveis quanto em desktop.

![Caixa de diálogo do Google Agenda para adicionar um evento com os detalhes do evento adicionados e prontos para salvar.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal ou Outlook {#ical-or-outlook}

Ao clicar no desktop, um arquivo ICS é baixado no local de download padrão do seu navegador (normalmente a pasta **Downloads**). O usuário então precisa abrir o arquivo ICS, que abre o iCal ou o Outlook e solicita que o usuário adicione o evento ao calendário.

![Calendário do iCal com uma caixa de diálogo para adicionar um novo evento, que solicita ao usuário selecionar um calendário e confirmar.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![Calendário do iCal com o evento adicionado.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

Em dispositivos móveis, o comportamento depende do dispositivo e do app de e-mail.

{% alert note %}
No iPhone, o app Mail e o Microsoft Outlook baixam o arquivo ICS para o dispositivo quando os usuários tocam no link do iCal, mas esses apps não abrem o Calendário a partir do link. Para adicionar o evento, abra o arquivo baixado em **Arquivos**, **Downloads** ou na visualização de anexos (dependendo do app), e então conclua as etapas no Calendário. A localização específica depende do app de e-mail e das configurações do iOS.
{% endalert %}

Em alguns outros apps de e-mail ou navegadores em dispositivos móveis, pressionar e segurar o link pode exibir uma opção para adicionar o evento ao calendário.

![Pop-up do iOS quando você pressiona e segura um link de calendário, que inclui um botão para "Adicionar ao Calendário".]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Para saber mais, consulte:
* [Criar eventos no Google Agenda](https://developers.google.com/calendar/api/guides/create-events)
* [Criar um link "Adicionar ao calendário" em uma mensagem de e-mail](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)