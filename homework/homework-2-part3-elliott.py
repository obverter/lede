# Ben Elliott
# 2022-06-07
# Homework 2, Part 3

import json

data = json.loads(
    '{"tracks":[{"album":{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/1YxmW7DO2dM05gwMKTbr7l"},"href":"https://api.spotify.com/v1/albums/1YxmW7DO2dM05gwMKTbr7l","id":"1YxmW7DO2dM05gwMKTbr7l","images":[{"height":640,"url":"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d","width":640},{"height":300,"url":"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c","width":300},{"height":64,"url":"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb","width":64}],"name":"Fake Love","type":"album","uri":"spotify:album:1YxmW7DO2dM05gwMKTbr7l"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":207813,"explicit":true,"external_ids":{"isrc":"USCM51600333"},"external_urls":{"spotify":"https://open.spotify.com/track/6NMNgWgEAzde5M8U3lc6FN"},"href":"https://api.spotify.com/v1/tracks/6NMNgWgEAzde5M8U3lc6FN","id":"6NMNgWgEAzde5M8U3lc6FN","name":"Fake Love","popularity":90,"preview_url":"https://p.scdn.co/mp3-preview/b1c79b52128cc45a962cb87ba5a616ea6a435356?cid=null","track_number":1,"type":"track","uri":"spotify:track:6NMNgWgEAzde5M8U3lc6FN"},{"album":{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH"},"href":"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH","id":"0G1ffjfFuTUTVjDrVdLimH","images":[{"height":640,"url":"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568","width":640},{"height":300,"url":"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353","width":300},{"height":64,"url":"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66","width":64}],"name":"Views","type":"album","uri":"spotify:album:0G1ffjfFuTUTVjDrVdLimH"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"},{"external_urls":{"spotify":"https://open.spotify.com/artist/3tVQdUvClmAT7URs9V3rsp"},"href":"https://api.spotify.com/v1/artists/3tVQdUvClmAT7URs9V3rsp","id":"3tVQdUvClmAT7URs9V3rsp","name":"WizKid","type":"artist","uri":"spotify:artist:3tVQdUvClmAT7URs9V3rsp"},{"external_urls":{"spotify":"https://open.spotify.com/artist/77DAFfvm3O9zT5dIoG0eIO"},"href":"https://api.spotify.com/v1/artists/77DAFfvm3O9zT5dIoG0eIO","id":"77DAFfvm3O9zT5dIoG0eIO","name":"Kyla","type":"artist","uri":"spotify:artist:77DAFfvm3O9zT5dIoG0eIO"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":173986,"explicit":false,"external_ids":{"isrc":"USCM51600028"},"external_urls":{"spotify":"https://open.spotify.com/track/12VWzyPDBCc8fqeWCAfNwR"},"href":"https://api.spotify.com/v1/tracks/12VWzyPDBCc8fqeWCAfNwR","id":"12VWzyPDBCc8fqeWCAfNwR","name":"One Dance","popularity":84,"preview_url":"https://p.scdn.co/mp3-preview/98f60b086bb1da2ca2e4c217331b8c8cc801358d?cid=null","track_number":12,"type":"track","uri":"spotify:track:12VWzyPDBCc8fqeWCAfNwR"},{"album":{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/2z3NlPY0n0gHJPCPqrzA6V"},"href":"https://api.spotify.com/v1/albums/2z3NlPY0n0gHJPCPqrzA6V","id":"2z3NlPY0n0gHJPCPqrzA6V","images":[{"height":640,"url":"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d","width":640},{"height":300,"url":"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c","width":300},{"height":64,"url":"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb","width":64}],"name":"Sneakin’","type":"album","uri":"spotify:album:2z3NlPY0n0gHJPCPqrzA6V"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"},{"external_urls":{"spotify":"https://open.spotify.com/artist/1URnnhqYAYcrqrcwql10ft"},"href":"https://api.spotify.com/v1/artists/1URnnhqYAYcrqrcwql10ft","id":"1URnnhqYAYcrqrcwql10ft","name":"21 Savage","type":"artist","uri":"spotify:artist:1URnnhqYAYcrqrcwql10ft"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":251333,"explicit":true,"external_ids":{"isrc":"USCM51600337"},"external_urls":{"spotify":"https://open.spotify.com/track/4ckuS4Nj4FZ7i3Def3Br8W"},"href":"https://api.spotify.com/v1/tracks/4ckuS4Nj4FZ7i3Def3Br8W","id":"4ckuS4Nj4FZ7i3Def3Br8W","name":"Sneakin’","popularity":82,"preview_url":"https://p.scdn.co/mp3-preview/4fa89ace286252c33a1ca0d36e7555d6a451a2db?cid=null","track_number":1,"type":"track","uri":"spotify:track:4ckuS4Nj4FZ7i3Def3Br8W"},{"album":{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH"},"href":"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH","id":"0G1ffjfFuTUTVjDrVdLimH","images":[{"height":640,"url":"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568","width":640},{"height":300,"url":"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353","width":300},{"height":64,"url":"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66","width":64}],"name":"Views","type":"album","uri":"spotify:album:0G1ffjfFuTUTVjDrVdLimH"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"},{"external_urls":{"spotify":"https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H"},"href":"https://api.spotify.com/v1/artists/5pKCCKE2ajJHZ9KAiaK11H","id":"5pKCCKE2ajJHZ9KAiaK11H","name":"Rihanna","type":"artist","uri":"spotify:artist:5pKCCKE2ajJHZ9KAiaK11H"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":263373,"explicit":true,"external_ids":{"isrc":"USCM51600088"},"external_urls":{"spotify":"https://open.spotify.com/track/7fJtPlEZKxu6gvkfBFc5tW"},"href":"https://api.spotify.com/v1/tracks/7fJtPlEZKxu6gvkfBFc5tW","id":"7fJtPlEZKxu6gvkfBFc5tW","name":"Too Good","popularity":79,"preview_url":"https://p.scdn.co/mp3-preview/e702c76de627c3fb04da1bcbf6a8b53c3326a0cc?cid=null","track_number":16,"type":"track","uri":"spotify:track:7fJtPlEZKxu6gvkfBFc5tW"},{"album":{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH"},"href":"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH","id":"0G1ffjfFuTUTVjDrVdLimH","images":[{"height":640,"url":"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568","width":640},{"height":300,"url":"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353","width":300},{"height":64,"url":"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66","width":64}],"name":"Views","type":"album","uri":"spotify:album:0G1ffjfFuTUTVjDrVdLimH"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":245226,"explicit":true,"external_ids":{"isrc":"USCM51600080"},"external_urls":{"spotify":"https://open.spotify.com/track/4CpKEkdGbOJV51cSvx7SoG"},"href":"https://api.spotify.com/v1/tracks/4CpKEkdGbOJV51cSvx7SoG","id":"4CpKEkdGbOJV51cSvx7SoG","name":"Controlla","popularity":79,"preview_url":"https://p.scdn.co/mp3-preview/c5b5845dc83410f5731e395c5a725d6b6e94ff69?cid=null","track_number":11,"type":"track","uri":"spotify:track:4CpKEkdGbOJV51cSvx7SoG"},{"album":{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"},{"external_urls":{"spotify":"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi"},"href":"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi","id":"3ubFn9991d8ygM3MSi7NDi","name":"Future","type":"artist","uri":"spotify:artist:3ubFn9991d8ygM3MSi7NDi"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/1ozpmkWcCHwsQ4QTnxOOdT"},"href":"https://api.spotify.com/v1/albums/1ozpmkWcCHwsQ4QTnxOOdT","id":"1ozpmkWcCHwsQ4QTnxOOdT","images":[{"height":640,"url":"https://i.scdn.co/image/77b0c91524867cc72d1974f66ad8cd21d063a20e","width":640},{"height":300,"url":"https://i.scdn.co/image/f2405b82d0578dd815a3082ca0f7ec4e18e937a1","width":300},{"height":64,"url":"https://i.scdn.co/image/a5435bb3ab4fabe43bc7f7ce46a6c23aa30d8eae","width":64}],"name":"What A Time To Be Alive","type":"album","uri":"spotify:album:1ozpmkWcCHwsQ4QTnxOOdT"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"},{"external_urls":{"spotify":"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi"},"href":"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi","id":"3ubFn9991d8ygM3MSi7NDi","name":"Future","type":"artist","uri":"spotify:artist:3ubFn9991d8ygM3MSi7NDi"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":205879,"explicit":true,"external_ids":{"isrc":"USCM51500300"},"external_urls":{"spotify":"https://open.spotify.com/track/27GmP9AWRs744SzKcpJsTZ"},"href":"https://api.spotify.com/v1/tracks/27GmP9AWRs744SzKcpJsTZ","id":"27GmP9AWRs744SzKcpJsTZ","name":"Jumpman","popularity":77,"preview_url":"https://p.scdn.co/mp3-preview/4f3e954bb232a96c196389017d961016c8cbd7fc?cid=null","track_number":9,"type":"track","uri":"spotify:track:27GmP9AWRs744SzKcpJsTZ"},{"album":{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH"},"href":"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH","id":"0G1ffjfFuTUTVjDrVdLimH","images":[{"height":640,"url":"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568","width":640},{"height":300,"url":"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353","width":300},{"height":64,"url":"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66","width":64}],"name":"Views","type":"album","uri":"spotify:album:0G1ffjfFuTUTVjDrVdLimH"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":267066,"explicit":false,"external_ids":{"isrc":"USCM51500238"},"external_urls":{"spotify":"https://open.spotify.com/track/1OAYKfE0YdrN7C1yLWaLJo"},"href":"https://api.spotify.com/v1/tracks/1OAYKfE0YdrN7C1yLWaLJo","id":"1OAYKfE0YdrN7C1yLWaLJo","name":"Hotline Bling","popularity":75,"preview_url":"https://p.scdn.co/mp3-preview/53a8f039eb0b567e47868f5a53de4683ba5d5f0c?cid=null","track_number":20,"type":"track","uri":"spotify:track:1OAYKfE0YdrN7C1yLWaLJo"},{"album":{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH"},"href":"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH","id":"0G1ffjfFuTUTVjDrVdLimH","images":[{"height":640,"url":"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568","width":640},{"height":300,"url":"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353","width":300},{"height":64,"url":"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66","width":64}],"name":"Views","type":"album","uri":"spotify:album:0G1ffjfFuTUTVjDrVdLimH"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":189853,"explicit":true,"external_ids":{"isrc":"USCM51600078"},"external_urls":{"spotify":"https://open.spotify.com/track/4YJmZfvlheSziXem8HBWrj"},"href":"https://api.spotify.com/v1/tracks/4YJmZfvlheSziXem8HBWrj","id":"4YJmZfvlheSziXem8HBWrj","name":"Still Here","popularity":73,"preview_url":"https://p.scdn.co/mp3-preview/39384d3485d21184dd3719cfd8d644182b0b1d8b?cid=null","track_number":10,"type":"track","uri":"spotify:track:4YJmZfvlheSziXem8HBWrj"},{"album":{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/79qV4McLzhs8U3FyRKnocz"},"href":"https://api.spotify.com/v1/albums/79qV4McLzhs8U3FyRKnocz","id":"79qV4McLzhs8U3FyRKnocz","images":[{"height":640,"url":"https://i.scdn.co/image/2151a609fd5a5ec69586920a85bf308cdf56f3a1","width":640},{"height":300,"url":"https://i.scdn.co/image/9c6eb30ff5270c115b1ecd2b74430e505c281f25","width":300},{"height":64,"url":"https://i.scdn.co/image/ef4e90b4dde72134365a732659dccf9e1bd7b519","width":64}],"name":"Back To Back","type":"album","uri":"spotify:album:79qV4McLzhs8U3FyRKnocz"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":170637,"explicit":true,"external_ids":{"isrc":"USCM51500241"},"external_urls":{"spotify":"https://open.spotify.com/track/5lFDtgWsjRJu8fPOAyJIAK"},"href":"https://api.spotify.com/v1/tracks/5lFDtgWsjRJu8fPOAyJIAK","id":"5lFDtgWsjRJu8fPOAyJIAK","name":"Back To Back","popularity":73,"preview_url":"https://p.scdn.co/mp3-preview/b5bb11586af5cfde7c0eaef26300b2f6f62d2ac4?cid=null","track_number":1,"type":"track","uri":"spotify:track:5lFDtgWsjRJu8fPOAyJIAK"},{"album":{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"external_urls":{"spotify":"https://open.spotify.com/album/0ptlfJfwGTy0Yvrk14JK1I"},"href":"https://api.spotify.com/v1/albums/0ptlfJfwGTy0Yvrk14JK1I","id":"0ptlfJfwGTy0Yvrk14JK1I","images":[{"height":640,"url":"https://i.scdn.co/image/d329671363eb7826b5871eef978841c7db97c757","width":640},{"height":300,"url":"https://i.scdn.co/image/bcd6801c26cb293a45df9b092227395c5b403b4c","width":300},{"height":64,"url":"https://i.scdn.co/image/14d65d4565838431345e35575b8b74d95134990a","width":64}],"name":"If You\'re Reading This It\'s Too Late","type":"album","uri":"spotify:album:0ptlfJfwGTy0Yvrk14JK1I"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4"},"href":"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4","id":"3TVXtAsR1Inumwj472S9r4","name":"Drake","type":"artist","uri":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}],"available_markets":["CA","MX","US"],"disc_number":1,"duration_ms":241853,"explicit":true,"external_ids":{"isrc":"USCM51500010"},"external_urls":{"spotify":"https://open.spotify.com/track/1ID1QFSNNxi0hiZCNcwjUC"},"href":"https://api.spotify.com/v1/tracks/1ID1QFSNNxi0hiZCNcwjUC","id":"1ID1QFSNNxi0hiZCNcwjUC","name":"Legend","popularity":72,"preview_url":"https://p.scdn.co/mp3-preview/34fe00d7d951e42017bbbd8a424244c3cf1006e1?cid=null","track_number":1,"type":"track","uri":"spotify:track:1ID1QFSNNxi0hiZCNcwjUC"}]}'
)

# Let's see what we have
# print(type(data))

# data is a dictionary.
# what are its keys?
# print(data.keys())

# It has one key: 'tracks'
# let's print 'tracks'
# print(data['tracks'])

# It's a hot mess.
# What type is 'tracks'?
# print(type(data['tracks']))

# The hot mess is a list.
# How long is the list?
# print(len(data['tracks']))

# 'tracks' has len 10
# What's the first item in 'tracks'?
# print(data['tracks'][0])

# It's another, hotter mess.
# What's this mess's type?
# print(type(data['tracks'][0]))

# Oh hey it's another dictionary.
# What's in this dictionary?
# print(data["tracks"][0].keys())

# A list of keys.
# dict_keys(['album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri'])


# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪ It's time to boogie ♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩

hline = "♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩"

print(hline)

## ?1

print("\n1. How many songs are this mess?\n")
print(f"There are {len(data['tracks'])} songs in this mess.\n")

# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
print(hline)
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩

## ?2

print("\n2. List the name of each song in this mess along with its popularity.\n")
print(f"Here is a list of the songs in this mess along with their popularity scores:\n")
dt = data["tracks"]
for i in dt:
    print(f"{i['name']}: {i['popularity']}")

# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
print(f"\n{hline}")
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩

## ?3

print(
    "\n3. How long would it take, in minutes, to listen to all of these songs in a row?\n"
)

duration_sum = 0  # init duration summifier variable
for i in dt:  # summify song durations
    duration = i["duration_ms"]
    duration_sum += int(duration)

convert_ms = duration_sum / 1000  # variables to convert milliseconds to macroseconds
minutes = convert_ms // 60
seconds = convert_ms % 60

print(
    f"It would take about {int(minutes)} minutes, {round(seconds)} seconds to suffer through all of these songs.\n"
)

# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
print(f"\n{hline}")
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩

## ?4


print("\n4. For each song, list every artist that worked on it.\n")

# We need to generate a dictionary of track-dictionaries containing a key for artists.


# 1. Generate a loop through raw data targeting each track. ✅
#    A. Init target dictionary, which will feed final dictionary. ✅
#    B. Index loop through data ✅
#       i. For each track, retrieve track title ✅
#       ii. Store track title in a list. ✅
#          a. For contributing artists: ✅
#          b. Store contributing artists in a list. ✅
#    C. Print results via f-string, probably. ✅

for i in dt:  # master loop # track dict to feed to staging list
    track_master = {}  # init track dict
    track_name = []  # init track name list
    track_name.append(i["name"])  # append track name to track name list

    for track in track_name:
        track_master["track"] = track

    contributors_master = {}
    contributors = []
    for artist in i["artists"]:
        contributors.append(artist["name"])
    for i in contributors:
        contributors_master["artists"] = contributors

    for i in track_master:
        artist_count = len(contributors_master["artists"])
        if artist_count >= 2:
            for each in track_master:
                collab = ", ".join(list(*(contributors_master.values())))
                print(f"The track '{track_master['track']}' features {collab}.")
        else:
            print(
                f"The track '{track_master['track']}' features {contributors_master['artists'].pop()}."
            )


# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
print(f"\n{hline}")
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩

## ?5

print("\n5. For each song, list every musician that worked on it EXCEPT Drake\n")

for i in dt:
    track_master = {}  # init track dict
    track_name = []  # init track name list
    track_name.append(i["name"])  # append track name to track name list

    for track in track_name:
        track_master["track"] = track

    contributors_master = {}
    contributors = []
    for artist in i["artists"]:
        contributors.append(artist["name"])
    for i in contributors:
        contributors_master["artists"] = contributors

    for i in track_master:
        contributors_master["artists"] = [
            "" if item == "Drake" else item for item in contributors_master["artists"]
        ]
        artist_count = len(contributors_master["artists"])
        cma = contributors_master["artists"]
        if artist_count > 2:
            for each in track_master:
                print(
                    f"{cma[1]} and {cma[2]} worked on the track '{track_master['track']}' while Drake was locked out of the building."
                )
        elif artist_count > 1:
            for each in track_master:
                print(
                    f"{cma[1]} worked on the track '{track_master['track']}' while Drake lost at the mall."
                )
        else:
            print(
                f"The track '{track_master['track']}' features nobody. Not even Drake."
            )

# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
print(f"\n{hline}")
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩

## ?6

print("\n6. How many songs are from albums, and how many are from singles?\n")

song = 0
albums = []
singles = []
while song < 10:
    if data["tracks"][song]["album"]["album_type"] == "single":
        singles.append(song)
        song += 1
    else:
        albums.append(song)
        song += 1

print(
    f"Of the tracks from this mess, {len(albums)} are from albums and {len(singles)} are singles."
)

# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
print(f"\n{hline}")
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩

## ?7

print("7. What percentage of these songs are marked as explicit?")

song = 0
explicit = []
disney = []
while song < 10:
    if data["tracks"][song]["explicit"] == True:
        explicit.append(song)
        song += 1
    else:
        disney.append(song)
        song += 1

print(
    f"Of the tracks from this mess, {len(explicit)} are labeled as 'explicit' and {len(disney)} are not labeled as 'explicit'. If my calculations are correct, then {int(len(explicit) / song * 100)}% of the tracks are labeled as 'explicit."
)

# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
print(f"\n{hline}")
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩

## ?8

print(
    "8. I'd like to listen to one of the songs! Is there maybe a URL where I can listen to it?\n"
)

print("Hell yeah you can.\n")
jam = 0
links = []
while jam < 10:
    for song in dt:
        links.append(dt[jam]["href"])
        jam += 1

for url in range(len(dt)):
    print(f"You can listen to '{dt[url]['name']}' at the following url:\n{links[url]}\n")


# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩
print(f"\n{hline}")
# ♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩♪♬♩

## ?9

print("\n9. What is the most popular song?\n")

print(
    "The lazy person in me would note that this is a Top Ten list, which is already sorted by popularity. So we could just return the first item in (2)'s answer. But that doesn't seem interesting. So we'll do it the actual way."
)
popularity = []
name = []
sorter = {}
for song in dt:
    popularity.append(song["popularity"])
    name.append(song["name"])
sorter = zip(name, popularity)
sorter = dict(sorter)
score = sorter.values()
highest_score = max(score)
most_popular = [k for k, v in sorter.items() if v == highest_score]

print(
    f"\nThe most popular song is '{most_popular[0]}', which had a popularity score of {highest_score} on a completely arbitrary scale."
)
