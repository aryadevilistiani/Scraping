import json
import pandas as pd
# Load via context manager and read_json() method
with open('output.json', 'r', encoding='utf8') as file:
    # load JSON data and parse into Dictionary object
    data = json.load(file)
# Load JSON as DataFrame
df = pd.json_normalize(
    data, "comments", ["datetime_post", "account_instagram_artist", "caption_postingan", "link_post", "img_link"])
# Print Result
print(df)

# output DataFrame to CSV file
df.to_csv('jeromepolin.csv')
