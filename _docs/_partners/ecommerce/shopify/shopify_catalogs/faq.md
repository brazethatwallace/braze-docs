---
nav_title: FAQ
article_title: Shopify product sync FAQ
page_order: 0
page_type: FAQ
description: "This page provides answers to frequently asked questions about syncing Shopify products to Braze catalogs."
---

# Frequently asked questions

> This page provides answers to some frequently asked questions about [Shopify product sync]({{site.baseurl}}/shopify_catalogs/).

## Catalog and sync behavior

### Can I edit my Shopify catalog directly in Braze?

No. The Shopify catalog is read-only in Braze. Any manual edits may be overwritten by the next sync. Make all product updates directly in Shopify.

### How do I delete my Shopify catalog?

To delete your Shopify catalog, deactivate the sync from the Shopify partner page. Do not delete the catalog directly from the **Catalogs** page. Deactivating removes your entire catalog, including all synced tags, collections, and metafield data. Before deactivating, update or pause any campaigns or Canvases that reference this catalog, as they may send messages with missing product details.

### What happens if I delete a previously synced product or product field in Shopify?

Braze automatically removes the product or field from your Shopify catalog when it detects the deletion. However, any campaigns, Canvases, or segments that reference the deleted product or field will break. Before deleting products or fields in Shopify, verify they are not actively used in Braze.

### How do I change my catalog ID (product identifier)?

To change your catalog ID, first deactivate the sync and confirm that no active messages reference this catalog data. Then re-run the initial sync and select your desired identifier.

### Will changing my synced tags, collections, or metafields affect active campaigns?

Yes. Changing your synced selections may affect active campaigns, Canvases, or [catalog selections]({{site.baseurl}}/catalog_selections/) that reference them. Verify that your active content is updated before making changes.

### How long does the initial sync take?

Sync time depends on the number of products and variants in your store. The initial sync pulls products in batches, so it may take some time for all product tags, metafields, and collection associations to appear. Monitor your sync status on the Shopify partner page.

## Configuration and limits

### How many tags, collections, or metafields can I sync?

You can sync up to 20 of each per configuration:

- Up to 20 product tags
- Up to 20 collections
- Up to 20 product metafields

### What if a product belongs to more than 250 collections?

Shopify allows products to belong to more than 250 collections, but Braze can only fetch the first 250 collection associations per product. If a product belongs to a selected collection that falls outside the first 250 fetched, that association will not be reflected in your Shopify catalog. If you notice missing collection associations, contact your customer success manager.

### Why don't I see all my collections in the configuration modal?

The configuration modal displays up to 5,000 of the most recently updated collections. If your store exceeds this limit, older collections may not appear. Previously selected collections that fall outside the top 5,000 will still be shown in your selection.

### Can I filter by both tags and collections in a single catalog selection?

No. Catalog selections support only one array field per selection filter. You cannot combine tags and collections in the same selection. If you need to target users based on both tag and collection criteria, use [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) with SQL queries instead.

### What are the catalog selection limits?

Catalog selections are subject to the same limits as standard catalog selections. For details on item limits, filter constraints, and tier-based storage caps, see [Catalog selections]({{site.baseurl}}/catalog_selections/).

## Metafields and troubleshooting

### Why are some of my metafield types not showing up?

Only supported metafield types appear in the configuration modal. The following types are not currently supported: `dimension`, `json`, `link`, `money`, `rating`, `rich_text_field`, `volume`, and `weight`. For supported types and the full list, see [Shopify product metafields]({{site.baseurl}}/shopify_catalogs/#shopify-product-metafields) on the Shopify product sync page.

### I got a "Duplicate Metafield Column Name" error. What do I do?

Two or more of your selected metafields would create the same column name in the catalog. Deselect one of the conflicting metafields, or rename the metafield key in Shopify so each maps to a unique column name. Then re-save your configuration.

### Why are my tags taking longer than expected to load?

Tags are fetched directly from Shopify when you open the configuration modal. If your store has a large number of products or tags, this may take longer to load. This is expected behavior and does not affect sync performance. If loading consistently times out, try reducing the total number of tags in your Shopify store or contact support.

## Storage

### Will syncing additional product data affect my catalog storage?

Yes. Syncing tags, metafields, and collections increases your catalog storage usage. The free catalog tier has a 100 MB storage limit. If your sync exceeds your limit, Braze stops syncing and product updates will no longer be reflected. Contact your account manager to upgrade your tier if needed.
