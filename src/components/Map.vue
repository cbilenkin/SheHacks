<style>
.map-container {
    width: 900px;
    height: 1500px;
}
</style>
<template>
    <div id="map">
        <gmap-map
                id="map"
                :center="center"
                :zoom="18"
                style="width: 180%; height: 400px"
        >
            <gmap-marker
                    :key="index"
                    v-for="(m, index) in markers"
                    :position="center = m.position"
                    :clickable="true"
                    :draggable="true"
                    @click="center=m.position"
            ></gmap-marker>
        </gmap-map>
    </div> 
</template>   
<script> 
    export default{
        data(){
            return {
                center: {lat: 23.8103, lng: 90.4125},
                markers: [
                    {position: {lat: 10.0, lng: 10.0}}
                ],
                getMap: this.$root.mapping,
                description: '',
                latLng: {},
                place: null
            }
        },

        mounted(){
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    let pos = {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude
                    };
                    const positionForZip = {
                        latitude: pos.lat,
                        longitude: pos.lng
                    }

                    const { geo2zip } = require('geo2zip')
                    geo2zip(positionForZip).then(zip => {
                        console.log(zip)
                    })
                    this.center.lat = pos.lat;
                    this.center.lng = pos.lng;
                    this.markers[0].position.lat = pos.lat;
                    this.markers[0].position.lng = pos.lng;

                    this.geocodeLatLng(new google.maps.Geocoder, pos, google.maps.InfoWindow);

                }.bind(this));
            }
        },
        methods: {
            setDescription(description){
                this.description = description
            },
            setPlace(place){
                this.latLng = {
                    lat: place.geometry.location.lat(),
                    lng: place.geometry.location.lng(),
                }
            },
            geocodeLatLng(geocoder, map, infowindow){
                geocoder.geocode({'location':this.center}, function(results, status){
                    console.log(results, status); 
                });
            }
        },
    }
</script>