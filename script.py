import os
import django
import json
from datetime import datetime

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notify_nepal.settings")  # ← replace with your project name
django.setup()

from api.models import Feed, FeedItem  # adjust to your app name

# List of allowed FeedItem fields (update if needed)
FEED_ITEM_FIELDS = {
    "uuid",
    "slug",
    "link",
    "title",
    "summary",
    "content",
    "image_url",
    "published_at",
    "published_raw_nepali_date",
    "fetched_at",
    "updated_at",
}

# Load your data (replace with actual file path or load from a string)
with open("nep_data.json", "r") as f:
    data = json.load(f)

for item in data:
    # Extract and create/update Feed
    feed_data = item.pop("feed")
    feed, _ = Feed.objects.get_or_create(
        slug=feed_data["slug"],
        defaults={
            "name": feed_data["name"],
            "name_nepali": feed_data.get("name_nepali", ""),
            "language": feed_data["language"],
            "website": feed_data["website"],
            "logo_url": feed_data["logo_url"],
        }
    )

     # Prepare valid FeedItem fields only
    filtered_item = {k: v for k, v in item.items() if k in FEED_ITEM_FIELDS}

   # Parse date fields
    for field in ["published_at", "fetched_at", "updated_at"]:
        if field in filtered_item and filtered_item[field]:
            filtered_item[field] = datetime.fromisoformat(filtered_item[field].replace("Z", "+00:00"))

    # Attach Feed FK
    filtered_item["feed"] = feed

    # Create or update FeedItem
    FeedItem.objects.update_or_create(uuid=filtered_item["uuid"], defaults=filtered_item)

print("✅ Feed items imported successfully (ignoring extra fields).")
