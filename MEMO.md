# Search API

search tracks by q = 'yello'
```
curl --request GET   --url 'https://api.spotify.com/v1/search?q=track:yellow&type=track&include_external=audio&limit=1'   --header 'Authorization: Bearer '   --header 'Content-Type: application/json' | jq -C
```