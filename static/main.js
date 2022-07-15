function success(position)
{
    const latitude  = position.coords.latitude;
    const longitude = position.coords.longitude;

    console.log('https://www.openstreetmap.org/#map=18/' + latitude + '/' + longitude);
    console.log('Latitude: ' + latitude + ' °, Longitude: ' + longitude + ' °');
}

function error()
{
    console.log('Unable to retrieve your location');
}

if (!navigator.geolocation)
{
    console.log('Geolocation is not supported by your browser');
}
else
{
    console.log('Locating…');
    navigator.geolocation.getCurrentPosition(success, error);
}

console.log("Hi!");