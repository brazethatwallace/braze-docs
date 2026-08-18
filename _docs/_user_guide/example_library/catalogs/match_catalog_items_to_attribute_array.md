---
nav_title: Match catalog items to an attribute array
article_title: Match catalog items to a custom attribute array
page_order: 2
page_type: reference
description: "Use a catalog selection and Liquid to show catalog rows whose names or IDs appear in a custom attribute array, such as a wishlist."
---

# Match catalog items to a custom attribute array

> When each user keeps a list of saved product names on their profile, use a catalog selection plus Liquid to show only catalog rows that appear in that list—for example, a wishlist email.

## About this example

Flash & Thread stores each customer's saved product names in a string array custom attribute (`saved_product_names`). Their catalog holds full product details (category, price, image URL, inventory).

Catalog selections can filter catalog columns against static or Liquid values, including array fields on catalog rows. They do not filter a catalog row against values stored in a user profile array. To personalize from the user's list, return a broad set of catalog items with a selection, then use Liquid to keep only rows that match the profile array.

This pattern:

1. Assigns the user's array custom attribute to a Liquid variable.
2. Calls `catalog_selection_items` for a pre-filtered catalog selection (up to 50 items).
3. Loops over `items` and uses `contains` to match each catalog field (for example `name` or `id`) against the array.

{% alert important %}
This pattern works only when the selection's result set (up to 50 catalog rows) can plausibly contain each user's saved items—for example, small catalogs, or catalogs where filters narrow the selection tightly enough to cover a typical list. If a user's saved items fall outside the 50 rows returned, the loop finds no matches and the message renders nothing for those items—no filter resolves this in the general case, because the selection can't match against the user's profile array.
{% endalert %}

## Considerations

- Test Liquid and catalog data in a staging workspace before you send to customers.
- Because a selection returns at most 50 catalog rows, add filters (for example, in stock, active category, or price band) that keep each user's likely saved items within that result set.
- This example uses a string array on the user profile.
- For an array of objects, match on a property inside each object (for example `product_id`) and adjust the `contains` check or use a `for` loop over objects. See [Array of objects]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/).
- `contains` behavior depends on attribute type; for arrays, use `contains` rather than `==`. See [Conditional logic]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/).
- Match on stable identifiers (for example catalog `id`) when product names can change or duplicate.
- The Liquid snippets in this article are examples. Validate rendering in your channels (email HTML, push, and so on).

## Setup

This example assumes:

| Asset | Details |
| --- | --- |
| Custom attribute | `saved_product_names` — string array (for example `["linen_shirt", "trail_jacket", "canvas_tote"]`) |
| Catalog | `apparel_products` with columns `id`, `category`, `name`, `price`, `inventory`, `image_url` |
| Selection | `in_stock_apparel` on `apparel_products`, results limit 50, with filters that exclude irrelevant rows (for example `inventory` greater than `0`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Setup" }

### Step 1: Create the catalog and selection

1. Import or sync product rows into a catalog named `apparel_products`.
2. Create a selection (for example `in_stock_apparel`) that returns as many relevant rows as you need, up to the 50 item limit.
3. Add selection filters to drop rows you never want in the message (out of stock, wrong category, and so on).

For selection setup, see [Selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/).

### Step 2: Add Liquid in your message

Assign the profile array, load the selection, and loop with `contains`:

{% raw %}
```liquid
{% assign saved_product_names = custom_attribute.${saved_product_names} %}
{% catalog_selection_items apparel_products in_stock_apparel %}
{% for item in items %}
{% if saved_product_names contains item.name %}
Product: {{ item.name }}
Category: {{ item.category }}
Price: ${{ item.price }}
Image: {{ item.image_url }}
{% endif %}
{% endfor %}
```
{% endraw %}

Replace `item.name` with `item.id` (or another column) if your array stores IDs instead of display names. Add spacing or HTML between fields for your channel. In {% raw %}`${{ item.price }}`{% endraw %}, the `$` is a literal currency symbol that prints before the Liquid output—it isn't part of Braze's {% raw %}`${}`{% endraw %} personalization syntax.

To generate this Liquid automatically, open the **Add Personalization** modal (**Catalog Items** > **Use a selection**). See [Using catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/use/).

### Step 3: Preview and test

Send test messages to profiles with different `saved_product_names` values. Confirm only matching catalog rows appear and that an empty array produces no product lines.

## Related articles

- [Catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/)
- [Selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)
- [Using catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/use/)
- [Custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)
- [Conditional logic]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/)
- [Liquid use case library — find a string within an array]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/#misc-string-in-array)
