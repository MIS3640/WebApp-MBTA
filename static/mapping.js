var keys = document.getElementById('map-keys');
var mapKey = keys.getAttribute('mapquest_key');
var searchKey = keys.getAttribute('search_key');

function createMap() {
    L.mapquest.key = mapKey;
    var data = document.getElementById("map_data");
    var lat = data.getAttribute("lat");
    var lng = data.getAttribute("lng");
    var stopName = data.getAttribute("stop_name");
    var wheelchair = data.getAttribute("wheelchair");

    if (stopName == "No stops nearby") {
        lat = 42.3601;
        lng = -71.0589;
        stopName = null;
    }

    let map = L.mapquest.map('map', {
        center: [lat, lng],
        layers: L.mapquest.tileLayer('map'),
        zoom: 12
    });

    console.log("map loaded")
    // make sure there is a stopName
    if (stopName != null && stopName != "") {
        L.mapquest.textMarker([lat, lng], {
            text: stopName,
            subtext: "Wheelchair accessible: " + wheelchair,
            position: "right",
            type: 'marker',
            icon: {
                primaryColor: '#333333',
                secondaryColor: '#333333',
                size: 'sm'
            }
        }).addTo(map);
    }

}

function createSearch() {
    placeSearch({
        key: searchKey,
        container: document.querySelector('#search-input'),
        useDeviceLocation: true,
        collection: [
            'poi',
            'airport',
            'address',
            'adminArea',
        ]
    });
    console.log(document.querySelector('#search-input'));
}

window.onload = function () {
    createMap();
    createSearch();
};