<style>
  .map-container {
    width: 500px;
    height: 300px;
  }
</style>

<template>
  <div id="app">
    <gmap-map class="map-container" :center="{lat:1.38, lng:103.8}" :zoom="12">
      <gmap-marker :position="{lat:1.38, lng:103.8}">
      </gmap-marker>
      <gmap-info-window :position="{lat:1.38, lng:103.8}">
        Hello world!
      </gmap-info-window>
    </gmap-map>
  </div>
</template>