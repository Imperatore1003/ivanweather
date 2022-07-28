const staticCacheName = 'site-static-v1';
const dynamicCacheName = 'site-dynamic-v1';
// const assets = [
//     "/static/main.js",
//     "/static/style.css",
//     "/static/img/android-icon-36x36.png",
//     "/static/img/android-icon-48x48.png",
//     "/static/img/android-icon-72x72.png",
//     "/static/img/android-icon-96x96.png",
//     "/static/img/android-icon-144x144.png",
//     "/static/img/android-icon-192x192.png",
//     "/static/img/android-icon-512x512.png",
//     "/static/img/android-icon-640x640.png",
//     "/static/img/apple-icon-57x57.png",
//     "/static/img/apple-icon-60x60.png",
//     "/static/img/apple-icon-72x72.png",
//     "/static/img/apple-icon-76x76.png",
//     "/static/img/apple-icon-114x114.png",
//     "/static/img/apple-icon-120x120.png",
//     "/static/img/apple-icon-144x144.png",
//     "/static/img/apple-icon-152x152.png",
//     "/static/img/apple-icon-180x180.png",
//     "/static/img/apple-icon-precomposed.png",
//     "/static/img/apple-icon.png",
//     "/static/img/favicon-16x16.png",
//     "/static/img/favicon-32x32.png",
//     "/static/img/favicon-96x96.png",
//     "/static/img/favicon.ico",
//     "/static/img/IvanWeather.png",
//     "/static/img/IvanWeather.svg",
//     "/static/img/ms-icon-144x144.png",
//     "/static/img/ms-icon-70x70.png",
//     "/static/img/ms-icon-150x150.png",
//     "/static/img/ms-icon-310x310.png",
//     "/manifest.json",
//     "/browserconfig.xml",
//     "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js",
//     "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css",
//     "https://openweathermap.org/img/wn/01d.png",
//     "https://openweathermap.org/img/wn/01n.png",
//     "https://openweathermap.org/img/wn/02d.png",
//     "https://openweathermap.org/img/wn/02n.png",
//     "https://openweathermap.org/img/wn/03d.png",
//     "https://openweathermap.org/img/wn/03n.png",
//     "https://openweathermap.org/img/wn/04d.png",
//     "https://openweathermap.org/img/wn/04n.png",
//     "https://openweathermap.org/img/wn/09d.png",
//     "https://openweathermap.org/img/wn/09n.png",
//     "https://openweathermap.org/img/wn/10d.png",
//     "https://openweathermap.org/img/wn/10n.png",
//     "https://openweathermap.org/img/wn/11d.png",
//     "https://openweathermap.org/img/wn/11n.png",
//     "https://openweathermap.org/img/wn/13d.png",
//     "https://openweathermap.org/img/wn/13n.png",
//     "https://openweathermap.org/img/wn/50d.png",
//     "https://openweathermap.org/img/wn/50n.png",
//     "/fallback"
// ];
const assets = [
        "/static/img/android-icon-36x36.png",
        "/static/img/android-icon-48x48.png",
        "/static/img/android-icon-72x72.png",
        "/static/img/android-icon-96x96.png",
        "/static/img/android-icon-144x144.png",
        "/static/img/android-icon-192x192.png",
        "/static/img/android-icon-512x512.png",
        "/static/img/android-icon-640x640.png",
        "/static/img/apple-icon-57x57.png",
        "/static/img/apple-icon-60x60.png",
        "/static/img/apple-icon-72x72.png",
        "/static/img/apple-icon-76x76.png",
        "/static/img/apple-icon-114x114.png",
        "/static/img/apple-icon-120x120.png",
        "/static/img/apple-icon-144x144.png",
        "/static/img/apple-icon-152x152.png",
        "/static/img/apple-icon-180x180.png",
        "/static/img/apple-icon-precomposed.png",
        "/static/img/apple-icon.png",
        "/static/img/favicon-16x16.png",
        "/static/img/favicon-32x32.png",
        "/static/img/favicon-96x96.png",
        "/static/img/favicon.ico",
        "/static/img/IvanWeather.png",
        "/static/img/IvanWeather.svg",
        "/static/img/ms-icon-144x144.png",
        "/static/img/ms-icon-70x70.png",
        "/static/img/ms-icon-150x150.png",
        "/static/img/ms-icon-310x310.png",
        "/manifest.json",
        "/browserconfig.xml",
        "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js",
        "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css",
        "https://openweathermap.org/img/wn/01d.png",
        "https://openweathermap.org/img/wn/01n.png",
        "https://openweathermap.org/img/wn/02d.png",
        "https://openweathermap.org/img/wn/02n.png",
        "https://openweathermap.org/img/wn/03d.png",
        "https://openweathermap.org/img/wn/03n.png",
        "https://openweathermap.org/img/wn/04d.png",
        "https://openweathermap.org/img/wn/04n.png",
        "https://openweathermap.org/img/wn/09d.png",
        "https://openweathermap.org/img/wn/09n.png",
        "https://openweathermap.org/img/wn/10d.png",
        "https://openweathermap.org/img/wn/10n.png",
        "https://openweathermap.org/img/wn/11d.png",
        "https://openweathermap.org/img/wn/11n.png",
        "https://openweathermap.org/img/wn/13d.png",
        "https://openweathermap.org/img/wn/13n.png",
        "https://openweathermap.org/img/wn/50d.png",
        "https://openweathermap.org/img/wn/50n.png",
        "/fallback"
];

// install event
self.addEventListener('install', evt => {
    //console.log('service worker installed');
    evt.waitUntil(
        caches.open(staticCacheName).then((cache) => {
            console.log('caching shell assets');
            cache.addAll(assets);
        })
    );
});

// activate event
self.addEventListener('activate', evt => {
    //console.log('service worker activated');
    evt.waitUntil(
        caches.keys().then(keys => {
            //console.log(keys);
            return Promise.all(keys
                .filter(key => key !== staticCacheName && key !== dynamicCacheName)
                .map(key => caches.delete(key))
            );
        })
    );
});

// fetch event
self.addEventListener('fetch', evt => {
    //console.log('fetch event', evt);
    evt.respondWith(
        caches.match(evt.request).then(cacheRes => {

        //     return cacheRes || fetch(evt.request)
        // })


        //     return cacheRes || fetch(evt.request).then(fetchRes => {
        //         return caches.open(dynamicCacheName).then(cache => {
        //             cache.put(evt.request.url, fetchRes.clone());
        //             return fetchRes;
        //         })
        //     });
        // })

        
            return cacheRes || fetch(evt.request)
        }).catch(() => caches.match('/fallback'))

    );
});