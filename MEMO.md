# Search API

1. search tracks by q = 'yello'
```
curl --request GET   --url 'https://api.spotify.com/v1/search?q=track:yellow&type=track&include_external=audio&limit=1'   --header 'Authorization: Bearer '   --header 'Content-Type: application/json' | jq -C
```

2. search tracks by q = {track = '好不容易', artist = '告五人'}

```
curl --request GET   --url 'https://api.spotify.com/v1/search?q=track:%E5%A5%BD%E4%B8%8D%E5%AE%B9%E6%98%93&artist=%E5%91%8A%E4%BA%94%E4%BA%BA&type=track&include_external=audio&limit=1'   --header 'Authorization: Bearer '   --header 'Content-Type: application/json' | jq -C
```