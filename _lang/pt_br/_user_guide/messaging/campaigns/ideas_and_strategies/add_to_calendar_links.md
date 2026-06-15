---
nav_title: Links de adicionar ao calendário
article_title: Links de adicionar ao calendário
page_order: 1
page_type: tutorial
description: "Este artigo descreve como incluir um link de adicionar ao calendário nas suas campanhas de e-mail."
channel: email

---

# Links de adicionar ao calendário

> Ao promover um evento, promoção ou compromisso, você pode ajudar os usuários a salvar facilmente o evento no calendário adicionando um link "adicionar ao calendário" nos seus e-mails.

Para isso, crie o rascunho do seu e-mail e defina onde deseja posicionar os links. Em seguida, adicione duas opções: uma para o Google Calendar e outra para outros calendários (como iCal ou Outlook). Por exemplo, "Adicionar ao Google Calendar" e "Adicionar ao iCal ou Outlook".

![Caixa de diálogo de link ao adicionar um link no dashboard. A guia "Link Info" está selecionada e o texto está definido como "Add to Google Calendar".]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## Formato da URL

Adicione a seguinte URL aos seus links, substituindo os espaços reservados. A única diferença entre essas duas URLs é que o Google Calendar precisa de um parâmetro adicional: `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal or Outlook %}

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

Substitua os espaços pelo código de escape HTML `%20`. Por exemplo, um assunto "Meet Braze" ficaria "Meet%20Braze".

Veja um exemplo de URL "Adicionar ao Google Calendar":

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Parâmetros adicionais

Os parâmetros a seguir são opcionais e podem ser usados para definir aspectos adicionais de um evento.

- **Nome do organizador:** `&organizer=name`
- **Anexar URL relacionada ao evento:** `&attach=http://www.example.com/`
- **Duração:** `duration=30M`, como alternativa ao horário de término do evento (dtend), especifique uma duração como 1H ou 30M
- **Lembrete em minutos:** `&reminder=15`
- **Evento de dia inteiro:** `&allday=1`
- **ID do usuário:** parâmetro opcional para definir manualmente o identificador único do evento, permitindo que alguns apps de calendário atualizem o evento ao longo do tempo. A string @ics.agical.io é automaticamente adicionada ao valor.

Você também pode adicionar parâmetros adicionais para eventos recorrentes:
- **Eventos semanais:** `&recur=weekly`
- **Eventos mensais:** `&recur=monthly`
- **Fim da recorrência:** `&recuruntil=END_DATE`, onde `END_DATE` é a data e hora em que a recorrência termina no formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) em UTC

## Comportamento do link

Quando um usuário clica no link, os calendários transformam automaticamente os timestamps UTC nas URLs para refletir o fuso horário configurado no calendário do usuário.

Por exemplo, se você abrir o link de exemplo "Adicionar ao Google Calendar" e seu calendário estiver configurado para CST, o horário do evento será preenchido automaticamente de acordo com o que 15h UTC representa em CST (10h).

### Google Calendar

Ao clicar, o Google Calendar abre em uma nova guia ou janela com os detalhes do evento preenchidos no convite, pronto para o usuário salvar. Isso acontece tanto no celular quanto no desktop.

![Caixa de diálogo do Google Calendar para adicionar um evento com os detalhes do evento preenchidos e prontos para salvar.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal ou Outlook

Ao clicar no desktop, um arquivo ICS é baixado. O usuário precisa então abrir o arquivo ICS, que abrirá o iCal ou Outlook e solicitará que o usuário adicione o evento ao calendário.

![Calendário iCal com uma caixa de diálogo para adicionar um novo evento, que solicita ao usuário selecionar um calendário e confirmar.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![Calendário iCal com o evento adicionado.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

No celular, os usuários precisam manter o link pressionado, o que exibirá a opção de adicioná-lo ao calendário.

![Pop-up do iOS ao manter pressionado um link de calendário, que inclui um botão "Add to Calendar".]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Para saber mais, consulte:
* [Create events for Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Create an Add to calendar link in an email message](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)