---
nav_title: Código personalizado e ponte JavaScript
article_title: Código personalizado e ponte JavaScript para Banners
page_order: 2
page_type: reference
description: "Saiba como usar HTML personalizado em Banners e a ponte JavaScript para registrar cliques e acionar ações da Braze."
channel:
  - banners
---

# Código personalizado e ponte JavaScript para Banners

> Ao usar o bloco do editor **Código Personalizado** no criador de Banner, você deve chamar `brazeBridge.logClick()` de dentro do seu HTML personalizado para registrar cliques. Os Banners usam a mesma ponte JavaScript que as mensagens no app em HTML, então os mesmos métodos e padrões se aplicam.

Se você usar HTML personalizado no design do seu Banner, o SDK da Braze não consegue anexar automaticamente listeners de clique aos elementos dentro do seu código personalizado. Você deve chamar explicitamente `brazeBridge.logClick()` para quaisquer elementos clicáveis (links, botões e similares) que deseja rastrear na análise de dados da campanha.

Por exemplo, para registrar um clique quando um usuário toca em um botão no seu HTML personalizado:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Para a referência completa da ponte JavaScript, incluindo todos os métodos disponíveis e opções de rastreamento de cliques, consulte a seção abaixo.

## Ponte JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}