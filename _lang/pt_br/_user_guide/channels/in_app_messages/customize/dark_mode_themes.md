---
nav_title: Temas de modo escuro
article_title: Temas de modo escuro
page_order: 2
description: "Este artigo de referência aborda o suporte ao modo escuro nas mensagens no app da Braze, incluindo como definir um tema de modo escuro e considerações de compatibilidade."
channel:
  - in-app messages

---

# Temas de modo escuro {#dark-mode-themes}

> Este artigo se aplica ao [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional). O modo escuro oferece aos usuários a oportunidade de definir uma preferência de cor em todo o sistema (introduzido no [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) e no [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Os temas "escuros" têm como objetivo economizar bateria e reduzir o cansaço visual dos usuários, ao mesmo tempo que oferecem aos desenvolvedores de apps uma forma de implementar temas de cores escuras.

As mensagens no app da Braze permitem adicionar um tema escuro alternativo para entregar a mensagem com as cores certas aos seus usuários com base na preferência deles e manter a consistência com o design do seu app.

## Como o modo escuro funciona {#how-dark-mode-works}

Usuários com versões a partir do Android 10 ou iOS 13 podem ativar ou desativar o modo escuro nas configurações do dispositivo.

Quando o modo escuro está ativado, os menus e telas nativos do dispositivo (notificações por push, configurações do dispositivo, etc.) mudam para um cinza escuro. Os apps também podem optar por oferecer suporte ao modo escuro especificando os temas alternativos no código do app.

## Definindo um tema de modo escuro {#setting-a-dark-mode-theme}

O modo escuro, localizado na guia **Design** ao [criar uma mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional), permite adicionar um tema de cores alternativo para usuários que estão no modo escuro em seus dispositivos.

![Usuário alternando entre os estilos de modo claro e modo escuro na guia Estilo ao criar uma mensagem no app.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Quando essa opção está ativada, você pode escolher cores de tema escuro para sua mensagem no app usando o seletor de cores ou selecionando [perfis de cores]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#color-profile) existentes para reutilizar temas escuros ou claros já criados.

{% alert note %}
Você ainda pode usar esse recurso mesmo que seu app não ofereça seu próprio tema escuro. No entanto, dispositivos que não suportam o modo escuro exibirão o tema claro por padrão. Alterar o tema do dispositivo no Android enquanto uma mensagem no app está sendo exibida não mudará qual tema é usado para essa mensagem no app.
{% endalert %}

### Usando o modo escuro de forma consistente {#using-dark-mode-consistently}

Para usar o modo escuro em todas as mensagens no app, primeiro crie um perfil de cores alinhado com o seu tema de modo escuro.

1. Acesse **Conteúdo** > **Mensagem no app**.
2. Selecione **Criar modelos** e escolha [Perfil de cores]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#color-profile) no menu suspenso.
3. Crie e salve seu perfil de cores.

Ao criar uma versão em modo escuro de uma mensagem no app, você pode selecionar esse perfil de cores para manter a aparência das suas mensagens no app consistente.

## Compatibilidade {#compatibility}

- Seus usuários devem estar em dispositivos iOS versão 13 ou superior, ou dispositivos Android versão 10 ou superior.
- É necessário o SDK da Braze para iOS v3.21.0+ e o SDK da Braze para Android v3.8.0+.

{% alert note %}
Os apps com modo escuro foram introduzidos com o Android 10 e o iOS 13. Usuários que não atualizaram seus telefones para pelo menos essas versões verão apenas o tema claro. <br><br>As campanhas ainda serão entregues a todos os usuários elegíveis para o público que você selecionou, independentemente da configuração de modo escuro ou da versão do sistema operacional dos usuários.
{% endalert %}

## Usando mensagens no app em HTML {#using-html-in-app-messages}

Para criar um tema escuro e claro para mensagens no app em HTML, você pode usar o recurso de mídia CSS [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) para detectar a preferência do usuário.

Por exemplo:

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

