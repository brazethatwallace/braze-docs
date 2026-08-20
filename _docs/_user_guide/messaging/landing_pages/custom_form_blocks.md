---
nav_title: Create custom form blocks
article_title: Create custom form blocks on landing pages
page_order: 6
page_type: reference
description: "Learn how to build custom interactive form inputs on Braze landing pages so their values validate and submit alongside standard form blocks."
---

# Create custom form blocks on landing pages

> Braze landing page [form blocks]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) capture standard inputs, such as text fields, checkboxes, and dropdowns. Custom form blocks expand possibilities by letting you build your own interactive elements, such as a star rating, an emoji sentiment picker, or a scratch-off card.

When a visitor submits the custom form, the value they selected is validated and saved alongside your standard fields, and then sent to Braze as a custom user attribute. This lets you collect richer, more engaging input without leaving the landing page editor.

You build custom form blocks with a single JavaScript helper, `window.brazeHelpers.forms.registerFormInput`, which you call from a **Custom Code** block on the landing page.

{% alert note %}
Surveys and in-app messages have their own form blocks, but `registerFormInput`—the JavaScript API for connecting a custom-coded UI to a form block—is available only on landing pages.
{% endalert %}

## How it works

A custom form input is any element on your landing page whose value you want to capture and submit with the form. You connect that element to the Braze form system by registering it. Registration tells Braze which element to watch, how to read its current value, and what to do with that value when the form is submitted.

1. Build your custom UI inside a **Custom Code** block on the landing page and give it a stable CSS selector, such as an `id`.
2. Register the element by calling `window.brazeHelpers.forms.registerFormInput` with a configuration object.
3. Braze calls your `getValue` function to read the current value when it needs it.
4. If the field is required, or you provide an `onValidate` function, Braze blocks submission until the value passes, and flags an invalid element with a CSS class you can style. See [Validation and required fields](#validation-and-required-fields).
5. When the form is submitted and validation passes, Braze calls your `onSubmit` function, where you can call the Braze SDK to log information such as a custom user attribute.

Because you supply the functions that read, validate, and submit the value, this approach works with nearly any custom form element, so you're not limited to the standard field types in the editor.

## Basic framework

The simplest registration targets one element, treats it as required, reads its value from a data attribute, and writes that value to a custom user attribute when the form is submitted. Wrap the call in a `DOMContentLoaded` listener, as in the examples on this page, so the element exists before `registerFormInput` runs:

```js
document.addEventListener("DOMContentLoaded", () => {
  window.brazeHelpers.forms.registerFormInput({
    selector: "#my-custom-input",
    isRequired: true,
    getValue: (element) => element.dataset.value ?? null,
    onSubmit: (value) => {
      window.brazeBridge.getUser().setCustomUserAttribute("my_attribute", value);
    },
  });
});
```

Call `registerFormInput` once for each custom input on the page. Standard form fields placed through the landing page editor don't need to be registered; registration is only for the custom inputs you build in a **Custom Code** block.

## Configuration reference

`registerFormInput` accepts a single configuration object. Expressed as a function signature, the full shape is:

```js
window.brazeHelpers.forms.registerFormInput({
  // Provide exactly one of `selector` or `element` to identify the input.
  selector?: string,
  element?: HTMLElement,
  isRequired?: boolean | Promise<boolean>,
  getValue: (element: HTMLElement) => value,
  onValidate?: (value, element: HTMLElement) => boolean | Promise<boolean>,
  onSubmit?: (value, element: HTMLElement) => void | Promise<void>,
});
```

At minimum, you must supply a way to locate the element (`selector` or `element`) and a `getValue` function. Everything else is optional.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `selector` | `string` | Yes (or `element`) | A CSS selector that matches your custom element, for example `"#scratch-card"`. Braze resolves it lazily with `querySelector` at validation and submit time, so it can match an element added to the DOM after `registerFormInput` runs. |
| `element` | `HTMLElement` | Yes (or `selector`) | A direct reference to the element, used instead of `selector`. It's only used while the element remains attached to the page, and it takes precedence over `selector` when both are provided. |
| `isRequired` | `boolean \| Promise<boolean>` | No | When `true`, the form can't be submitted until the input has a non-empty value—`null`, `undefined`, empty strings (including whitespace-only strings), and empty arrays all count as empty. May also be a promise that resolves to a boolean, which Braze re-evaluates each time the input is validated, so you can decide the required state at runtime. Defaults to `false`. See [Validation and required fields](#validation-and-required-fields) for the full validation order. |
| `getValue` | `function` | Yes | Returns the current value of the input. Braze passes the matched element as an argument, so you can read the value from the DOM, for example `element.dataset.sentiment`, or from a variable in your own code. Return `null` when there's no value yet. |
| `onValidate` | `function` | No | Receives the current value and the matched element, and must return `boolean \| Promise<boolean>`—the same return type as `isRequired`—where `true` means the value is valid and `false` means it isn't. Use it to enforce rules beyond having a value, for example that the value is one of an allowed set. If omitted, only `isRequired` and native constraint validation are enforced. |
| `onSubmit` | `function` | No | Runs when the form is submitted and validation passes. Receives the current value and the matched element. This is where you log the value to Braze, typically with `setCustomUserAttribute`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Configuration reference" }

### Act on the value in onSubmit

`onSubmit` is a plain JavaScript callback, so you can act on the captured value however your integration needs. Because `onSubmit` runs as part of form submission, `brazeBridge` calls made inside it work as expected, even for a visitor who opened the landing page anonymously. See [Bridge availability]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#bridge-availability) for the other situation where bridge calls work.

The most common pattern is writing the captured value to the user profile with the [Braze JavaScript bridge]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) available on landing pages:

```js
window.brazeBridge.getUser().setCustomUserAttribute("attribute_name", value);
```

Use a custom attribute name that already exists, or one you want to create, in your workspace. The value you pass is stored on the user's profile and can then be used for segmentation, personalization, and triggering follow-up messages.

You aren't limited to custom attributes. From the same callback, you can call any [`brazeBridge.getUser()` method]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#supported-methods). For example, to add the user to a subscription group, set a standard attribute, log a custom event, or send the value to your own API endpoint.

{% alert note %}
You don't need to call `requestImmediateDataFlush` inside `onSubmit`. The form submission process automatically flushes all data to Braze after your `onSubmit` callback completes.
{% endalert %}

## Examples

The following examples are complete and self-contained. Each one is a single block containing markup, a `<script>` tag, and a `<style>` tag that you paste into one **Custom Code** (HTML) block on your landing page. The `registerFormInput` call near the end of each script connects the custom input to the Braze form. Hover over a code sample and select the copy icon to copy it.

{% alert important %}
These examples run entirely in the visitor's browser. For the scratch-off example, the "prize" is chosen by JavaScript in the visitor's browser, so a technically savvy visitor could modify that code to get whichever outcome they want. Don't rely on this pattern for rewards, discounts, or other outcomes that require strict per-visitor enforcement. Validate anything security- or revenue-sensitive on your own servers instead.
{% endalert %}

<div class="scrollable-code-examples" markdown="1">

{% tabs local %}
{% tab Sentiment picker %}

**Goal:** The visitor selects a happy or unhappy face, and their choice is written to a string custom attribute named `feedback_sentiment`.

Paste the following into a single **Custom Code** (HTML) block:

```html
<div id="sentiment-picker" class="sentiment-picker">
  <button type="button" data-sentiment="positive" aria-label="Happy">🙂</button>
  <button type="button" data-sentiment="negative" aria-label="Unhappy">🙁</button>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const picker = document.getElementById("sentiment-picker");

    picker.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => {
        picker.dataset.sentiment = button.dataset.sentiment;
        picker.querySelectorAll("button").forEach((b) => b.classList.remove("selected"));
        button.classList.add("selected");
      });
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#sentiment-picker",
      isRequired: true,
      getValue: (element) => element.dataset.sentiment ?? null,
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("feedback_sentiment", value);
      },
    });
  });
</script>

<style>
  .sentiment-picker {
    display: flex;
    gap: 16px;
    justify-content: center;
    font-size: 40px;
  }

  .sentiment-picker button {
    background: none;
    border: 2px solid transparent;
    border-radius: 12px;
    cursor: pointer;
    line-height: 1;
    padding: 8px;
  }

  .sentiment-picker button.selected {
    border-color: #1f2933;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .sentiment-picker.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**How it works:** Selecting a button stores its `data-sentiment` value on the container element. `getValue` reads that value back from the container element Braze passes in. Because `isRequired` is `true`, the form doesn't submit until the visitor chooses a face, and the container is flagged with the `bz-validation-error` class while it's empty. On submit, the chosen value (`"positive"` or `"negative"`) is written to `feedback_sentiment`.

{% endtab %}
{% tab Scratch-off %}

**Goal:** The visitor scratches a card to reveal one of three discounts (10% Off, 20% Off, or 25% Off), and the discount is written to a string custom attribute named `scratch_off_reward`.

This example draws a scratch-off card on an HTML Canvas. A reward is chosen at random when the page loads and is hidden under an opaque layer that the visitor scratches away. You can swap the Canvas approach for any scratch widget you prefer; only the `registerFormInput` call connects it to Braze. Paste the following into a single **Custom Code** (HTML) block:

```html
<div id="scratch-card" class="scratch-card" data-reward="">
  <span class="scratch-card__reward"></span>
  <canvas class="scratch-card__surface" width="300" height="150"></canvas>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const rewards = ["10% Off", "20% Off", "25% Off"];

    const card = document.getElementById("scratch-card");
    const label = card.querySelector(".scratch-card__reward");
    const canvas = card.querySelector(".scratch-card__surface");
    const ctx = canvas.getContext("2d");

    // Randomly assign which reward this visitor will reveal.
    const reward = rewards[Math.floor(Math.random() * rewards.length)];
    label.textContent = reward;

    // Paint the opaque scratch layer over the reward.
    ctx.fillStyle = "#b3b3b3";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.globalCompositeOperation = "destination-out";

    let isScratching = false;

    function scratchAt(event) {
      const rect = canvas.getBoundingClientRect();
      ctx.beginPath();
      ctx.arc(event.clientX - rect.left, event.clientY - rect.top, 18, 0, Math.PI * 2);
      ctx.fill();
    }

    canvas.addEventListener("pointerdown", () => { isScratching = true; });
    canvas.addEventListener("pointermove", (event) => {
      if (isScratching) scratchAt(event);
    });
    canvas.addEventListener("pointerup", () => {
      isScratching = false;
      // The visitor has scratched the card, so record the revealed reward.
      card.dataset.reward = reward;
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#scratch-card",
      isRequired: true,
      getValue: (element) => element.dataset.reward || null,
      onValidate: (value) => rewards.includes(value),
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("scratch_off_reward", value);
      },
    });
  });
</script>

<style>
  .scratch-card {
    position: relative;
    width: 300px;
    height: 150px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }

  /* The reward sits underneath and is revealed as the canvas is scratched away. */
  .scratch-card__reward {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    font-weight: 700;
    color: #1f2933;
  }

  .scratch-card__surface {
    position: absolute;
    inset: 0;
    border-radius: 12px;
    cursor: pointer;
    touch-action: none;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .scratch-card.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**How it works:** When the page loads, the script randomly picks one of the three rewards and paints an opaque layer over it on the Canvas. As the visitor drags across the Canvas, the `"destination-out"` composite mode erases that layer and reveals the reward beneath. On `pointerup`, the revealed reward is written to the card's `data-reward` attribute. `getValue` reads it back from there, `onValidate` confirms it's one of the three defined rewards, and `isRequired` prevents submission until the card has been scratched. On submit, the revealed discount (for example, `"20% Off"`) is written to `scratch_off_reward`.

{% endtab %}
{% tab Campaign attribution %}

**Goal:** Capture the campaign that referred the visitor to the landing page and log it as a custom event property for downstream reporting and attribution.

This example demonstrates how to attribute a landing page form submission to a specific campaign. By adding a Liquid variable like {% raw %}`{{campaign.${api_id}}}`{% endraw %} to your landing page URL in email, SMS, or WhatsApp messages, you can pass the campaign identifier to the landing page. The custom form block then reads this parameter from the URL and logs it as a custom event with the campaign API ID as an event property, making it easier to track which campaigns are driving form submissions.

Paste the following into a single **Custom Code** (HTML) block:

```html
<input type="hidden" id="campaign-attribution" value="" />

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const hiddenInput = document.getElementById("campaign-attribution");
    const campaignApiId = new URLSearchParams(window.location.search).get("campaign_api_id");

    if (campaignApiId) {
      hiddenInput.value = campaignApiId;
    }

    window.brazeHelpers.forms.registerFormInput({
      selector: "#campaign-attribution",
      isRequired: false,
      getValue: (element) => element.value || null,
      onSubmit: async (value) => {
        if (!value) {
          return;
        }

        await window.brazeBridge.logCustomEvent("landing_page_form_submitted", {
          campaign_api_id: value,
        });
      },
    });
  });
</script>
```

**How it works:** When you create an email, SMS, or WhatsApp message that links to your landing page, append the campaign identifier to the URL using Liquid templating: {% raw %}`https://your-landing-page.com?campaign_api_id={{campaign.${api_id}}}`{% endraw %}. When a visitor arrives at the landing page from that message, the script reads the `campaign_api_id` parameter from the URL and stores it in a hidden input field. On form submission, if a campaign ID is present, the `onSubmit` callback logs a custom event named `landing_page_form_submitted` with the campaign API ID as an event property. This event appears in Currents and can be used for reporting, segmentation, and attribution analysis.

{% alert tip %}
You can extend this pattern to capture additional URL parameters such as message variation, Canvas step, or any other Liquid variable you want to pass to the landing page for attribution purposes.
{% endalert %}

{% endtab %}
{% endtabs %}

</div>

## Validation and required fields

An input must pass all of the following layers that apply to it before the form can be submitted:

1. **`isRequired`** gates submission on the presence of a non-empty value. Return `null` from `getValue` when the input has no value yet so Braze can tell it's empty. Empty strings (including whitespace-only strings) and empty arrays are also treated as empty, while `0` and `false` count as present values. `isRequired` can be a boolean or a promise that resolves to one, and it's re-evaluated each time the input is validated.
2. **Native constraint validation.** If the matched element supports the standard HTML `checkValidity()` API, for example a native `<input>` with `required`, `pattern`, `min`, or `max`, Braze runs it and blocks submission when it fails. For fully custom, non-native elements (a `div`, a `canvas`, and so on), this check always passes, so it never interferes with your own logic.
3. **`onValidate`** gates submission on your own rules. It receives the current value and the matched element, and must return `boolean \| Promise<boolean>`—the same return type as `isRequired`—where `true` means the value is valid and `false` means it isn't. Use it for allowed-value checks, format checks, ranges, or any logic you can express in JavaScript.

### Error styling

Whenever an input fails validation, Braze adds the CSS class `bz-validation-error` to the element matched by your `selector` or `element`, and removes the class when the input becomes valid again. Style the invalid state however you like, for example an outline or border that draws attention to the offending input, by adding a rule that targets your element combined with the `bz-validation-error` class:

```css
#my-custom-input.bz-validation-error {
  outline: 3px solid #f94144;
  outline-offset: 4px;
}
```

Styling the error state is optional but recommended, so visitors can see which custom input is blocking submission. Each [example](#examples) on this page includes a `bz-validation-error` rule.

## Best practices

- Use a stable, unique selector. An `id` is the safest choice. Avoid selectors that could match more than one element.
- Return `null`, not an empty string or `undefined`, when there's no value, so required checks behave predictably. Empty strings and empty arrays are also treated as empty, but `null` is the clearest signal of "no value."
- Keep `getValue` cheap and synchronous. Braze can call it more than once, so it should read and return the current value rather than perform heavy work.
- Style the `bz-validation-error` state so visitors can see which custom input is blocking submission.
- Define your custom attribute names ahead of time and keep them consistent so you can reliably segment on the data later.
- Test the full submission. Confirm the attribute appears on the user profile after submitting, and that required and validation rules block submission as expected.

## Troubleshooting

### The form submits even though nothing was selected
Make sure `isRequired` is set to `true`. Braze treats `null`, `undefined`, empty strings (including whitespace-only strings), and empty arrays as no value—if `getValue` is returning something else (for example, a non-empty default or placeholder) when nothing has been selected, the required check won't catch it.

### The value doesn't appear on the profile
Confirm `onSubmit` calls `window.brazeBridge.getUser().setCustomUserAttribute` with the correct attribute name, and that the **Custom Code** block is on the same landing page as the form.

### Registration seems to do nothing
Check that the selector matches an element that exists in the DOM when `registerFormInput` runs, and that the script runs after that element is rendered. Then open your browser's developer console: `registerFormInput` validates its configuration and, when something is wrong (for example, a missing `getValue`, a selector that isn't a valid CSS selector, or a property of the wrong type), it ignores the registration and logs a warning prefixed with `[brazeHelpers.forms.registerFormInput]` describing what was invalid.

## Related content

- [JavaScript bridge for landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) covers the full `brazeBridge` reference used in `onSubmit`.
- [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
