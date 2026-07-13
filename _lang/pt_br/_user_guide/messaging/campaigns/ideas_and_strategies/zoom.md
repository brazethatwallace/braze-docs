---
nav_title: Automatizar inscrição no Zoom
article_title: Automatizar inscrição no Zoom
page_order: 1
page_type: tutorial
description: "Este artigo descreve como automatizar a inscrição de participantes no Zoom em suas campanhas de e-mail, push e mensagens no app."
channel:
  - email
  - push
  - in-app messages

---

# Automatizar inscrição no Zoom {#automate-zoom-registration}

> Webinars se tornaram comuns entre os clientes da Braze nos últimos anos. Ao hospedar um webinar no Zoom, os usuários precisam inserir suas informações em uma landing page do Zoom para se inscrever.

Um fluxo de usuário recomendado está descrito abaixo:
1. Programe um webinar no Zoom e gere um `webinarId`.
2. Use a Braze para promover webinars do Zoom por e-mail, push e mensagens no app.
3. Inclua um botão de call-to-action nessas comunicações que adiciona automaticamente os usuários ao webinar.

Isso pode ser feito usando as [APIs do Zoom](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) para adicionar automaticamente um usuário a um webinar por meio de um clique em um botão dentro de um e-mail, push ou mensagem no app. Use o endpoint a seguir, substituindo o ID do webinar na requisição da API.

POST: `/meetings/{webinarId}/registrants`

Para saber mais, consulte o [endpoint Add webinar registrant](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate) do Zoom.<br><br>

{% tabs %}
{% tab Email %}

Crie uma campanha de e-mail com um botão de call-to-action no corpo da mensagem. Quando um usuário clicar no botão, redirecione-o para a landing page do webinar (com os parâmetros apropriados incluídos no link de redirecionamento).

Usando os parâmetros na URL para passar dados de usuários, crie uma chamada de API que seja disparada quando a página carregar para adicionar o usuário ao webinar.

![Mensagem de e-mail com templates Liquid usados para incluir nome, sobrenome, endereço de e-mail e cidade.]({% image_buster /assets/img/zoom/zoom1.png %})

Os usuários agora estão inscritos no webinar com as informações que já existem em seu perfil na Braze.

{% endtab %}
{% tab Push %}

1. Crie uma campanha de push<br><br>

	Defina o comportamento ao clicar do botão para direcionar à landing page do webinar.<br>

	![Direcionando para o webinar quando um botão é clicado.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Um exemplo simples de landing page para usuários que se inscrevem via clique no botão de um push. Informe ao usuário no que ele se inscreveu e confirme a inscrição:<br>

	![Landing page de confirmação do webinar exibida após o usuário se inscrever pela Braze.]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Crie uma campanha de webhook disparada pela mensagem no app ou pelo clique no botão.<br><br>
 	Usando os dados de usuários existentes no perfil da Braze, inscreva o usuário no webinar.<br>

	![Uma campanha baseada em ação que será enviada aos usuários que clicaram em um botão de uma campanha específica.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Exemplo de chamada de webhook para o endpoint do Zoom.<br>
	{% raw %}
	```http
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. Os usuários agora estão inscritos no webinar com as informações que já existem em seu perfil na Braze.

{% endtab %}
{% tab In-app message %}

1. Crie uma campanha de mensagem no app<br><br>

	Defina o comportamento ao clicar do botão para direcionar à landing page do webinar.<br>

	![Direcionando para o webinar quando um botão é clicado.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Um exemplo simples de landing page para usuários que se inscrevem via clique no botão de uma mensagem no app. Informe ao usuário no que ele se inscreveu e confirme a inscrição:<br>

	![Landing page de confirmação do webinar exibida após o usuário se inscrever pela Braze.]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Crie uma campanha de webhook disparada pela mensagem no app ou pelo clique no botão.<br><br>
	Usando os dados de usuários existentes no perfil da Braze, inscreva o usuário no webinar.<br>

	![Uma campanha baseada em ação que será enviada aos usuários que clicaram em um botão de uma campanha específica.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Exemplo de chamada de webhook para o endpoint do Zoom.<br>
	{% raw %}
	```http
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. Os usuários agora estão inscritos no webinar com as informações que já existem em seu perfil na Braze.

{% endtab %}
{% endtabs %}